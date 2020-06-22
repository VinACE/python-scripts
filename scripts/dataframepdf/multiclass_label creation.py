# https://stackoverflow.com/questions/36909977/update-row-values-where-certain-condition-is-met-in-pandas

## converting the dataframe into required format...
import pandas as pd
df = pd.read_csv('/root/sharedfolder/CheXpert-v1.0-small/train_v1.csv')
df.head()
df1 = df.drop(['Sex', 'Age', 'Frontal/Lateral','AP/PA'], axis=1)
df1.shape

df_rename = df1.rename(columns={'No Finding':'NoFinding','Enlarged Cardiomediastinum': 'EnlargedCardiomediastinum', 'Lung Opacity': 'LungOpacity',
                        'Lung Lesion':'LungLesion', 'Pleural Effusion':'PleuralEffusion', 'Pleural Other':'PleuralOther','Support Devices':'SupportDevices'
                        
                       })
list(df_rename.columns)

df_rename=df_rename.dropna(subset=[ 'NoFinding', 'EnlargedCardiomediastinum', 'Cardiomegaly', 'LungOpacity', 'LungLesion', 'Edema', 'Consolidation', 'Pneumonia', 'Atelectasis', 'Pneumothorax', 'PleuralEffusion', 'PleuralOther', 'Fracture', 'SupportDevices'], how='all')


df_rename.columns
#df_rename.dropna(thresh=2)


new_cols = ['v1','v2','v3','v4','v5','v6','v7','v8','v9','v10','v11','v12','v13','v14']
df_rename = df_rename.reindex(df_rename.columns.union(new_cols), axis=1)

df_rename.loc[df_rename['NoFinding']==1, 'v1'] = 'NoFinding'
df_rename.loc[df_rename['Atelectasis']==1, 'v2'] = 'Atelectasis'
df_rename.loc[df_rename['Cardiomegaly']==1, 'v3'] = 'Cardiomegaly'
df_rename.loc[df_rename['Consolidation']==1, 'v4'] = 'Consolidation'
df_rename.loc[df_rename['Edema']==1, 'v5'] = 'Edema'
df_rename.loc[df_rename['EnlargedCardiomediastinum']==1, 'v6'] = 'EnlargedCardiomediastinum'
df_rename.loc[df_rename['Fracture']==1, 'v7'] = 'Fracture'
df_rename.loc[df_rename['LungLesion']==1, 'v8'] = 'LungLesion'
df_rename.loc[df_rename['LungOpacity']==1, 'v9'] = 'LungOpacity'
df_rename.loc[df_rename['PleuralEffusion']==1, 'v10'] = 'PleuralEffusion'
df_rename.loc[df_rename['PleuralOther']==1, 'v11'] = 'PleuralOther'
df_rename.loc[df_rename['Pneumonia']==1, 'v12'] = 'Pneumonia'
df_rename.loc[df_rename['Pneumothorax']==1, 'v13'] = 'Pneumothorax'
df_rename.loc[df_rename['Support'Path',Devices']==1, 'v14'] = 'SupportDevices'



df_final = df_rename[['Path','v1','v2','v3','v4','v5','v6','v7','v8','v9','v10','v11','v12','v13','v14']]


# replace all NaN
df_final = df_final.fillna('')
df_final['tags'] =  df_final[['v1','v2','v3','v4','v5','v6','v7','v8','v9','v10','v11','v12','v13','v14']].apply(lambda x: ' '.join(x), axis=1)
df_final01 = df_final[['Path','tags']]

df_final02.dropna(subset=['tags'])
df_final02.to_csv('/root/sharedfolder/train_v01.csv', sep=",", encoding='utf-8',index=False)

train_df = pd.read_csv('/root/sharedfolder/CheXpert-v1.0-small/train_v03.csv')
train_df