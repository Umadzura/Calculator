from typing import Callable


class ConversionToPostfix:

    def __init__(self):
        """Конструктор для инициализации переменных класса"""
        self.top = -1
        # Этот массив используется в стеке
        self.array = []
        # Настройка приоритета
        self.output = []
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def isEmpty(self) -> bool:
        """Проверяет, пуст ли стек"""
        return True if self.top == -1 else False

    def peek(self) -> int | str:
        """Возвращает значение вершины стека"""
        return self.array[-1]

    def pop(self) -> int | str:
        """Pop'ает элемент из стека"""
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"

    def push(self, op: str) -> None:
        """Помещает элемент в стек"""
        self.top += 1
        self.array.append(op)

    def isOperand(self, ch: str) -> bool:
        """Вспомогательная функция для проверки, что задан символ - операнд"""
        try:
            return str(abs(int(ch))).isdigit()
        except ValueError:
            return False

    def notGreater(self, i: int) -> bool:
        """Проверьте, строго ли приоритет оператора меньше вершины стека или нет."""
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return True if a <= b else False
        except KeyError:
            return False

    def infixToPostfix(self, exp: str) -> list:
        """Функция для перевода инфиксного выражения в постфиксное"""

        # Перебирает выражения для преобразования
        for i in exp.split():
            # Если символ является операндом, добавляет его в вывод
            if self.isOperand(i):
                self.output.append(i)

            # Если символ представляет собой '(', поместите его в стек
            elif i == '(':
                self.push(i)

            # Если отсканированный символ представляет собой ')',
            # извлекает его и выводит из стека до тех пор, пока не будет найден '('
            elif i == ')':
                while (not self.isEmpty()) and self.peek() != '(':
                    a = self.pop()
                    self.output.append(a)
                if not self.isEmpty() and self.peek() != '(':
                    return -1
                else:
                    self.pop()

            # Встречается оператор
            else:
                while not self.isEmpty() and self.notGreater(i):
                    self.output.append(self.pop())
                self.push(i)

        # Вытаскивает весь оператор из стека
        while not self.isEmpty():
            self.output.append(self.pop())

        # print("".join(self.output))
        return self.output


all_ops: dict[str, Callable[[list], int]] = {}


def binary_op(token: str):
    """Декоратор для бинарных операций"""
    def make_binop(func: Callable[[int, int], int]) -> Callable[[list], int]:
        def redef(stack: list) -> int:
            if len(stack) < 2:
                raise ValueError(f"Недостаточно операндов на стаке: len = {len(stack)}")

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


@binary_op('%')
def mod(a, b):
    return a % b


@binary_op('^')
def power(a, b):
    return a ** b


def execute_program(program: list) -> int:
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
