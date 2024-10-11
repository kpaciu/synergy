CREATE DATABASE WebAppDB;
GO

USE WebAppDB;
GO

CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName NVARCHAR(100),
    Price DECIMAL(18, 2),
    Quantity INT
);
GO

INSERT INTO Products (ProductID, ProductName, Price, Quantity)
VALUES
(1, 'Product A', 99.99, 10),
(2, 'Product B', 149.99, 5),
(3, 'Product C', 199.99, 3);
GO
