import pandas as pd

data = pd.read_csv('train.csv', sep=';', header=None)


def add_timeline(df):
    pass


def get_increments(data, rows):
    print(data.head)
    data = data.iloc[1: rows]
    data = data[[0, 1, 2, 3, 4]]
    return data


def add_headers(data):
    first_raw = data.head(1)
    headers_str = {
        'job': ['management', 'technician', 'entrepreneur', 'blue-colla', 'retired'],
        'marital': ['married', 'single', 'divorced'],
        'education': ['tertiary', 'secondary'],
        'Credit in default': ['no', 'yes']

    }
    headers_int = {
        'age': range(18, 90)
    }
    headers = []
    print(data.head)
    first_raw = first_raw.values[0]

    for k in first_raw:
        if k.isdigit():
            k = int(k)

        if type(k) == int:
            for key, value in headers_int.items():
                if k in value:
                    headers.append(key)
        else:
            for key, value in headers_str.items():
                if k in value:
                    headers.append(key)

    print(headers)


data = get_increments(data, 10)
add_headers(data)
