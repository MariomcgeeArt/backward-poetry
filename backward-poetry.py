# from random import shuffle
# import random


txt = "Do not stand at my grave and weep,I am not there; I do not sleep,I am a thousand winds that blow, I am the diamond glints on snow, I am the sun ripened grain, I am the gentle autum rain, When you awaken in the morning's hush, I am the swift uplifting rush, Of quiet birds in circled flight, I am the soft stars that shine at night, Do not stand at my grave and cry, I am not there; I did not die! "
#Source: https://www.familyfriendpoems.com/poem/do-not-stand-by-my-grave-and-weep-by-mary-elizabeth-frye




# def lines_printed_backward(txt):
#     x = txt.split(", ")
#     for word in reversed(x):
#         print(word)




# def lines_printed_rand(txt):
#     random_lines=[]
#     x = txt.split(', ') 
#     for lines in x:
#         random_lines.append(lines)

#     random.shuffle(random_lines)
#     y = len(random_lines)

#     for i in range(0, y): 
#         print (random_lines[i])
    #  x = txt.split(', ')
    #  for word in x:
    #      print(random.shuffle(word))
def idk (txt):
    string = txt   
    length = len(txt)
    for row in range(length):
        for col in range(row+1):
            print(string[col], end="")


            


idk(txt)


    # x = txt.split('n, ')
    # for i in range(n, 0, -3):
    #     print(x * i)
#print (lines_printed_backward(txt))
# lines_printed_rand(txt)
# triangle(txt)

