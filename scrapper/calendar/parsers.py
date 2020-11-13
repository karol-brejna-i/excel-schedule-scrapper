from scrapper.model.schedule import Month
from scrapper.model.cells import BLACK, BROWN, GREEN, BLUE, YELLOW, RED, BLACK_AND_BROWN

EVENT_UNKNOWN = -1
EVENT_MIESZANE, EVENT_BIO, EVENT_SZKLO, EVENT_PAPIER, EVENT_PLASTIK, EVENT_WOLNE = 0, 1, 2, 3, 4, 5
EVENT_TYPE_NAMES = ['MIESZANE', 'BIO', 'SZKŁO', 'PAPIER', 'PLASTIK', 'WOLNE']
EVENT_TYPE_BY_COLOR = {BLACK: EVENT_MIESZANE, BROWN: EVENT_BIO, GREEN: EVENT_SZKLO,
                       BLUE: EVENT_PAPIER, YELLOW: EVENT_PLASTIK, RED: EVENT_WOLNE, BLACK_AND_BROWN: [EVENT_BIO, EVENT_MIESZANE]}


class CalendarDataParser:

    @classmethod
    def events_from_colors(cls, colors_names: set):
        events = []
        for color_name in colors_names:
            if color_name not in EVENT_TYPE_BY_COLOR:
                events.append('UNKNOWN')
            else:
                event_type = EVENT_TYPE_BY_COLOR[color_name]
                if type(event_type) == list:
                    events.extend(event_type)
                else:
                    events.append(event_type)
        return events

    @classmethod
    def month_from_day_data(cls, month_of_year: int, no_of_days: int, days_data: list):
        month = Month(month_of_year, no_of_days)
        for day_data in days_data:
            day_of_month = day_data.day_of_month
            events = CalendarDataParser.events_from_colors(day_data.colors)
            month.add_events(day_of_month, events)

        return month

