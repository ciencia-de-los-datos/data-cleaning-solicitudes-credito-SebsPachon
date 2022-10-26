"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd
import numpy as np
import re

df = pd.read_csv("solicitudes_credito.csv", sep=";")
##clean nan
df[df.isna().any(axis=1)]
df=df.dropna()
#sort columns
columns_sort=['sexo', 'tipo_de_emprendimiento', 'idea_negocio', 'barrio','línea_credito','comuna_ciudadano','estrato','fecha_de_beneficio', 'monto_del_credito',]
df1=df[columns_sort]
#Categoric Variable
for i in columns_sort[:-4]:
    df1[i]=df1[i].str.lower()
    df1[i]=df1[i].str.replace('-','').str.replace('_','').str.replace('i¿o','iño').str.replace(' ','').str.replace('bel¿n','belen')
    sorted(df1[i].value_counts())
# numeric variable
df1.monto_del_credito = df1.monto_del_credito.str.strip('$')
df1.monto_del_credito = df1.monto_del_credito.str.replace(',','')
df1.monto_del_credito = df1.monto_del_credito.astype(float)
#date
df1.fecha_de_beneficio=pd.to_datetime(df1.fecha_de_beneficio,infer_datetime_format=True)
#estrato

# df.estrato[df.estrato < 1] = 1
# df[(df.estrato < 1) | (df.estrato > 3)].estrato
##comuna
df1.comuna_ciudadano=df1.comuna_ciudadano.astype(int)
#Clean duplicates
df1=df1.reset_index(drop=True)
df1.drop_duplicates(inplace=True)

for i in df1.columns:
    df1[i].value_counts()
df1.sexo.value_counts().to_list()#== == [6617, 3589]
df1.tipo_de_emprendimiento .value_counts()
10060+70+55+33+21+4+1+1+1

dfx=df1[df1.línea_credito =='microempresarial']
dfxx=dfx[dfx.tipo_de_emprendimiento =='agropecuaria']
for i in dfxx.columns:
    dfxx[i].value_counts()

 dfxx['']
def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    #
    # Inserte su código aquí
    #

    return df
