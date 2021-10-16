import tkinter as tk
from tkinter import ttk

from views.View import View


class HomeView(tk.Tk, View):
    '''View associated with HomeController. It will be responsible for
    program's main screen view'''
    PAD = 10
    BTN_CAPTION = [
        "Open Customers DB",
        "Show customers with TreeView",
        "Add customer",
        "Exit"
    ]

    def __init__(self, controller):
        '''Controller of this view'''
        super().__init__()
        self.title("Customers Manager")
        self.homeController = controller
        
        self._make_mainFrame()
        self._make_title()
        self._make_options()

    def _make_mainFrame(self):
        '''Creates view's frame'''
        self.mainFrame = ttk.Frame(self)
        self.mainFrame.pack(padx=self.PAD, pady=self.PAD)

    def _make_title(self):
        '''Sets view's title'''
        title = ttk.Label(self.mainFrame, text="Customers Manager", font=("Helvetica", 20))
        title.pack(padx=self.PAD, pady=self.PAD)

    def _make_options(self):
        '''Creates view's options'''
        frame_btn = ttk.Frame(self.mainFrame)
        frame_btn.pack(fill="x")
        
        for caption in self.BTN_CAPTION:
            if caption == "Exit":
                btn = ttk.Button(frame_btn, text=caption, command=self.destroy)
            else:
                btn = ttk.Button(frame_btn, text=caption, command=lambda txt=caption: self.homeController.btnClicked(txt))
            
            btn.pack(fill="x")
  
    def main(self):
        self.mainloop()

    def close(self):
        return
