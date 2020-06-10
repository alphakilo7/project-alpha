from django.test import TestCase
import orm

# Create your tests here.
def run():
	bu = orm.BasicUserForm(db_name="project_alpha", table="users")
	bu.add_user("A", "K", "a@k.in", "alpha", "ahpla")

if __name__ == "__main__":
	run()
