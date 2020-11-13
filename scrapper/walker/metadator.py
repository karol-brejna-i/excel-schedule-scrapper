from scrapper.walker import logger
from scrapper.walker.scanner import TableScanner


class MetadataScanner:
    """
    Walks through worksheet cells and tries to determine size of sections responsible for holding data for given day
    """

    def __init__(self, worksheet):
        self.worksheet = worksheet
        self.scanner = TableScanner(worksheet)

    def find_lowest_range(self):
        sorted_ranges = sorted(self.worksheet.merged_cells.ranges, key=lambda x: x.start_cell.row, reverse=True)

        lowest = sorted_ranges[0]
        return lowest

    def get_range_by_coords(self, coords: str):
        """
        Returns cell range that starts with a given coordinates.
        :param coords: str: top_left column coordinates (i.e. A1) of the requested cell range
        :return:
        """
        result = None
        for r in self.worksheet.merged_cells.ranges:
            if r.start_cell.coordinate == coords:
                result = r
                break
        return result

    def extract_area(self):
        logo_cells = self.get_range_by_coords("A1")

        header_starting_col = 1 + logo_cells.size['columns']
        top_header_cell = self.worksheet.cell(1, header_starting_col)
        header_cells = self.get_range_by_coords(top_header_cell.coordinate)

        header_width = header_cells.size['columns']

        area_row = 3

        result = ""
        for i in range(0, header_width):
            cell = self.worksheet.cell(area_row, header_starting_col + i)
            # print(f"cell {cell}")
            if cell.value:
                result += cell.value

        return result

    def extract_streets(self):
        lowest = self.find_lowest_range()
        width = lowest.size["columns"]
        logger.debug(f"lowest range is {width} wide - the worksheet is {self.worksheet.max_column} wide.")

        result = ""
        if width == self.worksheet.max_column:
            result = lowest.start_cell.value

        return result


