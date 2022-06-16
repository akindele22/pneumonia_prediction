import matplotlib.pyplot as plt
import pandas as pd

from pylab import *

from skimage.feature import hog
from skimage import  exposure
from scipy.stats import pearsonr
import os
cwd = os.getcwd()
# giving file extension
pwd = os.getcwd()
data1 = os.path.join(pwd,"Normal-8.pnghog.csv")
data1 = pd.read_csv(r'C:\Users\Badmen\Desktop\Olu\computervision\Normal\Normal-8.pnghog.csv')
data1 = data1[:5].copy()

ext = ('.csv')

df = pd.DataFrame()


desktop = os.path.join(cwd, "VP")
files = os.listdir(desktop)
cor_col = ['corr1']
col_df = pd.DataFrame(columns=cor_col)
try:
    for f in files:

        if f.endswith(ext):
            full_path = os.path.join(desktop, f)
            print(full_path)
            full_path = pd.read_csv(full_path)
        
            data2 = full_path[:5].copy()
            data12 = data1['0']
            data22 = data2['0']
            corr1, p =  pearsonr(data12, data22)
            corr1 = round(corr1, 2)
            data_ = full_path[:100].copy()
            #if corr1 == True:
            data_.drop("Unnamed: 0", axis=1, inplace=True)
            data_.drop("Unnamed: 0.1", axis=1, inplace=True)
            data_ = data_.T.copy()
            df = pd.concat([df, data_])
            to_append = [corr1]
            a_series = pd.Series(to_append, index = col_df.columns)
            col_df = col_df.append(a_series, ignore_index=True)
            
except ValueError:
    pass
df.to_csv('eng.csv')
col_df.to_csv('hog_correlation_.csv')
df_ = pd.concat([df,col_df], axis=1)

df_.drop("Unnamed: 0", axis=1, inplace=True)
#data.drop("Unnamed", axis=1, inplace=True)

