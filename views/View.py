import abc


class View(metaclass=abc.ABCMeta):
    '''Responsible for the program interface'''

    @abc.abstractmethod
    def main(self):
        '''Displays view on screen'''
        return

    @abc.abstractmethod
    def close(self):
        '''Closes the interface. It is called when the window is closed'''
        return
