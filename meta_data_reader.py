from typing import List
import os
import pandas as pd
from meta_data import MetaData

class MetaDataReader:
    def __init__(self, dir_path):
        self.dir_path = dir_path
        self.data: List[MetaData] = []
        self.read()
    
    def read(self):
        for file in os.listdir(self.dir_path):
            if file.endswith('.csv'):
                self.read_csv(os.path.join(self.dir_path, file))
       

    def read_csv(self,file_path):
        df = pd.read_csv(file_path)
        for _, row in df.iterrows():
            meta_data = MetaData(
                file_rein=str(row['FILEREIN']),
                category=""
                
            )
            self.data.append(meta_data)
    
    def get_data(self):
        return self.data