import customtkinter as ctk
from tkinter import filedialog
import os
from tkinter import messagebox

class CreateProject:
    def __init__(self):
        self.root = ctk.CTk()

        self.root.title("Создание проекта")
        self.root.geometry("500x230")
        
        self.proj_name = ctk.CTkEntry(self.root, placeholder_text="Название проекта", width=480)
        self.proj_name.pack(pady=10)

        # Создаем фрейм для пути и кнопки выбора
        path_frame = ctk.CTkFrame(self.root)
        path_frame.pack(pady=15)
        
        self.path_proj = ctk.CTkEntry(path_frame, placeholder_text="Путь к проекту", width=400)
        self.path_proj.pack(side='left', padx=5)
        
        browse_btn = ctk.CTkButton(path_frame, text="...", width=70, command=self.browse_folder)
        browse_btn.pack(side='right', padx=5)

        self.create_proj_btn = ctk.CTkButton(self.root, text="Создать проект", width=480, command=self.create_prj)
        self.create_proj_btn.pack(pady=40)

        # Запрещаем изменение размера окна
        self.root.resizable(False, False)

        self.root.mainloop()

    def browse_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.path_proj.delete(0, 'end')
            self.path_proj.insert(0, folder_path)

    def create_prj(self):
        project_name = self.proj_name.get()
        project_path = self.path_proj.get()

        if project_name and project_path:
            os.mkdir(project_path + "/" + project_name)
            open(project_path + "/" + project_name + "/main.hy", "w")
            with open(project_path + "/" + project_name + "/hydra_project.hyproj", "w") as hprj:
                hprj.write(f"""
                            HYDRA_PROJECT
                            HYDRA_LORE
                            HYDRA_PROJECT [
                             NAME: {project_name}
                             PATH: {project_path}
                           ]
                           """)
            print(f"Создание проекта: {project_name} в {project_path}")

        else:

            messagebox.showerror("Ошибка", "Необходимо указать название и путь к проекту")