# Программа, которая находит пересечение заданных n множеств


<h1>Алгоритм работы с кодом</h1>
<h2>0. Запуск программы</h2>
Для запуска программы необходимо запустить скрипт через редактор кода
<h2>1. Формат входных данных</h2>
На вход программе подаются следующие данные, которые необходимо записать в верхнем окне:

1. Количество исходных множеств (на отдельной строке)
2. Сами множества (каждое на отдельной строке), состоящие из целых чисел, разделенных пробелами


Пример ввода:

```
2
4 7 10 8
5 7 4 9 11
```
<h2>2. Запуск файла и вывод результата</h2>
Чтобы запустить скрипт нажмите на кнопку "Найти пересечение". 
Результат появится в нижнем окне.


Пример результата работы для приведенных выше данных:

```
[4, 7]
```

<h2>Примечание</h2>

1. Если множества не имеют пересечений, то на выходе получится пустой список ([])

2. Перед запуском скрипта проверьте входные данные на корректность и соответствие требуемому формату, иначе программа выведет ошибку

3. Для тестирования следующего набора данных измените данные в верхнем окне и запустите скрипт снова


# Нами был реализован алгоритм, позволяющий найти пересечение заданных n множеств, рассмотрим, что выполняется в строках кода

## [Написанная программа](https://github.com/Mihail-Bay/DiscMathHW1/blob/main/HW1/src/InteractionOfASet.py)



### Реализована функция _find_intersection(sets)_, отвечающая за нахождение пересечения множеств

```
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
```
1) Выполняется проверка, является ли список пустым, если является, то функция возвращает пустое множество

```
if not sets:
        return set()
```
2) Создается пустое множество **intersection** для хранения элементов, найденных во всех множествах

```
intersection = set()
```

3) Выполняется поиск пересечения, для каждого элемента проверяется, присутствует ли он во всех остальных множествах, если элемент найден во всех остальных множествах, то он добавляется в **intersection**

```
found_in_all = True

        for s in sets[1:]:
            if element not in s:
                found_in_all = False
                break

        if found_in_all:
            intersection.add(element)
```

4) Возвращается множество пересечения

```
return intersection
```

### Реализована функция _process_input()_, которая обрабатывает ввод пользователя
```
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
```
1) Считывается ввод пользователя

```
input_data = input_text.get("1.0", tk.END).strip()
```
2) Данные разделяются по строкам
```
lines = input_data.splitlines()
```
3) Извлекается количество множеств и каждая строка преобразуется в множество
```
try:
        n = int(lines[0].strip())  # Первая строка - количество множеств
        sets = []

        for i in range(1, n + 1):
            current_set = set(map(int, lines[i].strip().split()))  # Преобразуем каждую строку в множество
            sets.append(current_set)
```
4) Вызывается функция find_intersection для нахождения пересечения
```
intersection = find_intersection(sets) 
```
5) Выводится результат
```
 result_text.delete("1.0", tk.END)  # Очищаем текстовое поле результата
        result_text.insert(tk.END, str(sorted(intersection)))
```
6) Предусмотрен вывод ошибки при введении некорректных данных
```
except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка при обработке входных данных: {str(e)}")
```
### Реализована функция _on_control_v_,  позволяющая вставлять текст в текстовое поле при нажатии Ctrl+V
```
def on_control_v(event):
    event.widget.event_generate("<<Paste>>")  # Генерируем событие вставки

```
### Реализован графический интерфейс
Здесь создаются главное окно приложения с метками, текстовыми полями для ввода и вывода данных, а также кнопкой для запуска обработки ввода
```
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
```