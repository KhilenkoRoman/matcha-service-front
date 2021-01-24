from app.models.notifications import *
from flask import Flask, render_template, request, session, redirect, url_for, make_response
from flask_socketio import SocketIO, join_room, leave_room, emit, send

notif_users_sid_to_id = {}


def get_users_online_list():
	users_online = []
	for key, value in notif_users_sid_to_id.items():
		users_online.append(value)
	return users_online


def add_notification(id_user, notif_text):
	if not check_notification_in_db(id_user, notif_text):
		add_notification_to_db(id_user, notif_text)

		notifications = get_notifications_by_user_id(id_user)
		sid_to = None

		for key, value in notif_users_sid_to_id.items():
			if str(value) == str(id_user):
				emit('check_notifications', notifications, namespace='/notifications', room=key)
				sid_to = key
		if sid_to:
			emit('update_notifications', id_user, namespace='/notifications', room=sid_to)


# @socketio.on('connect', namespace='/notifications')
# def connect():
# 	notif_users_sid_to_id[request.sid] = session.get('id_user_logged')
#
#
# @socketio.on('disconnect', namespace='/notifications')
# def disconnect():
# 	notif_users_sid_to_id.pop(request.sid)
#
#
# @app.route('/ajax_clear_notifications', methods=['POST'])
# def ajax_clear_notifications():
# 	session.pop('notifications', None)
# 	res = remove_notifications_by_user_id(session.get('id_user_logged'))
#
# 	for key, value in notif_users_sid_to_id.items():
# 		if str(value) == str(session.get('id_user_logged')):
# 			emit('check_notifications', None, namespace='/notifications', room=key)
# 	if not res:
# 		return "notifications_clear"
# 	else:
# 		return "error"
#
#
# @app.route('/ajax_update_notifications', methods=['POST'])
# def ajax_update_notifications():
# 	session['notifications'] = get_notifications_by_user_id(request.form['id_user'])
# 	return "notifications_updated"
