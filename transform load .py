


print('transform !')

import pandas as pd




df = pd.read_csv('INCIDENTS.csv')

df.drop(columns=['NUMBERR'] , inplace=True )


df.to_csv('clean/incidents_clean.csv' , index=False)



