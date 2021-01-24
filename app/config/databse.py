import sqlite3
from sqlite3 import Error

db_name = "db_matcha.sqlite3"


def dict_factory(cursor, row):
	d = {}
	for idx, col in enumerate(cursor.description):
		d[col[0]] = row[idx]
	return d


def db_connect(sql, arguments=None):
	# create a database connection to a SQLite database
	try:
		conn = sqlite3.connect(db_name)
		conn.row_factory = dict_factory
		c = conn.cursor()
		if arguments:
			c.execute(sql, arguments)
		else:
			c.execute(sql)
		conn.commit()
		return c.fetchall()
	except Error as e:
		return e
	finally:
		conn.close()


def db_insert(sql, arguments=None):
	# create a database connection to a SQLite database
	try:
		conn = sqlite3.connect(db_name)
		conn.row_factory = dict_factory
		c = conn.cursor()
		if arguments:
			c.execute(sql, arguments)
		else:
			c.execute(sql)
		conn.commit()
		return c.lastrowid
	except Error as e:
		return e
	finally:
		conn.close()
