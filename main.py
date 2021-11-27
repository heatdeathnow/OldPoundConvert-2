import interfaces
import tkinter as tk
from tkinter import ttk
current_frame = ttk.Frame()


def clutch(to_delete, to_create, root):
    to_delete.destroy()

    global current_frame
    current_frame = to_create(root)
    current_frame.grid(column=0, row=0)


class MainFrame(ttk.Frame):

    def __init__(self, container):
        super().__init__(container)

        self.cointocoin_button = ttk.Button(self, text='Simplify coinage.',
                                            command=lambda: clutch(self, interfaces.SimplifyCoin, container))
        self.cointocoin_button.grid(column=0, row=0, padx=5, pady=5)


        self.valuetovalue_button = ttk.Button(self, text='Simplify values',
                                              command=lambda: clutch(self, interfaces.SimplifyValue, container))
        self.valuetovalue_button.grid(column=1, row=0, padx=5, pady=5)


        self.cointovalue_button = ttk.Button(self, text='Convert coinage to value',
                                             command=lambda: clutch(self, interfaces.ConvertCoinsToValue, container))
        self.cointovalue_button.grid(column=0, row=1, padx=5, pady=5)


        self.valuetocoin_button = ttk.Button(self, text='Convert values to coinage',
                                             command=lambda: clutch(self, interfaces.ConvertValueToCoin, container))
        self.valuetocoin_button.grid(column=1, row=1, padx=5, pady=5)


class App(tk.Tk):

    def __init__(self):
        super().__init__()

        self.rowconfigure(0, weight=6)
        self.rowconfigure(1, weight=0)
        self.resizable(False, False)
        self.title("Old Currency Converter - 2")
        self.iconbitmap("icon.ico")


        main_frame = MainFrame(self)
        main_frame.grid(column=0, row=0)

        back_button = ttk.Button(self, text='go back',
                                 command=lambda: clutch(current_frame, MainFrame, self))
        back_button.grid(column=0, row=1, padx=5, pady=5)


app = App()
app.mainloop()
