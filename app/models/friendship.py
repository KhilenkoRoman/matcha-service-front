from app.config.databse import db_connect


def add_friend(id_requester, id_user_requested):
	arguments = [id_requester, id_user_requested]
	sql = "INSERT INTO friendships (id_requester, id_user_requested) VALUES (?,?)"
	res = db_connect(sql, arguments)
	return res


def check_friends(id_requester, id_user_requested):
	arguments = [id_requester, id_user_requested]
	sql = "SELECT * FROM friendships WHERE id_requester=? AND id_user_requested=?"
	res = db_connect(sql, arguments)
	if res:
		return res[0]
	return res


def delete_user_request(id_requester, id_user_requested):
	arguments = [id_requester, id_user_requested]
	sql = "DELETE FROM friendships WHERE id_requester=? AND id_user_requested=?"
	res = db_connect(sql, arguments)
	return res


def confirm_user_request(id_requester, id_user_requested):
	arguments = [id_requester, id_user_requested]
	sql = "UPDATE friendships SET status=1 WHERE id_requester=? AND id_user_requested=?"
	res = db_connect(sql, arguments)
	return res


def all_friends(id_user):
	arguments = [id_user, id_user]
	sql = "SELECT * FROM friendships WHERE status=1 AND (id_requester=? OR id_user_requested=?)"
	res = db_connect(sql, arguments)
	return res


def all_friends_request(id_user):
	arguments = [id_user, id_user]
	sql = "SELECT * FROM friendships WHERE status=0 AND (id_requester=? OR id_user_requested=?)"
	res = db_connect(sql, arguments)
	return res
