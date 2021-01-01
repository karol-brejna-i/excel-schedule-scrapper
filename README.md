


# Obtaining the schedule data
All the waste collection schedule data for this experiment were taken from it source: http://szemud.pl/.

The information there is available in form of PDF files.

After downloading the files, they were converted to Excel format using pdf2go.com.
This free online service appeared to have the best conversion quality among other tested sites.
Did I mention it's free?

The URLs for particular schedules are collected in [schedules.2021.txt](./resources/schedules.2021.txt). 
You can dowload them all in one go with [download.schedules.sh](./resources/download.schedules.sh).


# Running the code

**test_extract_metadata.py** uses `MetadataScanner` object to parse the excel files end obtain data about the areas
(areas that the county is divided).

**test_parse_all.py** uses MetadataScanner **test_extract_metadata.py** uses `MetadataScanner` object to parse the excel 
files end obtain data about the areas and `TableScanner` to scan through the excel files and extract schedule information.

The script serializes the data in form of pickle 
files (https://docs.python.org/3/library/pickle.html): [areas.p](./areas.p) and [schedule.p](./schedule.p).

**test_exporters.py** imports data from the pickle files and runs `ScheduleRedisExporter` and `ScheduleCsvExporter` to
present the data in from of Redis commands and CSV lines respectively. 


# TO DO
1. Add proper README
4. Think of returning Value Objects instead of tuples