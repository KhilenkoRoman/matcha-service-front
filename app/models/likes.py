from app.config.databse import db_connect


def like(id_user, id_post):
	arguments = [id_user, id_post]
	sql = "INSERT INTO likes (id_user, id_post) VALUES (?, ?)"
	res = db_connect(sql, arguments)
	return res


def unlike(id_user, id_post):
	arguments = [id_user, id_post]
	sql = "DELETE FROM likes WHERE id_user=? AND id_post=?"
	res = db_connect(sql, arguments)
	return res


def dislike(id_user, id_post):
	arguments = [id_user, id_post]
	sql = "INSERT INTO dislikes (id_user, id_post) VALUES (?, ?)"
	res = db_connect(sql, arguments)
	return res


def undislike(id_user, id_post):
	arguments = [id_user, id_post]
	sql = "DELETE FROM dislikes WHERE id_user=? AND id_post=?"
	res = db_connect(sql, arguments)
	return res


def liked(id_user, id_post):
	arguments = [id_user, id_post]
	sql = "SELECT * FROM likes WHERE id_user=? AND id_post=?"
	res = db_connect(sql, arguments)
	if res:
		return True
	return False


def disliked(id_user, id_post):
	arguments = [id_user, id_post]
	sql = "SELECT * FROM dislikes WHERE id_user=? AND id_post=?"
	res = db_connect(sql, arguments)
	if res:
		return True
	return False


def post_likes(id_post):
	arguments = [id_post]
	sql = "SELECT * FROM likes WHERE id_post=?"
	res = db_connect(sql, arguments)
	return res


def post_dislikes(id_post):
	arguments = [id_post]
	sql = "SELECT * FROM dislikes WHERE id_post=?"
	res = db_connect(sql, arguments)
	return res


def len_post_likes(id_post):
	res = post_likes(id_post)
	count = len(res)
	return count


def len_post_dislikes(id_post):
	res = post_dislikes(id_post)
	count = len(res)
	return count


def dell_post_likes(post_id):
	arguments = [post_id]
	sql = "DELETE FROM likes WHERE id_post=?"
	res = db_connect(sql, arguments)
	return res


def dell_post_dislikes(post_id):
	arguments = [post_id]
	sql = "DELETE FROM dislikes WHERE id_post=?"
	res = db_connect(sql, arguments)
	return res

