import configparser
import logging.config
from os import path

import sqlalchemy as db
from sqlalchemy import Column, MetaData, Table
from sqlalchemy.orm import Session

from Models import Base, Customer

# ----- Config postgreSQL Database credentials ------
config = configparser.ConfigParser()
config.read('config.ini')
db_user = config['DEFAULT']['DB_USER']
db_pass = config['DEFAULT']['DB_PASSWORD']
db_name = config['DEFAULT']['DB_NAME']
db_host = config['DEFAULT']['DB_HOST']
db_port = config['DEFAULT']['DB_PORT']
# -----End config credentials ------

# ----- Config logging ------
log_file_path = path.join(
    path.dirname(
        path.abspath('log_file_config.conf')),
    'log_file_config.conf')
logging.config.fileConfig(log_file_path)
logger_main = logging.getLogger("database")
# -----End Config logging ------


class Database:
    """Class used for database connections and methods manipulating table.
    """
    try:
        DATABASE_URI = f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
        engine = db.create_engine(DATABASE_URI)
        Base.metadata.create_all(bind=engine)
    except Exception:
        logger_main.error(f"Error  in database {Exception}")

    def __init__(self) -> None:
        """Init method connect to postgreSQL.
        """
        self.connection = self.engine.connect()
        print("Database connection succesfuly")

    def fetchByQuery(self, query: str) -> None:
        """Fetch by query in customer table.
        """
        fetchByQuery = self.connection.execute(f'SELECT * FROM {query}')

        for data in fetchByQuery.fetchall():
            print(data)

    def fetchUserByName(self) -> None:
        """Fetch by username in customer table.
        """
        meta = MetaData()
        customer = Table('customer', meta, Column('name'), Column('age'))
        data = self.connection.execute(customer.select())
        for cust in data:
            logger_main.info(cust)

    def fetchAllUsers(self) -> None:
        """Fetch all users in customer table.
        """
        self.session = Session(bind=self.connection)
        customers = self.session.query(Customer).all()
        for cust in customers:
            print(cust)

    def saveData(self, customer) -> None:
        """Save data in table customer.

        Args:
            Customer (Customer): table mapper.
        """
        try:
            session = Session(bind=self.connection)
            session.add(customer)
            session.commit()
            logger_main.info("Customer save success")
        except Exception:
            logger_main.error(f"Error database {Exception}")

    def updateCustomer(self, customerName, address) -> None:
        """Update customer name and new address.

        Args:
            customerName (str): Customer name data.
            address (str): Customer address data.
        """

        session = Session(bind=self.connection)
        dataToUpdate = {Customer.address: address}
        try:
            customerData = session.query(Customer).filter(
                Customer.name == customerName)
            customerData.update(dataToUpdate)
            session.commit()
            logger_main.info("Updated DB with success")
        except Exception:
            logger_main.error(f"Error in DB update customer {Exception}")

    def deleteCustomer(self, customerName: str) -> None:
        """Delete customer data.

        Args:
            customerName (str): Customer name data.
        """
        session = Session(bind=self.connection)
        try:
            customerData = session.query(Customer).filter(
                Customer.name == customerName).first()
            session.delete(customerData)
            logger_main.info(f"Delete Customer: {customerData} was delete")
        except Exception:
            logger_main.error(f"Error in {Exception}")
        session.commit()


if __name__ == '__main__':

    dbinfo = Database()
    customer = Customer(
        "Johnny Robbins",
        23,
        "JohnnyR@myemail.com",
        "316 Hannah Street",
        "28202")

    dbinfo.saveData(customer)
    dbinfo.fetchUserByName()
    dbinfo.fetchAllUsers()
    dbinfo.updateCustomer("Johnny Robbins", "1826 Jerry Toth")
    dbinfo.deleteCustomer("Johnny Robbins")
