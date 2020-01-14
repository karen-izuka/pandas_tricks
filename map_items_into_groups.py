import pandas as pd

alphabet = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
letter_dict = {'consonants': list('bcdfghjklmnpqrstvwxz'), 'vowels': list('aeiouy')}

def membership_map(series, group_dict):
    groups = {x: k for k, v in group_dict.items() for x in v}
    mapped_series = series.map(groups)
    return mapped_series

mapped_data = membership_map(alphabet, letter_dict)
print(list(mapped_data))
