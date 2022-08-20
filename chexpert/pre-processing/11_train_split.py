import pandas as pd

# read the csv file
dataset_df = pd.read_csv("train_valid_frontal_6_classes_real_no_zeros_preprocessed.csv")

# 80/20 split
n = round(dataset_df.shape[0]*0.8)

df1 = dataset_df.iloc[:n,:]
df2 = dataset_df.iloc[n:,:]

print(df1.shape)
print(df2.shape)

df1.columns=[
    '',
    'Path',
    'Sex',
    'Age',
    'Frontal/Lateral',
    'AP/PA',
    'Cardiomegaly',
    'Edema',
    'Consolidation',
    'Pneumonia',
    'Atelectasis',
    'Pneumothorax',]

df2.columns=[
    '',
    'Path',
    'Sex',
    'Age',
    'Frontal/Lateral',
    'AP/PA',
    'Cardiomegaly',
    'Edema',
    'Consolidation',
    'Pneumonia',
    'Atelectasis',
    'Pneumothorax',]

df1.to_csv('train_94482_frontal_6_classes_real_no_zeros_preprocessed.csv', index=False)
df2.to_csv('train_23620_frontal_6_classes_real_no_zeros_preprocessed.csv', index=False)
