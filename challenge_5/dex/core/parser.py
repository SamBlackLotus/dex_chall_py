import core
import json
import csv
import xmltodict
import yaml
from typing import Dict, Union, List


def read_file(filepath: str) -> List[Dict[str, Union[str, int]]]:
    """
    This function reads a file and based on the format
    it will fit in one of the conditionals.

    If its a .json it uses load.
    If its a .csv it uses DictReader.
    If its a .xml it uses xmltodict.
    If its a .yaml it uses safe load.

    Parameters
    ----------
    filepath:
        The file path, it can be the full path or relative path.

    Returns
    -------
    data_read:
        The file received will be returned in python data types.
    """
    with open((filepath), "r") as source_data:
        if ".json" in filepath:
            return json.load(source_data)
        elif ".csv" in filepath:
            file = csv.DictReader(source_data, delimiter=",")
            data_read = [row for row in file]
            return data_read
        elif ".xml" in filepath:
            file = source_data.read()
            file_xml = xmltodict.parse(file)
            dict_id = {key: value for key, value in file_xml["root"].items()}
            data_read = []
            for key, value in dict_id.items():
                data_read += [
                    {key_list: value_list for key_list, value_list in value.items()}
                ]
            return data_read
        elif ".yaml" in filepath:
            file = source_data.read()
            data_read = yaml.safe_load(file)
            return data_read
        else:
            print(f"Error: File format not supported!\n{core.client_usage()}")
            quit()
