from app import ShoesObject, UsersObject
import pytest


def test_example_postgres(postgresql):
    """Check main postgresql fixture."""
    cur = postgresql.cursor()
    cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
    postgresql.commit()
    cur.close()

def test_add_user():
    user = UsersObject(name="test", email="test@email.com")

    assert user.name == 'test'
    assert user.email == 'test@email.com'
    assert type(user) is UsersObject
