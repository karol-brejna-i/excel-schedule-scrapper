import json
import os
import sys


def get_or_crash(env_name, message):
    value = os.getenv(env_name)
    if not value:
        sys.exit(message)

    return value


def get_with_default(env_name, default_value):
    value = os.getenv(env_name)
    if not value:
        value = default_value
    return value


AREA_NAME_ROW = int(get_with_default('AREA_NAME_ROW', 3))
month_names_env = get_with_default('MONTH_NAMES',
                                   '["STYCZEŃ 2021", "LUTY 2021", "MARZEC 2021", "KWIECIEŃ 2021", "MAJ 2021", '
                                   '"CZERWIEC 2021","LIPIEC 2021", "SIERPIEŃ 2021", "WRZESIEŃ 2021", "PAŹDZIERNIK 2021", '
                                   '"LISTOPAD 2021", "GRUDZIEŃ 2021"]')

MONTH_NAMES = json.loads(month_names_env)

COLOR_ENV_NAMES = [
    'COLOR_NONE',
    'COLOR_BROWN',
    'COLOR_BLACK',
    'COLOR_BLUE',
    'COLOR_RED',
    'COLOR_BLACK_AND_BROWN',
    'COLOR_YELLOW',
    'COLOR_GREEN']

COLOR_NAMES = [
    '',
    'BROWN',
    'BLACK',
    'BLUE',
    'RED',
    'BLACK AND BROWN',
    'YELLOW',
    'GREEN']

COLOR_NAMES_LOOKUP = {'00000000': '',
                      'FFFF0000': 'RED',
                      'FF6FAC46': 'GREEN',
                      'FF6FAD46': 'GREEN',
                      'FF538135': 'GREEN',
                      'FF00AFEF': 'BLUE',
                      'FF5B9BD4': 'BLUE',
                      'FFFFFF00': 'YELLOW',
                      'FF000000': 'BLACK',
                      'FF0D0D0D': 'BLACK',
                      'FFC55A11': 'BROWN',
                      'FF00B0F0': 'BROWN',
                      'FFC65810': 'BROWN',
                      'FF833B0B': 'BLACK AND BROWN',
                      'FF843B0C': 'BLACK AND BROWN'}


CURRENT_SCHEDULE = get_or_crash('CURRENT_SCHEDULE', 'Exiting. Please, set up CURRENT_SCHEDULE env variable.')

MONTH_DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]