# users.py
""" Module contains Data structure for a User"""


class User:
    """class defines the user data structure"""

    def __init__(self, id, user_name):
        self.id = id
        self.userName = user_name

    def __str__(self):
        return "User(id='%s',username='%s')" % (self.id, self.userName)


users = [
    User(1, 'user1'),
    User(2, 'user2'),
    User(3, 'admin')
]
user_name_table = {user.userName: user for user in users}
user_id_table = {user.id: user for user in users}


def verify_user_id(user_id):
    """verify user id
    Expects id of type int
    Returns:
        True if id exists
        False if id does not exist"""
    if user_id not in user_id_table.keys():
        return False
    return True
