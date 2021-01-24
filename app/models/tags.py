from app.config.databse import db_connect


def add_tag(tag, tag_sign):
	arguments = [tag, tag_sign]
	sql = "INSERT INTO tags (tag, tag_sign) VALUES (?, ?)"
	res = db_connect(sql, arguments)
	return res


def check_tag(tag):
	arguments = [tag]
	sql = "SELECT id_tag FROM tags WHERE tag=?"
	res = db_connect(sql, arguments)
	return res


def add_tag_to_user(id_tag, id_user):
	arguments = [id_tag, id_user]
	sql = "INSERT INTO tags_con (id_tag, id_user) VALUES (?, ?)"
	res = db_connect(sql, arguments)
	return res


def remove_tag_from_user(id_tag, id_user):
	arguments = [id_tag, id_user]
	sql = "DELETE FROM tags_con WHERE id_tag = ? AND id_user = ?"
	res = db_connect(sql, arguments)
	return res


def check_tag_in_user(id_tag, id_user):
	arguments = [id_tag, id_user]
	sql = "SELECT * FROM tags_con WHERE id_tag = ? AND id_user = ?"
	res = db_connect(sql, arguments)
	return res


def get_tags_by_id_user(id_user):
	arguments = [id_user]
	sql = "SELECT * FROM tags INNER JOIN tags_con tc on tags.id_tag = tc.id_tag WHERE tc.id_user = ?"
	res = db_connect(sql, arguments)
	return res
