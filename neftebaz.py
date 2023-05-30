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
            self.list_of_table.append(pd.read_excel("Книга1.xlsx", sheet_name=f"{i}"))
        self.title('Расчет выбросов на нефтебазах')
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

        self.left_frame = tk.Frame(self, bg='white', width=self.width // 2, height=self.height)
        self.left_frame.place(x=0, y=0)
        self.left_frame.grid_propagate(0)
        

        # Ввод исходных данных
        self.label_0 = tk.Label(self.left_frame, text='Ввод исходных данных', font='Arial 14', bg='white')
        self.label_0.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky='ew')

        tk.Label(self.left_frame, text='Q_ч', font='Arial 12',bg='white').grid(row=1, column=0, padx=10, pady=10, sticky='ew')
        self.Q_ch_entry = tk.Entry(self.left_frame, font='Arial 12', width=10) 
        self.Q_ch_entry.grid(row=1, column=1, padx=10, pady=10, sticky='ew')
        tk.Label(self.left_frame, text='м^3/ч', font='Arial 12',bg='white').grid(row=1, column=2, padx=10, pady=10, sticky='ew')

        tk.Label(self.left_frame, text='t_B_оз', font='Arial 12',bg='white').grid(row=2, column=0, padx=10, pady=10, sticky='ew')
        self.B_oz_entry = tk.Entry(self.left_frame, font='Arial 12', width=10) # Количество жидкости заливаемое в резервуар в осенне-зимний период
        self.B_oz_entry.grid(row=2, column=1, padx=10, pady=10, sticky='ew')
        tk.Label(self.left_frame, text='m', font='Arial 12',bg='white').grid(row=2, column=2, padx=10, pady=10, sticky='ew')

        tk.Label(self.left_frame, text='B_вл', font='Arial 12',bg='white').grid(row=3, column=0, padx=10, pady=10, sticky='ew')
        self.B_vl_entry = tk.Entry(self.left_frame, font='Arial 12', width=10) # Количество жидкости заливаемое в резервуар в весенне-летний период
        self.B_vl_entry.grid(row=3, column=1, padx=10, pady=10, sticky='ew')
        tk.Label(self.left_frame, text='m', font='Arial 12',bg='white').grid(row=3, column=2, padx=10, pady=10, sticky='ew')



        tk.Label(self.left_frame, text='Тип конструкции', font='Arial 12',bg='white').grid(row=4, column=0, padx=10, pady=10, sticky='ew')
        self.type_construction_cc = ttk.Combobox(self.left_frame,
                                                 values=[
                                                     "Наземный вертикальный",
                                                     "Заглубленный",
                                                     "Наземный горизонтальный"],
                                                 state="readonly") # Тип конструкции резервуара
        self.type_construction_cc.current(0)
        self.type_construction_cc.grid(row=4, column=1, padx=10, pady=10, sticky='ew', columnspan=2)

        tk.Label(self.left_frame, text='Режим эксплуатации', font='Arial 12',bg='white').grid(row=11, column=0, padx=10, pady=10,
                                                                                  sticky='ew')
        self.operation_mode_cc = ttk.Combobox(self.left_frame, values=["мерник", "буферная емкость"]
                                              , state="readonly") # Режим эксплуатации резервуара
        self.operation_mode_cc.current(0)
        self.operation_mode_cc.bind("<<ComboboxSelected>>", self.set_type_construction)
        self.operation_mode_cc.grid(row=11, column=1, padx=10, pady=10, sticky='ew', columnspan=2)

        tk.Label(self.left_frame, text='ССВ', font='Arial 12', background='white').grid(row=12, column=0, padx=10, pady=10,
                                                                    sticky='ew')
        self.SSV_cc = ttk.Combobox(self.left_frame,
                                   values=["отсутствует", "понтон", "плавающая крыша"]
                                   , state="readonly") # Средства сокращения выбросов
        self.SSV_cc.current(0)
        self.SSV_cc.bind("<<ComboboxSelected>>", self.set_type_construction)

        self.SSV_cc.grid(row=12, column=1, padx=10, pady=10, sticky='ew', columnspan=2)

        tk.Label(self.left_frame, text='V_p', font='Arial 12', background='white').grid(row=13, column=0, padx=10, pady=10,
                                                                    sticky='ew')
        self.V_p_entry = tk.Entry(self.left_frame, font='Arial 12', width=10) # Объем резервуара
        self.V_p_entry.grid(row=13, column=1, padx=10, pady=10, sticky='ew')
        tk.Label(self.left_frame, text='м^3', font='Arial 12', background='white').grid(row=13, column=2, padx=10, pady=10,
                                                                    sticky='ew')
        
    
        tk.Label(self.left_frame, text='N_p', font='Arial 12', background='white').grid(row=14, column=0, padx=10, pady=10, sticky='ew')
        self.N_p_entry = tk.Entry(self.left_frame, font='Arial 12', width=10) # Количество резервуаров
        self.N_p_entry.grid(row=14, column=1, padx=10, pady=10, sticky='ew')
        tk.Label(self.left_frame, text='шт', font='Arial 12', background='white').grid(row=14, column=2, padx=10, pady=10, sticky='ew')

        tk.Label(self.left_frame, text='K_p_max', font='Arial 12', background='white').grid(row=15, column=0, padx=10, pady=10, sticky='ew')
        self.K_p_max_entry = tk.Entry(self.left_frame, font='Arial 12', width=10) # Коэффициент 
        self.K_p_max_entry.grid(row=15, column=1, padx=10, pady=10, sticky='ew')
        tk.Label(self.left_frame, text='шт', font='Arial 12', background='white').grid(row=15, column=2, padx=10, pady=10, sticky='ew')



        tk.Label(self.left_frame, text='Вещество', font='Arial 12', background='white').grid(row=16, column=0, padx=10, pady=10, sticky='ew')
        self.substance_cc = ttk.Combobox(self.left_frame, values=self.list_of_table[17].iloc[:, 0].values.tolist(), state="readonly") # Вещество
        self.substance_cc.grid(row=16, column=1, padx=10, pady=10, sticky='ew', columnspan=2)


       

        tk.Button(self.left_frame, text='Рассчитать', font='Arial 12', command=self.calculate).grid(row=17, column=0, padx=10, pady=10, sticky='ew', columnspan=3)

        tk.Button(self.left_frame, text='Задать значения по умолчанию', font='Arial 12', command=self.autoEnter).grid(row=18, column=0, padx=10, pady=10, sticky='ew', columnspan=3)

        tk.Button(self.left_frame, text='Сохранить результаты расчета', font='Arial 12', command=self.export_result).grid(row=19, column=0, padx=10, pady=10, sticky='ew', columnspan=3)

        tk.Button(self.left_frame, text='Очистить поля', font='Arial 12', command=self.clear_fields).grid(row=20, column=0, padx=10, pady=10, sticky='ew', columnspan=3)




        # right_frame
        self.right_frame = tk.Frame(self, bg='white', width=self.width // 2, height=self.height)
        self.right_frame.place(x=self.width // 2, y=0)

        tk.Label(self.right_frame, text='Результаты расчета', font='Arial 12',bg='white').place(x=self.width//4, y=0, anchor='n')
        self.text_result = tk.Text(self.right_frame, font='Arial 12', width=self.width//2, height=self.height-30)
        self.text_result.place(x=0, y=30)



    def export_result(self):
        try:
            with open("result_neftebaz.txt", "w") as file:
                file.write(f"Результаты расчета:\n")
                file.write(self.text_result.get(1.0, tk.END))
            mb.showinfo("Успех", "Файл успешно сохранен!")
        except:
            mb.showerror("Ошибка", "Не удалось сохранить файл!")


    def clear_fields(self):
        self.K_p_max_entry.delete(0, tk.END)
        self.Q_ch_entry.delete(0, tk.END)
        self.B_oz_entry.delete(0, tk.END)
        self.B_vl_entry.delete(0, tk.END)
        self.N_p_entry.delete(0, tk.END)
        self.V_p_entry.delete(0, tk.END)
        self.text_result.delete(1.0, tk.END)

        #clear cc
        self.substance_cc.current(0)
        self.type_construction_cc.current(0)
        self.SSV_cc.current(0)
        self.operation_mode_cc.current(0)

    def calculate(self):
        # Проверка на заполнение всех полей
        if self.K_p_max_entry.get() == '' or self.Q_ch_entry.get() == '' or self.B_oz_entry.get() == '' or self.B_vl_entry.get() == '' or self.N_p_entry.get() == '' or self.V_p_entry.get() == '':
            self.text_result.delete(1.0, tk.END)
            self.text_result.insert(tk.END, 'Не все поля заполнены')
        else:

            self.text_result.delete(1.0, tk.END)
            self.substance = self.substance_cc.get() # Тип топлива
            self.K_p_max = float(self.K_p_max_entry.get()) # Коэффициент
            self.Q_ch = float(self.Q_ch_entry.get()) # Количество нефтепродуктов, закачиваемое в резервуар
            self.B_oz = float(self.B_oz_entry.get()) # Количество жидкости, закачиваемое в резервуары в течение осенне-зимнего периода
            self.B_vl = float(self.B_vl_entry.get()) # Количество жидкости, закачиваемое в резервуары в течение весенне-летнего периода
            self.N_p = float(self.N_p_entry.get()) # Количество резервуаров
            self.type_construction = self.type_construction_cc.get() # Тип конструкции резервуара
            self.SSV = self.SSV_cc.get() # ССВ
            self.V_p = self.V_p_entry.get() # Объем резервуара

            C1_table = self.list_of_table[17] # Таблица с коэффициентами C1, У2, У3
            substance_row = C1_table.loc[C1_table.iloc[:, 0] == self.substance]
            substance_row = substance_row.iloc[:, 4:7]
            self.C1, self.U2, self.U3 = substance_row.iloc[0, :].values
            self.text_result.insert(tk.END, f'C1:\t{self.C1} г/м^3\n')
            self.text_result.insert(tk.END, f'U2:\t{self.U2} г/т\n')
            self.text_result.insert(tk.END, f'U3:\t{self.U3} г/т\n')
            
            G_table = self.list_of_table[18] # Таблица с коэффициентами Gхр
            G_table = G_table.loc[13:23]
            first_column = G_table.iloc[:, 0]
            self.text_result.insert(tk.END, f'K_p_max:\t{self.K_p_max}\n')
            self.M = self.C1*self.K_p_max*self.Q_ch/3600
            self.text_result.insert(tk.END, f'M:\t{self.M} г/с\n')
            column_name = G_table.columns[G_table.columns.str.contains(self.type_construction)]
            if  self.type_construction == "Наземный":
                column_name = column_name[column_name.str.contains(self.SSV)]
            G_values = G_table[column_name]
            G_values = pd.concat([first_column, G_values], axis=1)
            G_values = G_values.loc[G_values.iloc[:, 0] == self.V_p]
            self.Ghr = G_values.iloc[0, 1] # выбросы паров нефтепродуктов при хранении бензина в одном резервуаре в год
            self.text_result.insert(tk.END, f'Ghr:\t{self.Ghr} т/г\n')
            self.Ghr = float(self.Ghr)
            self.N_p = float(self.N_p)
            self.G = round((self.U2*self.B_oz+self.U3*self.B_vl)*self.K_p_max*10**(-6)+self.Ghr*self.N_p,4)
            self.text_result.insert(tk.END, f'G:\t{self.G} м^3/ч\n')

    def autoEnter(self):
        # Задать значения по умолчанию
        self.Q_ch_entry.delete(0, tk.END)
        self.Q_ch_entry.insert(0, 400)

        self.B_oz_entry.delete(0, tk.END)
        self.B_oz_entry.insert(0, 16000)

        self.type_construction_cc.current(0)
        self.operation_mode_cc.current(0)
        self.SSV_cc.current(0)

        self.V_p_entry.delete(0, tk.END)
        self.V_p_entry.insert(0, 5000)

        self.N_p_entry.delete(0, tk.END)
        self.N_p_entry.insert(0, 8)

        self.K_p_max_entry.delete(0, tk.END)
        self.K_p_max_entry.insert(0, 0.8)

        self.B_vl_entry.delete(0, tk.END)
        self.B_vl_entry.insert(0, 24000)

        self.substance_cc.current(0)


def run_app(parent):
    app = App(parent)
    app.create_widgets_0()
