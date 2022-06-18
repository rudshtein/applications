import sqlalchemy
from sqlalchemy import create_engine
import pytest


@pytest.fixture(scope='session')
def engine():
	db_string="postgresql://egr:egr@localhost:5432/main"
	db=create_engine(db_string)
	return db


def test_postgres_simple(engine):
	# db_string="postgresql://egr:egr@localhost:5432/main"
	# db=create_engine(db_string)

	# Create
	engine.execute("CREATE TABLE IF NOT EXISTS films (title text, director text, year text)")
	engine.execute("INSERT INTO films (title, director, year) VALUES ('Doctor Strange', 'Scott Derrickson', '2016')")

	# Read
	result_set=engine.execute("SELECT * FROM films")
	for r in result_set:
		#		print(r)
		pass

	engine.execute("UPDATE films SET title='Some2016Film' WHERE year='2016'")
	engine.execute("DELETE FROM films WHERE year='2016'")
