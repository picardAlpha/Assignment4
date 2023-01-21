import dbtools
import persistence
from persistence import *

import sys
import os


# This module builds the database and inserts the initial data from the configuration file. When run, it will be
# given a configuration file as an argument. For example: # python3 initiate.py config.txt # If the database file
# already exists remove it. # Initiate.py should create a “fresh” database with the tables as specified,
# parse the configuration file, and store the data given in the configuration file in the database appropriately.


def add_branche(splittedline: list[str]):
    # TODO: add the branch into the repo
    pass


def add_supplier(splittedline: list[str]):
    # TODO: insert the supplier into the repo
    pass


def add_product(splittedline: list[str]):
    # TODO: insert product
    pass


def add_employee(splittedline: list[str]):
    # TODO: insert employee
    pass


adders = {"B": add_branche,
          "S": add_supplier,
          "P": add_product,
          "E": add_employee}


def main(args: list[str]):
    inputfilename = args[1]
    # delete the database file if it exists
    repo._close()
    # uncomment if needed
    if os.path.isfile("bgumart.db"):
        os.remove("bgumart.db")
    repo.__init__()
    repo.create_tables()
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline: list[str] = line.strip().split(",")
            adders.get(splittedline[0])(splittedline[1:])

    # TODO : read the config.txt and create DTOs from it

    repo.branches.insert(persistence.Branche(1,"Bash",0))
    repo.employees.insert(persistence.Employee(1, "Adam",1000,3))  # TODO : When this happens we should update the number of employees in the branch!!





if __name__ == '__main__':
    main(sys.argv)
