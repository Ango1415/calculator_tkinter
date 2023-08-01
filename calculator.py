# Author: 'Ángel F. Gomez'  | Email: 'angelfabge@gmail.com'  | Github-LinkedIn: '../ango1415'
"""
Exercise where I'm going to develop a calculator GUI using Tkinter
"""
import re
import math
import tkinter as tk
from tkinter import ttk, messagebox


class Calculator(tk.Tk):
    """
    Class to create an object calculator, who allow us to make math operations like addition, subtraction,
    multiplication and division. It's displayed in a GUI interface.
    """

    def __init__(self):
        """
        Constructor of the class
        """
        super().__init__()

        # We use regular expressions to operate the math syntax
        self._symbols_regex = re.compile('[+\-*/]')
        self._numbers_regex = re.compile('[0-9.]')

        # Define initial config
        self.geometry('500x600')
        self.title('Calculator')
        self.resizable(False, False)
        self.iconbitmap('calculator.ico')

        # Row-column configuration
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)

        # Variable related with the result panel
        self._result_var = tk.StringVar(value='Welcome')

        # Create the elements for the window
        self._create_elements()

    def _create_elements(self):
        """
        In this method we create all the elements that are going to be inside the window
        :return:
        """
        # Entry boxes (Result panel)
        result_panel = ttk.Entry(self, justify=tk.RIGHT, state='readonly', textvariable=self._result_var)
        result_panel.grid(row=0, column=0, columnspan=4, sticky='NSEW')

        # Buttons 1st row
        clear_button = ttk.Button(self, text='C', command=self._clear_result_panel)
        clear_button.grid(row=1, column=0, columnspan=3, sticky='NSEW')

        division_button = ttk.Button(self, text='/', command=lambda: self._add_string_to_result('/'))
        division_button.grid(row=1, column=3, sticky='NSEW')

        # Buttons 2nd row
        n7_button = ttk.Button(self, text='7', command=lambda: self._add_string_to_result('7'))
        n7_button.grid(row=2, column=0, sticky='NSEW')

        n8_button = ttk.Button(self, text='8', command=lambda: self._add_string_to_result('8'))
        n8_button.grid(row=2, column=1, sticky='NSEW')

        n9_button = ttk.Button(self, text='9', command=lambda: self._add_string_to_result('9'))
        n9_button.grid(row=2, column=2, sticky='NSEW')

        multiplication_button = ttk.Button(self, text='*', command=lambda: self._add_string_to_result('*'))
        multiplication_button.grid(row=2, column=3, sticky='NSEW')

        # Buttons 3rd row
        n4_button = ttk.Button(self, text='4', command=lambda: self._add_string_to_result('4'))
        n4_button.grid(row=3, column=0, sticky='NSEW')

        n5_button = ttk.Button(self, text='5', command=lambda: self._add_string_to_result('5'))
        n5_button.grid(row=3, column=1, sticky='NSEW')

        n6_button = ttk.Button(self, text='6', command=lambda: self._add_string_to_result('6'))
        n6_button.grid(row=3, column=2, sticky='NSEW')

        sustraction_button = ttk.Button(self, text='-', command=lambda: self._add_string_to_result('-'))
        sustraction_button.grid(row=3, column=3, sticky='NSEW')

        # Buttons 4th row
        n1_button = ttk.Button(self, text='1', command=lambda: self._add_string_to_result('1'))
        n1_button.grid(row=4, column=0, sticky='NSEW')

        n2_button = ttk.Button(self, text='2', command=lambda: self._add_string_to_result('2'))
        n2_button.grid(row=4, column=1, sticky='NSEW')

        n3_button = ttk.Button(self, text='3', command=lambda: self._add_string_to_result('3'))
        n3_button.grid(row=4, column=2, sticky='NSEW')

        addition_button = ttk.Button(self, text='+', command=lambda: self._add_string_to_result('+'))
        addition_button.grid(row=4, column=3, sticky='NSEW')

        # Buttons 5th row
        n0_button = ttk.Button(self, text='0', command=lambda: self._add_string_to_result('0'))
        n0_button.grid(row=5, column=0, columnspan=2, sticky='NSEW')

        point_button = ttk.Button(self, text='.', command=lambda: self._add_string_to_result('.'))
        point_button.grid(row=5, column=2, sticky='NSEW')

        equal_button = ttk.Button(self, text='=', command=self._calculate)
        equal_button.grid(row=5, column=3, sticky='NSEW')

    def _clear_result_panel(self):
        """
        This method sets the value of the result panel to 0
        :return:
        """
        self._result_var.set('0')

    def _add_string_to_result(self, value: str):
        """
        This method concatenates the string values of the syntax to be operated
        :param value: the new part of the operation
        :return:
        """
        if (self._result_var.get() == 'Welcome') or (self._result_var.get() == '0' and value != '.'):
            self._result_var.set(value)
        else:
            new_val = self._result_var.get() + value
            self._result_var.set(new_val)

    def _calculate(self):
        """
        This method make the operation defined by the user
        :return:
        """
        try:
            operation = self._result_var.get()
            print(f'Operation: {operation}')
            symbols = self._symbols_regex.findall(operation)
            print(f'Symbols: {symbols}')
            numbers = []

            # This separates the symbols and the numbers from the expression
            while True:
                symbol_index = self._symbols_regex.search(operation)
                if symbol_index:
                    symbol_index = symbol_index.start()
                    numbers.append(operation[:symbol_index])
                    operation = operation[symbol_index + 1:]
                else:
                    numbers.append(operation)
                    break
            print(f'Numbers:{numbers}')

            """
            Make the operation.
            - If we don't have symbols that means that is just a number, so we don´t have to operate any value
            - We prevent syntax errors like starting the string with a symbol (operator) and having more symbols than 
              numbers
            """
            if symbols:
                if self._numbers_regex.match(numbers[0]):
                    total = float(numbers[0])
                else:
                    raise Exception(f'Incorrect operation syntax in "{self._result_var.get()}"')

                for i in range(len(symbols)):
                    if self._numbers_regex.match(numbers[i + 1]):
                        if symbols[i] == '+':
                            total += float(numbers[i + 1])
                        elif symbols[i] == '-':
                            total -= float(numbers[i + 1])
                        elif symbols[i] == '*':
                            total *= float(numbers[i + 1])
                        elif symbols[i] == '/':
                            total /= float(numbers[i + 1])
                    else:
                        raise Exception(f'Incorrect operation syntax in "{self._result_var.get()}"')
                if total - math.trunc(total) == 0:
                    self._result_var.set(str(int(total)))
                else:
                    self._result_var.set(str(total))

        except Exception as e:
            messagebox.showerror('Error', f'{e}')
            self._clear_result_panel()


if __name__ == '__main__':
    calculator = Calculator()
    calculator.mainloop()
