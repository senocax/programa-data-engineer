from datetime import datetime
from dateutil.relativedelta import relativedelta


class Empleados:
    """Class contains the properties of Employee.

    Args:
        nombre (str): Employee name
        apellido (str): Employee lastname
        fecha_nacimiento (str): Employee's date of birth
        nro_DNI (int): Employee ID
    Attributes:
        nombre (str): Internal attribute of Employee Name
        apellido (str): Employee Surname internal attribute
        fecha_nacimiento (str): Internal attribute of employee's date of birth
        nro_DNI (int): Internal attribute of the employee's DNI
    """

    def __init__(self, nombre, apellido, fecha_nacimiento, nro_DNI):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.nro_DNI = nro_DNI

    def calcular_edad(self):
        """Calculate employee age.

        Returns:
            int: Employee age
        """
        fecha_nacimiento = datetime.strptime(self.fecha_nacimiento, "%d/%m/%Y")
        edad = relativedelta(datetime.now(), fecha_nacimiento)
        return edad.years
