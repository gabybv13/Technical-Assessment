# The Snowpark package is required for Python Worksheets. 
# You can add more packages by selecting them using the Packages control and then importing them.

import snowflake.snowpark as snowpark
from snowflake.snowpark.functions import col
import pandas as pd

def main(session: snowpark.Session): 
    
    #descubrir patrones y tendencias valiosos
    table_name = 'SALES'
    query = f'SELECT * FROM {table_name}'
    dataframe = session.sql(query).to_pandas()

    data = {
    'Unit_price':dataframe["UNIT_PRICE"],
    'Quantity': dataframe["QUANTITY_OF_ITEMS_SOLD"],
    'Discount': dataframe["DISCOUNT"]
    }
    
    df_temporal = pd.DataFrame(data)
    #print(df_temporal)

    #Suma total de ventas Unit_Price * Quantity * Discount
    sum=0
    for index in range(len(df_temporal)):
        price= df_temporal['Unit_price'][index]*df_temporal['Quantity'][index]
        disc= price*df_temporal['Discount'][index]
        sum+=price-disc
        
    print(f'The total sales is {sum}')
    
    #Promedio 
    mean = dataframe['QUANTITY_OF_ITEMS_SOLD'].mean()
    print(f'The mean of quantity of items sold is {mean}')

    
    #Mostrar los clientes por transaction item con más compras
    queryClient = f'SELECT c.client_name, COUNT(*) AS Count_Sale '\
            f'FROM SALES s inner join Client c on c.client_id = s.client_id '\
            f'GROUP BY c.client_name '\
            f'ORDER BY Count_Sale DESC '\
            f'limit 10'
    
    clientData = session.sql(queryClient).to_pandas()
    print(clientData)

    