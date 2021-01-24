from app.config.databse import db_connect


def save_message(id_chat_room, id_from, id_to, msg, read):
	agruments = [id_chat_room, id_from, id_to, msg, read]
	sql = "INSERT INTO messages (id_chat_room, id_user_from, id_user_to, message, read_status, date_creation) VALUES (?,?,?,?,?, datetime('now', 'localtime'))"
	res = db_connect(sql, agruments)
	return res


def get_messages_by_room_id(room_id):
	agruments = [room_id]
	sql = "SELECT * FROM messages WHERE id_chat_room = ?"
	res = db_connect(sql, agruments)
	return res


def mark_as_read(id_user, id_user_from):
	agruments = [id_user, id_user_from]
	sql = "UPDATE messages SET read_status = 1 WHERE id_user_to=? and id_user_from=?"
	res = db_connect(sql, agruments)
	return res
