#!/usr/bin/env python
"""
# This code is to facilitate and automate Ice cream shop
# Date/Time: 07-June-2021 6:40pm
# Author: Vudayagiri Nagaraju
# Contact: vudayagiri.nagaraju@ltts.com
"""


from abc import ABC, abstractmethod


class Login(ABC):
    """ Login class used for user or admin profile"""

    def __init__(self):
        """ constructor to initialize login credentials"""
        self.user_pwd = "User@123"
        self.admin_pwd = "Admin@123"

    @abstractmethod
    def user_login(self, passwd):
        """ To authenticate the User login """
        if self.user_pwd == passwd:
            return 1
        return 0

    @abstractmethod
    def admin_login(self, passwd):
        """ To authenticate the admin login """
        if self.admin_pwd == passwd:
            return 1
        return 0


class IceCream:
    """ IceCream class which has Ice cream type and flavours list"""

    icecream_list = {"Cup": 25, "Cone": 30, "Scoop": 50, "Box": 200}
    flavour_list = {"Vanilla": 5, "Butterscotch": 10, "Chocolate": 15}
    coupon_disc = 50

    def icecream_add(self, name):
        """This function is to add/update a new ice cream/flavour and its price into the list """
        while True:
            try:
                price = int(input("Enter the ice cream price: "))
                break
            except ValueError:
                print("Invalid ice cream price")

        if self.icecream_search(name):
            print("\nIce cream already exists")
        else:
            self.icecream_list[name] = price
            print("Ice cream added successfully")
        return 0

    def flavour_add(self, flavour_name):
        """This function is to add/update a new ice cream/flavour and its price into the list """
        while True:
            try:
                flavour_price = input("Enter the " + flavour_name + "flavour price: ")
                break
            except ValueError:
                print("Invalid flavour price")

        if self.flavour_search(flavour_name):
            print("\nFlavour already exists")
        else:
            self.flavour_list[flavour_name] = int(flavour_price)
            print("New flavour added successfully")
        return 0

    def icecream_update(self, name, flavour_name):
        """This function is to update a new ice cream/flavour and its price into the list """
        while True:
            try:
                price = int(input("Enter the ice cream price: "))
                break
            except ValueError:
                print("Invalid ice cream price")
        if name not in self.icecream_list.keys():
            while True:
                try:
                    flavour_price = input("Enter the " + flavour_name + "flavour price: ")
                    break
                except ValueError:
                    print("Invalid flavour price")

            if flavour_name not in self.flavour_list.keys():
                self.icecream_list[name] = price
                self.flavour_list[flavour_name] = int(flavour_price)
                print("New ice cream and flavour added successfully")
                return 1
            self.icecream_list[name] = price
            self.flavour_list[flavour_name] = int(flavour_price)
            print("Ice cream prices updated successfully")
            return 1
        print("\nIce cream already exists")
        return 0

    def icecream_view(self):
        """This function is to view the list of available ice creams"""
        print("Ice creams available now")
        cnt = 1
        for i in self.icecream_list:
            print(cnt, "\tIce Cream:", i.ljust(10), "\tPrice: Rs.", self.icecream_list[i])
            cnt = cnt + 1

        for j in self.flavour_list:
            print(j.ljust(15), "\t  extra Price: Rs.", self.flavour_list[j])
        return 1

    def icecream_search(self, name):
        """This function is used to search a ice cream """
        if name in self.icecream_list.keys():
            return 1
        else:
            return 0

    def flavour_search(self, flavour_name):
        """This function is used to search a ice cream flavour """
        if flavour_name in self.flavour_list.keys():
            return 1
        else:
            return 0

    def ice_flavour_search(self, name, flavour_name):
        """This function is used to search a ice cream by its flavour"""
        name_flag = self.icecream_search(name)
        flavour_flag = self.flavour_search(flavour_name)
        if name_flag:
            print(" Ice cream " + name + " is available in ")
        else:
            print(" Ice cream " + name + " is NOT available in ")

        if flavour_flag:
            print(" flavour " + flavour_name)
        else:
            print(" flavour " + flavour_name + "  Out of stock\n")

        if name_flag and flavour_flag:
            return 1
        else:
            return 0

    def calculate_cost(self, icecream, flavour_name, total_quantity):
        """This function is to calculate the cost of ice creams"""
        price = self.icecream_list[icecream]
        flavour_price = self.flavour_list[flavour_name]
        cost = (flavour_price + price) * total_quantity
        return cost

    def order_icecream(self, coupon_disc=0):
        """This function is to get customer input and order ice creams accordingly"""
        customer_name = input("Enter customer name: ")
        total_amount = 0.0
        total_orders = 0
        while True:
            total_quantity = 0
            item_cost = 0
            flavour_name = None
            while True:
                # get the ice cream from customer
                icecream = input("Choose the Ice cream you wish to enjoy: ")
                if self.icecream_search(icecream) is False:
                    print("Invalid Ice cream")
                    break

                # get the flavour from customer
                flavour_name = input("Choose the Flavour: ")
                if self.flavour_search(flavour_name) is False:
                    print("Invalid Ice cream")
                    break

                # get the quantity from customer
                try:
                    total_quantity = 0
                    total_quantity = int(input("Enter the total quantity: "))
                    break
                except ValueError:
                    print("Invalid quantity")
                break

            # calculate the cost of item
            if self.icecream_search(icecream):
                if self.flavour_search(flavour_name):
                    item_cost = self.calculate_cost(icecream, flavour_name, total_quantity)
                    total_amount += item_cost

            # writing order data in to the file data.txt
            with open("data.txt", "a") as dat:
                dat.write("Item No: " + str(total_orders + 1) + "\t")
                dat.write(" " + flavour_name + "\t")
                dat.write(" " + icecream + " ice cream ordered " + "\t")
                dat.write(" " + str(total_quantity) + " quantity." + "\t")
                dat.write(" Cost is Rs. " + str(item_cost) + "\n")
                dat.close()

            # If want to order more items.
            next_order = int(input("\nEnter 1 to order more. Else 2 to check out: "))
            if next_order == 2:
                print("Ice cream ordered successfully!")
                break
            elif next_order == 1:
                total_orders += 1
                continue
            else:
                print("\n Invalid Input")

        # print total bill based on coupon discount
        print("Customer Name: Mr/Mrs. " + customer_name + "\t")
        if coupon_disc and (total_amount > 200):
            print("Amount to be paid: ", total_amount - coupon_disc, " [Coupon Applied!] \n")
        else:
            print("Amount to be paid: ", total_amount, "\n")
        print("-----------------------------------------\n")

        # writing total bill amount to the file data.txt
        with open("data.txt", "a") as dat:
            dat.write("Customer Name: Mr/Mrs. " + str(customer_name) + "\n")
            dat.write("Total Bill Amount : Rs. " + str(total_amount) + "\n")
            dat.write("-----------------------------------------\n\n")
            dat.close()
        print("Thank you for ordering. Enjoy the ice cream!! \n")
        input("Press any key for next customer.. ")
        return 0

    @staticmethod
    def view_orders():
        """To view the list of ice cream orders from the data file"""
        with open("data.txt", "r") as dat:
            print(dat.read())
            dat.close()
        return 1


class ShopLogin(Login, IceCream):
    """ ShopLogin class used for user or admin profile"""
    # def __init__(self):
    #    """ constructor to initialize parent class"""
    #    super().__init__()

    def user_login(self, passwd):
        """ To authenticate the User login """
        if self.user_pwd == passwd:
            return 1
        return 0

    def admin_login(self, passwd):
        """ To authenticate the admin login """
        if self.admin_pwd == passwd:
            return 1
        return 0

    def user_menu(self):
        """Display as the Dealer Home Screen"""
        while True:
            print("\n\nWelcome to the Ice Cream Shop\n")
            print("--------------------------------------\n")
            print("Enter 1 to view all ice creams")
            print("Enter 2 to search a ice cream")
            print("Enter 3 to order ice creams")
            print("Enter any other keys to exit\n")
            while True:
                try:
                    choice = int(input())
                    break
                except ValueError:
                    print("Invalid option")
            if choice == 1:
                self.icecream_view()

            elif choice == 2:
                icecream = input("Enter the ice cream you want to search: ")
                flavour_name = input("Enter the flavour you want to search: ")
                self.ice_flavour_search(icecream, flavour_name)

            elif choice == 3:
                print("Want to order ice creams with or without coupon")
                opt = int(input("Enter 1 if No Coupon \nEnter 2 if Coupon"))
                if opt == 1:
                    self.order_icecream()
                elif opt == 2:
                    self.order_icecream(self.coupon_disc)
            else:
                break

    def admin_menu(self):
        """Display as the Admin Home Screen"""
        while True:
            print("\n\nWelcome to the Ice Cream Shop\n")
            print("-------------------------------------- \n")
            print("Enter 1 to add an ice cream")
            print("Enter 2 to add a flavour")
            print("Enter 3 to view all ice creams")
            print("Enter 4 to check ice creams stock")
            print("Enter any other keys to exit: \n")
            while True:
                try:
                    choice = int(input())
                    break
                except ValueError:
                    print("Invalid option")
            if choice == 1:
                name = input("Enter the ice cream you want to add: ")
                self.icecream_add(name)
            elif choice == 2:
                flv = input("Enter the ice cream flavour: ")
                self.icecream_add(flv)
            elif choice == 3:
                self.icecream_view()
            elif choice == 4:
                self.view_orders()
            else:
                break

    def validate_user(self):
        """ Validate the User/admin login """
        print("\n\nWelcome to the Ice Cream Shop\n")
        print("--------------------------------------\n")
        passwd = input("Enter the password for admin/user login: ")
        if self.user_login(passwd):
            print("\nUser login successful!")
            self.user_menu()
        elif self.admin_login(passwd):
            print("\nAdmin login successful!")
            self.admin_menu()
        else:
            print("Entered wrong password")


obj_login = ShopLogin()
obj_login.validate_user()
