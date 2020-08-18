import glob
import pandas as pd


a = glob.glob('/scratch/nkwxol003/chest_xray/test/NORMAL/*')
my_df = pd.DataFrame(a)
my_df.to_csv('test_normal.csv', index=False, header=False)

a = glob.glob('/scratch/nkwxol003/chest_xray/test/PNEUMONIA/*')
my_df = pd.DataFrame(a)
my_df.to_csv('test_pneumonia.csv', index=False, header=False)

a = glob.glob('/scratch/nkwxol003/Desktop/chest_xray/train/NORMAL/*')
my_df = pd.DataFrame(a)
my_df.to_csv('train_normal.csv', index=False, header=False)

a = glob.glob('/scratch/nkwxol003/Desktop/chest_xray/train/PNEUMONIA/*')
my_df = pd.DataFrame(a)
my_df.to_csv('train_pneumonia.csv', index=False, header=False)
