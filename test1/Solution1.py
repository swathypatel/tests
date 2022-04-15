# This script parses the xml and modifies the dates and writes to output.xml.

# Please install xmltodict and lxml using pip3 before running the script.

import xmltodict
import lxml.etree as ET
from datetime import date, timedelta

filename = "test_payload1.xml"
QUOTE_REQUEST = 'QUOTE_REQUEST'
REQUEST = 'REQUEST'
TP = 'TP'
DEPART = 'DEPART'
RETURN = 'RETURN'

def modify_dates(X, Y):
    """
    This method modifies the dates in xml file and writes to output.xml.
    :param X: It is an int. Number of days ahead of current date.
    :param Y: It is an int. Number of days ahead of current date.
    :return: None
    """
    with open(filename, 'r') as f:   # open the input file using with statement.
        xml_data = f.read()          # read the input file.
        xml_dict = xmltodict.parse(xml_data)
        depart_date = xml_dict[QUOTE_REQUEST][REQUEST][TP][DEPART]    # get the depart date
        return_date = xml_dict[QUOTE_REQUEST][REQUEST][TP][RETURN]    # get the return date
        date1 = date(int(depart_date[:4]), int(depart_date[4:6]), int(depart_date[6:8])) + timedelta(days=X)   # add X days to the date
        date2 = date(int(return_date[:4]), int(return_date[4:6]), int(return_date[6:8])) + timedelta(days=Y)   # add Y days to the date.
        formatted_date1 = ''.join(str(date1).split('-'))  # remove - in date and join the date string.
        formatted_date2 = ''.join(str(date2).split('-'))

    with open(filename, encoding="utf8") as f:
        tree = ET.parse(f)
        root = tree.getroot()
        for elem in root.getiterator():
            try:
                elem.text = elem.text.replace(depart_date, formatted_date1)   # get the date and replace it with updated date.
                elem.text = elem.text.replace(return_date, formatted_date2)
            except AttributeError:
                pass

    tree.write('output.xml', method='xml', encoding="utf8")  # write the complete xml to the output file.

modify_dates(1, 2)  # It should add 1 and 2 days to depart and return dates respectively.

# python3 Solution1.py # Command to execute this script.
# Output is stored in output.xml
