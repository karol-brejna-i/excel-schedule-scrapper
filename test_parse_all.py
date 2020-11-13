import pickle

from openpyxl import load_workbook

from scrapper.model.schedule import Area
from scrapper.walker import logger
from scrapper.walker.metadator import MetadataScanner
from scrapper.walker.scanner import TableScanner

import log_config


def get_input_file_names():
    import glob
    names = glob.glob('./resources/excel/*.xlsx')
    return names


def parse_new():
    year = 2020
    names = get_input_file_names()
    # names = ['./resources/excel/bojano-2-harmonogram-2020-kalendarz-rejon-1-01.07.20-c.pdf-bojano-2.xlsx']
    # names = ['./resources/excel/karczemki-harmonogram-2020-kalendarz-rejon-1-01.07.20-c.pdf-karczemki.xlsx']
    # names = ['./resources/excel/koleczkowo-2-harmonogram-2020-kalendarz-rejon-1-01.07.20-c.pdf-koleczkowo-2.xlsx']

    areas, calendars = [], []
    for name in names:
        path = name
        wb = load_workbook(path)
        ws = wb.worksheets[0]
        # print(f"Sheet {ws} max rows: {ws.max_row} max cols: {ws.max_column}")
        logger.info(f"path: ----------------------------------------- {path}")
        scanner = TableScanner(ws)

        # extract metadata (area name, addresses)
        metadator = MetadataScanner(ws)
        area_name, streets = metadator.extract_area(), metadator.extract_streets()
        area = Area(area_name, streets, path)
        areas.append(area)
        # extract event data
        calendar = scanner.get_calendar(year, area_name, path)

        calendars.append(calendar)

    return areas, calendars


result = parse_new()
print(result[0])
print(result[1])

pickle.dump(result[0], open("areas.p", "wb"))
pickle.dump(result[1], open("schedule.p", "wb"))
