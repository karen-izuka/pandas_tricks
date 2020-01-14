import numpy as np
import pandas as pd

df_01 = pd.DataFrame({'letter': list('abcdefghijklmnopqrstuvwxyz'),
                      'value': np.random.randint(1,100, size=26)})

df_02 = pd.DataFrame({'letter': list('abcdefghijklmnopqrstuvwxyz'),
                      'value': np.random.randint(1,100, size=26)})

df = df_01.merge(df_02, left_on='letter', right_on='letter', how='left')
