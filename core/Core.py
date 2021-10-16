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
        controller = controller[0].upper() + controller[1:]
        controller_name = controller + "Controller"

        # Check if file exists
        if os.path.exists(APP_PATH + "/controllers/" + controller_name + ".py"):
            module = importlib.import_module("controllers." + controller_name)
            import pdb; pdb.set_trace()
            class_ = getattr(module, controller_name)
            response = class_()
 
        return response
