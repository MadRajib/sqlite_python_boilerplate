import sqlite3

con = None
def init_db(db):
	global con 
	con = sqlite3.connect(db)

def init_table(table_name):
	if not con:
		return
	cur = con.cursor()
	cur.execute(f"CREATE TABLE {table_name}(sl_no INTEGER  PRIMARY KEY, url TEXT NOT NULL, name TEXT, reported_price REAL NOT_NULL, current_price REAL NOT NULL)")

def insert_in_table(table_name, data):
	if not con:
		return
	cur = con.cursor()
	cur.execute(f"INSERT INTO {table_name} (url, name, reported_price, current_price) VALUES (?,?,?, ?)", (data['url'], data['name'], data['reported_price'], data['current_price']))
	con.commit()

def get_all_from_table(table_name):
	if not con:
		return
	cur = con.cursor()
	for row in cur.execute(f"SELECT * FROM {table_name}"):
		print(row)

def remove_from_table(table_name, id):
	if not con:
		return
	cur = con.cursor()
	cur.execute(f"DELETE FROM {table_name} WHERE sl_no =?", (id,))
	con.commit()

def update_from_table(table_name,id,new_value):
	if not con:
		return
	cur = con.cursor()
	cur.execute(f"UPDATE {table_name} SET current_price = ? WHERE sl_no= ?", (new_value, id))
	con.commit()


