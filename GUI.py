import tkinter as tk


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.create_ui()

    def create_ui(self):
        # Entry widget to show current input
        self.entry = tk.Entry(self.root, font=('Arial', 24), justify=tk.RIGHT)
        self.entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

        # Button labels
        buttons = [
            ['C', '(', ')', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=', '+']
        ]

        # Create the buttons and add to grid
        for i, row in enumerate(buttons):
            for j, button_text in enumerate(row):
                button = tk.Button(self.root, text=button_text, font=('Arial', 20),
                                   command=lambda bt=button_text: self.on_button_click(bt))
                button.grid(row=i + 1, column=j, sticky="nsew")

        # Configure rows and columns to have equal weight
        for i in range(5):
            self.root.grid_rowconfigure(i, weight=1)
            for j in range(4):
                self.root.grid_columnconfigure(j, weight=1)

    def on_button_click(self, char):
        current_text = self.entry.get()

        if char == 'C':  # Clear the entry
            self.entry.delete(0, tk.END)
        elif char == '=':  # Evaluate the expression
            try:
                result = eval(current_text)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        else:  # Add the character to the entry
            self.entry.insert(tk.END, char)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("iPhone-style Calculator")
    app = CalculatorApp(root)
    root.mainloop()
