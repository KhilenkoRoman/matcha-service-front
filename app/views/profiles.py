from app import app
from flask import render_template, session, redirect, request
from flask_uploads import configure_uploads, IMAGES, UploadSet
from datetime import datetime
from app.models.users import *
from app.models.friendship import *
from app.models.posts import all_user_post
from app.models.tags import get_tags_by_id_user
from app.models.comments import all_post_comments
from app.models.likes import liked, disliked, len_post_dislikes, len_post_likes
from app.models.location import get_location_by_id
from app.views.notifications import add_notification
from app.views.login import get_friendlist
from app.views.newsfeed import get_not_friends
import html


photos = UploadSet('photos', IMAGES)
app.config['UPLOADED_PHOTOS_DEST'] = "app/static/uploads"
configure_uploads(app, photos)

ALLOWED_EXTENSIONS = [
		'image/gif',
		'image/jpeg',
		'image/pjpeg',
		'image/png',
		'image/svg+xml',
		'image/tiff',
		'image/vnd.microsoft.icon',
		'image/vnd.wap.wbmp',
		'image/webp'
	]


def allowed_ex(mime):
	return mime.lower() in ALLOWED_EXTENSIONS


@app.route('/profile/')
@app.route('/user/id<uuid:id_user>/')
def profile(id_user=None):
	if not session.get('user_data') and not id_user:
		return redirect('/')
	if id_user:
		user = get_user_by_id(id_user)
		posts = all_user_post(id_user)
	else:
		user = session.get('user_data')
		posts = all_user_post(session.get('id_user_logged'))
	if session.get('user_data'):
		user_cur = session.get('user_data')
	else:
		user_cur = None

	if session.get('id_user_logged') and not user['id_user'] == session.get('id_user_logged'):
		msg = "User: " + session.get('user_data')['first_name'] + " " + \
			session.get('user_data')['last_name'] + " view your profile"
		add_notification(user['id_user'], msg)
	data = {
		'user': user,
		'user_cur': user_cur,
		'posts': posts,
		'get_user_by_id': get_user_by_id,
		'all_post_comments': all_post_comments,
		'len_post_likes': len_post_likes,
		'len_post_dislikes': len_post_dislikes,
		'liked': liked,
		'disliked': disliked,
		'all_friends': all_friends(user['id_user'])
	}
	return render_template('timeline.html', data=data)


@app.route('/profile/edit/basic/')
def edit_profile():
	if session.get('id_user_logged'):
		data = {
			'user': session.get('user_data'),
			'about': get_about(session.get('id_user_logged')),
			'date': datetime,
			'all_friends': all_friends(session.get('id_user_logged'))
		}
		return render_template('edit-profile-basic.html', data=data)
	return redirect('/')


@app.route('/ajax_edit_basic/', methods=['POST'])
def ajax_edit_basic():
	if session.get('id_user_logged'):
		first_name = html.escape(request.form.get('first_name').strip())
		last_name = html.escape(request.form.get('last_name').strip())
		email = html.escape(request.form.get('email').strip())
		optradio = html.escape(request.form.get('optradio').strip())
		sex = html.escape(request.form.get('sex').strip())
		city = html.escape(request.form.get('city').strip())
		country = html.escape(request.form.get('country').strip())
		information = html.escape(request.form.get('information').strip())
		theme = html.escape(request.form.get('theme').strip())
		id_user = session.get('id_user_logged')
		location = str(city) + " " + str(country)

		if not first_name:
			return "Enter first name"
		if not last_name:
			return "Enter last name"
		if not email:
			return "Enter email"
		res1 = update_basic_user(first_name, last_name, email, optradio, sex, theme, id_user)
		if not res1:
			res2 = update_basic_about(location, information, id_user)
			if not res2:
				user = get_user_by_id(id_user)
				session['user_data'] = user
				return "success"
			return "Wrong save location or about"
		return "Wrong save user data"
	return redirect('/')


@app.route('/profile/edit/advanced/')
def edit_profile_advanced():
	if session.get('id_user_logged'):
		data = {
			'user': session.get('user_data'),
			'about': get_about(session.get('id_user_logged')),
			'all_friends': all_friends(session.get('id_user_logged'))
		}
		return render_template('edit-profile-advanced.html', data=data)
	return redirect('/')


@app.route('/ajax_edit_advanced/', methods=['POST'])
def ajax_edit_advanced():
	if session.get('id_user_logged'):
		phone = html.escape(request.form.get('phone').strip())
		language = html.escape(request.form.get('language').strip())
		status = html.escape(request.form.get('status').strip())
		political = html.escape(request.form.get('political').strip())
		fb = html.escape(request.form.get('fb').strip())
		tw = html.escape(request.form.get('tw').strip())
		inst = html.escape(request.form.get('inst').strip())
		site = html.escape(request.form.get('site').strip())
		hobbies = html.escape(request.form.get('hobbies').strip())
		tv_shows = html.escape(request.form.get('tv_shows').strip())
		movies = html.escape(request.form.get('movies').strip())
		games = html.escape(request.form.get('games').strip())
		music = html.escape(request.form.get('music').strip())
		books = html.escape(request.form.get('books').strip())
		writers = html.escape(request.form.get('writers').strip())
		others = html.escape(request.form.get('others').strip())
		id_user = session.get('id_user_logged')
		res = update_advanced_about(phone, language, status, political, fb, tw, inst, site, hobbies, tv_shows, movies, games, music, books, writers, others, id_user)
		if not res:
			return "Success"
		return "Fail update profile"
	return redirect('/')


@app.route('/profile/edit/interests/')
def edit_profile_interests():
	if session.get('id_user_logged'):
		tags = get_tags_by_id_user(session.get('id_user_logged'))
		data = {
			'user': session.get('user_data'),
			'about': get_about(session.get('id_user_logged')),
			'all_friends': all_friends(session.get('id_user_logged')),
			'tags': tags
		}
		return render_template('edit-profile-interests.html', data=data)
	return redirect('/')


@app.route('/profile/edit/avatar/')
def edit_profile_avatar():
	if session.get('id_user_logged'):
		data = {
			'user': session.get('user_data'),
			'all_friends': all_friends(session.get('id_user_logged'))
		}
		return render_template('edit-profile-ava.html', data=data)
	return redirect('/')


@app.route('/ajax_save_ava/', methods=['POST'])
def ajax_save_ava():
	if session.get('id_user_logged'):
		if request.files:
			ava = request.files['ava']
			filename = str(datetime.now().timestamp()).replace(".", "") + "-" + session.get('user_data')['first_name'] + \
				"-" + session.get('user_data')['last_name'] + "." + ava.filename.rsplit('.', 1)[1].lower()
			res = allowed_ex(ava.content_type)
			if res:
				photos.save(ava, "avatars", filename)
				update_avatar("/static/uploads/avatars/" + filename, session.get('id_user_logged'))
				user = get_user_by_id(session.get('id_user_logged'))
				rating = user['rating'] + 5
				update_rating(rating, session.get('id_user_logged'))
				session['user_data'] = get_user_by_id(session.get('id_user_logged'))
		return redirect(request.referrer)
	return redirect('/')


@app.route('/profile/edit/password/')
def edit_profile_password():
	if session.get('id_user_logged'):
		data = {
			'user': session.get('user_data'),
			'about': get_about(session.get('id_user_logged')),
			'all_friends': all_friends(session.get('id_user_logged'))
		}
		return render_template('edit-profile-password.html', data=data)
	return redirect('/')


@app.route('/profile/edit/location/')
def edit_profile_location():
	if session.get('id_user_logged'):
		data = {
			'user': session.get('user_data'),
			'about': get_about(session.get('id_user_logged')),
			'all_friends': all_friends(session.get('id_user_logged'))
		}
		return render_template('edit-profile-location.html', data=data)
	return redirect('/')


def is_friends_with(auth_id, user_id):
	user = check_friends(auth_id, user_id)
	if user:
		return user
	return "0"


@app.route('/ajax_check_friends/')
def ajax_check_friends():
	auth_id = session.get('id_user_logged')
	user_id = request.args.get('user_id')
	user1 = is_friends_with(auth_id, user_id)
	user2 = is_friends_with(user_id, auth_id)

	if auth_id:
		if str(auth_id) == str(user_id):
			return "same user"
		if user1 == "0":
			if user2 == "0":
				return "0"
			else:
				if user2['status'] == 0:
					return "pending"
				else:
					return "1"
		else:
			if user1['status'] == 0:
				return "waiting"
			else:
				return "1"
	return "false"


@app.route('/ajax_delete_user_request/')
def ajax_delete_user_request():
	auth_id = session.get('id_user_logged')
	user_id = request.args.get('user_id')

	if auth_id:
		if auth_id == user_id:
			return "same user"
		del_fr = delete_user_request(auth_id, user_id)
		if not del_fr:
			msg = "User: " + session.get('user_data')['first_name'] + " " + \
				session.get('user_data')['last_name'] + " delete request to friends."
			add_notification(user_id, msg)
			return "0"
	return "false"


@app.route('/ajax_add_user_request/')
def ajax_add_user_request():
	auth_id = session.get('id_user_logged')
	user_id = request.args.get('user_id')

	if auth_id:
		if auth_id == user_id:
			return "same user"
		add_fr = add_friend(auth_id, user_id)
		if not add_fr:
			msg = "User: " + session.get('user_data')['first_name'] + " " + \
				session.get('user_data')['last_name'] + " add you request to friends."
			add_notification(user_id, msg)
			return "waiting"
	return "false"


@app.route('/ajax_confirm_user_request/')
def ajax_confirm_user_request():
	auth_id = session.get('id_user_logged')
	user_id = request.args.get('user_id')

	if auth_id:
		if auth_id == user_id:
			return "same user"
		conf_fr = confirm_user_request(user_id, auth_id)
		if not conf_fr:
			msg = "User: " + session.get('user_data')['first_name'] + " " + \
				session.get('user_data')['last_name'] + " confirm you request to friends."
			add_notification(user_id, msg)
			user = get_user_by_id(user_id)
			rating = user['rating'] + 10
			update_rating(rating, user_id)
			user2 = get_user_by_id(auth_id)
			rating2 = user2['rating'] + 10
			update_rating(rating2, auth_id)
			session['friendlist'] = get_friendlist(auth_id)
			session['not_friends'] = get_not_friends(auth_id)
			return "1"
	return "false"


@app.route('/ajax_delete_user_friend/')
def ajax_delete_user_friend():
	auth_id = session.get('id_user_logged')
	user_id = request.args.get('user_id')

	if auth_id:
		if auth_id == user_id:
			return "same user"
		res1 = delete_user_request(auth_id, user_id)
		if not res1:
			res2 = delete_user_request(user_id, auth_id)
			if not res2:
				msg = "User: " + session.get('user_data')['first_name'] + " " + \
					session.get('user_data')['last_name'] + " delete friendsip."
				add_notification(user_id, msg)
				user = get_user_by_id(user_id)
				rating = user['rating'] - 10
				update_rating(rating, user_id)
				user2 = get_user_by_id(auth_id)
				rating2 = user2['rating'] - 10
				update_rating(rating2, auth_id)
				session['friendlist'] = get_friendlist(auth_id)
				session['not_friends'] = get_not_friends(auth_id)
				return "0"
	return "false"


@app.route('/profile/about/')
@app.route('/user/id<int:id_user>/about/')
def about(id_user=None):
	if not session.get('user_data') and not id_user:
		return redirect('/')
	if id_user:
		user = get_user_by_id(id_user)
		about = get_about(id_user)
	else:
		user = session.get('user_data')
		about = get_about(session.get('id_user_logged'))
	if session.get('id_user_logged') and not user['id_user'] == session.get('id_user_logged'):
		msg = "User: " + session.get('user_data')['first_name'] + " " + \
			session.get('user_data')['last_name'] + " view your profile"
		add_notification(user['id_user'], msg)

	location = get_location_by_id(id_user)
	tags = get_tags_by_id_user(id_user)
	data = {
		'user': user,
		'about': about,
		'all_friends': all_friends(user['id_user']),
		'location': location,
		'tags': tags
	}
	return render_template("timeline-about.html", data=data)


@app.route('/profile/album/')
@app.route('/user/id<int:id_user>/album/')
def album(id_user=None):
	if not session.get('id_user_logged') and not id_user:
		return redirect('/')
	if id_user:
		user = get_user_by_id(id_user)
		album = user_images(id_user)
	else:
		user = get_user_by_id(session.get('id_user_logged'))
		album = user_images(session.get('id_user_logged'))
	if session.get('id_user_logged') and not user['id_user'] == session.get('id_user_logged'):
		msg = "User: " + session.get('user_data')['first_name'] + " " + \
			session.get('user_data')['last_name'] + " view your profile"
		add_notification(user['id_user'], msg)
	data = {
		'user': user,
		'all_friends': all_friends(user['id_user']),
		'album': album
	}
	return render_template("timeline-album.html", data=data)


@app.route('/profile/album/create/')
def create_album():
	if session.get('id_user_logged'):
		data = {
			'user': get_user_by_id(session.get('id_user_logged')),
			'all_friends': all_friends(session.get('id_user_logged'))
		}
		return render_template("edit-profile-album.html", data=data)
	return redirect('/')


@app.route('/ajax_save_album/', methods=['POST'])
def ajax_save_album():
	if session.get('id_user_logged'):
		if request.files:
			images = request.files.getlist('images[]')
			i = 0
			for image in images:
				filename = str(datetime.now().timestamp()).replace(".", "") + "-" + session.get('user_data')['first_name'] + \
					"-" + session.get('user_data')['last_name'] + "-" + str(i) + "." + image.filename.rsplit('.', 1)[1].lower()
				res = allowed_ex(image.content_type)
				if res:
					photos.save(image, "img", filename)
					add_image(session.get('id_user_logged'), "/static/uploads/img/" + filename)
					i = i + 1
					user = get_user_by_id(session.get('id_user_logged'))
					rating = user['rating'] + 5
					update_rating(rating, session.get('id_user_logged'))
		return redirect(request.referrer)
	return redirect('/')


@app.route('/user/id<int:id_user>/report/')
def report(id_user):
	if not session.get('id_user_logged') and not id_user:
		return redirect('/')
	if if_user_reported(session.get('id_user_logged'), id_user) or session.get('id_user_logged') == id_user:
		return redirect(request.referrer)
	report_user(session.get('id_user_logged'), id_user)
	if session.get('id_user_logged') and not id_user == session.get('id_user_logged'):
		msg = "User: " + session.get('user_data')['first_name'] + " " + \
			session.get('user_data')['last_name'] + " send report to you."
		add_notification(id_user, msg)
		user = get_user_by_id(id_user)
		rating = user['rating'] - 10
		update_rating(rating, id_user)
	return redirect(request.referrer)


@app.route('/user/id<int:id_user>/block/')
def block(id_user):
	if not session.get('id_user_logged') and not id_user:
		return redirect('/')
	if if_user_blocked(session.get('id_user_logged'), id_user) or session.get('id_user_logged') == id_user:
		return redirect(request.referrer)
	block_user(session.get('id_user_logged'), id_user)
	if session.get('id_user_logged') and not id_user == session.get('id_user_logged'):
		msg = "User: " + session.get('user_data')['first_name'] + " " + \
			session.get('user_data')['last_name'] + " block you."
		add_notification(id_user, msg)
		user = get_user_by_id(id_user)
		rating = user['rating'] - 10
		update_rating(rating, id_user)
	return redirect(request.referrer)

