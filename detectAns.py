import requests
from bs4 import BeautifulSoup
import pytesseract
from PIL import Image
import cv2
import numpy as np

def detectAns():
    # setting image dpi values
    file_path = "./resources/image.jpg"
    im = Image.open(file_path)
    im.save('./resources/ocr.png', dpi=(300, 300))
    # making image cleaner
    image = cv2.imread("./resources/ocr.png")
    grayImage=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    retval, threshold = cv2.threshold(grayImage,200,255,cv2.THRESH_BINARY)
    #some added code 
    # canimage = cv2.Canny(threshold, 100, 200)
    cv2.imshow("Threshold image", threshold)
    # cv2.imshow("Canny image image", canimage)
    cv2.waitKey(0)
    # running tesseract
    # detecting text in image
    cv2.imwrite("./resources/processedImage.jpg",threshold)
    text = pytesseract.image_to_string(threshold)
    # text += pytesseract.image_to_string(canimage)
    print(text)
    question=text.split('?')[0]
    print(question)
    #code for detecting answer options from text ocr returned
    tempanswers=text.split('\n\n')[1:]
    answers=list()
    for ta in tempanswers:
        if ta.strip()!='':
            answers.append(ta)

    print(answers)
    # web scraping code 
    url="https://www.google.com/search?q="+question
    r=requests.get(url)
    soup = BeautifulSoup(r.content, "html5lib")
    links = soup.findAll("a")
    data=list()
    i=0
    # finding first few links data
    for link in links :
        link_href = link.get('href')
        if "url?q=" in link_href and not "webcache" in link_href:
            filterlink=link.get('href').split("?q=")[1].split("&sa=U")[0]
            r1=requests.get(filterlink)
            tempSoup=BeautifulSoup(r1.content,'html.parser')
            data.append(tempSoup)
            i=i+1
            if(i==7):
                break
    datastring=''
    for d in data:
        # print(d.text)
        # print("*************************************************************************************")
        datastring=datastring+d.text

    # print(datastring)
    lowdatastring=datastring.lower()
    # print(lowdatastring)
    lineWiseData=lowdatastring.split('.')

    #find the occurance of each answers

    occurrance=[0,0,0,0,0,0]
    flag=0
    for ans in answers:
        smallAns=ans.lower()
        for line in lineWiseData:
            if smallAns in line:
                occurrance[flag]+=1
        if flag==2:
            break
        flag+=1
    print(occurrance)

    # now print most occured answer
    answerIndex=occurrance.index(max(occurrance))
    print(answerIndex)
    print("The Answer is: "+ answers[answerIndex])
    return("The Answer is :  "+ answers[answerIndex])


# detectAns()   

        


