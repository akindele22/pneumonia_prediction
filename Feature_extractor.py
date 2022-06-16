import matplotlib.pyplot as plt
import pandas as pd
from pylab import *
from skimage.feature import hog
from skimage import  exposure
from scipy.stats import pearsonr
import pickle
import os

#from Project.app import predict
print('pass0')
def FEATURE_PEDICTION(image_path):
    cwd = os.getcwd()
    # giving file extension
    ext = ('png')

    desktop = os.path.join(cwd, "images")
    files = os.listdir(desktop)
    for f in files:
        
            if f.endswith(ext):

                full_path = os.path.join(desktop, f)
                print(full_path)
                var1 = full_path
                var2 = ".csv"
                var3 = var1 + var2
                image = imread(full_path)
                #hog_image  = hog(image, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(2, 2), block_norm='L2-Hys', visualize=False, transform_sqrt=False, feature_vector=True, channel_axis=None)
                try:
                        hog_image  = hog(image, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(2, 2), block_norm='L2-Hys', visualize=False, transform_sqrt=False, feature_vector=True, channel_axis=None)
                        DF = pd.DataFrame(hog_image)
                        DF.to_csv(var3)



                        #print("x")
                except:
                        print('hog() got an unexpected keyword argument "channel_axis"')
                        print("delete the image")
                        os. remove(full_path)
                        print("try again")
                #fd, hog_image = hog(image, orientations=8, pixels_per_cell=(16, 16),
                        #cells_per_block=(1, 1), visualize=True, channel_axis=-1)
                #DF = pd.DataFrame(hog_image)
                #DF.to_csv(var3)
    print('pass1')
    ###########################################################################################################################################################
    cwd = os.getcwd()
    ext = ('.csv')

    desktop = os.path.join(cwd, "images")
    files = os.listdir(desktop)
    for f in files:

            if f.endswith(ext):
                full_path1 = os.path.join(desktop, f)
                print(full_path1)
                full_path = pd.read_csv(full_path1)
                cols = ['0']
                full_path[cols] = full_path[cols].replace({'0':np.nan, 0:np.nan})
                full_path = full_path.dropna(subset = ['0'])       
                os.remove(full_path1)
                print(5)
                full_path.drop("Unnamed: 0", axis=1, inplace=True)
                full_path.to_csv(full_path1)
#########################################################################################################################################
    cwd = os.getcwd()
    # giving file extension
    pwd = os.getcwd()
    data1 = os.path.join(pwd,r"Normal-28.pnghog.csv")
    data1= pd.read_csv(data1)
    data1 = data1[:5].copy()

    ext = ('.csv')

    df = pd.DataFrame()


    desktop = os.path.join(cwd, r"images")
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
            
                data_ = data_.T.copy()
                df = pd.concat([df, data_])
                to_append = [corr1]
                a_series = pd.Series(to_append, index = col_df.columns)
                col_df = col_df.append(a_series, ignore_index=True)
                
    except ValueError:
        pass
    print('pass2')
    df.to_csv('eng.csv')
    col_df.to_csv('hog_correlation_.csv')
    ##########################################################################################################################################

    cwd = os.getcwd()
    df = os.path.join(cwd, r"eng.csv")
    df2 = os.path.join(cwd, r"hog_correlation_.csv")
    data = pd.read_csv(df)
    data2 = pd.read_csv(df2)
    df_ = pd.concat([data,data2], axis=1)
    df_.drop("Unnamed: 0", axis=1, inplace=True)
    df_.to_csv('fulldata.csv')
    print('pass3')
    #######################################################################################################
    df_ = pd.read_csv('fulldata.csv')
    for index , row in df_.iterrows():
        if row.corr1/1 >= 0:
            pass
        elif row.corr1/1 <= 0:
            row.corr1 = row.corr1 * -1
    df_ = df_.drop("Unnamed: 0", axis=1).copy()
    df_ = df_.drop("0", axis=1).copy()
    df_.to_csv('samples.csv')
    print('pass4')
    sample = pd.read_csv('samples.csv')
    print(sample.shape)
    sample = np.array(sample)
    sample= sample.reshape(1,-1)
    cwd = os.getcwd()
    file = os.path.join(cwd, r"MLP.sav")
    model = pickle.load(open( file,  'rb'))
    print('pass5')
    prediction = model.predict(sample)
    
    
    return prediction