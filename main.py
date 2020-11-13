from __future__ import absolute_import

if __name__ == '__main__':
    # inside of SWS.time

    from scrapper import calendar as cal

    c = cal.TextCalendar(cal.Monday)
    # print(calendar.month(2020, 7))
    print(c)