#%%
import pandas as pd

#%% 
df = pd.read_csv('UserActions.csv', header = None)
df.columns = ['time','window','type','action','name','path','description']
# %%
df.head()

# %%
