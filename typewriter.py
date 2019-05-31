import pyautogui
import random
import requests

pyautogui.PAUSE = 2

word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
response = requests.get(word_site)
WORDS = response.content.splitlines()

pyautogui.hotkey('alt','tab')

for x in range(random.randint(1,6)):
    pyautogui.typewrite("from "+str(random.choice(WORDS))[2:-1]+" import "+str(random.choice(WORDS))[2:-1]+"\n")

pyautogui.typewrite("\nclass "+str(random.choice(WORDS))[2:-1]+"("+str(random.choice(WORDS))[2:-1]+"):")

def writeMethod():
    pyautogui.typewrite("def "+str(random.choice(WORDS))[2:-1]+"("+str(random.choice(WORDS))[2:-1])
    for x in range(random.randint(0, 4)):
        pyautogui.typewrite(", "+str(random.choice(WORDS))[2:-1])
    pyautogui.typewrite("):\n")

def writeSentence():
    output = "\""+str(random.choice(WORDS))[2:-1]
    for x in range(random.randint(1,5)):
        output+=" "+str(random.choice(WORDS))[2:-1]
    return output+"\""

pyautogui.typewrite("\n")
writeMethod()

pyautogui.typewrite(str(random.choice(WORDS))[2:-1]+" = "+writeSentence()+"\n")

status = 3
while True:
    resultInt = random.randint(1,101)
    if(resultInt<=20 and status!=1 and status!=2):
        if(status==3):
            pyautogui.hotkey('backspace')
            pyautogui.hotkey('backspace')
        elif(status==4):
            pyautogui.hotkey('backspace')
        pyautogui.typewrite("\nclass "+str(random.choice(WORDS))[2:-1]+"("+str(random.choice(WORDS))[2:-1]+"):")
        status = 1
    elif(resultInt>20 and resultInt<=50 and status !=2):
        if(status==1):
            pyautogui.typewrite("\n")
        elif(status==3):
            pyautogui.typewrite("\n")
            pyautogui.hotkey('backspace')
        elif(status==4):
            pyautogui.typewrite("\n")
        writeMethod()
        status = 2
    elif(resultInt>50):
        if(status==1):
            pyautogui.typewrite("\n")
            status = 4
        elif(status==2):
            status = 3
        resultInt2 = random.randint(1,101)
        if(resultInt2<=40):
            pyautogui.typewrite(str(random.choice(WORDS))[2:-1]+"_"+str(random.choice(WORDS))[2:-1]+" = "+writeSentence()+"\n")
        elif(resultInt2>40 and resultInt2<=80):
            pyautogui.typewrite(str(random.choice(WORDS))[2:-1]+" = "+str(random.randint(1,101)*5)+"\n")
        elif(resultInt2>80):
            pyautogui.typewrite(str(random.choice(WORDS))[2:-1]+"_"+str(random.choice(WORDS))[2:-1]+" = ["+str(random.choice(WORDS))[2:-1])
            for x in range(random.randint(1, 5)):
                pyautogui.typewrite(", "+str(random.choice(WORDS))[2:-1])
            pyautogui.typewrite("]\n")
