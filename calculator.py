import tkinter as tk

button_values = [
    ["AC", "+/-", "%", "÷"], 
    ["7", "8", "9", "×"], 
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols = ["÷", "×", "-", "+", "=", "√"]
top_symbols = ["AC", "+/-", "%"]

row_count=len(button_values)
column_count=len(button_values[0]) 

colour_light_grey ="#D3D3D3"
colour_black = "#000000"
colour_dark_grey="#505050"
colour_orange="#FF9500"
colour_white="white"

window= tk.Tk()
window.title("Calculator")

frame = tk.Frame(window)
label=tk.Label(frame,text="0", font=("Arial",45),background=colour_black,
               foreground=colour_white,anchor="e", width=column_count)
label.grid(row=0,column=0, columnspan=column_count, sticky="we")

for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        button = tk.Button(frame,text=value, font=("Arial", 30),
                           width = column_count-1, height=1,
                           command=lambda value=value: button_clicked(value))
        if value in top_symbols:
            button.config(foreground=colour_black, background=colour_light_grey)
        elif value in right_symbols:
            button.config(foreground=colour_white, background=colour_orange)
        else:
            button.config(foreground=colour_white, background=colour_dark_grey)
        button.grid(row=row+1,column=column)
        

frame.pack()

a= "0"
operator=None
b=None

def clear_all():
    global a,b, operator
    a= "0"
    operator=None
    b=None

def remove_zero_decimal(num):
    if num %1 ==0:
        num=int(num)
    return str(num)

def button_clicked(value): 
    global right_symbols,top_symbols,label,a,b,operator
    
    if value in right_symbols:
        if value =="=":
            if a  is not None and operator is not None:
                b = label['text']
                numa = float(a)
                numb=float(b)
                
                if operator =="+":
                    label['text'] = remove_zero_decimal(numa+numb)
                elif operator =="-":
                    label['text'] = remove_zero_decimal(numa-numb)
                elif operator =="×":
                    label['text'] = remove_zero_decimal(numa*numb)
                elif operator =="÷":
                    label['text'] = remove_zero_decimal(numa/numb)
                
        elif value == "√":  
                numA = float(label["text"])
                if numA >= 0:
                    label["text"] = remove_zero_decimal(numA ** 0.5)
                else:
                    label["text"]= "Error"
            
        elif value in "+-×÷":
            if operator is None:
                a= label['text']
                label['text']='0'
                b='0'
            operator =value
    
    elif value in top_symbols:
        if value =="AC":
            clear_all()
            label['text']='0'
        elif value =="+/-":
            result = float(label['text'])*-1
            label['text']= remove_zero_decimal(result)
        elif value =="%":
            result = float(label['text'])/100
            label['text']= remove_zero_decimal(result)
    else:
        if value ==".": 
            if value not in label['text']:
                label['text']+= value
        elif value in "0123456789":
            if label["text"] =="0":
                label["text"] =value 
            else: 
                 label['text'] += value

window.update()
window_width=window.winfo_width()
window_height= window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height=window.winfo_screenheight()

window_x= int((screen_width/2)-(window_width/2))
window_y= int((screen_height/2)-(window_height/2))
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()