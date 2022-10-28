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




def clean_data():
    # Inserte su código aquí
    df = pd.read_csv("solicitudes_credito.csv", sep=";",usecols=[1,2,3,4,5,6,7,8,9,])

    ##clean nan
    # df[df.isna().any(axis=1)]x
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)
    #sort columns
    columns_sort=['sexo', 'tipo_de_emprendimiento', 'idea_negocio','línea_credito', 'barrio', 'monto_del_credito','comuna_ciudadano','estrato','fecha_de_beneficio',]
    df[columns_sort]
    #Categoric Variable

    # df[i]=df[i].apply(lambda x :str(x).lower().strip())
    # df[i]=df[i].apply(lambda x :str(x).replace('-','').strip().replace('_','').strip())

    for i in columns_sort[:-3]:
        print(i)
        df[i]=df[i].apply(lambda x :str(x).lower().strip())
        if i in ['idea_negocio','línea_credito', 'barrio']:
            df[i]=df[i].apply(lambda x :str(x).replace('-','').strip().replace('_','').strip())
        elif i=="monto_del_credito":
            df[i] =  df[i].apply(lambda x: str(x).strip("$").strip().replace(".00", "").replace(",", ""))
        
    #date
    df["fecha_de_beneficio"]=pd.to_datetime(df["fecha_de_beneficio"], dayfirst=True)

    #Clean duplicates
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)

    df.sexo.value_counts()  

    return df
