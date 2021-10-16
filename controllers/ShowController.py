from tkinter import messagebox

from core.Core import Core
from core.Controller import Controller
from models.Customers import Customers


'''Responsible for ShowView behavior'''
class ShowController(Controller):

    def __init__(self):
        self.customers = Customers()
        self.showView = self.loadView("show")
        self.core = Core()

    def getCustomers(self):
        '''All customers in database'''
        data = self.customers.getAll()
        return data

    def btnEdit(self, id_customer):
        '''Opens EditController'''
        customer = self.customers.get(id_customer)
        c = self.core.openController("edit")
        c.main(customer, self.showView)

    def btnDel(self, id_customer):
        '''Deletes the chosen customer and updates the ShowView'''
        self.customers.delete(id_customer)
        self.showView.update()
        messagebox.showinfo("Delete customer", "Customer deleted with success!")

    def main(self):
        self.showView.main()
