from typing import List
import os
import pandas as pd
from meta_data import MetaData
from dataclasses import asdict

class MetaDataReader:
    def __init__(self, dir_path, chunksize=1000):
        self.dir_path = dir_path
        self.chunksize = chunksize
    
    def read(self):
        for file in os.listdir(self.dir_path):
            if file.endswith('.csv'):
                yield from self.read_csv(os.path.join(self.dir_path, file))
    
    def read_csv(self, file_path):
        for chunk in pd.read_csv(file_path, chunksize=self.chunksize):
            chunk_data = []
            for _, row in chunk.iterrows():
                meta_data = MetaData(
                    file_rein=str(row['FILEREIN']),
                    category=""
                )
                print(f"Successfully read data for {meta_data.file_rein}")
                chunk_data.append(meta_data)
            yield chunk_data