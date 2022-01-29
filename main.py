import pandas as pd
import numpy as np
data = pd.read_csv('train.csv', sep=';', header=None)

def get_increments(data, rows):
    # print(data.head)
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

    return headers

def add_timeline():
    start = pd.to_datetime('2000-01-01')
    end = pd.to_datetime('2018-01-01')
    return random_dates(start, end, 9)

def random_dates(start, end, n, out_format='datetime'):
    (divide_by, unit) = (24*60*60*10**9, 'D')
    start_u = start.value//divide_by
    end_u = end.value//divide_by
    return pd.to_datetime(np.random.randint(start_u, end_u, n), unit=unit)


# print(add_timeline())
data = get_increments(data, 10)
headers = add_headers(data)
data = data.set_axis(headers, axis=1, inplace=False)
data['Date of signing'] = add_timeline()
print(data)
add_headers(data)