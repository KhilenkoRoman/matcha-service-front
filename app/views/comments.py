from app import app
from flask import session, redirect, request, jsonify
import html
from app.models.comments import add_comment, get_by_comment_id, dell_comment
from app.models.users import get_user_by_id


@app.route('/ajax_add_comment/', methods=['POST'])
def ajax_add_comment():
	if session.get('id_user_logged'):
		id_user = session.get('id_user_logged')
		id_post = request.form.get('id_post')
		text = html.escape(request.form.get('text').strip())

		if text:
			user = get_user_by_id(id_user)
			if user and user['active']:
				res = add_comment(id_user, id_post, text)
				if res:
					data = {
						'user_avatar': user['avatar'],
						'user_first_name': user['first_name'],
						'id_user': id_user,
						'id_post': id_post,
						'id_comment': res,
						'text': text
					}
					return jsonify(data)
	return "False"


@app.route('/ajax_dell_comment/', methods=['POST'])
def ajax_dell_comment():
	if session.get('id_user_logged'):
		id_user = session.get('id_user_logged')
		id_comment = request.form.get('id_comment')

		res = get_by_comment_id(id_comment)
		if res and res['id_user'] == id_user:
			dell = dell_comment(id_comment)
			if not dell:
				return "deleted"
	return "Fail"

