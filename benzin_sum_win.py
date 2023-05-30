import tkinter as tk
from tkinter import ttk
import numpy as np
import pandas as pd
from tkinter import messagebox as mb

class App(tk.Tk):
    def __init__(self, *parent):
        super().__init__()
        self.list_of_table = []
        for i in range(0,22):
            self.list_of_table.append(pd.read_excel("C:\\Users\\renaz\\Documents\\machine_learning\\bit\\Книга1.xlsx", sheet_name=f"{i}"))
        self.title('Расчета выброса бензина, нефтей и других нефтепродуктов с летним и зимним периодом')
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

        tk.Label(self.left_frame, text='P38_letniy', font='Arial 7', bg='white').grid(row=1, column=0, padx=10, pady=10, sticky='ew')
        self.P38_letniy_entry = tk.Entry(self.left_frame, font='Arial 7', width=10) # Давление насыщенных паров при 38°С в летний период
        self.P38_letniy_entry.grid(row=1, column=1, padx=10, pady=10, sticky='ew')
        tk.Label(self.left_frame, text='мм.рт.ст.', font='Arial 7',bg='white').grid(row=1, column=2, padx=10, pady=10, sticky='ew')

        tk.Label(self.left_frame, text='P38_zimniy', font='Arial 7',bg='white').grid(row=2, column=0, padx=10, pady=10, sticky='ew')
        self.P38_zimniy_entry = tk.Entry(self.left_frame, font='Arial 7', width=10) # Давление насыщенных паров при 38°С в зимний период
        self.P38_zimniy_entry.grid(row=2, column=1, padx=10, pady=10, sticky='ew')
        tk.Label(self.left_frame, text='мм.рт.ст.', font='Arial 7',bg='white').grid(row=2, column=2, padx=10, pady=10, sticky='ew')

        tk.Label(self.left_frame, text="t_nk_letniy", font='Arial 7',bg='white').grid(row=3, column=0, padx=10, pady=10, sticky='ew')
        self.t_nk_letniy_entry = tk.Entry(self.left_frame, font='Arial 7', width=10) # Температура начала кипения в летний период
        self.t_nk_letniy_entry.grid(row=3, column=1, padx=10, pady=10, sticky='ew')
        tk.Label(self.left_frame, text='°С', font='Arial 7',bg='white').grid(row=3, column=2, padx=10, pady=10, sticky='ew')

        tk.Label(self.left_frame, text='t_nk_zimniy', font='Arial 7',bg='white').grid(row=4, column=0, padx=10, pady=10, sticky='ew')
        self.t_nk_zimniy_entry = tk.Entry(self.left_frame, font='Arial 7', width=10) # Температура начала кипения в зимний период
        self.t_nk_zimniy_entry.grid(row=4, column=1, padx=10, pady=10, sticky='ew')
        tk.Label(self.left_frame, text='°С', font='Arial 7',bg='white').grid(row=4, column=2, padx=10, pady=10, sticky='ew')

        tk.Label(self.left_frame, text='t_zh_max', font='Arial 7',bg='white').grid(row=5, column=0, padx=10, pady=10, sticky='ew')
        self.t_zh_max_entry = tk.Entry(self.left_frame, font='Arial 7', width=10) # Максимальная температура жидкости в резервуаре
        self.t_zh_max_entry.grid(row=5, column=1, padx=10, pady=10, sticky='ew')
        tk.Label(self.left_frame, text='°С', font='Arial 7',bg='white').grid(row=5, column=2, padx=10, pady=10, sticky='ew')

        tk.Label(self.left_frame, text='t_zh_min', font='Arial 7',bg='white').grid(row=6, column=0, padx=10, pady=10, sticky='ew')
        self.t_zh_min_entry = tk.Entry(self.left_frame, font='Arial 7', width=10) # Минимальная температура жидкости в резервуаре
        self.t_zh_min_entry.grid(row=6, column=1, padx=10, pady=10, sticky='ew')
        tk.Label(self.left_frame, text='°С', font='Arial 7',bg='white').grid(row=6, column=2, padx=10, pady=10, sticky='ew')

        tk.Label(self.left_frame, text='V_ch_max', font='Arial 7',bg='white').grid(row=7, column=0, padx=10, pady=10, sticky='ew')
        self.V_ch_max_entry = tk.Entry(self.left_frame, font='Arial 7', width=10) # Максимальный объем жидкости в резервуаре
        self.V_ch_max_entry.grid(row=7, column=1, padx=10, pady=10, sticky='ew')
        tk.Label(self.left_frame, text='м/с', font='Arial 7',bg='white').grid(row=7, column=2, padx=10, pady=10, sticky='ew')

        tk.Label(self.left_frame, text='B', font='Arial 7',bg='white').grid(row=8, column=0, padx=10, pady=10, sticky='ew')
        self.B_entry = tk.Entry(self.left_frame, font='Arial 7', width=10) # Количество жидкости закачиваемой в резервуар
        self.B_entry.grid(row=8, column=1, padx=10, pady=10, sticky='ew')
        tk.Label(self.left_frame, text='м', font='Arial 7',bg='white').grid(row=8, column=2, padx=10, pady=10, sticky='ew')

        tk.Label(self.left_frame, text='ro_zh', font='Arial 7',bg='white').grid(row=9, column=0, padx=10, pady=10, sticky='ew')
        self.ro_zh_entry = tk.Entry(self.left_frame, font='Arial 7', width=10) # Плотность жидкости
        self.ro_zh_entry.grid(row=9, column=1, padx=10, pady=10, sticky='ew')
        tk.Label(self.left_frame, text='кг/м3', font='Arial 7',bg='white').grid(row=9, column=2, padx=10, pady=10, sticky='ew')

        tk.Label(self.left_frame, text='Режим эксплуатации', font='Arial 7',bg='white').grid(row=10, column=0, padx=10, pady=10, sticky='ew')
        self.operation_mode_cc = ttk.Combobox(self.left_frame, font='Arial 7', width=10,
                                              values=["мерник", "буферная емкость"],
                                              state='readonly') # Режим эксплуатации
        self.operation_mode_cc.grid(row=10, column=1, padx=10, pady=10, sticky='ew', columnspan=2)
        self.operation_mode_cc.current(0)


        tk.Label(self.left_frame, text='Конструкция резервуара', font='Arial 7',bg='white').grid(row=11, column=0, padx=10, pady=10, sticky='ew')
        self.type_construction_cc = ttk.Combobox(self.left_frame, font='Arial 7', width=10,
                                                 values=["Наземный вертикальный",
                                                     "Заглубленный",
                                                     "Наземный горизонтальный"],
                                                     state='readonly') # Тип конструкции резервуара
        self.type_construction_cc.grid(row=11, column=1, padx=10, pady=10, sticky='ew', columnspan=2)
        self.type_construction_cc.current(0)

        tk.Label(self.left_frame, text='ССВ летний', font='Arial 7',bg='white').grid(row=12, column=0, padx=10, pady=10, sticky='ew')
        self.SSV_letniy_cc = ttk.Combobox(self.left_frame, font='Arial 7', width=10,
                                          values=["отсутствует","понтон", "плавающая крыша", "буферная емкость"],
                                          state='readonly') # Средства сокращения выбросов в летний период
        self.SSV_letniy_cc.grid(row=12, column=1, padx=10, pady=10, sticky='ew', columnspan=2)
        self.SSV_letniy_cc.current(0)

        tk.Label(self.left_frame, text='ССВ зимний', font='Arial 7',bg='white').grid(row=13, column=0, padx=10, pady=10, sticky='ew')
        self.SSV_zimniy_cc = ttk.Combobox(self.left_frame, font='Arial 7', width=10,
                                          values=["отсутствует","понтон", "плавающая крыша", "буферная емкость"],
                                          state='readonly') # Средства сокращения выбросов в зимний период
        self.SSV_zimniy_cc.grid(row=13, column=1, padx=10, pady=10, sticky='ew', columnspan=2)
        self.SSV_zimniy_cc.current(0)

        tk.Label(self.left_frame, text='V_p летний', font='Arial 7',bg='white').grid(row=14, column=0, padx=10, pady=10, sticky='ew')
        self.V_p_letniy_entry = tk.Entry(self.left_frame, font='Arial 7', width=10) # Объем резервуара в летний период
        self.V_p_letniy_entry.grid(row=14, column=1, padx=10, pady=10, sticky='ew')
        tk.Label(self.left_frame, text='м3', font='Arial 7',bg='white').grid(row=14, column=2, padx=10, pady=10, sticky='ew')

        tk.Label(self.left_frame, text='V_p зимний', font='Arial 7',bg='white').grid(row=15, column=0, padx=10, pady=10, sticky='ew')
        self.V_p_zimniy_entry = tk.Entry(self.left_frame, font='Arial 7', width=10) # Объем резервуара в зимний период
        self.V_p_zimniy_entry.grid(row=15, column=1, padx=10, pady=10, sticky='ew')
        tk.Label(self.left_frame, text='м3', font='Arial 7',bg='white').grid(row=15, column=2, padx=10, pady=10, sticky='ew')

        tk.Label(self.left_frame, text='N_p_letniy', font='Arial 7',bg='white').grid(row=16, column=0, padx=10, pady=10, sticky='ew')
        self.N_p_letniy_entry = tk.Entry(self.left_frame, font='Arial 7', width=10) # Количество резервуаров в летний период
        self.N_p_letniy_entry.grid(row=16, column=1, padx=10, pady=10, sticky='ew')
        tk.Label(self.left_frame, text='шт', font='Arial 7',bg='white').grid(row=16, column=2, padx=10, pady=10, sticky='ew')

        tk.Label(self.left_frame, text='N_p_zimniy', font='Arial 7',bg='white').grid(row=17, column=0, padx=10, pady=10, sticky='ew')
        self.N_p_zimniy_entry = tk.Entry(self.left_frame, font='Arial 7', width=10) # Количество резервуаров в зимний период
        self.N_p_zimniy_entry.grid(row=17, column=1, padx=10, pady=10, sticky='ew')
        tk.Label(self.left_frame, text='шт', font='Arial 7',bg='white').grid(row=17, column=2, padx=10, pady=10, sticky='ew')

        tk.Label(self.left_frame, text='Количество групп', font='Arial 7',bg='white').grid(row=18, column=0, padx=10, pady=10, sticky='ew')
        self.N_group_entry = tk.Entry(self.left_frame, font='Arial 7', width=10) # Количество групп
        self.N_group_entry.grid(row=18, column=1, padx=10, pady=10, sticky='ew')
        tk.Label(self.left_frame, text='шт', font='Arial 7',bg='white').grid(row=18, column=2, padx=10, pady=10, sticky='ew')


        

        tk.Button(self.left_frame, text='Рассчитать', font='Arial 7', command=self.calculate).grid(row=19, column=0, padx=10, pady=10, sticky='ew', columnspan=1)

        tk.Button(self.left_frame, text='Задать значения по умолчанию', font='Arial 7', command=self.autoEnter).grid(row=20, column=0, padx=10, pady=10, sticky='ew', columnspan=1)

        tk.Button(self.left_frame, text='Сохранить результаты расчета', font='Arial 7', command=self.export_result).grid(row=19, column=2, padx=10, pady=10, sticky='ew', columnspan=1)

        tk.Button(self.left_frame, text='Очистить поля', font='Arial 7', command=self.clear_fields).grid(row=20, column=2, padx=10, pady=10, sticky='ew', columnspan=1)


        # right_frame
        self.right_frame = tk.Frame(self, bg='white', width=self.width // 2, height=self.height)
        self.right_frame.place(x=self.width // 2, y=0)

        tk.Label(self.right_frame, text='Результаты расчета', font='Arial 7',bg='white').place(x=self.width//4, y=0, anchor='n')
        self.text_result = tk.Text(self.right_frame, font='Arial 7', width=self.width//2, height=self.height-30)
        self.text_result.place(x=0, y=30)

    def clear_fields(self):
        self.V_p_letniy_entry.delete(0, tk.END)
        self.V_p_zimniy_entry.delete(0, tk.END)
        self.N_p_letniy_entry.delete(0, tk.END)
        self.N_p_zimniy_entry.delete(0, tk.END)
        self.N_group_entry.delete(0, tk.END)
        self.text_result.delete(1.0, tk.END)
        self.P38_letniy_entry.delete(0, tk.END)
        self.P38_zimniy_entry.delete(0, tk.END)
        self.t_nk_letniy_entry.delete(0, tk.END)
        self.t_nk_zimniy_entry.delete(0, tk.END)
        self.t_zh_max_entry.delete(0, tk.END)
        self.t_zh_min_entry.delete(0, tk.END)
        self.V_ch_max_entry.delete(0, tk.END)
        self.B_entry.delete(0, tk.END)
        self.ro_zh_entry.delete(0, tk.END)
        self.operation_mode_cc.current(0)
        self.SSV_cc.current(0)
        self.type_construction_cc.current(0)


    def export_result(self):
        try:
            with open("result_benzin_sam_win.txt", "w") as file:
                file.write(f"Результаты расчета:\n")
                file.write(self.text_result.get(1.0, tk.END))
            mb.showinfo("Успех", "Файл успешно сохранен!")
        except:
            mb.showerror("Ошибка", "Не удалось сохранить файл!")

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

    def search_7(self,product, search_element):
        cols = self.list_of_table[6].iloc[:, 0::2].columns # Столбы поиска
        element = search_element
        if product == "Нефти и бензины":
            result = self.list_of_table[6].iloc[:18, self.list_of_table[6].columns.get_indexer(cols)].isin([element])
        elif "Нефтепродукты (кроме бензина)":
            result = self.list_of_table[6].iloc[19:, self.list_of_table[6].columns.get_indexer(cols)].isin([element])
        else:
            Exception("Неверное название продукта")
        row_index, col_name = result.stack()[result.stack()].index[0]
        col_index = self.list_of_table[6].columns.get_loc(col_name)
        value = self.list_of_table[6].iloc[row_index, col_index+1]
        return value
    
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
        if self.operation_mode_cc.get() == "" or self.SSV_letniy_cc.get()=="" or self.SSV_zimniy_cc.get()=="" or self.type_construction_cc.get() == "" or self.SSV_letniy_cc.get() == "" or self.SSV_zimniy_cc.get() == "" or self.V_p_letniy_entry.get() == "" or self.V_p_zimniy_entry.get() == "" or self.N_p_letniy_entry.get() == "" or self.N_group_entry.get() == "":
            self.text_result.insert(1.0, "Не все поля заполнены")
        else:

            # вычисление m
            self.t_nk_letniy = int(self.t_nk_letniy_entry.get()) # температура начала кипения в летний период
            self.t_nk_zimniy = int(self.t_nk_zimniy_entry.get()) # температура начала кипения в зимний период
            self.m_letniy = self.list_of_table[4].loc[self.list_of_table[4]["tнк2"] == self.t_nk_letniy]["m2"].values[0] # молекулярная масса в летний период
            self.m_zimniy = self.list_of_table[4].loc[self.list_of_table[4]["tнк2"] == self.t_nk_zimniy]["m2"].values[0] # молекулярная масса в зимний период
            
            self.text_result.insert(1.0, f'm_letniy:\t{self.m_letniy} г/моль\n')
            self.text_result.insert(2.0, f'm_zimniy:\t{self.m_zimniy} г/моль\n')

            self.t_zh_max = self.t_zh_max_entry.get() # температура жидкости в летний период
            self.t_zh_min = self.t_zh_min_entry.get() # температура жидкости в зимний период

            #self.K_t_max = float(self.search_7("Нефти и бензины", self.t_zh_max)) # опытный коэффициент
            self.K_t_max = 0.74 # опытный коэффициент
            self.K_t_min = 0.35 # опытный коэффициент

            self.text_result.insert(3.0, f'K_t_max:\t{self.K_t_max}\n')
            self.text_result.insert(4.0, f'K_t_min:\t{self.K_t_min}\n')

            self.V_p_letniy = int(self.V_p_letniy_entry.get()) # Объем резервуара в летний период
            self.V_p_zimniy = int(self.V_p_zimniy_entry.get()) # Объем резервуара в зимний период
            self.SSV_letniy = self.SSV_letniy_cc.get() # ССВ в летний период
            self.SSV_zimniy = self.SSV_zimniy_cc.get() # ССВ в зимний период

            self.K_p_max_letniy, self.K_p_sr_letniy = self.calculate_K_p(self.V_p_letniy, self.SSV_letniy) # коэффициенты в летний период
            self.K_p_max_zimniy, self.K_p_sr_zimniy = self.calculate_K_p(self.V_p_zimniy, self.SSV_zimniy) # коэффициенты в зимний период

            self.text_result.insert(5.0, f'K_p_max_letniy:\t{self.K_p_max_letniy}\n')
            self.text_result.insert(5.0, f'K_p_max_zimniy:\t{self.K_p_max_zimniy}\n')
            self.text_result.insert(6.0, f'K_p_sr_letniy:\t{self.K_p_sr_letniy}\n')
            self.text_result.insert(6.0, f'K_p_sr_zimniy:\t{self.K_p_sr_zimniy}\n')

            self.N_p_letniy = int(self.N_p_letniy_entry.get()) # количество резервуаров в летний период
            self.N_p_zimniy = int(self.N_p_zimniy_entry.get()) # количество резервуаров в зимний период

            self.K_p_sr = (self.K_p_sr_letniy*self.V_p_letniy+self.K_p_sr_zimniy*self.V_p_zimniy)/(self.V_p_letniy+self.V_p_zimniy) # средний коэффициент
            self.K_p_sr = round(self.K_p_sr, 2)
            self.text_result.insert(tk.END, f'K_p_sr:\t{self.K_p_sr}\n')

            # n
            self.B = float(self.B_entry.get()) # количество жидкости, закачиваемое в резервуары в течение года, т/год
            self.ro_zh = float(self.ro_zh_entry.get()) # плотность жидкости, т/м3
            self.n = round(self.B/(self.ro_zh*(self.V_p_letniy*self.N_p_letniy+self.V_p_zimniy*self.N_p_zimniy))) 
            self.text_result.insert("end", f'n:\t{self.n}\n')

            # K_b
            self.P38_letniy = float(self.P38_letniy_entry.get()) # давление при температуре 38 градусов в летний период
            if self.P38_letniy<=540:
                self.K_b = 1.00
            else:
                row = self.list_of_table[8].loc[self.list_of_table[8][self.list_of_table[8].columns[0]] == self.P38]
                self.K_b = row.iloc[0][1]
            self.text_result.insert("end", f'K_b:\t{self.K_b}\n')


            k_ob_values = {100: 1.35, 80: 1.5, 60: 1.75, 40: 2, 30: 2.25, 20: 2.5}
            nearest_n = min(k_ob_values.keys(), key=lambda x: abs(x - self.n))
            self.K_ob = k_ob_values[nearest_n] # 
            self.text_result.insert("end", f'K_ob:\t{self.K_ob}\n')

            self.P38_zimniy = float(self.P38_zimniy_entry.get()) # давление при температуре 38 градусов в зимний период
            self.V_ch_max = float(self.V_ch_max_entry.get()) # объем резервуара, м3
            self.M = 0.163*self.P38_letniy*self.m_letniy*self.K_t_max*self.K_p_sr*self.K_b*self.V_ch_max*10**-4
            self.M = round(self.M, 4)
            self.text_result.insert("end", f'M:\t{self.M} г/с\n')
            self.G = np.round((0.294*((self.P38_letniy*self.K_t_max*self.K_b*self.m_letniy)+(self.P38_zimniy*self.K_t_min*self.m_zimniy))*self.K_p_sr*self.K_ob*self.B)/(10**7*self.ro_zh),4)
            self.text_result.insert("end", f'G:\t{self.G} т/год\n')


    def autoEnter(self):
        # clear text
        self.text_result.delete(1.0, "end")
        
        # clear entry
        self.P38_letniy_entry.delete(0, "end")
        self.P38_zimniy_entry.delete(0, "end")

        self.t_nk_letniy_entry.delete(0, "end")
        self.t_nk_zimniy_entry.delete(0, "end")

        self.t_zh_max_entry.delete(0, "end")
        self.t_zh_min_entry.delete(0, "end")

        self.V_ch_max_entry.delete(0, "end")

        self.B_entry.delete(0, "end")

        self.ro_zh_entry.delete(0, "end")

        self.type_construction_cc.current(0)
        self.operation_mode_cc.current(0)

        self.SSV_letniy_cc.current(2)
        self.SSV_zimniy_cc.current(2)

        self.N_group_entry.delete(0, "end")

        self.V_p_letniy_entry.delete(0, "end")
        self.V_p_zimniy_entry.delete(0, "end")

        self.N_p_letniy_entry.delete(0, "end")
        self.N_p_zimniy_entry.delete(0, "end")

        # Задать значения по умолчанию
        self.P38_letniy_entry.insert(0, 425)
        self.P38_zimniy_entry.insert(0, 525)

        self.t_nk_letniy_entry.insert(0, 40)
        self.t_nk_zimniy_entry.insert(0, 35)

        self.t_zh_max_entry.insert(0, 30)
        self.t_zh_min_entry.insert(0, 5)

        self.V_ch_max_entry.insert(0, 250)

        self.B_entry.insert(0, 1460000)

        self.ro_zh_entry.insert(0, 0.73)

        self.type_construction_cc.current(0)
        self.operation_mode_cc.current(0)

        self.SSV_letniy_cc.current(1)
        self.SSV_zimniy_cc.current(0)

        self.V_p_letniy_entry.insert(0, 10000)
        self.V_p_zimniy_entry.insert(0, 5000)

        self.N_p_letniy_entry.insert(0, 2)
        self.N_p_zimniy_entry.insert(0, 2)
        self.N_group_entry.insert(0, 22)


def run_app(parent):
    app = App(parent)
    app.create_widgets_0()

app = App()
app.create_widgets_0()