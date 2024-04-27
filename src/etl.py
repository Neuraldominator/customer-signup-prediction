import pandas as pd
import chardet
import re
# import numpy as np
# from fuzzywuzzy import fuzz, process


class DataPreprocessing:
    def __init__(self, file_path):
        self.file_path_raw_data = file_path
        self.df_raw = None
        self._df = None
        
    @property
    def df(self):
        return self._df

    def estimate_encoding(self, n=10000):
        """
        Reads the first n lines of the csv and makes a best guess on the character encoding scheme.
        
        Args:
            n (int): number of files to check for making best guess (default: 10,000).
   
        Returns:
            string with most likely encoding scheme.
        """
        with open(self.file_path_raw_data, 'rb') as rawdata:
            result = chardet.detect(rawdata.read(n))
        return result['encoding']

    def load_data_from_csv(self, encoding=None, **kwargs):
        """
        Reads csv file and saves it as DataFrame in attribute _raw. If encoding method is not specified, it is estimated by estimate_encoding().
        Also create an attribute df which is a copy of df_raw and is used for further transformations.
        
        Args:
            file_path_raw_data (string): file name of csv to the loaded.
            **kwargs: Additional keyword arguments to be passed to the pd.read_csv() function.
   
        Returns:
            Loaded data in pandas DataFrame.
        """
        if encoding is None:
            encoding = self.estimate_encoding()
        self.df_raw = pd.read_csv(self.file_path_raw_data, encoding=encoding, **kwargs)
        self._df = self.df_raw.copy()
        self.columns = self._df.columns
        return self._df
    
    def validate_postcode(self, column_name=None, valid_postcode_regex=None):
        """
        Validates the rows of the column postcode against a regex.

        Args:
            column_name (str, optional): Name of the DataFrame column to check for validity. Defaults to None. 
            valid_postcode_regex (str, optional): Regular expression to validate the rows of the dataframe against. Defaults to None.

        Returns:
            logical index specifing if row contains a valid (True) or invalid (False) postcode
        """
        if column_name is None:
            column_name = 'postcode'
        elif column_name not in self.columns:
            raise ValueError(f"The column {column_name} is not present in the DataFrame.")
        if valid_postcode_regex is None:
            valid_postcode_regex = r"^[0-9]{5}$"
        return self._df[column_name].apply(lambda row: True if re.match(valid_postcode_regex, row) else False)
        
    def remove_duplicate_rows(self, **kwargs):
        """
        Deletes duplicate data from df.
        
        Args:
            **kwargs: Additional keyword arguments to be passed to pandas drop_duplicates() method of dataframes.

        Returns:
            dataframe with dropped duplicates.
        """
        self._df = self._df.drop_duplicates(**kwargs)
        return self._df
    
    def save_data_to_csv(self, file_path, **kwargs):
        """
        Saves preprocessed data into data/processed/file_path.

        Args:
            file_path (str): path to data/processed/file_path.csv.
            **kwargs: Additional keyword arguments to be passed to pandas drop_duplicates() method of dataframes.
        
        Returns:
            None.
        """
        self.file_path_processed_data = file_path
        self._df.to_csv(self.file_path_processed_data, **kwargs)

    def missing_values(self, *args):
        """
        Returns a DataFrame with booleans indicating missing values in the specified columns.
        
        Args:
            *args: Variable-length arguments representing column names. Each argument can be a single column name or a list of column names.
        
        Returns:
            DataFrame with the original column shape, where True if indicates a missing value (NaN) and False otherwise.
        """
        if len(args) == 0:
            return pd.DataFrame()

        columns = []
        for arg in args:
            if isinstance(arg, str):
                columns.append(arg)
            elif isinstance(arg, list):
                columns.extend(arg)

        nonexisting_columns = [col for col in columns if col not in self.columns]
        if nonexisting_columns:
            raise ValueError(f"The columns {nonexisting_columns} are not present in the DataFrame.")

        return self._df[columns].isna()