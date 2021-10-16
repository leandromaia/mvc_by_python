import os
import importlib

from config import APP_PATH


'''Class responsible for opening controllers'''
class Core:   

    @staticmethod
    def openController(controller):
        '''Given a controller name, return an instance of it'''
        response = None

        # Set controller name
        controller = controller[0].upper()+controller[1:]
        controllerName = controller+"Controller"

        # Check if file exists
        if os.path.exists(APP_PATH+"/controllers/"+controllerName+".py"):
            module = importlib.import_module("controllers."+controllerName)
            class_ = getattr(module, controllerName)
            response = class_()
 
        return response
