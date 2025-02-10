import customtkinter as ctk
import sys
import os
import subprocess

class Debug:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Отладка")
        self.root.geometry("600x400")

        self.debug_text = ctk.CTkTextbox(self.root, width=600, height=400)
        self.debug_text.pack(padx=20, pady=20)
        
        # Запрещаем редактирование текста

        # Перенаправляем стандартный вывод
        sys.stdout = TextRedirector(self.debug_text)
        sys.stderr = TextRedirector(self.debug_text, "error")

        # Запускаем main.py и перехватываем его вывод
        try:
            # Временно разрешаем запись для вставки текста
            self.debug_text.configure(state="normal")
            
            process = subprocess.Popen(['python', 'hydra-language/main.py'], 
                                     stdout=subprocess.PIPE, 
                                     stderr=subprocess.PIPE,
                                     text=True)
            
            output, error = process.communicate()
            
            if output:
                self.debug_text.insert("end", output)
            if error:
                self.debug_text.insert("end", f"Ошибка:\n{error}")
                
            # Снова запрещаем запись
            self.debug_text.configure(state="disabled")
                
        except Exception as e:
            self.debug_text.insert("end", f"Ошибка запуска:\n{str(e)}")
            self.debug_text.configure(state="disabled")

        self.root.resizable(False, False)
        self.root.mainloop()

class TextRedirector:
    def __init__(self, widget, tag="stdout"):
        self.widget = widget
        self.tag = tag

    def write(self, str):
        self.widget.insert("end", str)
        self.widget.see("end")  # Автопрокрутка к концу

    def flush(self):
        pass