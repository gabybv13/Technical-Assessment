# The Snowpark package is required for Python Worksheets. 
# You can add more packages by selecting them using the Packages control and then importing them.

import snowflake.snowpark as snowpark
from snowflake.snowpark.functions import col
import pandas as pd
import numpy as np

def main(session: snowpark.Session): 
    
    #1.Delete the duplicate  transaction_sin_duplicados
    df= session.sql("CREATE OR REPLACE TABLE transaction_sin_duplicados AS SELECT DISTINCT * FROM transaction")
    df.collect()

    #2.Fill null values
    table_name = 'transaction_sin_duplicados'
    query = f'SELECT * FROM {table_name}'
    dataframe = session.sql(query).to_pandas()

    #3.Remove invalid caracters
    dataframe['UNIT_PRICE'] = dataframe['UNIT_PRICE'].round(2)

    #4.Fill null values 
    for index, valor in dataframe.iterrows():
         name = f'Client_'+str(dataframe['CLIENT_ID'][index])
         if pd.isna(valor['CLIENT_NAME']):
           dataframe['CLIENT_NAME'][index]=name
             
         store = f'Store_'+str(dataframe['STORE_ID'][index])
         if pd.isna(valor['STORE_NAME']):
           dataframe['STORE_NAME'][index]=store

         product = f'Product_'+str(dataframe['PRODUCT_ID'][index])
         if pd.isna(valor['PRODUC_NAME']):
           dataframe['PRODUC_NAME'][index]=product

    
    df_snow=session.write_pandas(dataframe,table_name,auto_create_table=False, overwrite=True)

    return df_snow
