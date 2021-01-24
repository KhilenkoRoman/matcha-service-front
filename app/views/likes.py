from app import app
from flask import request, session
from app.models.likes import like, dislike, unlike, undislike, liked, disliked
from app.views.notifications import add_notification
from app.models.users import update_rating, get_user_by_id
from app.models.posts import get_post_by_id


@app.route('/ajax_like/', methods=['POST'])
def ajax_like():
	id_user = session.get('id_user_logged')
	id_post = request.form.get('post_id')

	if id_user:
		if liked(id_user, id_post):
			res = unlike(id_user, id_post)
			if not res:
				user_post = get_post_by_id(id_post)
				if not user_post['id_user_from'] == id_user:
					msg = "User: " + session.get('user_data')['first_name'] + " " + \
						session.get('user_data')['last_name'] + " unlike your post"
					add_notification(user_post['id_user_from'], msg)
					user = get_user_by_id(user_post['id_user_from'])
					rating = user['rating'] - 5
					update_rating(rating, user_post['id_user_from'])
				return "unliked"
		else:
			res = like(id_user, id_post)
			if not res:
				user_post = get_post_by_id(id_post)
				if not user_post['id_user_from'] == id_user:
					msg = "User: " + session.get('user_data')['first_name'] + " " + \
						session.get('user_data')['last_name'] + " like your post"
					add_notification(user_post['id_user_from'], msg)
					user = get_user_by_id(user_post['id_user_from'])
					rating = user['rating'] + 5
					update_rating(rating, user_post['id_user_from'])
				return "liked"
	return "Fail"


@app.route('/ajax_dislike/', methods=['POST'])
def ajax_dislike():
	id_user = session.get('id_user_logged')
	id_post = request.form.get('post_id')

	if id_user:
		if disliked(id_user, id_post):
			res = undislike(id_user, id_post)
			if not res:
				user_post = get_post_by_id(id_post)
				if not user_post['id_user_from'] == id_user:
					msg = "User: " + session.get('user_data')['first_name'] + " " + \
						session.get('user_data')['last_name'] + " undislike your post"
					add_notification(user_post['id_user_from'], msg)
					user = get_user_by_id(user_post['id_user_from'])
					rating = user['rating'] + 10
					update_rating(rating, user_post['id_user_from'])
				return "undisliked"
		else:
			res = dislike(id_user, id_post)
			if not res:
				user_post = get_post_by_id(id_post)
				if not user_post['id_user_from'] == id_user:
					msg = "User: " + session.get('user_data')['first_name'] + " " + \
						session.get('user_data')['last_name'] + " dislike your post"
					add_notification(user_post['id_user_from'], msg)
					user = get_user_by_id(user_post['id_user_from'])
					rating = user['rating'] - 10
					update_rating(rating, user_post['id_user_from'])
				return "disliked"
	return "Fail"

