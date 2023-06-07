from tkinter import *
import math
#기호 함수
def operator(digit):
     value = entry_val.get()
     operList = ['%','/','*','+','-']
     flag = 0
     if len(value) == 0:
               pass
     else :
           for i in operList:
                 if value[-1] == i:
                    flag = 1
     
     if flag == 1 : 
          input_entry.delete((len(input_entry.get())-1))
          input_entry.insert(END,digit)
     else :
          input_entry.insert(END,digit)


#양,음수 변환
def plus_min():
     result = eval(input_entry.get())
     input_result = result * -1
     input_entry.delete(0,END)
     input_entry.insert(END,input_result)

      
 #숫자함수               
def click(digit):  
          if digit == 'CE':
               input_entry.delete(0,END)
          elif digit == 'C':
               input_entry.delete(0,END)
               result_label.config(text = '')
          else:
               input_entry.insert(END,digit)
     

#  = 입력시 라벨로 식 올리고 엔트리에 결과값 표시
def result():
     try :
          my_result = eval(input_entry.get())
     except :
           result_label.config(text = "Error")
     else :
          if my_result % 1 == 0 :
               my_result = math.trunc(my_result)
          text_result = input_entry.get()
          input_entry.delete(0,END)
          result_label.config(text = text_result + ' =')
          input_entry.insert(END,my_result)

 #백스페이스 입력
def press_backspace(BackSpace):
     input_entry.delete(END)

#엔터키 입력
def press_enter(Return):
     try :
          my_result = eval(input_entry.get())
     except :
           result_label.config(text = "Error")
     else :
          if my_result % 1 == 0 :
               my_result = math.trunc(my_result)
          text_result = input_entry.get()
          input_entry.delete(0,END)
          result_label.config(text = text_result + ' =')
          input_entry.insert(END,my_result)

#종료함수
def press_Esc(Escape):
     win.destroy()
     
dark_gray = '#696969'
light_gray = '#A9A9A9'


win = Tk()
win.title("Yongs Calcurator")
win.resizable(False,False)
win.config(padx = 10 , pady = 10 ,bg = 'black')

entry_val = StringVar()

input_entry = Entry(win, textvariable = entry_val, width=30, font=(None,20,'bold')
                    ,bg = 'black',fg='white',justify=RIGHT,borderwidth=10,relief='sunken')
input_entry.grid(column = 0,row= 1, columnspan=4)
input_entry.focus()

result_label = Label(win, text = '',width=38,bg = 'black',fg = 'gray',font = (None,15,'bold'),anchor='e')
result_label.grid(column=0, row = 0, columnspan= 8, pady = 5 )

digits = [
['7','8','9'],
['4','5','6'],
['1','2','3'],
]
for r in range(3):
    for c in range(3):
        digit = digits[r][c]
        button = Button(win, text = digit, width = 8 , font = (None,15,'bold'),bg='black',fg = 'white',
                        command = lambda x = digit : click(x))
        button.grid(row = r +3, column= c,pady = 2)


button = Button(win, text = '%', width= 8,font=(None ,15, 'bold') , bg = dark_gray, fg = 'white', 
                command=lambda x = '%' : operator(x))
button.grid(row = 2 , column= 0,pady =2  )

button = Button(win, text = 'CE', width= 8,font=(None ,15, 'bold') , bg = dark_gray, fg = 'white',
                 command = lambda x = 'CE' : click(x))
button.grid(row = 2 , column= 1,pady =2  )

button = Button(win, text = 'C', width= 8,font=(None ,15, 'bold') , bg = dark_gray, fg = 'white',
                command=lambda x = 'C' : click(x))
button.grid(row = 2 , column= 2,pady =2  )

button = Button(win, text = '÷', width= 8,font=(None ,15, 'bold') , bg = dark_gray, fg = 'white',
                command=lambda x = '/' : operator(x))
button.grid(row = 2 , column= 3,pady =2 )

button = Button(win, text = 'x', width= 8,font=(None ,15, 'bold') , bg = dark_gray, fg = 'white',
                command = lambda x = '*' : operator(x))
button.grid(row = 3 , column= 3,pady =2 )

button = Button(win, text = '-', width= 8,font=(None ,15, 'bold') , bg = dark_gray, fg = 'white',
                command = lambda x = '-' : operator(x))
button.grid(row = 4 , column= 3,pady =2 )

button = Button(win, text = '+', width= 8,font=(None ,15, 'bold') , bg = dark_gray, fg = 'white',
                command = lambda x = '+' : operator(x))
button.grid(row = 5 , column= 3,pady =2 )

button = Button(win, text = '=', width= 8,font=(None ,15, 'bold') , bg = dark_gray, fg = 'white',
                command = result)
button.grid(row = 6 , column= 3,pady =2 )

button = Button(win, text = '.', width= 8,font=(None ,15, 'bold') , bg = dark_gray, fg = 'white',
                command=lambda x = '.' : click(x))
button.grid(row = 6 , column= 2,pady =2 )

button = Button(win, text = '0', width= 8,font=(None ,15, 'bold') , bg = 'black', fg = 'white',
                command = lambda x = '0' : click(x))
button.grid(row = 6 , column= 1,pady =2 )

button = Button(win, text = '±', width= 8,font=(None ,15, 'bold') , bg = dark_gray, fg = 'white',command=plus_min)
button.grid(row = 6 , column= 0,pady =2)

win.bind("<Return>", press_enter)
win.bind("<BackSpace>", press_backspace)
win.bind("<Escape>", press_Esc)
win.mainloop()
