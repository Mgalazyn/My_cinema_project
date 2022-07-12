from new_movies import users_directory, permissions, configuration
from new_movies.datetime_preferences import DatetimePreference
from new_movies.exceptions import UserNotFound, ActionNotAllowed

from datetime import datetime, timedelta


def login():
    failed_login_attempt = 0
    last_attempt_datetime = None
    lock_time = timedelta()
    while True:
        user_login = input("Type in your login: ")

        if last_attempt_datetime is not None:
            login_attempts_invterval = datetime.now() - last_attempt_datetime
            last_attempt_datetime = datetime.now()
            if login_attempts_invterval < lock_time:
                failed_login_attempt += 1
                print('Authorization failure')
                print(f'Please wait {lock_time} s  before next attempt')
                continue
        last_attempt_datetime = datetime.now()

        try:
            return users_directory.find_user_by_login(user_login)
        except UserNotFound:
            failed_login_attempt += 1
            print("This user doesn't exist")
            if failed_login_attempt >= configuration.AUTH_FAILED_EXTENDED_LIMIT:
                lock_time = configuration.AUTH_FAILED_LOCK_TIME * 2
                print(f"Authorization failed, wait {lock_time} s ")
            elif failed_login_attempt >= configuration.AUTH_FAILED_LIMIT:
                lock_time = configuration.AUTH_FAILED_LOCK_TIME
                print(f"Authorization failed , you have to wait {lock_time} s")


def select_datetime_preferences(user):
    print("Available formats:")
    for option_index, datetime_preference in enumerate(DatetimePreference):
        print(f"{option_index}) {datetime_preference}")

    selected_option = int(input("Select an option: "))
    user.datetime_preferences = DatetimePreference.instance_by_index(selected_option)


def refresh_credits(acting_user, user_to_be_refreshed):
    if permissions.is_admin(acting_user) or permissions.is_moderator(acting_user):
        user_to_be_refreshed.credits_left = 5
    else:
        raise ActionNotAllowed()
