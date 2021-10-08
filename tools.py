def without_keys(dictionary, keys):
    """
    makes a new dictionary excluding a given key
    :param dictionary: original dictionary
    :param keys: key(s) value in dictionary
    :return: a new dictionary without the give key(s)
    """
    return {x: dictionary[x] for x in dictionary if x not in keys}