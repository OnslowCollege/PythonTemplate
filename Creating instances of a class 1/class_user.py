"""
class_user.py.

Created by: Arkin
Date: 15/02/2024
"""

class User:
    def __init__(self, full_name, birthday) -> None:
        self.name = full_name
        self.birthday = birthday # yyyymmdd

        # Extract first and last names
        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]
        pass

user = User("Dave Bowman", "19710315")
print(user.name)
print(user.first_name)
print(user.last_name)
print(user.birthday)