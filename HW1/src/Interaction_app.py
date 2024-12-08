import tkinter as tk
from tkinter import messagebox, scrolledtext


def find_intersection(sets):
    if not sets:
        return set()

    intersection = set()

    for element in sets[0]:
        found_in_all = True
        for s in sets[1:]:
            if element not in s:
                found_in_all = False
                break
        if found_in_all:
            intersection.add(element)

    return intersection


def process_input():
    input_data = input_text.get("1.0", tk.END).strip()  # Получаем текст из поля ввода
    lines = input_data.splitlines()  # Разделяем текст по строкам

    try:
        n = int(lines[0].strip())  # Первая строка - количество множеств
        sets = []

        for i in range(1, n + 1):
            current_set = set(map(int, lines[i].strip().split()))  # Преобразуем каждую строку в множество
            sets.append(current_set)

        intersection = find_intersection(sets)  # Находим пересечение множеств
        result_text.delete("1.0", tk.END)  # Очищаем текстовое поле результата
        result_text.insert(tk.END, str(sorted(intersection)))  # Выводим отсортированный результат

    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка при обработке входных данных: {str(e)}")


def on_control_v(event):
    event.widget.event_generate("<<Paste>>")  # Генерируем событие вставки


# Создание главного окна
root = tk.Tk()
root.title("Нахождение пересечения множеств")

# Поле для ввода
input_label = tk.Label(root, text="Введите множества (первое число - количество множеств):")
input_label.pack()

input_text = scrolledtext.ScrolledText(root, width=40, height=10)
input_text.pack()

# Устанавливаем обработчик для вставки текста на обеих раскладках
input_text.bind("<Control-v>", on_control_v)

# Кнопка для обработки ввода
process_button = tk.Button(root, text="Найти пересечение", command=process_input)
process_button.pack()

# Поле для вывода результата
result_label = tk.Label(root, text="Пересечение множеств:")
result_label.pack()

result_text = scrolledtext.ScrolledText(root, width=40, height=10)
result_text.pack()

# Запуск приложения
root.mainloop()