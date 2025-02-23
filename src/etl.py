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
            n (int): number of files to check for making best guess. Defaults to 10,000.
   
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
            column_name (str, optional): Name of the DataFrame column to check for validity. Defaults to 'postcode'. 
            valid_postcode_regex (str, optional): Regular expression to validate the rows of the dataframe against. Defaults to "^[0-9]{5}$".

        Returns:
            logical index specifing if row contains a valid (True) or invalid (False) postcode
        """
        if column_name is None:
            column_name = 'postcode'
        elif column_name not in self.columns:
            raise ValueError(f"The column {column_name} is not present in the DataFrame.")
        if valid_postcode_regex is None:
            valid_postcode_regex = r"^[0-9]{5}$"
        return self._df[column_name].apply(lambda row: True if re.fullmatch(valid_postcode_regex, row) else False)
    
    def validate_state(self, column_name=None):
        """
        Returns a DataFrame with booleans indicating whether the entries of a column refer to one of the 16 German states.
        
        Args:
            column_name (str): Column name of the dataframe that is checked for validity. Defaults to 'bundesland'.
        
        Returns:
            logical index whether entry is valid (True) or invalid (False) postcode
        
        """
        if column_name is None:
            column_name = 'bundesland'
        elif column_name not in self.columns:
            raise ValueError(f"The column {column_name} is not present in the DataFrame.")
        valid_states = ['bayern', 'hessen', 'baden-württemberg', 'berlin', 'brandenburg', 'bremen', 'hamburg', 'mecklenburg-vorpommern', 'niedersachsen', 'nordrhein-westfalen', 'rheinland-pfalz', 'saarland', 'sachsen', 'sachsen-anhalt', 'schleswig-holstein', 'thüringen']
        return self._df[column_name].str.strip().str.lower().isin(valid_states)
    
    def remove_decimals(self, column_name=None):
        """
        Overwrites the entries of the column by splitting the strings at the first comma and taking everything on the left of this comma.

        Args:
            column_name (str, optional): Name of the DataFrame column to check for remove decimals from. Defaults to 'postcode'. 

        Returns:
            None
        """
        if column_name is None:
            column_name = 'postcode'
        elif column_name not in self.columns:
            raise ValueError(f"The column {column_name} is not present in the DataFrame.")
        
        original_values = self._df[column_name].copy()  # Make a copy of the original column values
        self._df[column_name] = self._df[column_name].apply(lambda x: x.split(".")[0])      
        n_changes = sum(self._df[column_name] != original_values)  # Count the number of changed entries
        print(f"{n_changes} entries were changed.\n")
        return None 
    
    def zero_padding(self, column_name, side=None, n=None):
        """
        Pads the string entries in column with zeros until the string has n total characters. Side determines from with side of the string the zeros are padded.

        Args:
            side (str, optional): Specifies the side on which to add zeros. Defaults to left.
            n (int, optional): Number of characters to fill up to with zeros. Defaults to 5.

        Returns:
            None
        """
        if side is None:
            side='left'
        elif side.lower() not in ['left', 'right']:
            raise ValueError("input argument side must be either 'left' or 'right'.")
        
        if n is None:
            n=5
            
        original_values = self._df[column_name].copy()  # Make a copy of the original column values
        
        if side=='left':
            self._df[column_name] = self._df[column_name].str.rjust(5, fillchar='0')
        else:
            self._df[column_name] = self._df[column_name].str.ljust(5, fillchar='0')
        
        n_changes = sum(self._df[column_name] != original_values)  # Count the number of changed entries
        print(f"{n_changes} entries were changed.\n")
        return None
       
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

    def missing_values(self, *args):
        """
        Returns a DataFrame with booleans indicating missing values in the specified columns.
        
        Args:
            *args: Variable-length arguments representing column names. Each argument can be a single column name or a list of column names.
        
        Returns:
            If several columns are parsed, returns DataFrame with specified columns, where True if indicates a missing value (NaN) and False otherwise.
            If a single column is parsed, returns a Series.
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

        if len(columns) == 1:
            return self._df[columns[0]].isna()
        else:
            return self._df[columns].isna()

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