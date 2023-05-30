import tkinter as tk
from tkinter import ttk
import pandas as pd
import numpy as np
from tkinter import messagebox as mb


class App(tk.Tk):
    def __init__(self, *parent):
        super().__init__()
        self.list_of_table = []
        for i in range(0,22):
            self.list_of_table.append(pd.read_excel("C:\\Users\\renaz\\Documents\\machine_learning\\bit\\Книга1.xlsx", sheet_name=f"{i}"))
        self.title('Расчет выбросов автозаправочных станций')
        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()
        self.geometry(f'{self.width}x{self.height}+0+0')
        self.resizable(False, False)
        self.create_widgets_0()
        self.mainloop()

    def set_type_construction(self, event=None):
        operation_mode = self.operation_mode_cc.get()
        SSV = self.SSV_cc.get()
        if operation_mode == "мерник":
            self.SSV_cc.configure(state="readonly")
            if SSV == "понтон" or SSV == "плавающая крыша":
                self.type_construction_cc.configure(state="readonly")
                self.type_construction_cc.set("Наземный вертикальный")
            else:
                self.type_construction_cc.configure(state="readonly")
        elif operation_mode == "буферная емкость":
            self.SSV_cc.set("")
            self.SSV_cc.configure(state="disabled")
            self.type_construction_cc.set("")
            self.type_construction_cc.configure(state="disabled")


        

    def create_widgets_0(self):

        # left_frame
        self.left_frame = tk.Frame(self, bg='white', width=self.width // 2, height=self.height)
        self.left_frame.place(x=0, y=0)
        self.left_frame.grid_propagate(0)
        

        # Ввод исходных данных
        self.label_0 = tk.Label(self.left_frame, text='Ввод исходных данных', font='Arial 14', bg='white')
        self.label_0.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky='ew')


        tk.Label(self.left_frame, text='Продукт', font='Arial 12',bg='white').grid(row=1, column=0, padx=10, pady=10, sticky='ew')
        self.substance_cc = ttk.Combobox(self.left_frame, width=10, values=list(dict.fromkeys(self.list_of_table[20].iloc[11:20, 0].values.tolist()))) # Название продукта
        self.substance_cc.grid(row=1, column=1, padx=10, pady=10, sticky='ew', columnspan=2)
        self.substance_cc.current(0)

        tk.Label(self.left_frame, text='V сл', font='Arial 12',bg='white').grid(row=2, column=0, padx=10, pady=10, sticky='ew')
        self.V_sl_entry = tk.Entry(self.left_frame, font='Arial 12', width=10) # Объем слитого нефтепродукта в резервуар
        self.V_sl_entry.grid(row=2, column=1, padx=10, pady=10, sticky='ew')
        tk.Label(self.left_frame, text='м^3', font='Arial 12',bg='white').grid(row=2, column=2, padx=10, pady=10, sticky='ew')

        tk.Label(self.left_frame, text='Q оз', font='Arial 12',bg='white').grid(row=3, column=0, padx=10, pady=10, sticky='ew')
        self.Q_oz_entry = tk.Entry(self.left_frame, font='Arial 12', width=10) # Количество нефтепродуктов, закачиваемое в резервуары АЗС в течение осенне-зимнего периода
        self.Q_oz_entry.grid(row=3, column=1, padx=10, pady=10, sticky='ew')
        tk.Label(self.left_frame, text='м^3', font='Arial 12',bg='white').grid(row=3, column=2, padx=10, pady=10, sticky='ew')

        tk.Label(self.left_frame, text='Q вл', font='Arial 12',bg='white').grid(row=4, column=0, padx=10, pady=10, sticky='ew')
        self.Q_vl_entry = tk.Entry(self.left_frame, font='Arial 12', width=10) # Количество нефтепродуктов, закачиваемое из резервуаров АЗС в течение весенне-летнего периода
        self.Q_vl_entry.grid(row=4, column=1, padx=10, pady=10, sticky='ew')
        tk.Label(self.left_frame, text='м^3', font='Arial 12',bg='white').grid(row=4, column=2, padx=10, pady=10, sticky='ew')

        tk.Label(self.left_frame, text='Тип конструкции', font='Arial 12',bg='white').grid(row=5, column=0, padx=10, pady=10, sticky='ew')
        self.type_construction_cc = ttk.Combobox(self.left_frame,
                                                 values=[
                                                     "наземный",
                                                     "заглубленный"],
                                                 state="readonly")
        self.type_construction_cc.current(0)
        self.type_construction_cc.grid(row=5, column=1, padx=10, pady=10, sticky='ew', columnspan=2)
        



        tk.Button(self.left_frame, text='Рассчитать', font='Arial 12', command=self.calculate).grid(row=6, column=0, padx=10, pady=10, sticky='ew', columnspan=3)

        tk.Button(self.left_frame, text='Задать значения по умолчанию', font='Arial 12', command=self.autoEnter).grid(row=7, column=0, padx=10, pady=10, sticky='ew', columnspan=3)
        tk.Button(self.left_frame, text='Сохранить результат', font='Arial 12', command=self.export_result).grid(row=8, column=0, padx=10, pady=10, sticky='ew', columnspan=3)

        tk.Button(self.left_frame, text="Очистить поля", font='Arial 12', command=self.clear_fields).grid(row=9, column=0, padx=10, pady=10, sticky='ew', columnspan=3)

        # right_frame
        self.right_frame = tk.Frame(self, bg='white', width=self.width // 2, height=self.height)
        self.right_frame.place(x=self.width // 2, y=0)

        tk.Label(self.right_frame, text='Результаты расчета', font='Arial 12',bg='white').place(x=self.width//4, y=0, anchor='n')
        self.text_result = tk.Text(self.right_frame, font='Arial 12', width=self.width//2, height=self.height-30)
        self.text_result.place(x=0, y=30) 


    def calculate(self):

        # Проверка на пустые поля
        if self.substance_cc.get() == "" or self.V_sl_entry.get() == "" or self.Q_oz_entry.get() == "" or self.Q_vl_entry.get() == "" or self.type_construction_cc.get() == "":
            self.text_result.delete(1.0, tk.END)
            self.text_result.insert(tk.END, "Не все поля заполнены")
        else:
            self.text_result.delete(1.0, tk.END)

            # Получить значения из полей ввода
            self.substance = self.substance_cc.get()
            self.V_sl = float(self.V_sl_entry.get())
            self.Q_oz = float(self.Q_oz_entry.get())
            self.Q_vl = float(self.Q_vl_entry.get())
            self.type_construction = self.type_construction_cc.get()

            # Расчет
            fuels_table = self.list_of_table[20].iloc[11:20, 0:5]
            fuels_table = fuels_table.loc[fuels_table.iloc[:, 0] == self.substance]
            if self.type_construction=="наземный":
                column_C_p_index = 2
            elif self.type_construction=="заглубленный":
                column_C_p_index = 3

            C_p_column = fuels_table.iloc[:, column_C_p_index]
            self.C_max, self.C_oz_p, self.C_vl_p = map(float, C_p_column.values)
            self.C_oz_b, self.C_vl_b = map(float,fuels_table.iloc[1:, 4].values)
            self.text_result.insert(tk.END, f'C_max:\t{self.C_max} г/м^3\n')
            self.text_result.insert(tk.END, f'C_oz_p:\t{self.C_oz_p} г/м^3\n')
            self.text_result.insert(tk.END, f'C_vl_p:\t{self.C_vl_p} г/м^3\n')
            self.text_result.insert(tk.END, f'C_oz_b:\t{self.C_oz_b} г/м^3\n')
            self.text_result.insert(tk.END, f'C_vl_b:\t{self.C_vl_b} г/м^3\n')

            self.M = np.round((self.C_max*self.V_sl)/1200, 4)
            self.text_result.insert(tk.END, f'M:\t{self.M} г/с\n')
            self.G = np.round(((self.C_oz_p+self.C_oz_b)*self.Q_oz+(self.C_vl_p+self.C_vl_b)*self.Q_vl+125*(self.Q_oz+self.Q_vl))*10**(-6), 4)
            self.text_result.insert(tk.END, f'G:\t{self.G} т/год\n')


    def export_result(self):
        try:
            with open("result_autozap.txt", "w") as file:
                file.write(f"Результаты расчета:\n")
                file.write(self.text_result.get(1.0, tk.END))
            mb.showinfo("Успех", "Файл успешно сохранен!")
        except:
            mb.showerror("Ошибка", "Не удалось сохранить файл!")

    def clear_fields(self):
        self.substance_cc.current(0)
        self.V_sl_entry.delete(0, tk.END)
        self.Q_oz_entry.delete(0, tk.END)
        self.Q_vl_entry.delete(0, tk.END)
        self.type_construction_cc.current(0)
        self.text_result.delete(1.0, tk.END)

    def autoEnter(self):
        # Задать значения по умолчанию
        self.substance_cc.current(0)

        self.V_sl_entry.delete(0, tk.END)
        self.V_sl_entry.insert(0, 4.0)

        self.Q_oz_entry.delete(0, tk.END)
        self.Q_oz_entry.insert(0, 3150)

        self.Q_vl_entry.delete(0, tk.END)
        self.Q_vl_entry.insert(0, 3150)

        self.type_construction_cc.current(1)



def run_app(parent):
    app = App(parent)
    app.create_widgets_0()

app = App()
app.create_widgets_0()