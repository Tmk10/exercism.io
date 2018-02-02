def transform(legacy_data):
    dict = {value.lower(): key for key in legacy_data.keys() for value in legacy_data[key]}
    return dict

