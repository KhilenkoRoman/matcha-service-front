from app import app
from flask import render_template, session, redirect
from app.models.users import get_user_by_id
from app.models.friendship import check_friends, all_friends


@app.route('/profile/friends/')
@app.route('/user/id<int:id_user>/friends/')
def user_friends(id_user=None):
	if not session.get('user_data') and not id_user:
		return redirect('/')
	if id_user:
		user = get_user_by_id(id_user)
	else:
		user = session.get('user_data')
	friends = all_friends(user['id_user'])
	data = {
		'user': user,
		'get_by_id': get_user_by_id,
		'friends': friends,
		'all_friends': friends
	}
	return render_template("timeline-friends.html", data=data)

