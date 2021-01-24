from app import app
from flask import request, session, url_for, render_template
from app.models.location import *
from math import sin, cos, sqrt, atan2, radians


@app.route('/ajax_set_location', methods=['POST'])
def ajax_set_location():
	res = set_coords_to_id(int(request.form.get('id_user')), request.form.get('latitude'), request.form.get('longitude'))
	if not res:
		session['location'] = get_location_by_id(int(request.form.get('id_user')))
	return "response"


@app.route('/ajax_update_location', methods=['POST'])
def ajax_update_location():
	res = update_coords_by_id(int(request.form.get('id_user')), request.form.get('latitude'), request.form.get('longitude'))
	print(res)
	if not res:
		session['location'] = get_location_by_id(int(request.form.get('id_user')))
	print(get_location_by_id(int(request.form.get('id_user'))))
	return "response"


def calculate_distanse(lat1, lon1, lat2, lon2):
	# approximate radius of earth in km
	earth_rad = 6373.0

	lat1 = radians(float(lat1))
	lon1 = radians(float(lon1))
	lat2 = radians(float(lat2))
	lon2 = radians(float(lon2))

	dlon = lon2 - lon1
	dlat = lat2 - lat1

	a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
	c = 2 * atan2(sqrt(a), sqrt(1 - a))

	distance = earth_rad * c

	return distance
