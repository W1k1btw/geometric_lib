import circle  # Импортируем модуль circle, содержащий функции для работы с окружностями
import square  # Импортируем модуль square, содержащий функции для работы с квадратами

# Список доступных фигур
figs = ['circle', 'square']
# Список доступных функций
funcs = ['perimeter', 'area']
# Словарь для хранения размеров фигур и соответствующего количества аргументов
sizes = {}

# Функция для вычисления периметра или площади фигуры
def calc(fig, func, size):
    assert fig in figs  # Проверяем, что фигура допустима
    assert func in funcs  # Проверяем, что функция допустима

    # Вычисляем результат, вызывая соответствующую функцию из модуля фигуры
    result = eval(f'{fig}.{func}(*{size})')
    # Печатаем результат вычисления
    print(f'{func} of {fig} is {result}')

# Основной блок программы
if __name__ == "__main__":
    func = ''  # Инициализация переменной для функции
    fig = ''   # Инициализация переменной для фигуры
    size = list()  # Инициализация списка для размеров
    
    # Цикл для ввода допустимой фигуры
    while fig not in figs:
        fig = input(f"Enter figure name, avaliable are {figs}:\n")  # Запрашиваем у пользователя фигуру
    
    # Цикл для ввода допустимой функции
    while func not in funcs:
        func = input(f"Enter function name, avaliable are {funcs}:\n")  # Запрашиваем у пользователя функцию
    
    # Цикл для ввода размеров фигуры
    while len(size) != sizes.get(f"{func}-{fig}", 1):
        # Запрашиваем размеры, разделенные пробелами
        size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
    
    # Вызываем функцию calc с введенными параметрами
    calc(fig, func, size)
