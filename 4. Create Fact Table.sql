use database datatransactions;

use schema datatransactions.local;

Create table Sales(
transaction_id int not null,
quantity_of_items_sold numeric,
unit_price double,
discount double,
client_id int not null ,
store_id int not null ,
product_id int not null ,
address_id int not null ,
constraint pk_transaction_id primary key (transaction_id,client_id,store_id,product_id,address_id),
constraint fk_client_id foreign key(client_id) references Client(client_id) ,
constraint fk_store_id foreign key(store_id) references Store(store_id),
constraint fk_product_id foreign key(product_id) references Product(product_id),
constraint fk_address_id foreign key(address_id) references Address(address_id)
);


//Insert Sale
INSERT INTO Sales (transaction_id, quantity_of_items_sold,unit_price,discount,client_id,store_id,product_id,address_id) SELECT distinct transaction_id, quantity_of_items_sold,unit_price,discount,client_id,store_id,product_id,adress_id FROM "transaction_sin_duplicados"




