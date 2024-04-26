import pandas as pd
import numpy as np
import re
from fuzzywuzzy import fuzz, process


class DataPreprocessing:
    def __init__(self):
        pass
    
    def load_data_from_csv(self, file_path_raw_data, **kwargs):
        """
        Reads csv file and saves it as DataFrame in attribute df_raw. 
        Also create an attribute df which is a copy of df_raw and is used for further transformations.
        
        Args:
            file_path_raw_data (string): file name of csv to the loaded.
            **kwargs: Additional keyword arguments to be passed to the pd.read_csv() function.
   
        Returns:
            Loaded data in pandas DataFrame.
        """
        self.file_path_raw_data = file_path_raw_data
        self.raw_data = pd.read_csv(self.file_path_raw_data, **kwargs)
        self.df = self.raw_data.copy()
        return self.df

    def remove_duplicate_rows(self, **kwargs):
        """
        Deletes duplicate data from df.
        
        Args:
            **kwargs: Additional keyword arguments to be passed to pandas drop_duplicates() method of dataframes.

        Returns:
            dataframe with dropped duplicates.
        """
        self.df = self.df.drop_duplicates(**kwargs)
        return self.df
    
    def save_data_to_csv(self, file_path_processed_data, **kwargs):
        """
        Saves preprocessed data into data/processed/file_path_processed_data.

        Args:
            file_path_processed_data (_type_): _description_
            **kwargs: Additional keyword arguments to be passed to pandas drop_duplicates() method of dataframes.
        
        Returns:
            None.
        """
        self.file_path_processed_data = file_path_processed_data
        self.df.to_csv(self.file_path_processed_data, **kwargs)