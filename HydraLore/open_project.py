from tkinter import filedialog
from tkinter import messagebox
import os
import customtkinter as ctk

class OpenProject:
    def __init__(self):
        # Создаем окно
        self.window = ctk.CTkToplevel()
        self.window.title("Открыть проект")
        self.window.geometry("400x150")
        
        # Создаем поле для пути
        self.path_proj = ctk.CTkEntry(self.window, width=300)
        self.path_proj.pack(pady=20, padx=20)
        
        # Кнопка выбора директории
        self.browse_button = ctk.CTkButton(self.window, text="Выбрать директорию", command=self.browse_folder)
        self.browse_button.pack(pady=10)
        
        # Кнопка открытия проекта
        self.open_button = ctk.CTkButton(self.window, text="Открыть проект", command=self.open_project)
        self.open_button.pack(pady=5)

    def browse_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.path_proj.delete(0, 'end')
            self.path_proj.insert(0, folder_path)

    def open_project(self):
        folder_path = self.path_proj.get()
        if folder_path:
            try:
                project_file = self.find("hydra_project.hyproj", folder_path)
                if project_file:
                    # Здесь код для открытия проекта
                    self.window.destroy()
                else:
                    messagebox.showerror("Ошибка", "Файл проекта не найден")
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось распознать структуру проекта: {str(e)}")

    def find(self, name, path):
        for root, dirs, files in os.walk(path):
            if name in files:
                return os.path.join(root, name)
        return None
