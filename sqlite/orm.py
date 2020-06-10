import sqlite3
import pandas as pd


class BasicUserForm:
	def __init__(self, db_name, table):
		self.db_name = db_name + ".sqlite3"
		self.db = sqlite3.connect(self.db_name)
		self.table = table
		try:
			self.db.execute("SELECT * FROM %s;" % self.table)
			print("Database '%s' and Table '%s' exists!" % (self.db_name, self.table))
		except sqlite3.OperationalError as e:
			self.db.execute("CREATE TABLE %s (uid INTEGER PRIMARY KEY AUTOINCREMENT, fname TEXT, lname TEXT, email TEXT, uname TEXT, pword TEXT);" % self.table)
			print("Database '%s' and Table '%s' Created!" % (self.db_name, self.table))

	def add_user(self, fname, lname, email, uname, pword):
		self.__fname = fname
		self.__lname = lname
		self.__email = email
		self.__uname = uname
		self.__pword = pword
		add_user_qry = 'INSERT INTO %(table)s (fname, lname, email, uname, pword) VALUES ("%(fn)s", "%(ln)s", "%(em)s", "%(un)s", "%(pw)s")' % {'table': self.table,'fn': self.__fname, 'ln': self.__lname, 'em': self.__email, 'un': self.__uname, 'pw': self.__pword}
		print(add_user_qry)
