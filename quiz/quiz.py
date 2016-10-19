from I2CDisplay import *
from gpiozero import Button
import time

# File holding questions
# 4 lines are the question and then the 5 is T for true or F for false
# Repeat for Q 2 etc.
quizfilename = "quiz.txt"

start_button = Button(23)
true_button = Button(22)
false_button = Button(4)

# Initialise display
lcd_init()

# Send some test
lcd_string("Raspberry Pi",LCD_LINE_1)
lcd_string("True or False quiz",LCD_LINE_2)
lcd_string("",LCD_LINE_3)
lcd_string("Press start",LCD_LINE_4)

start_button.wait_for_press()

# Note that there is no error handling of file not exist 
# Consider using a try except block
# Open the file
file = open(quizfilename)

questions = 0
score = 0
answer = ''

while True:
    # print 4 lines as the questions
    thisline = file.readline().rstrip("\n")
    if thisline == "" : break
    lcd_string(thisline,LCD_LINE_1)
    thisline = file.readline().rstrip("\n")
    if thisline == "" : break
    lcd_string(thisline,LCD_LINE_2)
    thisline = file.readline().rstrip("\n")
    if thisline == "" : break
    lcd_string(thisline,LCD_LINE_3)
    thisline = file.readline().rstrip("\n")
    if thisline == "" : break
    lcd_string(thisline,LCD_LINE_4)
    # Next line should be T for answer = True or F for False
    thisline = file.readline().rstrip("\n")
    if thisline == "" : break
    if (thisline == "T"):
        answer = "T"
    elif (thisline == "F"):
        answer = "F"
    # should not reach this else - otherwise question file is invalid
    else : break
    
    # wait on True or False pressed
    while (true_button.is_pressed == False and \
        false_button.is_pressed == False):
        time.sleep (0.2)
    # Increment number of questions attempted
    questions = questions+1
    # Once one of the buttons is pressed - also check the other is not pressed to avoid cheating
    if (answer == "T" and true_button.is_pressed \
        and false_button.is_pressed == False):
        score = score+1
        lcd_string("Correct!",LCD_LINE_4)
    elif (answer == "F" and true_button.is_pressed == False \
        and false_button.is_pressed):
        score = score+1
        lcd_string("Correct!",LCD_LINE_4)
    else: 
        lcd_string("Wrong.",LCD_LINE_4)
    # Wait 2 seconds before next questions
    time.sleep(2)
    # Finished this question return to the start
# Outside of the quiz loop - give the score
lcd_string("End",LCD_LINE_1)
lcd_string("Score",LCD_LINE_2)
lcd_string(str(score)+" out of "+str(questions),LCD_LINE_3)
lcd_string("",LCD_LINE_4)
time.sleep (5)
file.close()
    

