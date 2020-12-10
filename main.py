from tkinter import *
import clickImage
import detectAns
from PIL import ImageTk,Image



def main():
    root=Tk()
    root.title('Quiz Quasar')
    root.iconbitmap('./resources/quizquasarico2.ico')
    root.configure(background='gray')
    welcomeLabel=Label(root,text="Welcome To Quiz Answer Detector",width=100,bg="gray",fg="pink")
    welcomeLabel.config(font=("Courier", 16))
    welcomeLabel.pack()

    ImageFrame=Frame(root)
    ImageFrame.pack(side=TOP)
    clickedImage=ImageTk.PhotoImage(Image.open("./resources/image.jpg"))
    myClickedImageLabel=Label(image=clickedImage,border=5)
    myClickedImageLabel.pack(in_=ImageFrame,side=LEFT)

    myAnswerLabel=Label(root,text='',bg="gray",fg="lightgreen")
    
    def detectAnswerFunc(): 
        detectedAnswer=detectAns.detectAns()
        myAnswerLabel.configure(text=detectedAnswer)
        myAnswerLabel.text=detectedAnswer        
        myAnswerLabel.config(font=("Courier", 20))
        

    def clickImageFunc():
        clickImage.clickImage()
        newImage=ImageTk.PhotoImage(Image.open("./resources/image.jpg"))
        myClickedImageLabel.configure(image=newImage)
        myClickedImageLabel.image=newImage
        


    buttons=Frame(root)
    buttons.pack(side=TOP)
    cliImgBtn=Button(root,text="Click Quiz Image",command=clickImageFunc,bg="gray",fg="pink",padx=50,pady=20)
    detectAnsBtn=Button(root,text="Detect Answer Of Quiz",command=detectAnswerFunc,bg="gray",fg="pink",padx=40,pady=20)

    cliImgBtn.pack(in_=buttons,side=LEFT)
    detectAnsBtn.pack(in_=buttons,side=LEFT)

    myAnswerLabel.pack()
    

    root.mainloop()

if __name__ == "__main__":
   main()