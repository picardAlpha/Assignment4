from persistence import *
import sqlite3
import os
import atexit
import persistence


def main():
    # TODO : print activities organized by dates with
    #        date of activity, item description, quantity, name of seller(=none if its a sale), name of supplier

    print("Activities")
    for activity in repo.activities.find_all():
        print((activity.product_id, activity.quantity, activity.activator_id, activity.date.decode('utf-8')))


    print("Branches")

    branches = repo.branches.find_all()
    for branch in branches:
        branches_tuple = (branch.id, branch.location.decode('utf-8'), branch.number_of_employees)
        print(branches_tuple)

    print("Employees")
    employees = repo.employees.find_all()
    for employee in employees:
        employees_tuple = (employee.id, employee.name.decode('utf-8'), employee.salary, employee.branche)
        print(employees_tuple)

    # TODO : print products ordered by id with : id, name, price, quantity

    print("Products")
    for product in repo.products.find_all():
        print((product.id, product.description.decode('utf-8'), product.price, product.quantity))

    # TODO : print suppliers ordered by id with : id, name, phone number

    print("Suppliers")
    for supplier in repo.suppliers.find_all():
        print((supplier.id, supplier.name.decode('utf-8'), supplier.contact_information.decode('utf-8')))

    print()
    print("Employees report")
    # TODO : print employees report NOT A TUPLE, each row contains :
    #  name, salary, working location, total sales income
    for employee in repo.getEmployeesOrderedByName():
        print(employee[1].decode('utf-8') + " " +  # employee name
              str(employee[2]) + " " +  # salary
              repo.branches.find(id=employee[3])[0].location.decode('utf-8') + " " +  # employee branch location name
              str(repo.getAllSalesByEmployeeID(employee[0])))

    # TODO : Activity Report : print tuples ordered by date of activities with :
    #        date, products sold description, change in quantity, name of seller, name of supplier.
    #        if the quantity number is positive then the id is of the supplier

    print()
    print("Activities report")

    for activity in repo.getActivitiesOrderedByDate():
        seller_name = None
        supplier_name = None

        if (activity[1] < 0):
            seller_name = repo.employees.find(id=activity[2])[0].name.decode('utf-8')
        elif activity[1] > 0:
            supplier_name = repo.suppliers.find(id=activity[2])[0].name.decode('utf-8')
        elif activity[1] == 0:  # SHOULDN'T EVEN BE HERE
            continue
        activity_tuple = (
            activity[3].decode('utf-8'), repo.products.find(id=activity[0])[0].description.decode('utf-8'), activity[1],
            seller_name, supplier_name)
        print(activity_tuple)


if __name__ == '__main__':
    main()
