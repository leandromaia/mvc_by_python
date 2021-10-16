# -*- encoding:utf-8 -*-
from core.Controller import Controller
from core.Core import Core


'''Main controller. It will be responsible for program's main screen behavior.'''
class HomeController(Controller):

    def __init__(self):
        self.homeView = self.loadView("Home")

    def btnClicked(self, caption):
        '''Opens controller according to the option chosen'''
        if caption == "Open Customers DB":
            c = Core.openController("show")
            c.main()
        elif caption == "Add customer":
            c = Core.openController("add")
            c.main()
        elif caption == "Show customers with TreeView":
            c = Core.openController("showTreeView")
            c.main()

    def main(self):
        self.homeView.main()
