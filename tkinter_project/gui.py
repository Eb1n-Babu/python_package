import tkinter as tk

def calculator():
    try:
        num1 = float(operand1_var.get())
        num2 = float(operand2_var.get())
        op = operator_var.get()

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            result = num1 / num2
        else:
            result = "Invalid operator"

        result_var.set(str(result))
    except Exception as error:
        print(error)


root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)

operand1_var = tk.StringVar()
operand2_var = tk.StringVar()
operator_var = tk.StringVar()
result_var = tk.StringVar()


tk.Label(root, text="Operand 1").pack()
tk.Entry(root, textvariable=operand1_var).pack()

tk.Label(root, text="Operator (+, -, *, /)").pack()
tk.Entry(root, textvariable=operator_var).pack()

tk.Label(root, text="Operand 2").pack()
tk.Entry(root, textvariable=operand2_var).pack()

tk.Button(root, text="Calculate", command=calculator).pack(pady=10)
tk.Label(root, text="Result").pack()
tk.Entry(root, textvariable=result_var, state='readonly').pack()



root.mainloop()
