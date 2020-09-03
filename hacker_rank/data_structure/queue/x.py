import pandas as pd

from functools import reduce
#z use pd.dataframe and b use str data type
# the bellow is hint dasta type specification in the funtion declaration.
#this hints don't apply any force rule in the data but give a clue of what data type it is
def x(z:pd.DataFrame,b:str)->int:
    print(type(z))
    print(z,b)

p = x("hello",1)
print(p)