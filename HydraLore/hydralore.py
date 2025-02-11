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

        # Создаем фрейм для текстового поля и номеров строк
        self.text_frame = ctk.CTkFrame(self)
        self.text_frame.pack(expand=True, fill='both')

        # Создание поля для номеров строк
        self.line_numbers = ctk.CTkTextbox(self.text_frame, width=25, font=("Arial", 15))
        self.line_numbers.pack(side='left', fill='y')
        self.line_numbers.configure(state='disabled')  # Запрещаем редактирование

        # Создаем сепаратор
        self.separator = ctk.CTkFrame(self.text_frame, width=0.5)  # Уменьшили толщину с 1 до 0.5
        self.separator.pack(side='left', fill='y', padx=2)

        # Создание текстового поля
        self.text_area = ctk.CTkTextbox(self.text_frame, font=("Arial", 15))
        self.text_area.pack(side='left', expand=True, fill='both')

        # Добавляем биндинги для автозакрытия скобок и кавычек
        self.text_area.bind('{', self.auto_close_curly)
        self.text_area.bind('(', self.auto_close_round)
        self.text_area.bind('"', self.auto_close_double_quote)
        self.text_area.bind("'", self.auto_close_single_quote)

        # Добавляем биндинг для обновления номеров строк
        self.text_area.bind('<Key>', self.update_line_numbers)
        self.text_area.bind('<MouseWheel>', self.sync_scroll)
        self.line_numbers.bind('<MouseWheel>', self.sync_scroll)

        # Добавляем биндинг для Enter
        self.text_area.bind('<Return>', self.handle_enter)

        # Создание стандартного меню
        self.menu = Menu(self, tearoff=0)
        self.config(menu=self.menu)
        
        # Меню "Файл"
        self.proj_menu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Файл", menu=self.proj_menu)
        self.proj_menu.add_command(label="Создать файл", command=self.create_file)
        self.proj_menu.add_command(label="Открыть файл", command=self.open_file)
        self.proj_menu.add_separator()
        self.proj_menu.add_command(label="Открыть папку", command=self.open_folder)
        self.proj_menu.add_separator()
        self.proj_menu.add_command(label="Запустить", command=self.run)

        # Меню "Справка"
        self.help_menu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Справка", menu=self.help_menu)
        self.help_menu.add_command(label="О программе", command=self.show_about)
        self.help_menu.add_separator()
        self.help_menu.add_command(label="Документация по Hydra", command=self.doc_hydra)
        self.help_menu.add_command(label="Документация по HydraLore", command=self.doc_hydralore)

    def show_about(self):
        messagebox.showinfo("О программе", "HydraLore - редактор кода для языка программирования Hydra\nВерсия: \n(by Disvord, на основе SKINT IDE by PRoX)")
    
    def doc_hydra(self):
        webbrowser.open("https://github.com/Kross1de/Hydra---The-programming-language")

    def doc_hydralore(self):
        webbrowser.open("https://github.com/Disvord-projects/Hydralore-IDE")

    def run(self):
        """Метод для запуска проекта"""
        source_code = self.text_area.get("1.0", "end-1c")
        
        # Записываем код во временный файл
        with open("temp_code.hy", "w", encoding='utf-8') as f:
            f.write(source_code)
        
        debug_window = debug.Debug()  # Создаем окно отладки

    def create_file(self):
        """Метод для создания нового файла"""
        pass

    def open_file(self):
        """Метод для открытия файла"""
        pass

    def open_folder(self):
        """Метод для открытия папки"""
        pass

    def auto_close_curly(self, event):
        """Метод для автоматического закрытия фигурных скобок с форматированием"""
        self.text_area.insert("insert", "{\n")
        current_line = int(self.text_area.index("insert").split('.')[0])
        self.text_area.insert("insert", "    \n}")
        self.text_area.mark_set("insert", f"{current_line}.4")
        return "break"

    def auto_close_round(self, event):
        """Метод для автоматического закрытия круглых скобок"""
        self.text_area.insert("insert", "()")
        self.text_area.mark_set("insert", "insert-1c")
        return "break"

    def auto_close_double_quote(self, event):
        """Метод для автоматического закрытия двойных кавычек"""
        self.text_area.insert("insert", '""')
        self.text_area.mark_set("insert", "insert-1c")
        return "break"

    def auto_close_single_quote(self, event):
        """Метод для автоматического закрытия одинарных кавычек"""
        self.text_area.insert("insert", "''")
        self.text_area.mark_set("insert", "insert-1c")
        return "break"

    def update_line_numbers(self, event=None):
        """Обновление номеров строк"""
        # Получаем количество строк
        lines = self.text_area.get('1.0', 'end-1c').count('\n') + 1
        
        # Получаем текущий текст номеров строк
        line_numbers_text = '\n'.join(str(i) for i in range(1, lines + 1))
        
        # Обновляем номера строк
        self.line_numbers.configure(state='normal')
        self.line_numbers.delete('1.0', 'end')
        self.line_numbers.insert('1.0', line_numbers_text)
        self.line_numbers.configure(state='disabled')

        # Синхронизируем прокрутку
        self.line_numbers.yview_moveto(self.text_area.yview()[0])

    def sync_scroll(self, event=None):
        """Синхронизация прокрутки между текстовым полем и номерами строк"""
        self.line_numbers.yview_moveto(self.text_area.yview()[0])
        return 'break'

    def handle_enter(self, event):
        """Обработка нажатия Enter с учетом контекста"""
        # Получаем текущую позицию курсора
        cursor_pos = self.text_area.index("insert")
        line_num = int(cursor_pos.split('.')[0])
        
        # Получаем текущую строку до курсора
        current_line = self.text_area.get(f"{line_num}.0", "insert")
        
        # Проверяем последний символ перед курсором
        if current_line.strip().endswith('{'):
            # Если перед курсором {, добавляем отступ и переносим }
            next_line = self.text_area.get("insert", f"{line_num}.end")
            if '}' in next_line:
                self.text_area.delete("insert", f"{line_num}.end")
                self.text_area.insert("insert", "\n    \n}")
                self.text_area.mark_set("insert", f"{line_num + 1}.4")
                return "break"
            
            # В остальных случаях просто добавляем перенос строки с отступом
            self.text_area.insert("insert", "\n    ")
            return "break"
        
        # Проверяем, находимся ли мы внутри блока
        prev_text = self.text_area.get("1.0", "insert")
        if prev_text.count('{') > prev_text.count('}'):
            self.text_area.insert("insert", "\n    ")
            return "break"
        
        # В остальных случаях просто добавляем перенос строки
        self.text_area.insert("insert", "\n")
        return "break"

if __name__ == "__main__":
    app = TextEditor()
    app.mainloop()