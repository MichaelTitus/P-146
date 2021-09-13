from tkinter import *

root=Tk()

root.title("Fibonacci")
root.geometry("400x500")

text_input=Entry(root)
text_input.pack()
label_series=Label(root,text="Fibonacci Series: ")
label2=Label(root,text='fibonacci sum:')



def fibonacci():
    num=int(text_input.get());
    first_number=0;
    second_number=1;
    sum=0;
    sum2=0;
    counter=1
    
    while(counter<=num):
        label_series["text"]+=str(sum)+" "
        label2["text"]="Fibonacci sum "+str(sum2)+" "
        counter=counter+1
        first_number=second_number
        second_number=sum
        sum=first_number+second_number
        sum2=sum2+sum
        
   
    

label_series.pack()         
label2.pack()

btn=Button(root, text="Show Fibonacci series", command=fibonacci)

btn.pack()


root.mainloop()
