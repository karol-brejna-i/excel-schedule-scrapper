

class DayCellDescription:
    """

    """

    def __init__(self, value: int, coords, size):
        self.value = value
        self.coords = coords
        """ (height, width)"""
        self.size = size

    def __str__(self):
        return f'{self.value} at {self.coords} with size {self.size}'

    def __repr__(self):
        return self.__str__()


class DayData:
    """

    """

    def __init__(self, day_of_month: int, colors: set):
        self.day_of_month = day_of_month
        self.colors = colors

    def __str__(self):
        return f'{self.day_of_month} {self.colors if self.colors else "{}"}'

    def __repr__(self):
        return self.__str__()


class MonthCellsDescription:

    def __init__(self, month_name: str, top_left_cell, top_right_cell=None, column_widths=None):
        self.month_name = month_name
        self.top_left_cell = top_left_cell
        self.top_right_cell = top_right_cell
        self.column_widths = column_widths if column_widths else []

    def __str__(self):
        return f'MonthCellsDescription {self.month_name} {self.top_left_cell} {self.top_right_cell} {self.column_widths}'

    def __repr__(self):
        return self.__str__()
