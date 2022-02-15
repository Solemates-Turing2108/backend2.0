from app import ShoesObject, UsersObject
import pytest

#
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
# 
# with app.test_client() as c:
#     rv = c.post('/api/v1/shoes', json={
#                                             "side": "left",
#                                             "style": "boots",
#                                             "size": 18,
#                                             "photo_url": "url",
#                                             "description": "cool shoes",
#                                             "brand": "cool brand",
#                                             "user_id": 4
#                                         })
#     json_data = rv.get_json()
    # assert verify_token(email, json_data['token'])
