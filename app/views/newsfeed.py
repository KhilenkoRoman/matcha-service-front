from app import app
from flask import session, render_template, redirect
from app.models.friendship import all_friends_request, all_friends
from app.models.users import get_user_by_id, get_users_and_locations, if_user_blocked
from app.views.geolocation import calculate_distanse
from app.views.notifications import get_users_online_list


def get_not_friends(id_user):
	not_friends = []
	if not session.get('location'):
		return not_friends
	lon1 = session.get('location')[0].get('longitude')
	lat1 = session.get('location')[0].get('latitude')

	users_list = get_users_and_locations(id_user)
	friends_list = all_friends(id_user)

	friends_id = []
	for i in friends_list:
		if i['id_requester'] != id_user:
			friends_id.append(i['id_requester'])
		if i['id_user_requested'] != id_user:
			friends_id.append(i['id_user_requested'])

	for user in users_list:
		if user['id_user'] not in friends_id and not if_user_blocked(id_user, user['id_user']):
			lon2 = user.get('longitude')
			lat2 = user.get('latitude')
			user['distance'] = round(calculate_distanse(lat1, lon1, lat2, lon2), 2)
			if user['distance'] < 100:
				not_friends.append(user)
	return not_friends


@app.route('/friends/')
def friends():
	if session.get('id_user_logged'):
		data = {
			'user': get_user_by_id(session.get('id_user_logged')),
			'get_by_id': get_user_by_id,
			'friends': all_friends_request(session.get('id_user_logged')),
			"all_friends": all_friends(session.get("id_user_logged")),
			'users_online': get_users_online_list()
		}
		return render_template("newsfeed-friends.html", data=data)
	return redirect("/")


@app.route('/people_nearby/')
def people_nearby():
	if not session.get('id_user_logged'):
		return redirect('/')
	id_user = session.get('id_user_logged')
	user = get_user_by_id(id_user)

	not_friends = get_not_friends(id_user)
	session['not_friends'] = not_friends

	data = {
		'user': user,
		'all_friends': all_friends(user['id_user']),
		'not_friends': not_friends,
		'users_online': get_users_online_list()
	}
	return render_template("newsfeed-people-nearby.html", data=data)
