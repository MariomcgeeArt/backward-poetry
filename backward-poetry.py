from random import shuffle
import random


txt = "1.Do not stand at my grave and weep, 2.I am not there; I do not sleep, 3.I am a thousand winds that blow, 4.I am the diamond glints on snow, 5.I am the sun ripened grain, 6.I am the gentle autum rain, 7.When you awaken in the morning's hush, 8.I am the swift uplifting rush, 9.Of quiet birds in circled flight, 10.I am the soft stars that shine at night, 11.Do not stand at my grave and cry, 13.  I am not there; I did not die! "
 #Source: https://www.familyfriendpoems.com/poem/do-not-stand-by-my-grave-and-weep-by-mary-elizabeth-frye




def lines_printed_backward(txt):
    x = txt.split(", ")
    for word in reversed(x):
        print(word)




def lines_printed_rand(txt):
    random_lines=[]
    x = txt.split(', ') 
    for lines in x:
        random_lines.append(lines)
        random.shuffle(random_lines)
        y = len(random_lines)
    for i in range(0, y):
        print (random_lines[i])
        print("complete")

def idk (txt):
    string = txt   
    length = len(txt)
    for row in range(length):
        for col in range(row+1):
            print(string[col], end="")


            
lines_printed_rand(txt)

# idk(txt)


    # x = txt.split('n, ')
    # for i in range(n, 0, -3):
    #     print(x * i)
#print (lines_printed_backward(txt))
# lines_printed_rand(txt)
# triangle(txt)

