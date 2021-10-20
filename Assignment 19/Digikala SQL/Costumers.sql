DELETE FROM Customers;

INSERT INTO Customers(id , name , city , country)
VALUES(1000 , 'Ali Rezaee' , 'Tehran' , 'Iran');

INSERT INTO Customers(id , name , city , country)
VALUES(1001 , 'Mina Rahimian' , 'Tehran' , 'Iran');

INSERT INTO Customers(id , name , city , country)
VALUES(1002 , 'Sara Amiri' , 'Kish' , 'Iran');


INSERT INTO Customers(id , name , city , country)
VALUES(1003 , 'Dan Reynolds' , 'NYC' , 'USA');

DELETE FROM Customers 
WHERE country!= 'Iran';





