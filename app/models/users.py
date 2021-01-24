from app.config.databse import db_connect, db_insert


def user_to_db(login, email, pwd, token, first_name, last_name, gender, birthday, cover):
	agruments = [login, email, pwd, token, first_name, last_name, gender, birthday, cover]
	sql = "INSERT INTO users (login, email, password, token, first_name, last_name, gender, date_birth, cover) VALUES (?,?,?,?,?,?,?,?,?)"
	res = db_insert(sql, agruments)
	return res


def check_user(login, email):
	agruments = [login, email]
	sql = "SELECT * FROM users WHERE login=? OR email=?"
	res = db_connect(sql, agruments)
	return res


def check_user_token(email):
	agruments = [email]
	sql = "SELECT id_user, token, active FROM users WHERE email=?"
	res = db_connect(sql, agruments)
	return res


def activate_user(id_user):
	agruments = [id_user]
	sql = "UPDATE users SET active = 1, token = NULL WHERE id_user=?"
	res = db_connect(sql, agruments)
	return res


def user_update_token(id_user, token):
	agruments = [token, id_user]
	sql = "UPDATE users SET token = ? WHERE id_user=?"
	res = db_connect(sql, agruments)
	return res


def user_new_pwd(id_user, pwd):
	agruments = [pwd, id_user]
	sql = "UPDATE users SET password = ?, token = NULL WHERE id_user=?"
	res = db_connect(sql, agruments)
	return res


def get_user_by_id(id_user):
	arguments = [id_user]
	sql = "SELECT * FROM users WHERE id_user = ?"
	res = db_connect(sql, arguments)
	if res:
		return res[0]
	return res


def get_about(id_user):
	arguments = [id_user]
	sql = "SELECT * FROM about WHERE id_user=?"
	res = db_connect(sql, arguments)
	if res:
		return res[0]
	return res


def create_about(id_user):
	arguments = [id_user]
	sql = "INSERT INTO about (id_user) VALUES (?)"
	res = db_connect(sql, arguments)
	return res


def update_basic_user(first_name, last_name, email, gender, sex_pref, theme, id_user):
	arguments = [first_name, last_name, email, gender, sex_pref, theme, id_user]
	sql = "UPDATE users SET first_name=?, last_name=?, email=?, gender=?, sex_pref=?, theme=? WHERE id_user=?"
	res = db_connect(sql, arguments)
	return res


def update_basic_about(location, biography, id_user):
	arguments = [location, biography, id_user]
	sql = "UPDATE about SET location=?, biography=? WHERE id_user=?"
	res = db_connect(sql, arguments)
	return res


def update_advanced_about(phone, language, status, political, fb, tw, inst, site, hobbies, tv_shows, movies, games, music, books, writers, others, id_user):
	arguments = [phone, language, status, political, fb, tw, inst, site, hobbies, tv_shows, movies, games, music, books, writers, others, id_user]
	sql = "UPDATE about SET phone=?, language=?, status=?, political=?, fb=?, tw=?, inst=?, site=?, hobbies=?, tv_shows=?, movies=?, games=?, music=?, books=?, writers=?, others=? WHERE id_user=?"
	res = db_connect(sql, arguments)
	return res


def update_avatar(avatar, id_user):
	arguments = [avatar, id_user]
	sql = "UPDATE users SET avatar=? WHERE id_user=?"
	res = db_connect(sql, arguments)
	return res


def add_image(id_user, img):
	arguments = [id_user, img]
	sql = "INSERT INTO images (id_user, img_src) VALUES (?, ?)"
	res = db_connect(sql, arguments)
	return res


def user_images(id_user):
	arguments = [id_user]
	sql = "SELECT * FROM images WHERE id_user=?"
	res = db_connect(sql, arguments)
	return res


def report_user(id_from, id_to):
	arguments = [id_from, id_to]
	sql = "INSERT INTO report (id_reporter, id_user) VALUES (?, ?)"
	res = db_connect(sql, arguments)
	return res


def if_user_reported(id_from, id_to):
	arguments = [id_from, id_to]
	sql = "SELECT * FROM report WHERE id_reporter=? AND id_user=?"
	res = db_connect(sql, arguments)
	if res:
		return True
	return False


def block_user(id_from, id_to):
	arguments = [id_from, id_to]
	sql = "INSERT INTO blocked (id_who_block, id_user) VALUES (?, ?)"
	res = db_connect(sql, arguments)
	return res


def if_user_blocked(id_from, id_to):
	arguments = [id_from, id_to]
	sql = "SELECT * FROM blocked WHERE id_who_block=? AND id_user=?"
	res = db_connect(sql, arguments)
	if res:
		return True
	return False


def update_rating(rating, id_user):
	arguments = [rating, id_user]
	sql = "UPDATE users SET rating=? WHERE id_user=?"
	res = db_connect(sql, arguments)
	return res


def get_users_and_locations(id_user):
	arguments = [id_user]
	sql = "SELECT * FROM users INNER JOIN location ON users.id_user = location.id_user WHERE users.id_user != ? AND users.active = 1"
	res = db_connect(sql, arguments)
	return res

def get_users_search(id_user):
	arguments = [id_user]
	sql = "SELECT * FROM users INNER JOIN location ON users.id_user = location.id_user INNER JOIN about ON users.id_user = about.id_user WHERE users.id_user != ? AND users.active = 1"
	res = db_connect(sql, arguments)
	return res