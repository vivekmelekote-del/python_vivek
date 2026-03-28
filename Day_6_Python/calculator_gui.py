#A AI generated calculator GUI using tkinter
import tkinter as tk
from tkinter import Entry, Button, Label

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        # Display
        self.display = Entry(root, font=('Arial', 24), justify='right', bd=10)
        self.display.grid(row=0, column=0, columnspan=4, sticky='nsew', padx=10, pady=10)
        
        self.output = 0
        self.first_num = 0
        self.operation = ""
        
        # Configure grid
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
        
        # Buttons layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('←', 5, 1), ('Exit', 5, 2),
        ]
        
        for (text, row, col) in buttons:
            self.create_button(text, row, col)
    
    def create_button(self, text, row, col):
        # Color coding for buttons
        if text in ['+', '-', '*', '/']:
            color = '#FF9500'  # Orange for operations
        elif text == '=':
            color = '#4CAF50'  # Green for equals
        elif text in ['C', '←', 'Exit']:
            color = '#f44336'  # Red for special
        else:
            color = '#2196F3'  # Blue for numbers
        
        btn = Button(self.root, text=text, font=('Arial', 18),
                    command=lambda: self.on_button_click(text),
                    bg=color, fg='white', activebackground='#0D47A1',
                    relief=tk.RAISED, bd=2)
        btn.grid(row=row, column=col, sticky='nsew', padx=5, pady=5)
    
    def on_button_click(self, char):
        if char == 'C':
            self.display.delete(0, tk.END)
            self.output = 0
            self.first_num = 0
            self.operation = ""
        
        elif char == '←':
            current = self.display.get()
            self.display.delete(0, tk.END)
            self.display.insert(0, current[:-1])
        
        elif char == 'Exit':
            self.root.quit()
        
        elif char in ['+', '-', '*', '/']:
            try:
                self.first_num = float(self.display.get() or 0)
                self.operation = char
                self.display.delete(0, tk.END)
            except ValueError:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        
        elif char == '=':
            try:
                second_num = float(self.display.get() or 0)
                
                if self.operation == '+':
                    self.output = self.first_num + second_num
                elif self.operation == '-':
                    self.output = self.first_num - second_num
                elif self.operation == '*':
                    self.output = self.first_num * second_num
                elif self.operation == '/':
                    if second_num == 0:
                        self.display.delete(0, tk.END)
                        self.display.insert(0, "Error: Div by 0")
                        return
                    self.output = self.first_num / second_num
                
                self.display.delete(0, tk.END)
                self.display.insert(0, str(self.output))
                self.operation = ""
            except ValueError:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        
        else:
            self.display.insert(tk.END, char)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
