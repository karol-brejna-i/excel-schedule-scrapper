import pickle

from scrapper.utils.exporters import ScheduleRedisExporter, ScheduleCsvExporter
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
    cre = ScheduleRedisExporter()
    result = cre.schedules_to_commands(schedule)
    print(result)
    with open("events.txt", "wb") as f:
        f.write(result.encode("utf-8"))

    print("---------------------------------")
    result = cre.areas_to_commands(areas)
    print(result)
    with open("areas.txt", "wb") as f:
        f.write(result.encode("utf-8"))
    print("---------------------------------")


def test_csv_exporter():
    print("---------------------------------")
    ace = ScheduleCsvExporter()
    result = ace.areas_to_string(areas)
    print(result)
    # with open("areas.csv", "wb") as f:
    #     f.write(result.encode("utf-8"))
    print("---------------------------------")
    result = ace.schedules_to_string(schedule)
    print(result)
    # with open("schedule.csv", "wb") as f:
    #     f.write(result.encode("utf-8"))
    print("---------------------------------")


test_redis_exporter()
test_csv_exporter()
