"""
Этот код создает приложение с секундомером и четырьмя кнопками управления (старт, стоп, продолжить, сброс)
"""
from tkinter import *
from datetime import datetime

temp = 0  # Переменная для хранения времени (в секундах)
after_id = ''  # Идентификатор для метода after()


# Функция для обновления времени в Label
def tick():
    global temp, after_id
    after_id = root.after(1000, tick)
    f_temp = datetime.fromtimestamp(temp).strftime('%M:%S')
    label1.configure(text=str(f_temp))
    temp += 1


# Функция для старта таймера
def start_tick():
    start_button.pack_forget()
    stop_button.pack()
    tick()


# Функция для остановки таймера
def stop_tick():
    stop_button.pack_forget()
    continue_button.pack()
    reset_button.pack()
    root.after_cancel(after_id)


# Функция для продолжения работы таймера
def continue_tick():
    continue_button.pack_forget()
    reset_button.pack_forget()
    stop_button.pack()
    tick()


# Функция для сброса таймера
def reset_tick():
    global temp
    temp = 0
    label1.configure(text='00:00')

    continue_button.pack_forget()
    reset_button.pack_forget()
    start_button.pack()


# Функция для преобразования RGB в шестнадцатеричный код цвета
def rgb_to_hex(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'


# Создание окна приложения
root = Tk()
root.title('Секундомер')
root.resizable(width=False, height=False)
root.configure(background='black')
# Установка положения окна по центру экрана
root.geometry(f'250x200+{(root.winfo_screenwidth() - 250) // 2}+{(root.winfo_screenheight() - 200) // 2}')

# Создание и настройка Label для отображения времени
label1 = Label(root, width=10, font=('Ubuntu', 30), text='00:00', fg=rgb_to_hex(17, 209, 23))
label1.configure(background='black')  # Установка черного фона метки
label1.pack()

# Создание и настройка кнопок с функционалом для управления таймером
start_button = Button(root, text='Старт', font=('Ubuntu', 30), width=15, command=start_tick, fg=rgb_to_hex(17, 209, 23))
start_button.configure(background='black')
stop_button = Button(root, text='Стоп', font=('Ubuntu', 30), width=15, command=stop_tick, fg=rgb_to_hex(17, 209, 23))
stop_button.configure(background='black')
continue_button = Button(root, text='Продолжить', font=('Ubuntu', 30), width=15, command=continue_tick,
                         fg=rgb_to_hex(17, 209, 23))
continue_button.configure(background='black')
reset_button = Button(root, text='Сброс', font=('Ubuntu', 30), width=15, command=reset_tick, fg=rgb_to_hex(17, 209, 23))
reset_button.configure(background='black')
start_button.pack()

# Запуск основного цикла приложения
root.mainloop()
