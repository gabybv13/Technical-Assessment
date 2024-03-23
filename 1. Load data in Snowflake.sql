use database datatransactions;

use schema datatransactions.local;

Create table Transaction(
client_id numeric,
client_name varchar(50),
client_lastname varchar(50),
email varchar(70),
store_id numeric,
store_name varchar(50), 
location varchar(50),
product_id numeric,
produc_name varchar(50),
category varchar(50),
brand varchar(50),
adress_id numeric,
street varchar(50),
city varchar(50),
state varchar(50),
zip_code numeric,
transaction_id numeric,
quantity_of_items_sold numeric,
unit_price double,
discount double
);


