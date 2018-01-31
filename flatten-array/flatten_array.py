def flatten(iterable):
    if iterable is None:
        return []
    flatten_list = []
    for item in iterable:
        flatten_list.append(item) if type(item) in [int, str] else flatten_list.extend(flatten(item))
    return flatten_list





