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
from lib2to3.pgen2.pgen import DFAState
import pandas as pd
import numpy as np
import re



def clean_data():
    # Inserte su código aquí
    df = pd.read_csv("solicitudes_credito.csv", sep=";",usecols=[1,2,3,4,5,6,7,8,9,])
    #clean nan and duplicates
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    columns_sort=['sexo', 'tipo_de_emprendimiento', 'idea_negocio', 'monto_del_credito',
        'línea_credito' 'barrio', 'estrato',
        'comuna_ciudadano', 'fecha_de_beneficio',]

    #Lower()
    for i in columns_sort[:-3]:
        df[i]=df[i].apply(lambda x :str(x).lower().strip())

    #Replace column by column
    df.idea_negocio = df.idea_negocio.apply(lambda x: str(x).replace("-"," ").replace("_"," ").strip())
    df.línea_credito= df.línea_credito.apply(lambda x: str(x).lower().replace("-", " ").replace("_", " ").strip())
    df.barrio= df.barrio.apply(lambda x: str(x).lower().replace("-"," ").replace("_"," "))
    df.monto_del_credito= df.monto_del_credito.apply(lambda x: str(x).strip("$").strip().replace(",", ""))
    df.monto_del_credito= df.monto_del_credito.astype('float')

    #date
    df.fecha_de_beneficio=pd.to_datetime(df["fecha_de_beneficio"], dayfirst=True)

    #clean nan and duplicates 
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    return df