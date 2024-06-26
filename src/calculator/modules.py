from typing import Callable


class Conversion:

    def __init__(self):
        """Конструктор для инициализации переменных класса"""
        self.top = -1
        # Этот массив используется в стеке
        self.array = []
        # Настройка приоритета
        self.output = []
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def is_empty(self) -> bool:
        """Проверяет, пуст ли стек"""
        return True if self.top == -1 else False

    def peek(self) -> int | str:
        """Возвращает значение вершины стека"""
        return self.array[-1]

    def pop(self) -> int | str:
        """Pop'ает элемент из стека"""
        if not self.is_empty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"

    def push(self, op: str) -> None:
        """Помещает элемент в стек"""
        self.top += 1
        self.array.append(op)

    def is_operand(self, ch: str) -> bool:
        """Вспомогательная функция для проверки, что задан символ - операнд"""
        try:
            return str(abs(int(ch))).isdigit()
        except ValueError:
            return False

    def not_greater(self, i: int) -> bool:
        """Проверьте, строго ли приоритет оператора меньше вершины стека или нет."""
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return True if a <= b else False
        except KeyError:
            return False

    def infix_to_postfix(self, exp: str) -> list:
        """Функция для перевода инфиксного выражения в постфиксное"""

        # Перебирает выражения для преобразования
        for i in exp.split():
            # Если символ является операндом, добавляет его в вывод
            if self.is_operand(i):
                self.output.append(i)

            # Если символ представляет собой '(', поместите его в стек
            elif i == '(':
                self.push(i)

            # Если отсканированный символ представляет собой ')',
            # извлекает его и выводит из стека до тех пор, пока не будет найден '('
            elif i == ')':
                while (not self.is_empty()) and self.peek() != '(':
                    a = self.pop()
                    self.output.append(a)
                if not self.is_empty() and self.peek() != '(':
                    return -1
                else:
                    self.pop()

            # Встречается оператор
            else:
                while not self.is_empty() and self.not_greater(i):
                    self.output.append(self.pop())
                self.push(i)

        # Вытаскивает весь оператор из стека
        while not self.is_empty():
            self.output.append(self.pop())

        # print("".join(self.output))
        return self.output


all_ops: dict[str, Callable[[list], int]] = {}


def binary_op(token: str):
    """Декоратор для бинарных операций"""

    def make_binop(func: Callable[[int, int], int]) -> Callable[[list], int]:
        def redef(stack: list) -> int:
            if len(stack) < 2:
                raise ValueError(f"Недостаточно операндов на стеке: len = {len(stack)}")

            b = stack.pop()
            a = stack.pop()
            result = func(a, b)

            stack.append(result)

            return result

        all_ops[token] = redef
        return redef

    return make_binop


@binary_op('+')
def add(a, b):
    return a + b


@binary_op('-')
def sub(a, b):
    return a - b


@binary_op('*')
def mul(a, b):
    return a * b


@binary_op('/')
def div(a, b):
    return a // b


@binary_op('^')
def power(a, b):
    return a ** b


def calculate_postfix(program: list) -> int:
    stack = []
    for token in program:
        operation = all_ops.get(token, None)
        if operation is not None:

            operation(stack)
        else:
            try:
                stack.append(int(token))
            except ValueError:
                raise ValueError(f"{token!r} - неизвестная операция или не целое число")

    if len(stack) != 1:
        raise ValueError(f"Ошибка! К концу вычислений на стеке осталось не одно число: {stack}")

    return stack.pop()


def print_options() -> None:
    print('1. Перевод в постфиксную форму.')
    print('2. Посчитать постфиксное выражение.')
    print('3. Посчитать инфиксное выражение.')
    print('4. Выход.')


def get_valid_choice():
    choice = input("Ваш выбор: ").strip()
    while choice not in ["1", "2", "3", "4"]:
        choice = input("Выберите легальное действие (1-4): ").strip()
    print()
    return choice


def convert_to_postfix(exp: str) -> list:
    obj = Conversion()
    postfix = obj.infix_to_postfix(exp)
    return postfix


def get_valid_extension(func):
    def wrapper():
        choice = True
        while choice:
            try:
                exp = input("Введите выражение: ")
                func(exp)
                print()
                choice = False
            except ValueError:
                print("Проверьте корректность ввода")
                print()

    return wrapper


@get_valid_extension
def func1(exp):
    postfix = convert_to_postfix(exp)
    calculate_postfix(postfix)
    print(' '.join(postfix))


@get_valid_extension
def func2(exp):
    result = calculate_postfix(exp.split())
    print(result)


@get_valid_extension
def func3(exp):
    postfix = convert_to_postfix(exp)
    result = calculate_postfix(postfix)
    print(result)
