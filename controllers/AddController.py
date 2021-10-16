from tkinter import messagebox
from tkinter.constants import END

from models.Customers import Customers
from core.Controller import Controller


class AddController(Controller):
    '''Responsible for AddView behavior'''

    def __init__(self):
        self.addView = self.loadView("add")
        self.customers = Customers()
        
    def btn_clear(self, fields):
        '''Clear all fields of AddView'''
        for field in fields:
            field.delete(0, END)

    def btn_add(self, fields):
        '''Adds a new customer with field data'''
        response = self.customers.add(fields)
        
        if response > 0:
            messagebox.showinfo("Add customer", "Customer successfully added!")
        else:
            messagebox.showerror("Add customer", "Error while adding customer")
            
        self.addView.close()

    def main(self):
        self.addView.main()
