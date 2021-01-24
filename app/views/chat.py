from app import app
from flask_socketio import SocketIO, join_room, leave_room, emit, send
from flask import Flask, render_template, request, session, redirect, url_for
from app.models.chat import *
from app.models.users import *
from app.models.messages import *
from collections import Counter
from datetime import datetime
import html
from app.views.notifications import add_notification
from app.models.friendship import all_friends, all_friends_request
from app.views.notifications import get_users_online_list

chat_users_sid_to_id = {}
chat_users_sid_to_room = {}


def create_room(user_from, user_to):
	room_name = str(user_from + user_to)
	create_chat_room_in_db(room_name)
	add_user_to_chat_room(room_name, user_from)
	add_user_to_chat_room(room_name, user_to)
	return room_name


def check_user_online(user_id):
	for key, value in chat_users_sid_to_id.items():
		if str(value) == user_id:
			return 1
	return 0


@app.route('/chat', methods=['POST', 'GET'])
def chat():
	if not session.get('id_user_logged'):
		return redirect(url_for('index'))
	context = {'chat_room': 'room_for_all'}
	data = {
		'friends': all_friends_request(session.get('id_user_logged')),
		"all_friends": all_friends(session.get("id_user_logged")),
		'users_online': get_users_online_list()
	}

	try:
		room_data = get_chat_room_by_name(request.form['room_name'])
		messages = get_messages_by_room_id(room_data[0]['id_chat_room'])
		if messages:
			context['messages'] = messages
		else:
			context['messages'] = None
	except:
		return redirect(url_for('index'))

	try:
		context['chat_room'] = request.form['room_name']
		context['chat_to'] = check_user(request.form['chat_to'], request.form['chat_to'])
		print("-----")
		print(context['chat_to'])
		print(check_user(request.form['chat_to'], request.form['chat_to']))
		print(request.form['chat_to'])
		print("-----")
		context['chat_from'] = check_user(request.form['chat_from'], request.form['chat_from'])
	except:
		return redirect(url_for('index'))

	return render_template('newsfeed-messages.html', context=context, data=data)


@app.route('/ajax_create_chat', methods=['POST'])
def ajax_create_chat():
	user_from = request.form['chat_from']
	user_to = request.form['chat_to']
	room_name = None

	res = check_room_by_users(user_from, user_to)
	if not res:
		room_name = create_room(user_from, user_to)
	else:
		rooms = []
		for i in res:
			rooms.append(i['room_name'])
		for room, i in Counter(rooms).items():
			if i == 2:
				room_name = room
		if room_name is None:
			room_name = create_room(user_from, user_to)
	return room_name


# @socketio.on("test_print", namespace='/chat')
# def test_print(msg):
# 	print(msg['room'])
#
#
# @socketio.on('message', namespace='/chat')
# def message(data):
# 	room = chat_users_sid_to_room[request.sid]
# 	user_data = get_user_by_id(data['user_id'])
# 	data['user_data'] = user_data
# 	data['date_time'] = "{:%Y-%m-%d %H:%M:%S}".format(datetime.now())
# 	data['message'] = html.escape(data['message'])
# 	room_data = get_chat_room_by_name(room)
# 	user_to_online = check_user_online(data['user_to_id'])
# 	save_message(room_data[0]['id_chat_room'], data['user_id'], data['user_to_id'], data['message'], user_to_online)
# 	emit('message_from_server', data, room=room)
# 	if not user_to_online:
# 		add_notification(data['user_to_id'], "new message from " + user_data['first_name'] + " " + user_data['last_name'])
#
#
# @socketio.on('connect', namespace='/chat')
# def connect():
# 	chat_users_sid_to_id[request.sid] = session.get('id_user_logged')
#
#
# @socketio.on('disconnect', namespace='/chat')
# def disconnect():
# 	chat_users_sid_to_id.pop(request.sid)
# 	room = chat_users_sid_to_room[request.sid]
# 	leave_room(room)
# 	chat_users_sid_to_room.pop(request.sid)
#
#
# @socketio.on('join_room', namespace='/chat')
# def test_print(data):
# 	join_room(data['room'])
# 	chat_users_sid_to_room[request.sid] = data['room']
# 	mark_as_read(data['user_id'], data['user_to_id'])

# print("sid:" + request.sid + " joined room " + data['room'])
# print(chat_users_sid_to_id)
# print(chat_users_sid_to_room)
