from app import app
from flask import request, session
from app.models.tags import *

tags_to_fa = {}
tags_to_fa.update({'icon ion-ios-camera': ['camera', 'photo', 'model', 'photgraphy']})
tags_to_fa.update({'icon ion-android-plane': ['travel', 'traveling', 'fly', 'flying']})
tags_to_fa.update({'icon ion-android-restaurant': ['eating', 'restaurant', 'dinner']})
tags_to_fa.update({'fas fa-gamepad': ['game', 'games', 'gaming', 'dota', 'dota2']})
tags_to_fa.update({'fas fa-fighter-jet': ['fighter', 'jet', 'fighters', 'aviation', 'interseptor']})
tags_to_fa.update({'fas fa-female': ['girl', 'gitls']})
tags_to_fa.update({'fab fa-grunt': ['boar', 'kaban']})
tags_to_fa.update({'fab fa-python': ['python', 'python3']})
tags_to_fa.update({'fab fa-itunes-note': ['music', 'songs']})
tags_to_fa.update({'fab fa-js': ['js', 'java script', 'java-script']})
tags_to_fa.update({'fab fa-instagram': ['insta', 'instagram', 'dich', 'хрень', 'ерунда']})
tags_to_fa.update({'fab fa-steam': ['steam']})
tags_to_fa.update({'fas fa-wine-glass': ['wine', 'drink', 'drinking', 'бухать']})


@app.route('/ajax_add_tag', methods=['POST'])
def ajax_add_tag():
	id_user = request.form.get('id_user')
	tag = request.form.get('tag_name')
	tag_sign = ""

	try:
		id_tag = check_tag(tag)[0].get('id_tag')
	except:
		id_tag = None

	if not id_tag:
		for key, value in tags_to_fa.items():
			if tag.lower() in value:
				tag_sign = key
		add_tag(tag, tag_sign)
		id_tag = check_tag(tag)[0].get('id_tag')

	if check_tag_in_user(id_tag, id_user):
		return "tag_exist"

	res = add_tag_to_user(id_tag, id_user)
	if not res:
		for key, value in tags_to_fa.items():
			if tag.lower() in value:
				tag_sign = key
		return tag_sign
	else:
		return "error"


@app.route('/ajax_remove_tag', methods=['POST'])
def ajax_remove_tag():
	id_user = request.form.get('id_user')
	tag = request.form.get('tag_name')

	try:
		id_tag = check_tag(tag)[0].get('id_tag')
	except:
		return "error_no_tag"
	res = remove_tag_from_user(id_tag, id_user)
	if not res:
		return "success"
	else:
		return "error"
