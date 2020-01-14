import pandas as pd

#create initial df
my_dict = {
        'letter': list('abcdefghijklmnopqrstuvwxyz'),
        'value': [0.0816,0.0149,0.0278,0.0425,0.1270,0.0228,0.0202,0.0609,0.0697,0.0015,0.0074,0.0402,0.0251,0.0674,0.0750,0.0192,0.0009,0.0598,0.0633,0.0905,0.0275,0.0103,0.0246,0.0015,0.0197,0.0007]
}
df = pd.DataFrame(my_dict)


#create lookup dictionary
letter_dict = {'consonant': list('bcdfghjklmnpqrstvwxz'), 'vowel': list('aeiouy')}
def transform_dict(series, group_dict):
    groups = {x: k for k, v in group_dict.items() for x in v}
    return groups
map_dict = transform_dict(df['letter'], letter_dict)

#apply lookup dictionary and perform transform
df['category'] = df['letter'].map(map_dict)
df = df[['letter', 'category', 'value']]
df['category_value'] = df.groupby('category')['value'].transform('sum')
