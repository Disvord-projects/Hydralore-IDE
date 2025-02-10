import customtkinter as ctk
import debug
import create_project
import open_project
import webbrowser
from tkinter import filedialog, messagebox, Menu
import os

class TextEditor(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("dark")  
        ctk.set_default_color_theme("blue")  

        self.title("HydraLore")
        self.geometry("800x600")

        # Создание текстового поля
        self.text_area = ctk.CTkTextbox(self, font=("Arial", 15))
        self.text_area.pack(expand=True, fill='both')

        # Создание стандартного меню
        self.menu = Menu(self)
        self.config(menu=self.menu)
        
        # Меню "Проект"
        # частично не реализовано
        self.proj_menu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Проект", menu=self.proj_menu)  # Добавляем меню проектов
        # self.proj_menu.add_command(label="Создать", command=self.create_project)
        # self.proj_menu.add_command(label="Открыть", command=self.open_project)
        self.proj_menu.add_command(label="Запустить", command=self.run)

        # Меню "Справка"
        self.help_menu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Справка", menu=self.help_menu)
        self.help_menu.add_command(label="О программе", command=self.show_about)
        self.help_menu.add_command(label="Документация по Hydra", command=self.doc_hydra)
        self.help_menu.add_command(label="Документация по HydraLore", command=self.doc_hydralore)

    def show_about(self):
        messagebox.showinfo("О программе", "HydraLore - редактор кода для языка программирования Hydra\nВерсия: dev0.1\n(by Disvord, на основе SKINT IDE by PRoX)")
    
    def doc_hydra(self):
        webbrowser.open("https://github.com/Kross1de/Hydra---The-programming-language")

    def doc_hydralore(self):
        messagebox.showinfo("Документация по HydraLore", "Документация по HydraLore пока не реализована")

    def run(self):
        """Метод для запуска проекта"""
        source_code = self.text_area.get("1.0", "end-1c")
        
        # Записываем код во временный файл
        with open("temp_code.hy", "w", encoding='utf-8') as f:
            f.write(source_code)
        
        debug_window = debug.Debug()  # Создаем окно отладки


    # пожалуйста, не раскомментируйте этот код, пока я не закончу его реализовывать
    def create_project(self):
        """Метод для создания нового проекта"""
        # create_project.CreateProject()
        messagebox.showinfo("Ошибка", "Эта функция пока не реализована")

    def open_project(self):
        """Метод для открытия проекта"""
        # open_project.OpenProject()
        messagebox.showinfo("Ошибка", "Эта функция пока не реализована")

if __name__ == "__main__":
    app = TextEditor()
    app.mainloop()