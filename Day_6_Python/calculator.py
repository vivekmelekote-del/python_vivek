import tkinter as tk
from tkinter import Entry, Button, Label

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x300")
        
        # Display
        self.display = Entry(root, font=('Arial', 20), justify='right')
        self.display.grid(row=0, column=0, columnspan=4, sticky='nsew', padx=10, pady=10)
        
        self.output = 0
        self.first_num = 0
        self.operation = ""
        
        # Buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0),
        ]
        
        for (text, row, col) in buttons:
            self.create_button(text, row, col)
    
    def create_button(self, text, row, col):
        btn = Button(self.root, text=text, font=('Arial', 18),
                    command=lambda: self.on_button_click(text))
        btn.grid(row=row, column=col, sticky='nsew', padx=5, pady=5)
    
    def on_button_click(self, char):
        if char == 'C':
            self.display.delete(0, tk.END)
            self.output = 0
            self.first_num = 0
            self.operation = ""
        elif char in ['+', '-', '*', '/']:
            self.first_num = float(self.display.get() or 0)
            self.operation = char
            self.display.delete(0, tk.END)
        elif char == '=':
            second_num = float(self.display.get() or 0)
            if self.operation == '+':
                self.output = self.first_num + second_num
            elif self.operation == '-':
                self.output = self.first_num - second_num
            elif self.operation == '*':
                self.output = self.first_num * second_num
            elif self.operation == '/':
                self.output = self.first_num / second_num
            self.display.delete(0, tk.END)
            self.display.insert(0, str(self.output))
        else:
            self.display.insert(tk.END, char)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()