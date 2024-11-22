import tkinter as tk
import math

def button_click(value):
    current = display.get()
    if current == "0" and value != ".":
        display.set(value)  
    else:
        display.set(current + str(value))

def clear():
    display.set("")

def calculate():
    try:
        result = eval(display.get())

        if isinstance(result, float):
            if result.is_integer(): 
                result = int(result) 
            else:
                result = round(result, 10)  

        display.set(result)
    except ZeroDivisionError:
        display.set("خطأ: قسمة على صفر")
    except Exception as e:
        display.set("خطأ")

def square_root():
    try:
        value = float(display.get())
        result = math.sqrt(value)
        display.set(result)
    except ValueError:
        display.set("خطأ")

def cube_root():
    try:
        value = float(display.get())
        result = value ** (1/3)
        display.set(result)
    except ValueError:
        display.set("خطأ")

def power():
    try:
        value = float(display.get())
        display.set("")  
        root.after(200, lambda: display.set(f"{value} ^"))
    except ValueError:
        display.set("خطأ")

def log():
    try:
        value = float(display.get())
        if value <= 0:
            display.set("خطأ: القيمة يجب أن تكون أكبر من الصفر")
        else:
            result = math.log(value)
            display.set(result)
    except ValueError:
        display.set("خطأ")

def log10():
    try:
        value = float(display.get())
        if value <= 0:
            display.set("خطأ: القيمة يجب أن تكون أكبر من الصفر")
        else:
            result = math.log10(value)
            display.set(result)
    except ValueError:
        display.set("خطأ")

def sin_func():
    try:
        value = float(display.get())
        result = math.sin(math.radians(value)) 
        display.set(result)
    except ValueError:
        display.set("خطأ")

def cos_func():
    try:
        value = float(display.get())
        result = math.cos(math.radians(value))  
        display.set(result)
    except ValueError:
        display.set("خطأ")

def tan_func():
    try:
        value = float(display.get())
        result = math.tan(math.radians(value))  
        display.set(result)
    except ValueError:
        display.set("خطأ")

def asin_func():
    try:
        value = float(display.get())
        result = math.degrees(math.asin(value)) 
        display.set(result)
    except ValueError:
        display.set("خطأ")

def acos_func():
    try:
        value = float(display.get())
        result = math.degrees(math.acos(value))  
        display.set(result)
    except ValueError:
        display.set("خطأ")

def atan_func():
    try:
        value = float(display.get())
        result = math.degrees(math.atan(value))  
        display.set(result)
    except ValueError:
        display.set("خطأ")

root = tk.Tk()
root.title("الآلة الحاسبة المتقدمة")
root.geometry("600x700") 

display = tk.StringVar()

entry = tk.Entry(root, textvariable=display, font=("Arial", 20), bd=10, relief="sunken", justify="right")
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('√', 1, 4),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('^', 2, 4),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('C', 3, 4),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3), ('³√', 4, 4),
    ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('log', 5, 3), ('ln', 5, 4),
    ('asin', 6, 0), ('acos', 6, 1), ('atan', 6, 2), ('log10', 6, 3)
]

for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, font=("Arial", 20), command=calculate, bg="#4CAF50", fg="white")
    elif text == 'C':
        button = tk.Button(root, text=text, font=("Arial", 20), command=clear, bg="#f44336", fg="white")
    elif text == '√':
        button = tk.Button(root, text=text, font=("Arial", 20), command=square_root, bg="#2196F3", fg="white")
    elif text == '³√':
        button = tk.Button(root, text=text, font=("Arial", 20), command=cube_root, bg="#2196F3", fg="white")
    elif text == '^':
        button = tk.Button(root, text=text, font=("Arial", 20), command=power, bg="#FF9800", fg="white")
    elif text == 'sin':
        button = tk.Button(root, text=text, font=("Arial", 20), command=sin_func, bg="#4CAF50", fg="white")
    elif text == 'cos':
        button = tk.Button(root, text=text, font=("Arial", 20), command=cos_func, bg="#4CAF50", fg="white")
    elif text == 'tan':
        button = tk.Button(root, text=text, font=("Arial", 20), command=tan_func, bg="#4CAF50", fg="white")
    elif text == 'log':
        button = tk.Button(root, text=text, font=("Arial", 20), command=log, bg="#FF9800", fg="white")
    elif text == 'ln':
        button = tk.Button(root, text=text, font=("Arial", 20), command=log10, bg="#FF9800", fg="white")
    elif text == 'asin':
        button = tk.Button(root, text=text, font=("Arial", 20), command=asin_func, bg="#FF9800", fg="white")
    elif text == 'acos':
        button = tk.Button(root, text=text, font=("Arial", 20), command=acos_func, bg="#FF9800", fg="white")
    elif text == 'atan':
        button = tk.Button(root, text=text, font=("Arial", 20), command=atan_func, bg="#FF9800", fg="white")
    else:
        button = tk.Button(root, text=text, font=("Arial", 20), command=lambda value=text: button_click(value))
    
    button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

for r in range(1, 7):
    root.grid_rowconfigure(r, weight=1)
for c in range(5):
    root.grid_columnconfigure(c, weight=1)

root.mainloop()