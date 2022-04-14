# This script parses the jmeter logs and prints label, response code, response message, failure message and human readable date and time in PST.

# Please install csv, datetime and pytz using pip3 before running the script.

from csv import reader
import datetime
from pytz import timezone

date_time_format = '%Y-%m-%d %H:%M:%S'
pacific_time = 'US/Pacific'

def parse_jmeter_log(files):
    """
    This function takes files as input and prints label, response code, response message, failure message and human readable date and time in PST.
    :param files: list of strings. strings are file names.
    :return: None.
    """
    for filename in files:
        print("filename: {}".format(filename))
        with open(filename, 'r') as read_object:
            csv_reader = reader(read_object)      # reads the file.
            header = next(csv_reader)
            if header is not None:
                for row in csv_reader:
                    if '200' not in row:
                        time = datetime.datetime.fromtimestamp(int(row[0])/1000).strftime(date_time_format)
                        datetime_obj_naive = datetime.datetime.strptime(time, date_time_format)
                        datetime_obj_pacific = timezone(pacific_time).localize(datetime_obj_naive)
                        pst_time = datetime_obj_pacific.strftime(date_time_format + " %Z%z")  # convert the data time to PST date time.
                        print("label: {0}, responseCode: {1}, responseMessage:{2}, failureMessage: {3}, time: {4}".format(row[2], row[3], row[4], row[8], pst_time))


parse_jmeter_log(["Jmeter_log1.jtl", "Jmeter_log2.jtl"])

# python3 Solution3.py # Command to execute this script.
