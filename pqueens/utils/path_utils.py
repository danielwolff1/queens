"""Path utilities for QUEENS."""
import os

PATH_TO_PQUEENS = os.path.join(os.path.dirname(__file__), "../")
PATH_TO_QUEENS = os.path.join(os.path.dirname(__file__), "../../")
QUEENS_TMP = create_folder_if_not_existent(PATH_TO_QUEENS, "tmp/")


def from_pqueens(relative_path):
    """Create relative path from `pqueens/`.

    As an example to create:
        queens/pqueens/folder/file.A

    call relative_path_from_pqueens("folder/file.A")

    Args:
        relative_path (str): Path starting from queens/pqueens/

    Returns:
        [str]: Absolute path to the file
    """
    return os.path.join(PATH_TO_PQUEENS, relative_path)


def relative_path_from_queens(relative_path):
    """Create relative path from `queens/`.

    As an example to create:
        queens/pqueens/folder/file.A

    call relative_path_from_pqueens("pqueens/folder/file.A")

    Args:
        relative_path (str): Path starting from queens/

    Returns:
        [str]: Absolute path to the file
    """
    return os.path.join(PATH_TO_QUEENS, relative_path)


def relative_path_from_queens_tmp(relative_path):
    """Create relative path from `queens/tmp*`.

    As an example to create:
        queens/tmp/folder/file.A

    call relative_path_from_queens_tmp("folder/file.A")

    Args:
        relative_path (str): Path starting from queens/tmp

    Returns:
        [str]: Absolute path to the file
    """
    return os.path.join(QUEENS_TMP, relative_path)


def create_folder_if_not_existent(path):
    """Create folder if not existent.

    Args:
        path (str): Path to be created
    """
    os.makedirs(path, exist_ok=True)
