import tkinter as tk  
from tkinter import ttk  
  
from src.LogicJudge import *  
# 假设这是你的自定义函数  

  
def on_button_click():  
    input_text = entry.get()  
    logstr = Logic2algbra(input_text)
    res = BooleReduce(Boolstr2symstr(logstr))
    flag = "False"
    if (res == "1"):
        flag = "True"
    output_label1.config(text= logstr)  
    output_label2.config(text=flag)
# 创建主窗口  
root = tk.Tk()  
root.title("Logical judgment")  
  
# 创建提示标签  
prompt_label1 = ttk.Label(root, text="Please enter a logical expression containing only &, |, ~, (), -->:", font=('Arial', 12))  
prompt_label1.grid(row=0, column=0, padx=10, pady=5)  
  
# 创建输入框  
entry = ttk.Entry(root, width=30, font=('Arial', 14))  
entry.grid(row=1, column=0, padx=10, pady=5)  
  
# 创建按钮  
button = ttk.Button(root, text="Click", command=on_button_click)  
button.grid(row=1, column=1, padx=10, pady=5)  
  

# 创建输出标签  
prompt_label2 = ttk.Label(root, text="The input logical expression is converted into a Boolean expression as:", font=('Arial', 12))  
prompt_label2.grid(row=2, column=0, padx=10, pady=5)  

output_label1 = ttk.Label(root, text="", font=('Arial', 14))  
output_label1.grid(row=3, column=0, columnspan=2, padx=10, pady=5)  
  
prompt_label3 = ttk.Label(root, text="The result of the judgment is: ", font=('Arial', 12))  
prompt_label3.grid(row=4, column=0, padx=10, pady=5)    
output_label2 = ttk.Label(root, text="", font=('Arial', 14))  
output_label2.grid(row=5, column=0, columnspan=2, padx=10, pady=5)  
  
# 运行界面  
root.mainloop()  