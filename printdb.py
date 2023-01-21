from persistence import *
import sqlite3
import os
import atexit
import persistence


def main():
    # TODO : print activities organized by dates with
    #        date of activity, item description, quantity, name of seller(=none if its a sale), name of supplier


    # TODO : print branches
    branches = repo.branches.find_all()
    employees = repo.employees.find(id=101)[0]
    print(employees.branche)



    # TODO : print employees ordered by id with :
    #        id, name, salary, working location, total sales income



    # TODO : print products ordered by id with : id, name, price, quantity



    # TODO : print suppliers ordered by id with : id, name, phone number


    # TODO : print employees report NOT A TUPLE, each row contains : name,


if __name__ == '__main__':
    main()
