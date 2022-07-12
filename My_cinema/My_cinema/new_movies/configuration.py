from datetime import date, timedelta

UNLIMITED_WATCHING_START_DATE = date(year=2022, month=2, day=1)
UNLIMITED_WATCHING_END_DATE = date(year=2022, month=9, day=30)


AUTH_FAILED_LIMIT = 3
AUTH_FAILED_EXTENDED_LIMIT = 5
AUTO_FAILED_LOCK_TIME = timedelta(seconds=10)