import os



def apply_keep_abs(path: str, file: str, keep_abs: bool = False):
    """
    Parameters
    ----------
    path : str
        Absolute path to keep
    file : str
        File to modify
    keep_abs : bool
        Keep the absolute path or not
    
    Returns
    -------
    returns the modified path (either the full path or file name only)
    """
    return file if not(keep_abs) else os.path.join(path, file)


def list_all_files(path: str, 
                   keep_abs: bool = False
                   ) -> list:
    """
    List all files at a given path

    Example 
    -------
    >>> ls <given_path>
    <dir1>
    <dir2>
    <dir3>
    <file1>
    <dir4>
    <file2>
    <file3>
    <file4>
    <file5>
    <exe1>
    >>> list_all_files(<given_path>)
    [<file1>, <file2>, <file3>, <file4>, <file5>]
    >>> list_all_files(<given_path>, keep_abs=True)
    [<given_path>/<file1>, <given_path>/<file2>, <given_path>/<file3>, <given_path>/<file4>, <given_path>/<file5>]
    
    Parameters
    ----------
    path : str
        Path to the list of files
    keep_abs : bool
        Keep the path to said files on return
    
    Returns
    -------
    list of files
        A list containing all file names (incl path if prompted) at given location 
    """
    if os.path.isfile(path):
        return [path]
    
    all_files = []

    for file in os.listdir(path):

        if not(os.path.isdir(os.path.join(path, file))):

            all_files.append(apply_keep_abs(path, file, keep_abs))
    

    return all_files


def unravel_files(path: str, keep_abs: bool = False, skip: list = [".git", "__pycache__"]) -> list:
    """
    Given a path, this function unravels all files existing in that directory
    including files under directories

    Parameters
    ----------
    path : str
        Path of the Directory to unravel
    keep_abs : bool
        Keep the absolute (here root is given path) path
    skip : list
        A list of all directories to ignore (incl. git and pycache folders as default)

    Returns
    -------
    a list of all files in said directory (incl. all hidden behind other sub directories) 
    """
    if os.path.isfile(path):
        return [path]
    
    all_files = []

    for file in os.listdir(path):
        if file in skip:
            continue

        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            unraveled = unravel_files(path=file_path, keep_abs=keep_abs, skip=skip)
            all_files.extend(unraveled)
        else:
            all_files.append(apply_keep_abs(path, file, keep_abs))
    

    return all_files



def filter_ext(files: list, ext: str) -> list:
    """
    Filter files by extension
    """
    pass