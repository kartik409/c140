from tkinter import *

root = Tk()

root.title("Fibonacci")
root.geometry("400x400")

label_series = Label(root, text="fibonacci series")
label_flower = Label(root)
label_spiral = Label(root)

def Fibonacci():
    num = 10
    n1 = 0
    n2 = 1
    sum = 0
    counter = 1
    while(counter<= num):
         label_series["text"] += str(sum) +" "
         counter = counter +1
         n1=n2
         n2=sum
         sum=n1+n2
    label_flower["text"] = "flower is fully bloomed"
    label_spiral["text"] = "spiral in right direction are" +str(n1) + "and spirals in left direction are" +str(n2) + "\n total spirals are "+ str(sum)
    
    
   

btn = Button(root, text= "show fibonacci series", command=Fibonacci)
btn.pack()
label_series.pack()
label_flower.pack() 
label_spiral.pack()


root.mainloop()