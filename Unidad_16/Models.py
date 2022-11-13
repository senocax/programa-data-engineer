from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()


class Customer(Base):
    """Representing customer table model.

    :param Base: Mapper ORM
    :type Base: Base
    :return: Get customer table data
    :rtype: Customer
    """

    __tablename__ = 'customer'
    name = Column(String)
    age = Column(Integer)
    email = Column(String)
    address = Column(String)
    zip_code = Column(String)
    id = Column(Integer, autoincrement=True, primary_key=True)

    def __init__(
            self,
            name: str,
            age: int,
            email: str,
            address: str,
            zip_code: str) -> None:
        """Customer class that will respect the same structure table.

        Args:
            name (str): Customer name.
            age (int): Customer age.
            email (str): Customer email.
            address (str): Customer address.
            zip_code (str): Customer zip_code.
        """
        self.name = name
        self.age = age
        self.email = email
        self.address = address
        self.zip_code = zip_code

    def __repr__(self) -> str:
        """Describe the object of customer table.

        Returns:
            str: Customer table data.
        """
        return f"""<Customer ({self.name}, {self.age}, {self.email}, {self.address},  {self.zip_code})>"""
