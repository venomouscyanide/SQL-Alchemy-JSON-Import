import argparse
from typing import Dict, List

from connection import connect
from models import NewsArticle
from utils import Utils
from sqlalchemy.orm import Session


def insert_data_from_json(json_path: str, current_session: Session) -> None:
    json_data_from_file = Utils.load_json_data_from_file(json_path)
    get_rows_to_create(json_data_from_file, current_session)
    current_session.commit()


def get_rows_to_create(json_data_from_file: Dict, current_session: Session) -> List[NewsArticle]:
    len_of_rows = len(json_data_from_file)
    print(f"Total rows to import {len_of_rows}")
    import_error_indices = list()
    for index, json_data in enumerate(json_data_from_file):
        print(f"Import {index} of {len_of_rows - 1}")
        _preprocess_data(json_data)
        new_row = NewsArticle(**json_data)
        try:
            current_session.add(new_row)
        except Exception as e:
            print(f"Exception occurred {str(e)}")
            import_error_indices.append(index)
    print("Could Not Import: ", import_error_indices)


def _preprocess_data(json_data: Dict):
    json_data['published_at'] = Utils.convert_to_datetime(json_data['published_at'])
    json_data['body'] = Utils.encode_to_latin1(json_data['body'])
    json_data['hashtags'] = Utils.convert_list_to_str_with_encoding(json_data['hashtags'])
    json_data['keywords'] = Utils.convert_list_to_str_with_encoding(json_data['keywords'])
    json_data['title'] = Utils.encode_to_latin1(json_data['title'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--db_URI', help='MySQL URI', required=False,
                        default='mysql+mysqldb://root:starpark@localhost:7674/newsdumo'),
    parser.add_argument('--input_json_file', help='Input Json file', required=False, default='test_output.json'),

    args = parser.parse_args()
    current_session = connect(args.db_URI)
    insert_data_from_json(args.input_json_file, current_session)
