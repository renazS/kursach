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
        self.title('C20')
        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()
        self.geometry(f'{self.width}x{self.height}+0+0')
        self.resizable(False, False)
        self.create_widgets_0()
        self.mainloop()


    def create_widgets_0(self):

        # left_frame
        self.left_frame = tk.Frame(self, bg='white', width=self.width // 2, height=self.height)
        self.left_frame.place(x=0, y=0)
        self.left_frame.grid_propagate(0)
        

        # Ввод исходных данных
        self.label_0 = tk.Label(self.left_frame, text='Ввод исходных данных', font='Arial 14', bg='white')
        self.label_0.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky='ew')

        tk.Label(self.left_frame, text='C20', font='Arial 12',bg='white').grid(row=1, column=0, padx=10, pady=10, sticky='ew')
        self.C20_entry = tk.Entry(self.left_frame, font='Arial 12', width=10) # Концентрация насыщенных паров при 20°С
        self.C20_entry.grid(row=1, column=1, padx=10, pady=10, sticky='ew')
        tk.Label(self.left_frame, text='г/м^3', font='Arial 12',bg='white').grid(row=1, column=2, padx=10, pady=10, sticky='ew')

        tk.Label(self.left_frame, text='t_zh_max', font='Arial 12',bg='white').grid(row=2, column=0, padx=10, pady=10, sticky='ew')
        self.t_zh_max_entry = tk.Entry(self.left_frame, font='Arial 12', width=10) # Максимальная температура жидкости
        self.t_zh_max_entry.grid(row=2, column=1, padx=10, pady=10, sticky='ew') 
        tk.Label(self.left_frame, text='°С', font='Arial 12',bg='white').grid(row=2, column=2, padx=10, pady=10, sticky='ew')

        tk.Label(self.left_frame, text='t_zh_min', font='Arial 12',bg='white').grid(row=3, column=0, padx=10, pady=10, sticky='ew')
        self.t_zh_min_entry = tk.Entry(self.left_frame, font='Arial 12', width=10) # Минимальная температура жидкости
        self.t_zh_min_entry.grid(row=3, column=1, padx=10, pady=10, sticky='ew')
        tk.Label(self.left_frame, text='°С', font='Arial 12',bg='white').grid(row=3, column=2, padx=10, pady=10, sticky='ew')

        tk.Label(self.left_frame, text='V_ch_max', font='Arial 12',bg='white').grid(row=4, column=0, padx=10, pady=10, sticky='ew')
        self.V_ch_max_entry = tk.Entry(self.left_frame, font='Arial 12', width=10)
        self.V_ch_max_entry.grid(row=4, column=1, padx=10, pady=10, sticky='ew')
        tk.Label(self.left_frame, text='м^3/с', font='Arial 12', bg="white").grid(row=4, column=2, padx=10, pady=10, sticky='ew')

        tk.Label(self.left_frame, text='B', font='Arial 12',bg='white').grid(row=5, column=0, padx=10, pady=10, sticky='ew')
        self.B_entry = tk.Entry(self.left_frame, font='Arial 12', width=10) # Количество жидкости, закачиваемое в резервуары в течение года, т/год
        self.B_entry.grid(row=5, column=1, padx=10, pady=10, sticky='ew')
        tk.Label(self.left_frame, text='т/год', font='Arial 12',bg='white').grid(row=5, column=2, padx=10, pady=10, sticky='ew')

        tk.Label(self.left_frame, text='ro_zh', font='Arial 12',bg='white').grid(row=6, column=0, padx=10, pady=10, sticky='ew')
        self.ro_zh_entry = tk.Entry(self.left_frame, font='Arial 12', width=10) # Плотность жидкости
        self.ro_zh_entry.grid(row=6, column=1, padx=10, pady=10, sticky='ew')
        tk.Label(self.left_frame, text='т/м^3', font='Arial 12',bg='white').grid(row=6, column=2, padx=10, pady=10, sticky='ew')

        tk.Label(self.left_frame, text='V_p', font='Arial 12',bg='white').grid(row=7, column=0, padx=10, pady=10, sticky='ew')
        self.V_p_entry = tk.Entry(self.left_frame, font='Arial 12', width=10) # Объем резервуара
        self.V_p_entry.grid(row=7, column=1, padx=10, pady=10, sticky='ew')
        tk.Label(self.left_frame, text='м^3', font='Arial 12',bg='white').grid(row=7, column=2, padx=10, pady=10, sticky='ew')

        tk.Label(self.left_frame, text='N_p', font='Arial 12',bg='white').grid(row=8, column=0, padx=10, pady=10, sticky='ew')
        self.N_p_entry = tk.Entry(self.left_frame, font='Arial 12', width=10) # Количество резервуаров
        self.N_p_entry.grid(row=8, column=1, padx=10, pady=10, sticky='ew')
        tk.Label(self.left_frame, text='шт.', font='Arial 12',bg='white').grid(row=8, column=2, padx=10, pady=10, sticky='ew')

        tk.Label(self.left_frame, text='Количество групп', font='Arial 12',bg='white').grid(row=9, column=0, padx=10, pady=10, sticky='ew')
        self.N_gr_entry = tk.Entry(self.left_frame, font='Arial 12', width=10) # Количество групп
        self.N_gr_entry.grid(row=9, column=1, padx=10, pady=10, sticky='ew')
        tk.Label(self.left_frame, text='шт.', font='Arial 12',bg='white').grid(row=9, column=2, padx=10, pady=10, sticky='ew')

        

        tk.Button(self.left_frame, text='Рассчитать', font='Arial 12', command=self.calculate).grid(row=14, column=0, padx=10, pady=10, sticky='ew', columnspan=3)

        tk.Button(self.left_frame, text='Задать значения по умолчанию', font='Arial 12', command=self.autoEnter).grid(row=15, column=0, padx=10, pady=10, sticky='ew', columnspan=3)

        tk.Button(self.left_frame, text='Сохранить результаты расчета', font='Arial 12', command=self.export_result).grid(row=16, column=0, padx=10, pady=10, sticky='ew', columnspan=3)

        tk.Button(self.left_frame, text='Очистить поля', font='Arial 12', command=self.clear_fields).grid(row=17, column=0, padx=10, pady=10, sticky='ew', columnspan=3)

        # right_frame
        self.right_frame = tk.Frame(self, bg='white', width=self.width // 2, height=self.height)
        self.right_frame.place(x=self.width // 2, y=0)

        tk.Label(self.right_frame, text='Результаты расчета', font='Arial 12',bg='white').place(x=self.width//4, y=0, anchor='n')
        self.text_result = tk.Text(self.right_frame, font='Arial 12', width=self.width//2, height=self.height-30)
        self.text_result.place(x=0, y=30)
    
        tk.Label(self.left_frame, text='Тип конструкции', font='Arial 12',bg='white').grid(row=10, column=0, padx=10, pady=10, sticky='ew')
        self.type_construction_cc = ttk.Combobox(self.left_frame,
                                                 values=[
                                                     "Наземный вертикальный",
                                                     "Заглубленный",
                                                     "Наземный горизонтальный"],
                                                 state="readonly")
        self.type_construction_cc.current(0)
        self.type_construction_cc.grid(row=10, column=1, padx=10, pady=10, sticky='ew', columnspan=2)

        tk.Label(self.left_frame, text='Режим эксплуатации', font='Arial 12',bg='white').grid(row=11, column=0, padx=10, pady=10,
                                                                                  sticky='ew')
        self.operation_mode_cc = ttk.Combobox(self.left_frame, values=["мерник", "буферная емкость"]
                                              , state="readonly")
        self.operation_mode_cc.current(0)
        self.operation_mode_cc.bind("<<ComboboxSelected>>", self.set_type_construction)
        self.operation_mode_cc.grid(row=11, column=1, padx=10, pady=10, sticky='ew', columnspan=2)

        tk.Label(self.left_frame, text='ССВ', font='Arial 12', background='white').grid(row=12, column=0, padx=10, pady=10,
                                                                    sticky='ew')
        self.SSV_cc = ttk.Combobox(self.left_frame,
                                   values=["отсутствует", "понтон", "плавающая крыша"]
                                   , state="readonly")
        self.SSV_cc.current(0)
        self.SSV_cc.bind("<<ComboboxSelected>>", self.set_type_construction)

        self.SSV_cc.grid(row=12, column=1, padx=10, pady=10, sticky='ew', columnspan=2)

    def export_result(self):
        try:
            with open("result_C20.txt", "w") as file:
                file.write(f"Результаты расчета:\n")
                file.write(self.text_result.get(1.0, tk.END))
            mb.showinfo("Успех", "Файл успешно сохранен!")
        except:
            mb.showerror("Ошибка", "Не удалось сохранить файл!") 

    def clear_fields(self):
        self.C20_entry.delete(0, tk.END)
        self.t_zh_max_entry.delete(0, tk.END)
        self.t_zh_min_entry.delete(0, tk.END)
        self.V_ch_max_entry.delete(0, tk.END)
        self.B_entry.delete(0, tk.END)
        self.ro_zh_entry.delete(0, tk.END)
        self.V_p_entry.delete(0, tk.END)
        self.N_p_entry.delete(0, tk.END)
        self.N_gr_entry.delete(0, tk.END)
        self.type_construction_cc.current(0)
        self.operation_mode_cc.current(0)
        self.SSV_cc.current(0)

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

    def find_next_column_value(self,df, t_zh):
        columns = df.columns
        columns_search = df.columns[::2]

        col_name_max = next((col for col in columns_search if len(df.loc[df[col] == t_zh])), None)

        if col_name_max:
            row_index_max = df.loc[df[col_name_max] == t_zh].index[0]
            col_index_max = df.columns.get_loc(col_name_max)
            result = df.loc[row_index_max, columns[col_index_max+1]]
        else:
            result = None
        
        return result
    
    def calculate_K_p(self, V_p, SSV, event=None):
        K_table = self.list_of_table[7]
        self.type_construction = self.type_construction_cc.get()

        K_p_max = None
        K_p_sr = None
        self.operation_mode = self.operation_mode_cc.get()
        search_table = None
        if self.operation_mode == "мерник" and SSV != "буферная емкость":
            if SSV == "отсутствует":
                search_table = K_table.iloc[1:7, :]
                search_table = search_table[search_table["Категория 1"] == "Б"]
                search_table = search_table[search_table["Конструкция резервуаров 2"] == self.type_construction]
            elif SSV == "понтон":
                search_table = K_table.iloc[8:10, :]
            elif SSV == "плавающая крыша":
                search_table = K_table.iloc[11:13, :]
            else:
                pass
            K_p_max = search_table[search_table["Крmax или Крср 3"] == "Крmax"]
            K_p_sr = search_table[search_table["Крmax или Крср 3"] == "Крср"]
            

    
            if V_p <= 100:
                K_p_max_value = K_p_max.iloc[:, 3].values[0]
                K_p_sr_value = K_p_sr.iloc[:, 3].values[0]
            elif 200 <= V_p <= 400:
                K_p_max_value = K_p_max.iloc[:, 4].values[0]
                K_p_sr_value = K_p_sr.iloc[:, 4].values[0]
            elif 700 <= V_p <= 1000:
                K_p_max_value = K_p_max.iloc[:, 5].values[0]
                K_p_sr_value = K_p_sr.iloc[:, 5].values[0]
            elif V_p >= 2000:
                K_p_max_value = K_p_max.iloc[:, 6].values[0]
                K_p_sr_value = K_p_sr.iloc[:, 6].values[0]
            else:
                pass
        else:
            K_p_max_value = 0.1
            K_p_sr_value = 0.1

        return float(K_p_max_value), float(K_p_sr_value)



    def calculate(self):
        self.text_result.delete(1.0, tk.END)
        
        # Проверка на пустые поля
        if self.C20_entry.get() == '' or self.t_zh_max_entry.get() == '' or self.t_zh_min_entry.get() == '' or self.V_ch_max_entry.get() == '' or self.B_entry.get() == '' or self.V_p_entry.get() == '' or self.N_p_entry.get() == '' or self.N_gr_entry.get() == '':
            self.text_result.insert(1.0, 'Заполните все поля!')
        
        else:

            # C20
            self.C20 = float(self.C20_entry.get()) # концентрация насыщенных паров нефтепродуктов (кроме бензина) при температуре 20°С


            self.t_zh_max = self.t_zh_max_entry.get() # максимальная температура жидкости в резервуаре
            self.t_zh_min = self.t_zh_min_entry.get() # минимальная температура жидкости в резервуаре
            df = self.list_of_table[6] # таблица для поиска K_t_max и K_t_min
            df = df.loc[18:]
            self.K_t_max = self.find_next_column_value(df, self.t_zh_max) # Опытный коэффициент K_t_max
            self.K_t_min = self.find_next_column_value(df, self.t_zh_min) # Опытный коэффициент K_t_min

            # continue text_result
            self.text_result.insert("end", f'K_t_max:\t{self.K_t_max}\n')
            self.text_result.insert("end", f'K_t_min:\t{self.K_t_min}\n')

            # Тип конструкции
            self.type_construction = self.type_construction_cc.get() # тип конструкции резервуара

            # Режим эксплуатации
            self.operation_mode = self.operation_mode_cc.get() # режим эксплуатации
            
            # ССВ
            self.SSV = self.SSV_cc.get() # ССВ

            # V_p
            self.V_p = int(self.V_p_entry.get()) # объем резервуара


            # B
            self.B = int(self.B_entry.get()) # количество жидкости, закачиваемое в резервуары в течение года, т/год

            # ro_zh
            self.ro_zh = float(self.ro_zh_entry.get()) # плотность жидкости, т/м3

            # N_p
            self.N_p = int(self.N_p_entry.get()) # количество резервуаров

            # V_ch_max
            self.V_ch_max = float(self.V_ch_max_entry.get())  # максимальный объем жидкости, закачиваемый в резервуары

    
            # K_p_sr, K_p_max
            self.K_p_max, self.K_p_sr = self.calculate_K_p(self.V_p, self.SSV)


            self.text_result.insert("end", f'K_p_sr:\t{self.K_p_sr}\n')
            self.text_result.insert("end", f'K_p_max:\t{self.K_p_max}\n')



        
            self.n = round(self.B/(self.ro_zh*self.V_p*self.N_p))
            self.text_result.insert("end", f'n:\t{self.n}\n')

            k_ob_values = {100: 1.35, 80: 1.5, 60: 1.75, 40: 2, 30: 2.25, 20: 2.5}
            nearest_n = min(k_ob_values.keys(), key=lambda x: abs(x - self.n))
            self.K_ob = k_ob_values[nearest_n]
            self.text_result.insert("end", f'K_ob:\t{self.K_ob}\n')


            self.K_p_max = float(self.K_p_max) # Опытный коэффициент
            self.K_t_max = float(self.K_t_max) # Опытный коэффициент
            self.K_p_sr = float(self.K_p_sr) # Опытный коэффициент
            self.K_t_min = float(self.K_t_min) # Опытный коэффициент

            self.M = np.round(self.C20*self.K_t_max*self.K_p_sr*self.V_ch_max/3600,4)
            self.text_result.insert("end", f'M:\t{self.M} г/с\n')

            # G = (C*(K_t_max+K_t_min)*K_p_sr*K_ob*B)/(B*10^6*ro_zh)
            self.G = np.round((self.C20*(self.K_t_max+self.K_t_min)*self.K_p_sr*self.K_ob*self.B)/(2*10**6*self.ro_zh),4)
            self.text_result.insert("end", f'G:\t{self.G} т/год\n')





    def autoEnter(self):
        # Задать значения по умолчанию

        self.C20_entry.delete(0, tk.END)
        self.C20_entry.insert(0, 11.2)

        self.t_zh_max_entry.delete(0, tk.END)
        self.t_zh_max_entry.insert(0, 55)

        self.t_zh_min_entry.delete(0, tk.END)
        self.t_zh_min_entry.insert(0, 25)

        self.V_ch_max_entry.delete(0, tk.END)
        self.V_ch_max_entry.insert(0, 70)

        self.B_entry.delete(0, tk.END)
        self.B_entry.insert(0, 500000)

        self.ro_zh_entry.delete(0, tk.END)
        self.ro_zh_entry.insert(0, 0.85)

        self.V_p_entry.delete(0, tk.END)
        self.V_p_entry.insert(0, 3000)

        self.N_p_entry.delete(0, tk.END)
        self.N_p_entry.insert(0, 4)

        self.N_gr_entry.delete(0, tk.END)
        self.N_gr_entry.insert(0, 22)

        self.type_construction_cc.current(0)
        self.operation_mode_cc.current(0)
        self.SSV_cc.current(0)


def run_app(parent):
    app = App(parent)
    app.create_widgets_0()

