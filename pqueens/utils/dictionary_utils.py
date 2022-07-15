"""Dictionary utils."""
from collections import namedtuple


def findkeys(dictionary, key):
    """Get all the values of a 'key' in a nested dictionary.

    Args:
        key ('str'): String of key in dictionary we are interested in
        dictionary (dict): Actual dictionary variable

    Returns:
        result (list): List of values that have the specified key.
    """
    if isinstance(dictionary, list):
        for i in dictionary:
            for x in findkeys(i, key):
                yield x
    elif isinstance(dictionary, dict):
        if key in dictionary:
            yield dictionary[key]
        for j in dictionary.values():
            for x in findkeys(j, key):
                yield x


def to_named_tuple(dict_data, tuple_name="named_tuple"):
    """Create namedtuple from dictionary.

    If the dict contains dicts itself, these remain dicts.
    Args:
        dict_data (dict): Dict to be converted to a dict
        tuple_name (str, optional): Name for the named tuple. Defaults to "named_tuple".

    Returns:
        namedtuple: Named tuple
    """
    return namedtuple(tuple_name, dict_data.keys())(*dict_data.values())


def to_named_tuple_nested(dict_data, tuple_name="named_tuple"):
    """Create namedtuple from dictionary.

    If the dict contains dicts itself, these are also casted into named tuples.
    Args:
        dict_data (dict): Dict to be converted to a dict
        tuple_name (str, optional): Name for the named tuple. Defaults to "named_tuple".

    Returns:
        namedtuple: Named tuple
    """
    return namedtuple(tuple_name, dict_data.keys())(
        *tuple(map(lambda x: x if not isinstance(x, dict) else toNametuple(x), dict_data.values()))
    )
