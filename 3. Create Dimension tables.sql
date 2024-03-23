use database datatransactions;

use schema datatransactions.local;

Create table Client(
client_id int not null,
client_name varchar(50),
client_last_name varchar(50),
email varchar(70),
constraint pk_client_id primary key (client_id)
);

Create table Store(
store_id int not null,
store_name varchar(50),
location varchar(50),
constraint pk_store_id primary key (store_id)
);


Create table Product(
product_id int not null,
product_name varchar(50),
category varchar(50),
brand varchar(50),
constraint pk_product_id primary key (product_id)
);

Create table Address(
address_id int not null,
street varchar(50),
city varchar(50),
state varchar(50),
zip_code  varchar(50),
constraint pk_address_id primary key (address_id)
);

//Insert Client
INSERT INTO Client (client_id,client_name,client_last_name,email) SELECT distinct client_id,client_name,client_lastname,email FROM "transaction_sin_duplicados"

//Insert Store
INSERT INTO Store (store_id,store_name,location) SELECT distinct
store_id,store_name,location FROM "transaction_sin_duplicados"

//Insert Product
INSERT INTO Product (product_id,product_name,category,brand) SELECT  distinct
product_id,produc_name,category,brand FROM "transaction_sin_duplicados"

//Insert Address
INSERT INTO Address (address_id,street,city,state,zip_code) SELECT distinct
adress_id,street,city,state,zip_code FROM "transaction_sin_duplicados"





