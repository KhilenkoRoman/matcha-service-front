from app import app
from flask import request, session, render_template, redirect
from app.models.tags import *
from datetime import date, datetime
from app.models.users import get_users_search
from app.views.geolocation import calculate_distanse
from app.models.tags import get_tags_by_id_user
from app.models.friendship import all_friends
import json


def get_search_users(id_user):
	users = []
	if not session.get('location'):
		return users
	lon1 = session.get('location')[0].get('longitude')
	lat1 = session.get('location')[0].get('latitude')

	users = get_users_search(id_user)
	for user in users:
		lon2 = user.get('longitude')
		lat2 = user.get('latitude')
		user['distance'] = round(calculate_distanse(lat1, lon1, lat2, lon2), 2)
		user['age'] = date.today().year - datetime.strptime(user['date_birth'], '%Y-%m-%d %H:%M:%S').year
	return users


@app.route('/search/')
def search():
	id_user = session.get('id_user_logged')
	if id_user:
		users_query = get_search_users(id_user)
		data = {
			'users_query': users_query,
			'all_friends': all_friends(session.get('id_user_logged'))
		}
		return render_template('people-search.html', data=data)
	return redirect("/")


@app.route('/ajax_filter_apply', methods=['POST'])
def ajax_filter_apply():
	id_user = session.get('id_user_logged')
	users = get_search_users(id_user)
	filtered_users = []

	for user in users:
		flag = True
		if request.form['age_from']:
			if user['age'] <= int(request.form['age_from']):
				flag = False
		if request.form['age_to']:
			if user['age'] >= int(request.form['age_to']):
				flag = False
		if request.form['fame_from']:
			if user['rating'] <= int(request.form['fame_from']):
				flag = False
		if request.form['fame_to']:
			if user['rating'] >= int(request.form['fame_to']):
				flag = False
		if request.form['country']:
			if user['location'].find(request.form['country']) == -1:
				flag = False
		if request.form['city']:
			if user['location'].find(request.form['city']) == -1:
				flag = False
		tags = get_tags_by_id_user(user['id_user'])
		tags_list = []
		for tag in tags:
			tags_list.append(tag['tag'])
		if request.form['tag_1']:
			if not request.form['tag_1'] in tags_list:
				flag = False
		if request.form['tag_2']:
			if not request.form['tag_2'] in tags_list:
				flag = False
		if request.form['tag_3']:
			if not request.form['tag_3'] in tags_list:
				flag = False
		if int(request.form['gender']) != 0:
			if int(request.form['gender']) != int(user['gender']):
				flag = False
		if flag:
			filtered_users.append(user)

	if request.form['sort'] == 'dist_asc':
		filtered_users = sorted(filtered_users, key=lambda k: k['distance'])
	if request.form['sort'] == 'dist_desc':
		filtered_users = sorted(filtered_users, key=lambda k: k['distance'], reverse=True)
	if request.form['sort'] == 'age_asc':
		filtered_users = sorted(filtered_users, key=lambda k: k['age'])
	if request.form['sort'] == 'age_desc':
		filtered_users = sorted(filtered_users, key=lambda k: k['age'], reverse=True)
	if request.form['sort'] == 'rate_asc':
		filtered_users = sorted(filtered_users, key=lambda k: k['rating'])
	if request.form['sort'] == 'rate_desc':
		filtered_users = sorted(filtered_users, key=lambda k: k['rating'], reverse=True)

	return json.dumps(filtered_users)
