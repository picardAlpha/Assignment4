import sqlite3
import atexit

import DTOs
import dbtools
from dbtools import Dao


# ARE THESE DTOS OR DAOS?
# DTOs - Data Transfer Objects:
class Employee(object):
    # TODO: implement
    def __init__(self, id, name, salary, branche):
        self.id = id
        self.name = name
        self.salary = salary
        self.branche = branche


class Supplier(object):
    # TODO: implement
    def __init__(self, id, name, contact_information):
        self.id = id
        self.name = name
        self.contact_information = contact_information

    pass


class Product(object):
    # TODO: implement
    def __init__(self, id, description, price, quantity):
        self.id = id
        self.description = description
        self.price = price
        self.quantity = quantity

    pass


class Branche(object):
    # TODO: implement
    def __init__(self, id, location, number_of_employees):
        self.id = id
        self.location = location
        self.number_of_employees = number_of_employees


class Activitie(object):
    # TODO: implement
    def __init__(self, product_id, quantity, activator_id, date):
        self.product_id = product_id
        self.quantity = quantity
        self.activator_id = activator_id
        self.date = date


# Repository
class Repository(object):
    def __init__(self):
        self._conn = sqlite3.connect('bgumart.db')
        self._conn.text_factory = bytes
        self.employees = Dao(Employee, self._conn)  # This initiates DAOs
        self.suppliers = Dao(Supplier, self._conn)
        self.products = Dao(Product, self._conn)
        self.activities = Dao(Activitie, self._conn)
        self.branches = Dao(Branche, self._conn)

        # TODO: complete

    def _close(self):
        self._conn.commit()
        self._conn.close()

    def create_tables(self):
        self._conn.executescript("""
            CREATE TABLE employees (
                id              INT         PRIMARY KEY,
                name            TEXT        NOT NULL,
                salary          REAL        NOT NULL,
                branche    INT REFERENCES branches(id)
            );
    
            CREATE TABLE suppliers (
                id                   INTEGER    PRIMARY KEY,
                name                 TEXT       NOT NULL,
                contact_information  TEXT
            );

            CREATE TABLE products (
                id          INTEGER PRIMARY KEY,
                description TEXT    NOT NULL,
                price       REAL NOT NULL,
                quantity    INTEGER NOT NULL
            );

            CREATE TABLE branches (
                id                  INTEGER     PRIMARY KEY,
                location            TEXT        NOT NULL,
                number_of_employees INTEGER
            );
    
            CREATE TABLE activities (
                product_id      INTEGER REFERENCES products(id),
                quantity        INTEGER NOT NULL,
                activator_id    INTEGER NOT NULL,
                date            TEXT    NOT NULL
            );
        """)

    def execute_command(self, script: str) -> list:
        return self._conn.cursor().execute(script).fetchall()

    def updateProductsQuantity(self, productID, newQuantity):
        statement = 'UPDATE products SET quantity={} WHERE id={}'.format(newQuantity, productID)
        self._conn.execute(statement)

    def getAllSalesByEmployeeID(self, employeeID):
        statement = 'SELECT * FROM activities WHERE activator_id = {}'.format(employeeID)
        sales_records =  self._conn.cursor().execute(statement).fetchall()
        sales = 0
        for record in sales_records:
            if record[1] < 0:
                sales = sales + abs(record[1])*repo.products.find(id=record[0])[0].price     # multiply by product price

        return sales

    def getEmployeesOrderedByName(self):
        statement = 'SELECT * FROM employees ORDER BY name'
        return self._conn.cursor().execute(statement).fetchall()

    def getActivitiesOrderedByDate(self):
        statement = 'SELECT * FROM activities ORDER BY date ASC'
        return self._conn.cursor().execute(statement).fetchall()

# singleton
repo = Repository()
atexit.register(repo._close)
