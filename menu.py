import tkinter as tk
from tkinter import ttk

import benzin
import benzin_sum_win
import C20
import neftebaz
import avtozap

class Menu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Выбор типа расчета выбросов')
        self.resizable(False, False)
        self.create_widgets()
        self.mainloop()

    def open_benzin(self):
        top = tk.Toplevel()
        top.withdraw()
        benzin.run_app(top)

    def open_benzin_sum(self):
        top = tk.Toplevel()
        top.withdraw()
        benzin_sum_win.run_app(top)

    def open_С20(self):
        top = tk.Toplevel()
        top.withdraw()
        C20.run_app(top)

    def open_neftebaz(self):
        top = tk.Toplevel()
        top.withdraw()
        neftebaz.run_app(top)

    def open_avtozap(self):
        top = tk.Toplevel()
        top.withdraw()
        avtozap.run_app(top)

    def create_widgets(self):
        tk.Button(self, text='Расчет выбросов нефтепродуктов и бензинов ', font='Arial 12', command=self.open_benzin).pack(padx=10, pady=10, anchor='w', fill='x')
        tk.Button(self, text='Расчет выбросов нефтепродуктов и бензинов с разделением на летний и зимний период', font='Arial 12', command=self.open_benzin_sum).pack(padx=10, pady=10, anchor='w', fill='x')
        tk.Button(self, text='Расчет расчет выбросов с данной концентрацией насыщенных паров при 20°С', font='Arial 12', command=self.open_С20).pack(padx=10, pady=10, anchor='w', fill='x')
        tk.Button(self, text='Расчет выбросов для нефтебаз', font='Arial 12', command=self.open_neftebaz).pack(padx=10, pady=10, anchor='w', fill='x')
        tk.Button(self, text='Расчет выбросов автозаправочных станций', font='Arial 12', command=self.open_avtozap).pack(padx=10, pady=10, anchor='w', fill='x')
        

App = Menu()