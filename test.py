from app import ShoesObject, UsersObject
import pytest


# def test_example_postgres(postgresql):
#     """Check main postgresql fixture."""
#     cur = postgresql.cursor()
#     cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
#     postgresql.commit()
#     cur.close()

def test_add_user():
    user = UsersObject(name="test", email="test@email.com")

    assert user.name == 'test'
    assert user.email == 'test@email.com'
    assert type(user) is UsersObject

def test_add_shoe():
    shoe = ShoesObject(side="left", style="sneaker", size=7, photo_url='test_url', description='this is a test', brand='test_brand', user_id=3)

    assert shoe.side == 'left'
    assert shoe.style == 'sneaker'
    assert shoe.size == 7
    assert shoe.photo_url == 'test_url'
    assert shoe.description == 'this is a test'
    assert shoe.brand == 'test_brand'
    assert shoe.user_id == 3
    assert type(shoe) is ShoesObject
