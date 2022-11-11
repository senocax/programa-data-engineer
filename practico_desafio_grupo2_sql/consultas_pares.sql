-- 2. De la tabla ORDERS obtener los números de las últimas 5 órdenes

SELECT orderNumber
FROM orders
ORDER BY orderNumber DESC
LIMIT 5

/* 4. Indicar en una misma consulta: la cantidad de registros de la tabla productos,
el precio promedio de los mismos, el precio máximo y el precio mínimo y la suma total
de productos en stock (sin agrupar por producto) */


SELECT
    COUNT(*) AS 'Total productos',
    TRUNCATE(AVG(MSRP), 2) AS 'Precio promedio',
    MAX(MSRP) AS 'Precio maximo',
    MIN(MSRP) AS 'Precio minimo',
    SUM(quantityInStock) AS 'Total productos en stock'
FROM products

-- 6. Obtener la cantidad de clientes por país, ordenado de mayor a menor

SELECT 
    country,
	COUNT(*) AS 'Total clientes'
FROM customers
GROUP BY country
ORDER BY COUNT(*) DESC

/* 8. Obtener todas las ordenes por número de cliente que hayan sido emitidas
en el año 2005. Solo mostrar aquellos clientes con mas de 3 ordenes */

SELECT 
    customerNumber AS 'Cliente',
    orderNumber AS 'Orden',
    orderDate AS 'Fecha de orde',
    COUNT(*) AS 'Total ordenes'
FROM Orders
WHERE YEAR(orderDate) = '2005'
GROUP BY customerNumber
HAVING COUNT(*) > 3
ORDER BY COUNT(*) DESC

/* 10. Obtener los nombres de los clientes y el monto (amount) de aquellos que
realizaron compras en los meses de Marzo de cada año. Ordenar por monto de
mayor a menor */

SELECT 
    customers.customerName,
    payments.paymentDate,
    payments.amount
FROM customers 
INNER JOIN payments ON customers.customerNumber=payments.customerNumber
WHERE MONTH(payments.paymentDate) = '03'
ORDER BY payments.amount DESC
    
-- 12. Obtener los registros de los productos cuyo codigo inicie con la secuencia " S10_ "

SELECT *
FROM products
WHERE UPPER(productCode) LIKE 'S10_%'

/* 14. Obtenga los codigos de los pagos (payments) , fecha y monto de aquellos que comienzan
con la secuencia "IP" y son mayores o iguales a 1000 */

SELECT
    checkNumber AS 'Codigo de pago',
    paymentDate AS 'Fecha',
    amount AS 'Monto'
FROM payments
WHERE UPPER(checkNumber) LIKE 'IP%'
    AND amount >= 1000
    
    
    /* 16. Obtener la cantidad de cheques emitidos por año desde el mas actual hasta el mas antiguo,
    el importe promedio de los mismos, el máximo importe y el mínimo importe */
    
  SELECT
      YEAR(paymentDate) AS 'Año',
      COUNT(*) AS 'Total cheques', 
      ROUND(AVG(amount), 2) AS 'Importe promedio',
      MAX(amount) AS 'Importe maximo',
      MIN(amount) AS 'Importe minimo'
  FROM payments
  GROUP BY YEAR(paymentDate) 
  ORDER BY YEAR(paymentDate) DESC
  
  
  /* 18. Obtener el listado de clientes que sean USA o España cuyo límite de crédito
  sea mayor a 50000 que no tengan ningun representante de ventas (salesRepEmployeeNumber) asignado */
  
  SELECT
      customerNumber AS 'ID cliente',
      customerName AS 'Nombre',
      country AS 'Pais',
      creditLimit AS 'Limite de credito',
      salesRepEmployeeNumber AS 'Representante de ventas'
  FROM customers
  WHERE UPPER(country) IN('USA', 'SPAIN')
      AND creditLimit > 50000 
      AND salesRepEmployeeNumber = NULL
      
   
