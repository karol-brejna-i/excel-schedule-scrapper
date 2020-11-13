import pickle

from openpyxl import load_workbook

from scrapper.model.schedule import Area
from scrapper.walker import logger
from scrapper.walker.metadator import MetadataScanner

import log_config


def get_input_file_names():
    import glob
    names = glob.glob('./resources/excel/*.xlsx')
    return names


def right_number_of_days(month_no, no_of_days):
    MONTH_DAYS = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    against = MONTH_DAYS[month_no - 1]

    if type(against) == list:
        return no_of_days in against
    else:
        return no_of_days == against


def parse_all():
    names = get_input_file_names()
    # names = ['./resources/excel/bojano-2-harmonogram-2020-kalendarz-rejon-1-01.07.20-c.pdf-bojano-2.xlsx']
    # names = ['./resources/excel/karczemki-harmonogram-2020-kalendarz-rejon-1-01.07.20-c.pdf-karczemki.xlsx']
    # names = ['./resources/excel/koleczkowo-2-harmonogram-2020-kalendarz-rejon-1-01.07.20-c.pdf-koleczkowo-2.xlsx']

    result = []

    for name in names:
        path = name
        wb = load_workbook(path)
        ws = wb.worksheets[0]
        # print(f"Sheet {ws} max rows: {ws.max_row} max cols: {ws.max_column}")
        logger.info(f"path: ----------------------------------------- {path}")
        print(f"path: ----------------------------------------- {path}")

        metadator = MetadataScanner(ws)
        area_name, streets = metadator.extract_area(), metadator.extract_streets()
        result.append(Area(area_name, streets, path))

    return result


result = parse_all()
pickle.dump(result, open("areas.p", "wb"))

print(result)
print(type(result[0]))
