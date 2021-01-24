from app.config.databse import db_connect


def get_location_by_id(id_user):
	agruments = [id_user]
	sql = "SELECT * FROM location WHERE id_user = ?"
	res = db_connect(sql, agruments)
	return res


def set_coords_to_id(id_user, latitude, longitude):
	agruments = [id_user, latitude, longitude]
	sql = "INSERT INTO location (id_user, latitude, longitude) VALUES (?, ?, ?)"
	res = db_connect(sql, agruments)
	return res


def update_coords_by_id(id_user, latitude, longitude):
	agruments = [latitude, longitude, id_user]
	sql = "UPDATE location SET latitude = ?, longitude = ? WHERE id_user = ?"
	res = db_connect(sql, agruments)
	return res


