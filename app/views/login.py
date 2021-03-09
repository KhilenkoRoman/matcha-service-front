from app import app, settings
import hashlib
import html
import json
from flask import render_template, request, session, redirect, url_for
import re
from datetime import datetime
from flask_mail import Message
from app.models.users import *
from random import randint
from app.models.friendship import all_friends
from app.models.notifications import get_notifications_by_user_id
from app.models.location import *
from app.views.newsfeed import get_not_friends
import requests


@app.route('/')
def index():
	if session.get('token'):
		data = {
			'all_posts': 'all_user_post',
			'all_friends': all_friends(session.get('id_user_logged')),
			"get_user_by_id": get_user_by_id,
			"all_post_comments": 'all_post_comments',
			"liked": 'liked',
			"disliked": 'disliked',
			"len_post_likes": 'len_post_likes',
			"len_post_dislikes": 'len_post_dislikes',
			'users_online': 'get_users_online_list()'
		}
		return render_template('newsfeed.html', data=data)

	return render_template('index-register.html')



def get_friendlist(id_user):
	req = all_friends(id_user)
	if not req:
		return None
	friends_ids = []
	for i in req:
		if i['id_requester'] == id_user:
			friends_ids.append(i['id_user_requested'])
		if i['id_user_requested'] == id_user:
			friends_ids.append(i['id_requester'])
	frends_data = []
	for i in friends_ids:
		frends_data.append(get_user_by_id(i))
	return frends_data


@app.route('/ajax_registration', methods=['POST'])
def ajax_registration():
	r_email = html.escape(request.form['email'])
	pwd = request.form['pasword']
	r_first = request.form['first_name']
	r_last = request.form['last_name']
	r_gender = request.form['gender']
	num = randint(1, 12)

	if 0 < num <= 6:
		cover = str(num) + ".jpg"
	else:
		cover = str(num) + ".jpeg"

	str_date = request.form['year'] + request.form['month'] + request.form['day']
	try:
		r_birthday = datetime.strptime(str_date, '%Y%b%d')
	except:
		return "wrong_data"

	if not r_email:
		return "no_email"
	if not pwd:
		return "no_pwd"
	if len(r_email) > 100:
		return "long_mail"
	if len(pwd) > 100:
		return "long_pwd"
	if not re.match("^[_a-z0-9-]+(.[_a-z0-9-]+)*@[a-z0-9-]+(.[a-z0-9-]+)*(.[a-z]{2,4})$", r_email.lower()):
		return "wrong_email"
	if re.search("[a-zA-Z]+", pwd.lower()) is None or re.search("[0-9]+", pwd) is None:
		return "week_pwd"

	r = requests.post(settings['GATEWAY_URL'] + 'api/v1/user/register/', json={
		"email": r_email,
		"password": pwd,
		"first_name": r_first,
		"last_name": r_last,
		"user_info": {
			"gender": int(r_gender) - 1,
			"birth_date": r_birthday.strftime('%Y-%m-%d'),
		},
		})

	if r.status_code == 400 and r.json().get('email') == ['user with this email already exists.']:
		return "email_exist"

	if r.status_code == 201:
		session['token'] = r.json().pop('token')
		session['user'] = r.json()
		return "registered"
	else:
		return "error"


@app.route('/activate')
def activate():
	context = {'success': 'false'}

	email = request.args.get('email')
	token = request.args.get('token')
	if email is None or token is None:
		return render_template('activate.html', context=context)

	user = check_user_token(email)
	if not user:
		return render_template('activate.html', context=context)

	if user[0]['token'] == token and user[0]['active'] == 0:
		ret = activate_user(user[0]['id_user'])
		if not ret:
			context.update({'success': 'true'})
	return render_template('activate.html', context=context)


@app.route('/ajax_login', methods=['POST'])
def ajax_login():
	if session.get('id_user_logged'):
		return "already_logged"
	l_login = html.escape(request.form['login'])
	pwd = request.form['pwd']

	if not l_login:
		return "no_login"
	if not pwd:
		return "no_pwd"
	if len(l_login) > 40:
		return "long_login"
	if len(pwd) > 100:
		return "long_pwd"

	r = requests.post(settings['GATEWAY_URL'] + 'api/v1/user/token/', data={'email' : l_login, 'password': pwd})

	if r.status_code == 200:
		session['token'] = r.json().get('token')
		session['user'] = r.json().get('user')
		return "logged_in"
	else:
		return "no_user"


# @app.route('/ajax_logout', methods=['POST'])
@app.route('/logout')
def ajax_logout():
	session.pop('id_user_logged', None)
	session.pop('user_data', None)
	session.pop('friendlist', None)
	session.pop('notifications', None)
	session.pop('location', None)
	session.pop('not_friends', None)
	return redirect(request.referrer)


@app.route('/recover')
def recover():
	context = {'success': 'false', 'token': "none", 'email': "none"}
	if session.get('id_user_logged'):
		return redirect(url_for('index'))

	email = request.args.get('email')
	token = request.args.get('token')
	if email and token:
		check = check_user_token(email)
		if check:
			check = check[0]
			if token == check['token']:
				context.update({'success': 'true', 'token': token, 'email': email})
				return render_template('recover.html', context=context)
		return render_template('recover.html', context=context)

	return render_template('recover.html', context=context)


@app.route('/ajax_recover', methods=['POST'])
def ajax_recover():
	r_login = html.escape(request.form['login'])

	check = check_user(r_login, r_login)
	if len(check) == 1:
		check = check[0]
	else:
		return "no_user"
	if check["active"] != 1:
		return "not_active"

	date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	token_hash = hashlib.md5((r_login + date_str).encode('utf-8')).hexdigest()

	req = user_update_token(check['id_user'], token_hash)
	if not req:
		msg = Message('matcha recover', sender="rkhilenksmtp@gmail.com", recipients=[check['email']])
		msg.body = "To recover pwd goto " + request.url_root + "recover?email=" + check[
			'email'] + "&token=" + token_hash
		msg.html = "<p>To recover pwd goto " + request.url_root + "recover?email=" + check[
			'email'] + "&token=" + token_hash + "</p>"
		mail.send(msg)

	return "msg_sent"


@app.route('/ajax_new_pwd', methods=['POST'])
def ajax_new_pwd():
	pwd = request.form['pwd']
	token = request.form['token']
	email = request.form['email']

	if len(pwd) < 6:
		return "short_pwd"
	if len(pwd) > 100:
		return "long_pwd"
	if re.search("[a-zA-Z]+", pwd.lower()) is None or re.search("[0-9]+", pwd) is None:
		return "week_pwd"

	pwd_hash = hashlib.sha512(pwd.encode('utf-8')).hexdigest()
	check = check_user_token(email)

	if len(check) == 1:
		check = check[0]
	else:
		return "no_user"

	if check['token'] == token:
		res = user_new_pwd(check['id_user'], pwd_hash)
		if not res:
			return "changed"
	else:
		return "error"


@app.route('/ajax_change_pwd', methods=['POST'])
def ajax_change_pwd():
	old_pwd = request.form.get('old_pwd')
	new_pwd = request.form.get('new_pwd')
	conf_pwd = request.form.get('conf_pwd')

	if new_pwd != conf_pwd:
		return "wrong_confirm"
	if len(new_pwd) < 6:
		return "short_pwd"
	if len(new_pwd) > 100:
		return "long_pwd"
	if re.search("[a-zA-Z]+", new_pwd.lower()) is None or re.search("[0-9]+", new_pwd) is None:
		return "week_pwd"

	user = get_user_by_id(request.form.get('id_user'))
	if user.get('password') != hashlib.sha512(old_pwd.encode('utf-8')).hexdigest():
		return "wrong_old_pwd"
	else:
		user_new_pwd(request.form.get('id_user'), hashlib.sha512(new_pwd.encode('utf-8')).hexdigest())
		return "sucsess"
