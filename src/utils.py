import re

def validate_string(s, pat, fullmatch=True):
    '''
    Checks if the string s is valid by validating it with a regex.

    Parameters:
        s (str): The string to be checked for validity.
        pat (str): Regular expression to validate against.
        fullmatch (bool, optional): If True, the entire string must match the regex in pat. If False, a partial match is allowed. Defaults to True
        
    Returns:
        bool: True if the input is valid, False otherwise.
    '''
    if fullmatch:
        return bool(re.fullmatch(pat, s))
    else:
        return bool(re.match(pat, s))
    
def extract_partial_match(s, pat):
    '''
    Extracts the partial matching from s with the regex pat. 

    Parameters:
        s (str): The string to be checked for validity.
        pat (str): Regular expression to validate against.
        
    Returns:
        str: partial match of string if applicable. None otherwise.
    '''
    match = re.search(pat, s)
    if match:
        return match.group()
    else:
        return None
    
def get_string_length(s):
    '''
    Counts the number of characters of a string.

    Parameters:
        s (str): The string to be assessed.

    Returns:
        int: number of  if the input is valid, False otherwise.
    '''
    return len(s)
    
    
def remove_trailing_decimal_pattern(string):
    """
    This function splits a string at the pattern "." and only returns the left side.
    
    Parameters:
        string (str): string to checked against pattern.
    
    Returns
        string: All characters of the string before the first "." pattern occurs.
    """
    return string.split(".")[0]