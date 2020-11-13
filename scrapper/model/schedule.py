from typing import Set


class Day:
    """
    day_of_mont - int (1 .. 31) - as the name suggests
    events - set<string> - set of events that occur on that day
    """

    def __init__(self, day_of_month: int, events: Set[str] = None):
        self.day_of_month = day_of_month
        self.events = events if events else set()

    def add_event(self, event):
        self.events.add(event)

    def remove_event(self, event):
        self.events.discard(event)

    def __str__(self):
        return f'Day {self.day_of_month} {self.events}'

    def __repr__(self):
        return self.__str__()


class Month:
    MONTH_NAMES = ['STYCZEŃ', 'LUTY', 'MARZEC', 'KWIECIEN', 'MAJ', 'CZERWIEC',
                   'LIPIEC', 'SIERPIEŃ', 'WRZESIEŃ', 'PAŹDZIERNIK', 'LISTOPAD', 'GRUDZIEŃ']

    """
    month_of_year - int (1 .. 12)
    days - associative arrray[day_no]-><Day>
    """

    def __init__(self, month_of_year: int, no_of_days: int):
        """

        :type no_of_days: int
        :type month_of_year: int
        """
        self.month_of_year = month_of_year
        self.no_of_days = no_of_days
        self.days = {}

        for day_no in range(1, no_of_days + 1):
            self.days[day_no] = Day(day_no)

    def add_events(self, day: int, events):
        for event in events:
            self.add_event(day, event)

    def add_event(self, day: int, event: str):
        dejek = self.days[day]
        dejek.add_event(event)

    def remove_event(self, day: int, event: str):
        dejek = self.days[day]
        dejek.remove_event(event)

    def __str__(self):
        return f'Month {self.month_of_year} {self.no_of_days} {self.days}'

    def __repr__(self):
        return self.__str__()


class Calendar:
    def __init__(self, year: int, area: str = "", source: str = "", description: str = ""):
        """
        """
        self.year = year
        self.area = area
        self.source = source
        self.description = description
        self.months = {}

        for i in range(1, 12 + 1):
            self.months[i] = None

    def count_months(self):
        return sum(1 if self.months[x] else 0 for x in self.months)

    def get_month(self, month_no: int):
        return self.months[month_no]

    def set_month(self, month_no: int, month: Month):
        self.months[month_no] = month

    def __str__(self):
        return f'Calendar for {self.year} from {self.source}'

    def __repr__(self):
        return self.__str__()


class Area:
    def __init__(self, name: str, description: str = "", source: str = ""):
        """
        """
        self.name = name
        self.description = description
        self.source = source

    def __str__(self):
        desc = self.description if len(self.description) < 64 else f'{self.description[:64]}...'
        return f'Area {self.name} ({desc})'

    def __repr__(self):
        return self.__str__()
