from new_movies.exceptions import UserNotFound
from new_movies.user import User, Role, Admin

available_users = [
    User(
        first_name="Marcin",
        last_name="Galazyn",
        login="Marcin",
        credits_left=10,
        role=Role.USER,
        rented_movies=[],
    )
    ,
    Admin(
        first_name='Marcin',
        last_name='Developer',
        login="admin",
        credits_left=99,
        role=Role.USER,
        rented_movies=[],
    )
]


def find_user_by_login(login):
    lower_case_login = login.lower()
    for user in available_users:
        if lower_case_login == user.login.lower():
            return user
    raise UserNotFound()
