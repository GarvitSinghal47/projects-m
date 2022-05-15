from asyncio.windows_events import NULL
from calendar import c
import cv2 
from cvzone.HandTrackingModule import HandDetector

from pynput.keyboard import Key, Controller

keyboard = Controller()
key = "q"

class Button:
    def __init__(self, pos, width, height, value):
        self.pos = pos
        self.width = width
        self.height = height
        self.value = value

    def draw(self, img):
        cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height),(225, 225, 225), cv2.FILLED)
        cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height),(50, 50, 50), 3)
        cv2.putText(img, self.value, (self.pos[0] + 30, self.pos[1] + 70), cv2.FONT_HERSHEY_PLAIN,2, (50, 50, 50), 2)

    def checkClick(self, x, y):
        if self.pos[0] < x < self.pos[0] + self.width and self.pos[1] < y < self.pos[1] + self.height:
            cv2.rectangle(img, (self.pos[0] + 3, self.pos[1] + 3),(self.pos[0] + self.width - 3, self.pos[1] + self.height - 3),(255, 255, 255), cv2.FILLED)
            cv2.putText(img, self.value, (self.pos[0] + 25, self.pos[1] + 80), cv2.FONT_HERSHEY_PLAIN,5, (0, 0, 0), 5)
            return True
        else:
            return False


# Buttons
buttonListValues = [['7', '8', '9', '*'],['4', '5', '6', '-'],['1', '2', '3', '+'],['0', '/', '.', '='],['Cl',' ','C','Dl']]
buttonList = []
for x in range(4):
    for y in range(5):
        xpos = x * 80 + 800
        ypos = y * 80 + 150
        buttonList.append(Button((xpos, ypos), 80, 80, buttonListValues[y][x]))

# Variables
myEquation = ''
delayCounter = 0

# Webcam
cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
detector = HandDetector(detectionCon=0.8, maxHands=1)

while True:
    # Get image frame
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img)

    # Draw All
    # box or output display rectangle
    cv2.rectangle(img, (800, 70), (800 + 320, 70 + 80),(225, 225, 225), cv2.FILLED)

    cv2.rectangle(img, (800, 70), (800 + 320, 70 + 80),(50, 50, 50), 3)


    for button in buttonList:
        button.draw(img)

    # Check for Hand
    if hands:
        # Find distance between fingers
        lmList = hands[0]['lmList']
        length,info,img = detector.findDistance(lmList[8], lmList[12], img)
        print(length)
        x, y,z = lmList[8]

        # If clicked check which button and perform action
        if length < 50 and delayCounter == 0:
            for i, button in enumerate(buttonList):
                if button.checkClick(x, y):
                    myValue = buttonListValues[int(i % 5)][int(i / 5)]  # get correct number
                    if myValue == '=':
                        try:
                            ans=str(eval(myEquation))
                            myEquation=ans
                        except(NameError, SyntaxError):
                            myEquation='ERROR'
                            
                    elif myValue== 'C':
                        myEquation=''
                    elif myValue=='Cl':
                        keyboard.press(key)
                        keyboard.release(key)

                    elif myValue=='Dl':
                        myEquation=myEquation[:-1]
                    
                    else:
                        myEquation += myValue
                    delayCounter = 1

    # to avoid multiple clicks
    if delayCounter != 0:
        delayCounter += 1
        if delayCounter > 10:
            delayCounter = 0

    # Write the Final answer
    cv2.putText(img, myEquation, (810, 130), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)

    # Display
    key = cv2.waitKey(1)
    cv2.imshow("Image", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if key == ord('c'):
        myEquation = ''