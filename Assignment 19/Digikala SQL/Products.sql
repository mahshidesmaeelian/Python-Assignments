DELETE FROM Products;

INSERT INTO Products(id , name , price , count)
VALUES(2352 , 'Shampoo' , 36.8000 , 12);

INSERT INTO Products(id , name , price , count)
VALUES(5482 , 'soap' , 24.3000 , 0);

INSERT INTO Products(id , name , price , count)
VALUES(6842 , 'milk' , 14.0000 , 24);

INSERT INTO Products(id , name , price , count)
VALUES(9125 , 'ice cream' , 4.5000 , 50);

SELECT * FROM Products
WHERE count != 0 ;

UPDATE Products
SET price= price-price*20/100;




