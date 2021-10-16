from tkinter import messagebox

from models.Customers import Customers
from core.Controller import Controller


'''Responsible for EditView behavior'''
class EditController(Controller):

    def __init__(self):
        self.editView = self.loadView("edit")
        self.customers = Customers()

    def main(self, customer, showView):
        self.showView = showView
        self.customer = customer
        self.editView.main()

    def getCustomer(self):
        '''Customer being edited'''
        return self.customer

    def btnSave(self, fields):
        '''Saves customer edited'''
        response = self.customers.update(fields)
        self.showView.attributes("-topmost", False)
        if response > 0:
            messagebox.showinfo("Update customer", "Customer updated with success!")
        else:
            messagebox.showerror("Update customer", "Error while updating")
        self.showView.attributes("-topmost", True)
        self.showView.update()
        self.editView.close()
        self.showView.attributes("-topmost", False)
