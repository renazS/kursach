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
        self.title('Расчета выброса бензина, нефтей и других нефтепродуктов')
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

        tk.Label(self.left_frame, text='P38', font='Arial 12', bg='white').grid(row=1, column=0, padx=10, pady=10, sticky='ew')
        self.P38_entry = tk.Entry(self.left_frame, font='Arial 12', width=10) # Давление насыщенных паров при 38°С
        self.P38_entry.grid(row=1, column=1, padx=10, pady=10, sticky='ew')
        tk.Label(self.left_frame, text='мм.рт.ст.', font='Arial 12',bg='white').grid(row=1, column=2, padx=10, pady=10, sticky='ew')

        tk.Label(self.left_frame, text='t_nk', font='Arial 12',bg='white').grid(row=2, column=0, padx=10, pady=10, sticky='ew')
        self.t_nk_entry = tk.Entry(self.left_frame, font='Arial 12', width=10) # Температура начала кипения жидкости
        self.t_nk_entry.grid(row=2, column=1, padx=10, pady=10, sticky='ew')
        tk.Label(self.left_frame, text='°С', font='Arial 12',bg='white').grid(row=2, column=2, padx=10, pady=10, sticky='ew')

        tk.Label(self.left_frame, text='t_zh_max', font='Arial 12',bg='white').grid(row=3, column=0, padx=10, pady=10, sticky='ew')
        self.t_zh_max_entry = tk.Entry(self.left_frame, font='Arial 12', width=10) # Максимальная температура жидкости в резервуаре
        self.t_zh_max_entry.grid(row=3, column=1, padx=10, pady=10, sticky='ew')
        tk.Label(self.left_frame, text='°С', font='Arial 12',bg='white').grid(row=3, column=2, padx=10, pady=10, sticky='ew')

        tk.Label(self.left_frame, text='t_zh_min', font='Arial 12',bg='white').grid(row=4, column=0, padx=10, pady=10, sticky='ew')
        self.t_zh_min_entry = tk.Entry(self.left_frame, font='Arial 12', width=10) # Минимальная температура жидкости в резервуаре
        self.t_zh_min_entry.grid(row=4, column=1, padx=10, pady=10, sticky='ew')
        tk.Label(self.left_frame, text='°С', font='Arial 12',bg='white').grid(row=4, column=2, padx=10, pady=10, sticky='ew')

        tk.Label(self.left_frame, text='V_ch_max', font='Arial 12',bg='white').grid(row=5, column=0, padx=10, pady=10, sticky='ew')
        self.V_ch_max_entry = tk.Entry(self.left_frame, font='Arial 12', width=10) # Максимальный объем паровоздушной смеси, вытесняемой из резервуара
        self.V_ch_max_entry.grid(row=5, column=1, padx=10, pady=10, sticky='ew')
        tk.Label(self.left_frame, text='м^3/с', font='Arial 12', bg='white').grid(row=5, column=2, padx=10, pady=10, sticky='ew')

        tk.Label(self.left_frame, text='B', font='Arial 12',bg='white').grid(row=6, column=0, padx=10, pady=10, sticky='ew')
        self.B_entry = tk.Entry(self.left_frame, font='Arial 12', width=10) # Количество жидкости закачиваемой в резервуар
        self.B_entry.grid(row=6, column=1, padx=10, pady=10, sticky='ew')
        tk.Label(self.left_frame, text='т/год', font='Arial 12',bg='white').grid(row=6, column=2, padx=10, pady=10, sticky='ew')

        tk.Label(self.left_frame, text='ro_zh', font='Arial 12',bg='white').grid(row=7, column=0, padx=10, pady=10, sticky='ew') # Плотность жидкости
        self.ro_zh_entry = tk.Entry(self.left_frame, font='Arial 12', width=10) # Плотность жидкости
        self.ro_zh_entry.grid(row=7, column=1, padx=10, pady=10, sticky='ew')
        tk.Label(self.left_frame, text='т/м^3', font='Arial 12',bg='white').grid(row=7, column=2, padx=10, pady=10, sticky='ew')

        tk.Label(self.left_frame, text='V_p', font='Arial 12',bg='white').grid(row=8, column=0, padx=10, pady=10, sticky='ew') # Объем резервуара
        self.V_p_entry = tk.Entry(self.left_frame, font='Arial 12', width=10) # Объем резервуара
        self.V_p_entry.grid(row=8, column=1, padx=10, pady=10, sticky='ew')
        tk.Label(self.left_frame, text='м^3', font='Arial 12',bg='white').grid(row=8, column=2, padx=10, pady=10, sticky='ew')

        tk.Label(self.left_frame, text='N_p', font='Arial 12',bg='white').grid(row=9, column=0, padx=10, pady=10, sticky='ew')
        self.N_p_entry = tk.Entry(self.left_frame, font='Arial 12', width=10) # Количество резервуаров
        self.N_p_entry.grid(row=9, column=1, padx=10, pady=10, sticky='ew')
        tk.Label(self.left_frame, text='шт.', font='Arial 12',bg='white').grid(row=9, column=2, padx=10, pady=10, sticky='ew')

        tk.Label(self.left_frame, text='Количество групп', font='Arial 12',bg='white').grid(row=10, column=0, padx=10, pady=10, sticky='ew')
        self.N_gr_entry = tk.Entry(self.left_frame, font='Arial 12', width=10) # Количество групп
        self.N_gr_entry.grid(row=10, column=1, padx=10, pady=10, sticky='ew')
        tk.Label(self.left_frame, text='шт.', font='Arial 12',bg='white').grid(row=10, column=2, padx=10, pady=10, sticky='ew')

        tk.Label(self.left_frame, text='Тип конструкции', font='Arial 12',bg='white').grid(row=11, column=0, padx=10, pady=10, sticky='ew')
        

        self.type_construction_cc = ttk.Combobox(self.left_frame,
                                                 values=[
                                                     "Наземный вертикальный",
                                                     "Заглубленный",
                                                     "Наземный горизонтальный"],
                                                 state="readonly") # Тип конструкции
        self.type_construction_cc.current(0)
        self.type_construction_cc.grid(row=11, column=1, padx=10, pady=10, sticky='ew', columnspan=2)

        tk.Label(self.left_frame, text='Режим эксплуатации', font='Arial 12',bg='white').grid(row=12, column=0, padx=10, pady=10,
                                                                                  sticky='ew')
        self.operation_mode_cc = ttk.Combobox(self.left_frame, values=["мерник", "буферная емкость"]
                                              , state="readonly") # Режим эксплуатации
        self.operation_mode_cc.current(0)
        self.operation_mode_cc.bind("<<ComboboxSelected>>", self.set_type_construction)
        self.operation_mode_cc.grid(row=12, column=1, padx=10, pady=10, sticky='ew', columnspan=2)

        tk.Label(self.left_frame, text='ССВ', font='Arial 12', background='white').grid(row=13, column=0, padx=10, pady=10,
                                                                    sticky='ew')
        self.SSV_cc = ttk.Combobox(self.left_frame,
                                   values=["отсутствует", "понтон", "плавающая крыша"]
                                   , state="readonly") # Средства сокращения выбросов
        self.SSV_cc.current(0)
        self.SSV_cc.bind("<<ComboboxSelected>>", self.set_type_construction)

        self.SSV_cc.grid(row=13, column=1, padx=10, pady=10, sticky='ew', columnspan=2)

        tk.Label(self.left_frame, text='Пары:', font='Arial 10',bg='white').grid(row=14, column=0, padx=10, pady=10, sticky='ew')
        self.pari_cc = ttk.Combobox(self.left_frame, values=['нефтей и ловушечных продуктов', 'бензинов и бензиновых фракций'], font='Arial 10', width=10)
        self.pari_cc.grid(row=14, column=1, padx=10, pady=10, sticky='ew', columnspan=2)
        self.pari_cc.current(0)


        tk.Button(self.left_frame, text='Рассчитать', font='Arial 8', command=self.calculate).grid(row=15, column=0, padx=10, pady=10, sticky='ew', columnspan=3)

        tk.Button(self.left_frame, text='Задать значения по умолчанию', font='Arial 8', command=self.autoEnter).grid(row=16, column=0, padx=10, pady=10, sticky='ew', columnspan=3)
        self.right_frame = tk.Frame(self, bg='white', width=self.width // 2, height=self.height)
        self.right_frame.place(x=self.width // 2, y=0)

        tk.Button(self.left_frame, text='Сохранить результаты расчета', font='Arial 8', command=self.export_result).grid(row=17, column=0, padx=10, pady=10, sticky='ew', columnspan=3)

        tk.Button(self.left_frame, text='Очистить поля', font='Arial 8', command=self.clear_fields).grid(row=18, column=0, padx=10, pady=10, sticky='ew', columnspan=3)

        
        tk.Label(self.right_frame, text='Результаты расчета', font='Arial 12',bg='white').place(x=self.width//4, y=0, anchor='n')
        self.text_result = tk.Text(self.right_frame, font='Arial 12', width=self.width//2, height=self.height-30)
        self.text_result.place(x=0, y=30)

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

    def clear_fields(self):
        self.P38_entry.delete(0, tk.END)
        self.t_nk_entry.delete(0, tk.END)
        self.t_zh_max_entry.delete(0, tk.END)
        self.t_zh_min_entry.delete(0, tk.END)
        self.V_ch_max_entry.delete(0, tk.END)
        self.B_entry.delete(0, tk.END)
        self.ro_zh_entry.delete(0, tk.END)
        self.V_p_entry.delete(0, tk.END)
        self.N_p_entry.delete(0, tk.END)
        self.N_gr_entry.delete(0, tk.END)
        self.type_construction_cc.set("")
        self.operation_mode_cc.set("")
        self.SSV_cc.set("")
        self.pari_cc.set("")

    def export_result(self):
        try:
            with open("result_benzin.txt", "w") as file:
                file.write(f"Результаты расчета:\n")
                file.write(self.text_result.get(1.0, tk.END))
            mb.showinfo("Успех", "Файл успешно сохранен!")
        except:
            mb.showerror("Ошибка", "Не удалось сохранить файл!")

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
        if self.P38_entry.get() == '' or self.t_nk_entry.get() == '' or self.t_zh_max_entry.get() == '' or self.t_zh_min_entry.get() == '' or self.V_ch_max_entry.get() == '' or self.B_entry.get() == '' or self.V_p_entry == '' or self.N_p_entry.get() == '' or self.N_gr_entry.get() == '':
            self.text_result.insert(1.0, 'Заполните все поля!')
        
        else:

            # вычисление m
            self.t_nk = int(self.t_nk_entry.get()) # температура начала кипения
            self.pari = self.pari_cc.get() # вид паров
            if self.pari=="нефтей и ловушечных продуктов":
                row_index = self.list_of_table[4].loc[self.list_of_table[4]["tнк"]==self.t_nk].index[0]
                m = self.list_of_table[4].loc[row_index, "m"]
            else:
                row_index = self.list_of_table[4].loc[self.list_of_table[4]["tнк2"]==self.t_nk].index[0]
                m = self.list_of_table[4].loc[row_index, "m2"]
            

            self.m = m # молекулярная масса паров жидкости
            self.text_result.insert(1.0, f'm:\t{self.m} г/моль\n')

            self.t_zh_max = int(self.t_zh_max_entry.get()) # максимальная температура жидкости в резервуаре
            self.t_zh_min = int(self.t_zh_min_entry.get()) # минимальная температура жидкости в резервуаре
            count_column = self.list_of_table[6].shape[1]
            i_col_min = 0
            i_col_max = 0
            i_row_min = 0
            i_row_max = 0
            for i in range(16): # поиск коэффициентов K_t_max и K_t_min
                for j in range(count_column):
                    if self.list_of_table[6].iloc[i,j] == str(self.t_zh_max):
                        i_col_max = j
                        i_row_max = i
                    if self.list_of_table[6].iloc[i,j] == str(self.t_zh_min):
                        i_col_min = j
                        i_row_min = i
            self.K_t_max = float(self.list_of_table[6].iloc[i_row_max,i_col_max+1])
            self.K_t_min = float(self.list_of_table[6].iloc[i_row_min,i_col_min+1])
            
            self.text_result.insert("end", f'K_t_max:\t{self.K_t_max}\n')
            self.text_result.insert("end", f'K_t_min:\t{self.K_t_min}\n')
            self.type_construction = self.type_construction_cc.get() # тип конструкции
            self.operation_mode = self.operation_mode_cc.get() # режим работы
            self.SSV = self.SSV_cc.get() # ССВ
            self.V_p = int(self.V_p_entry.get()) # объем резервуара
            self.P38 = int(self.P38_entry.get()) # давление насыщенных паров нефтей и бензинов при температуре 38°С 
            self.B = int(self.B_entry.get()) #  количество жидкости, закачиваемое в резервуары в течение года, т/год
            self.ro_zh = float(self.ro_zh_entry.get()) # плотность жидкости, т/м3
            self.N_p = int(self.N_p_entry.get()) # количество резервуаров
            self.V_ch_max = float(self.V_ch_max_entry.get())  # максимальный объем паровоздушной смеси, вытесняемый из резервуара при его заполнении, м3/час

            # K_p
            self.K_p_max, self.K_p_sr = self.calculate_K_p(self.V_p, self.SSV)
            self.text_result.insert("end", f'K_p_sr:\t{self.K_p_sr}\n')


            # K_b
            if self.P38<=540:
                self.K_b = 1.00
            else:
                row = self.list_of_table[8].loc[self.list_of_table[8][self.list_of_table[8].columns[0]] == self.P38]
                self.K_b = row.iloc[0][1]
            self.text_result.insert("end", f'K_b:\t{self.K_b}\n')

            # n
            self.n = round(self.B/(self.ro_zh*self.V_p*self.N_p)) 
            print(f"{self.n}=round({self.B}/({self.ro_zh}*{self.V_p}*{self.N_p}))")
            self.text_result.insert("end", f'n:\t{self.n}\n')

            k_ob_values = {100: 1.35, 80: 1.5, 60: 1.75, 40: 2, 30: 2.25, 20: 2.5} # Коэффициенты Коб
            nearest_n = min(k_ob_values.keys(), key=lambda x: abs(x - self.n))
            self.K_ob = k_ob_values[nearest_n] # Коэффициент Коб
            self.text_result.insert("end", f'K_ob:\t{self.K_ob}\n')

            self.M = self.P38*self.m*self.K_t_max*self.K_p_sr*self.K_b*self.V_ch_max*0.163*10**(-4) # Максимальные выбросы загрязняющих веществ в атмосферу, г/с
            self.text_result.insert("end", f'M:\t{round(self.M,6)} г/c\n')

            self.G = self.P38*self.m*(self.K_t_max*self.K_b+self.K_t_min)*self.K_p_sr*self.K_ob*self.B*0.294/10**7/self.ro_zh # Годовые выбросы загрязняющих веществ в атмосферу, т/год
            # print formula
            print(f"{self.G}=({self.P38}*{self.m}*({self.K_t_max}*{self.K_b}+{self.K_t_min})*{self.K_p_sr}*{self.K_ob}*{self.B}*0.294/10**7/{self.ro_zh})")
            self.text_result.insert("end", f'G:\t{round(self.G,6)} т/год\n')



    def autoEnter(self):
        # Задать значения по умолчанию
        self.P38_entry.delete(0, tk.END)
        self.P38_entry.insert(0, 420)

        self.t_nk_entry.delete(0, tk.END)
        self.t_nk_entry.insert(0, 42)

        self.t_zh_max_entry.delete(0, tk.END)
        self.t_zh_max_entry.insert(0, 32)

        self.t_zh_min_entry.delete(0, tk.END)
        self.t_zh_min_entry.insert(0, 10)

        self.V_ch_max_entry.delete(0, tk.END)
        self.V_ch_max_entry.insert(0, 56)

        self.B_entry.delete(0, tk.END)
        self.B_entry.insert(0, 300000)

        self.ro_zh_entry.delete(0, tk.END)
        self.ro_zh_entry.insert(0, 0.74)

        self.V_p_entry.delete(0, tk.END)
        self.V_p_entry.insert(0, 1000)


        self.N_p_entry.delete(0, tk.END)
        self.N_p_entry.insert(0, 3)

        self.N_gr_entry.delete(0, tk.END)
        self.N_gr_entry.insert(0, 22)

        # Установить значения по умолчанию - нулевой выбор в combobox
        self.type_construction_cc.current(0)
        self.operation_mode_cc.current(0)
        self.SSV_cc.current(0)

        self.pari_cc.current(1)
         


def run_app(parent):
    app = App(parent)
    app.create_widgets_0()
