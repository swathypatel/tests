# This script parses the json file and removes keys that are given as input and writes the remaining content to output.json file.

# please install json module using pip if not already present.
import json


def delete_keys_from_dict(filename, lst_keys):
    """
    This function takes json file as input, parses it and removes the lst_keys and write it to the output.json file.
    :param filename: It is a string. It contains json data.
    :param lst_keys: list of keys that needs to be deleted from json file. Its a list of strings.
    :return: None.
    """
    with open(filename, 'r') as f:
        dict_data = json.load(f)
    for k in lst_keys:
        if k in dict_data:   # if string is found in keys.
            del dict_data[k]  # delete the key from dict.
    for v in dict_data.values():
        if isinstance(v, dict):
            delete_keys_from_dict(v, lst_keys)  # Similarly do for inner dict keys using recursion.

    with open('output.json', 'w') as outfile:
        json.dump(dict_data, outfile)   # update the remaining dict to output file.

delete_keys_from_dict('test_payload.json', ["inParams"])
#delete_keys_from_dict('test_payload.json', ["appdate"])


# python3 Solution2.py # Command to execute this script.
# Output is stored in output.json
