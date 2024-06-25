class Conversion:

    # Конструктор для инициализации переменных класса
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        # Этот массив используется в стеке
        self.array = []
        # Настройка приоритета
        self.output = []
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    # Проверяет, пуст ли стек
    def isEmpty(self):
        return True if self.top == -1 else False

    # Возвращает значение вершины стека
    def peek(self):
        return self.array[-1]

    # Pop'ает элемент из стека
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"

    # Помещает элемент в стек
    def push(self, op):
        self.top += 1
        self.array.append(op)

    # Вспомогательная функция для проверки, что задан символ - операнд
    def isOperand(self, ch):
        return ch.isdigit()

    # Проверьте, строго ли приоритет оператора меньше вершины стека или нет.
    def notGreater(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return True if a <= b else False
        except KeyError:
            return False

    # Основная функция, которая преобразует данное инфиксное выражение в постфиксное выражение.
    def infixToPostfix(self, exp):

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
        print(self.output)
