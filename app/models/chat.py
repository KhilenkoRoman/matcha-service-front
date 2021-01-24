from app.config.databse import db_connect


def get_chat_room_by_name(room_name):
	agruments = [room_name]
	sql = "SELECT * FROM chat_room WHERE room_name = ?"
	res = db_connect(sql, agruments)
	return res


def add_user_to_chat_room_by_id(id_chat_room, id_user):
	agruments = [id_chat_room, id_user]
	sql = "INSERT INTO chat_room_con (id_chat_room, id_user) VALUES (?,?)"
	res = db_connect(sql, agruments)
	return res


def check_room_by_users(user_login_from, user_login_to):
	agruments = [user_login_from, user_login_to]
	sql = "SELECT room_name ,users.login FROM chat_room INNER JOIN chat_room_con ON " \
		  "chat_room.id_chat_room=chat_room_con.id_chat_room INNER JOIN users ON chat_room_con.id_user=users.id_user " \
		  "WHERE users.login=? OR users.login=? "
	res = db_connect(sql, agruments)
	return res


def create_chat_room_in_db(room_name):
	agruments = [room_name]
	sql = "INSERT INTO chat_room (room_name) VALUES (?)"
	res = db_connect(sql, agruments)
	return res


def add_user_to_chat_room(chat_room_name, login):
	agruments = [chat_room_name, login]
	sql = "INSERT INTO chat_room_con (id_chat_room, id_user) VALUES ((SELECT id_chat_room FROM chat_room WHERE room_name=?),(SELECT id_user FROM users WHERE login=?))"
	res = db_connect(sql, agruments)
	return res
