import tkinter as tk
from tkinter import ttk

from views.View import View


class AddView(tk.Tk, View):
    '''View responsible for adding new customers'''
    PAD = 10
    FIELDS = [
        "First name", "Last name", "Zipcode", "Price paid"
    ]

    def __init__(self, controller):
        '''Controller of this view'''
        super().__init__()
        self.addController = controller

    def _make_mainFrame(self):
        '''Creates view's frame'''
        self.frame_main = tk.Frame(self)
        self.frame_main.pack()

    def _make_title(self):
        '''Creates view's title'''
        title = ttk.Label(self.frame_main, text="Customers Manager", font=("Helvetica", 20))
        title.pack(padx=self.PAD, pady=self.PAD)

    def _make_fields(self):
        '''Creates view's fields'''
        frame_fields = tk.Frame(self.frame_main)
        frame_fields.pack()
        fields = []
        
        i = 0
        for field in self.FIELDS:
            # Show headers
            f = ttk.Label(frame_fields, text=field)
            f.grid(row=i, column=0)
            
            # Show fields
            e = ttk.Entry(frame_fields, width=30)
            e.grid(row=i, column=1)
            fields.append(e)
            
            i += 1
            
        # Make buttons
        frame_buttons = tk.Frame(self.frame_main)
        frame_buttons.pack()
        
        btn_submit = ttk.Button(frame_buttons, text="Create", command=lambda:self.addController.btn_add(fields))
        btn_submit.pack(side="left")
        
        btn_clear = ttk.Button(frame_buttons, text="Clear", command=lambda:self.addController.btn_clear(fields))
        btn_clear.pack(side="left")

    def main(self):
        self._make_mainFrame()
        self._make_title()
        self._make_fields()
        
        self.mainloop()

    def close(self):
        self.destroy()
