/* Creando base de datos escuela */
CREATE DATABASE Escuela;

GO

/* Creando tabla Alumno, Materia y Cursa */
CREATE TABLE Alumnos(
Legajo INT primary key,
Nombre VARCHAR(20) not null,
Apellido VARCHAR(20) not null,
Fecha_nacimiento DATETIME
);

GO

CREATE TABLE Materia(
Codigo INT primary key,
Descripcion VARCHAR(20) NOT NULL
CONSTRAINT fk_Alumnos FOREIGN KEY (codigo) REFERENCES Alumnos (legajo),
);

GO

CREATE TABLE  Cursa(
legajo_Id INT primary key,
codigo_materia INT NOT NULL,
CONSTRAINT fk_Alumno FOREIGN KEY (legajo_id) REFERENCES Alumnos (Legajo),
CONSTRAINT fk_Materia FOREIGN KEY (codigo_materia) REFERENCES Materia (Codigo)
);

GO

/* Insertar 5 tuplas en cada tabla creada dentro de Alumnos, Materia y Cursa */
INSERT INTO dbo.Alumnos (Legajo, Nombre, Apellido, Fecha_nacimiento )
VALUES (1, 'Enrique','Solis', '1990/08/04'),
(2, 'Leandro','Montoya', '1990/08/04'), 
(3, 'Miguel','Lopez', '1991/04/04'),
(4, 'Nicolas','Garcìa', '1992/02/01'), 
(5,'Rodofol', 'Canes', '1991/07/03');

GO

INSERT INTO dbo.Alumnos (Legajo, Nombre, Apellido, Fecha_nacimiento )
VALUES (1, 'Química', 'Quimica basica'),
(2, 'Historia', 'Historia Argetina contemporánea'),
(3, 'Geografía', 'Geografía de argentina'),
(4, 'Física', 'física general'),
(5, 'Informàtica', 'Laboratorio de computaciòn');
GO
INSERT INTO dbo.Materia (Codigo, Descripcion)
VALUES (1, 'Quimica'),
(2, 'Historia Argetina'),
(3, 'Geografía'),
(4, 'física general'),
(5, 'Ciencias Sociales');

GO

INSERT INTO dbo.Cursa  (Legajo_id, codigo_materia)
VALUES (1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5);

/* Borra base de datos Escuela*/
/* DROP DATABASE Escuela; */
