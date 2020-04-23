import json
from datetime import datetime
from typing import Dict, List
from pytz import utc


class Utils:
    @staticmethod
    def load_json_data_from_file(input_file: str) -> Dict:
        with open(input_file) as file:
            data_dict = json.load(file)
            return data_dict

    @staticmethod
    def encode_to_latin1(string_to_encode: str) -> bytes:
        # ignores errors
        latin1_encoded_string = string_to_encode.encode('latin-1', errors='ignore')
        return latin1_encoded_string

    @staticmethod
    def convert_to_datetime(datetime_in_string: str) -> datetime:
        datetime_converted = datetime.strptime(datetime_in_string.split('+')[0], "%Y-%m-%d %X")
        datetime_converted = datetime_converted.replace(tzinfo=utc)
        return datetime_converted

    @staticmethod
    def convert_list_to_str_with_encoding(list_of_str: List[str]) -> bytes:
        string_converted = ','.join(list_of_str) if list_of_str else ''
        latin1_encoded_string = Utils.encode_to_latin1(string_converted)
        return latin1_encoded_string
