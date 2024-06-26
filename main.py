"""Основная программа"""
from src.calculator.modules import *


def main():
    choice = None
    while choice != "4":
        print_options()
        choice = get_valid_choice()
        if choice == "1":
            func1()
        elif choice == "2":
            func2()
        elif choice == '3':
            func3()


if __name__ == '__main__':
    main()
