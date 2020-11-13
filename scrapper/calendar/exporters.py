import csv
import io
from typing import Union, List

from scrapper.model.schedule import Calendar, Area


class CalendarRedisExporter:

    @classmethod
    def get_area_hset_statement(cls, area):
        hash_key = f'area:{area.name}'
        return f'HMSET "{hash_key}" name "{area.name}" source "{area.source}" description "{area.description}"'

    @staticmethod
    def get_schedule_hset_statement(calendar: Calendar):
        hash_key = f'schedule:2020:{calendar.area}'
        from_month = min(x for x in calendar.months if calendar.months[x])
        to_month = max(x for x in calendar.months if calendar.months[x])

        return f'HMSET "{hash_key}" source "{calendar.source}" description "{calendar.description}" from_month {from_month} to_month {to_month}'

    @staticmethod
    def get_event_hset_statement(area, month_of_year, day_of_month, events):
        hash_key = f'events:2020:{month_of_year}:{day_of_month}:{area}'
        events_string = " ".join(str(s) for s in events)
        return f'HMSET "{hash_key}" area "{area}" month_of_year {month_of_year} day_of_month {day_of_month} events "{events_string}"'

    @classmethod
    def calendars_to_commands(cls, calendar: Union[Calendar, List[Calendar]]):
        data = calendar if type(calendar) == list else [calendar]

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


class CalendarCsvExporter:

    @classmethod
    def calendars_to_string(cls, calendar: Union[Calendar, List[Calendar]]):
        data = calendar if type(calendar) == list else [calendar]

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
