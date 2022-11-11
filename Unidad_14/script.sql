/* Listar los nombres de los proveedores cuya ciudad contenga
la cadena de texto “Ramos”. */

SELECT Ciudad
FROM Proveedor
WHERE Ciudad LIKE '%Ramos%'

/* Listar los códigos de los materiales que provea el proveedor 4
y no los provea el proveedor 5. Se debe resolver de 3 formas. */

/* Primera forma */
SELECT CodMat
FROM Provisto_por
WHERE CodProv = 4 AND CodMat NOT IN (SELECT CodMat
FROM Provisto_por
WHERE CodProv = 5)

/* segunda forma */
SELECT CodMat
FROM Provisto_por pp
WHERE CodProv = 4 AND NOT EXISTS (SELECT 1
FROM Provisto_por pp2
WHERE CodProv = 5 and pp.CodMat=pp2.CodMat)

/* tercera forma */
SELECT CodMat
FROM Provisto_por
WHERE CodProv = 4
EXCEPT
SELECT CodMat
FROM Provisto_por
WHERE CodProv = 5

/*Listar los materiales, código y descripción, provistos por
proveedores de la ciudad de Ramos Mejía. */

SELECT m.*
FROM material m INNER JOIN Provisto_Por pp on
m.CodMat=pp.CodMat
INNER JOIN proveedor p ON p.CodProv=pp.CodProv
WHERE p.ciudad ='Ramos Mejía'

/* Listar los proveedores y materiales que provee. La lista
resultante debe incluir a aquellos proveedores que no proveen
ningún material. */
S
SELECT m.*, p.Nombre 
FROM material m FULL OUTER JOIN Provisto_Por pp ON
m.CodMat=pp.CodMat
FULL OUTER JOIN proveedor p ON p.CodProv=pp.CodProv

/* Listar los artículos que cuesten más de $30 o que estén
compuestos por el material 2. */

SELECT a.codArt
FROM Articulo a
WHERE a.precio > 30
UNION
Select cp.CodArt
FROM Compuesto_por cp
WHERE cp.codMat = 2;

/* Listar los artículos de Mayor precio. */

SELECT TOP 3 *
FROM Articulo
ORDER BY Precio DESC;

/* Otra forma */
SELECT *
FROM Articulo a
WHERE a.Precio = (SELECT Max(Precio) FROM Articulo);

/* Listar los proveedores que proveen más de 3 materiales */

SELECT  p.Nombre , COUNT(m.CodMat) AS cantidad
FROM material m INNER JOIN Provisto_Por pp ON
m.CodMat=pp.CodMat
INNER JOIN proveedor p ON p.CodProv=pp.CodProv
GROUP BY p.Nombre  
HAVING COUNT(m.CodMat) > 3
ORDER BY p.Nombre DESC

/* Crear una vista para el caso de los proveedores que proveen
más de 4 materiales. Mostrar la forma de invocar esa vista. */

CREATE VIEW v_lista_proveedores_mas_de_tres_materiales AS
SELECT  p.Nombre , COUNT(m.CodMat) AS cantidad
FROM material m INNER JOIN Provisto_Por pp ON
m.CodMat=pp.CodMat
INNER JOIN proveedor p ON p.CodProv=pp.CodProv
GROUP BY p.Nombre  
HAVING count(m.CodMat) > 4

/* Invocacion de la vista */

SELECT *
FROM v_lista_proveedores_mas_de_tres_materiales


