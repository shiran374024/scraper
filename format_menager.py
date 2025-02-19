import json
from dataclasses import asdict
from typing import List
from meta_data import MetaData

class FormatMenager:
    def __init__(self, file):
        self.file = file

    def save_to_file(self, data: List[MetaData]):
        with open(self.file, 'w') as f:
            json_data = [asdict(meta_data) for meta_data in data]
            json.dump(json_data, f, indent=4)