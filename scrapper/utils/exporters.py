import csv
import io
from typing import Union, List

from scrapper.env_config import CURRENT_SCHEDULE
from scrapper.model.schedule import Schedule, Area


class ScheduleRedisExporter:

    @classmethod
    def get_area_hset_statement(cls, area):
        hash_key = f'area:{area.name}'
        return f'HMSET "{hash_key}" name "{area.name}" source "{area.source}" description "{area.description}"'

    @staticmethod
    def get_schedule_hset_statement(schedule: Schedule, current_schedule: str = CURRENT_SCHEDULE):
        hash_key = f'schedule:{current_schedule}:{schedule.area}'
        from_month = min(x for x in schedule.months if schedule.months[x])
        to_month = max(x for x in schedule.months if schedule.months[x])

        return f'HMSET "{hash_key}" source "{schedule.source}" description "{schedule.description}" from_month {from_month} to_month {to_month}'

    @staticmethod
    def get_event_hset_statement(area, month_of_year, day_of_month, events, current_schedule: str = CURRENT_SCHEDULE):
        hash_key = f'events:{current_schedule}:{month_of_year:02}:{day_of_month:02}:{area}'
        events_string = " ".join(str(s) for s in events)
        return f'HMSET "{hash_key}" area "{area}" month_of_year {month_of_year} day_of_month {day_of_month} events "{events_string}"'

    @classmethod
    def schedules_to_commands(cls, schedule: Union[Schedule, List[Schedule]]):
        data = schedule if type(schedule) == list else [schedule]

        result = ""
        for d in data:
            area = d.area

            # dump schedule data
            result += cls.get_schedule_hset_statement(d) + "\n"

            # dump event data
            for month in (d.months[x] for x in d.months if d.months[x]):
                for j, days in month.days.items():
                    if days.events:
                        result += cls.get_event_hset_statement(area, month.month_of_year, days.day_of_month,
                                                               days.events) + "\n"
        return result

    @classmethod
    def areas_to_commands(cls, area: Union[Area, List[Area]]):
        data = area if type(area) == list else [area]

        result = ""
        for d in data:
            result += cls.get_area_hset_statement(d) + "\n"

        return result


class ScheduleCsvExporter:

    @classmethod
    def schedules_to_string(cls, schedule: Union[Schedule, List[Schedule]]):
        data = schedule if type(schedule) == list else [schedule]

        output = io.StringIO()
        writer = csv.writer(output, quoting=csv.QUOTE_NONNUMERIC)

        for d in data:
            # dump event data
            for month in (d.months[x] for x in d.months if d.months[x]):
                for j, days in month.days.items():
                    if days.events:
                        events_string = " ".join(str(s) for s in days.events)
                        writer.writerow([d.area, d.year, month.month_of_year, days.day_of_month, events_string])

        return output.getvalue()

    @classmethod
    def areas_to_string(cls, area: Union[Area, List[Area]], excel_compatible=False):
        data = area if type(area) == list else [area]

        output = io.StringIO()
        writer = csv.writer(output, quoting=csv.QUOTE_NONNUMERIC)

        for d in data:
            writer.writerow([d.name, d.source, d.description])

        return output.getvalue()
