import tkinter as tk
from tkinter import messagebox
class CalculatorApp:
    def __init__(create, play):
        create.play = play
        create.play.title("Simple Calculator")
        create.expression = ""
        create.display = tk.Entry(create.play, width=35, borderwidth=5)
        create.display.grid(row=0, column=0, columnspan=4, padx=20, pady=20)
        buttons = [
            '1', '2', '3', '/',
            '4', '5', '6', '*',
            '7', '8', '9', '-',
            '.', '0', '=', '+'
        ]
        row_val = 1
        col_val = 0
        for button in buttons:
            tk.Button(create.play, text=button, padx=30, pady=30, command=lambda b=button: create.button_click(b)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1
        tk.Button(create.play, text="C", padx=30, pady=30, command=create.button_clear).grid(row=row_val, column=col_val)
    def button_click(create, button):
        if button == "=":
            try:
                result = str(eval(create.expression))
                create.display.delete(0, tk.END)
                create.display.insert(0, result)
                create.expression = result
            except:
                messagebox.showerror("Error", "Undefined value")
                create.display.delete(0, tk.END)
                create.expression = ""
        else:
            create.expression += str(button)
            create.display.delete(0, tk.END)
            create.display.insert(0, create.expression)
    def button_clear(create):
        create.expression = ""
        create.display.delete(0, tk.END)
if __name__ == "__main__":
    play = tk.Tk()
    app = CalculatorApp(play)
    play.mainloop()
