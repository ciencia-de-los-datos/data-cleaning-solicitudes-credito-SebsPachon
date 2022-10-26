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
df=df.dropna()


#colum strings
columns_ordened=['sexo', 'tipo_de_emprendimiento', 'idea_negocio', 'barrio','comuna_ciudadano','estrato','línea_credito'
, 'fecha_de_beneficio', 'monto_del_credito',]
df1=df[columns_ordened]

# #categorical variable row by row
# #tipo emprendimiento
# df1.tipo_de_emprendimiento=df1.tipo_de_emprendimiento.str.lower()
# df1.tipo_de_emprendimiento.value_counts()
# #idea de negocio
# df1.idea_negocio=df1.idea_negocio.str.lower()
# df1.idea_negocio=df1.idea_negocio.str.replace('-','').str.replace('_','').str.replace(' ','')
# sorted(df1.idea_negocio.unique())

# re.search(r"^1[\s\.-]",)

# dfs.sort_values('idea_negocio', key=lambda series: [len(x) for x in series])


# dfs.idea_negocio.str.replace('+','')


for i in columns_ordened[:-4]:
    df1[i]=df1[i].str.lower()
    df1[i]=df1[i].str.replace('-','').str.replace('_','').str.replace('i¿o','iño').str.replace(' ','').str.replace('bel¿n','belen')
# numeric variable
df1.monto_del_credito = df1.monto_del_credito.str.strip('$')
df1.monto_del_credito = df1.monto_del_credito.str.replace(',','')
df1.monto_del_credito = df1.monto_del_credito.astype(float)

df1.fecha_de_beneficio=pd.to_datetime(df1.fecha_de_beneficio,infer_datetime_format=True)
#estrato
# df.estrato[df.estrato> 3] = 3
# df.estrato[df.estrato < 1] = 1
# df[(df.estrato < 1) | (df.estrato > 3)].estrato
# 'solidaria', 'solidiaria'
#comuna
df1.comuna_ciudadano=df1.comuna_ciudadano.astype(int)
# sorted(df1.comuna_ciudadano.unique())
# df1.sort_values(by=['fecha_de_beneficio'])
#Clean duplicates
df1=df1.reset_index(drop=True)
df1.drop_duplicates(inplace=True)
df1[df1.duplicated()]

# len(df1)-len(df1[df1.isna().any(axis=1)]),5754+2252+2247+164




df1.sexo.value_counts().to_list()#== [5754,2252,2247,164]
5754+2252+2247+164

def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    #
    # Inserte su código aquí
    #

    return df
