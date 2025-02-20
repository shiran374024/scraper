import json
from dataclasses import asdict
from typing import List
from meta_data import MetaData

class FormatMenager:

    def __init__(self, file_path: str):
        self.base_path = file_path
    
    def save_to_file(self, data: List[MetaData],chunk_number: int):
        file_path = f"{self.base_path}_{chunk_number}.json"
        with open(file_path, 'w') as f:
            json_data = [asdict(meta_data) for meta_data in data]
            json.dump(json_data, f, indent=4)