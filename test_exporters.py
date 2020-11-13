import pickle

from scrapper.calendar.exporters import CalendarRedisExporter, CalendarCsvExporter
from scrapper.walker import logger

import log_config

try:
    schedule = pickle.load(open("schedule.p", "rb"))
except Exception:
    logger.error("Error reading the schedule from pickled file `schedule.p` (produced by `test_parse_all.py`")

try:
    areas = pickle.load(open("areas.p", "rb"))
except Exception:
    logger.error("Error reading the schedule from pickled file `areas.p` (produced by `test_extract_metadata.py`")

print("Areas:")
print(areas)
print("Events:")
print(schedule)


def test_redis_exporter():
    print("---------------------------------")
    cre = CalendarRedisExporter()
    result = cre.calendars_to_commands(schedule)
    print(result)
    print("---------------------------------")
    result = cre.areas_to_commands(areas)
    print(result)
    print("---------------------------------")


def test_csv_exporter():
    print("---------------------------------")
    ace = CalendarCsvExporter()
    result = ace.areas_to_string(areas)
    print(result)
    # with open("areas.csv", "wb") as f:
    #     f.write(result.encode("utf-8"))
    print("---------------------------------")
    result = ace.calendars_to_string(schedule)
    print(result)
    # with open("schedule.csv", "wb") as f:
    #     f.write(result.encode("utf-8"))
    print("---------------------------------")


test_redis_exporter()
test_csv_exporter()
