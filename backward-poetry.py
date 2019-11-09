

txt = "Do not stand at my grave and weep,I am not there; I do not sleep,I am a thousand winds that blow, I am the diamond glints on snow, I am the sun ripened grain, I am the gentle autum rain, When you awaken in the morning's hush, I am the swift uplifting rush, Of quiet birds in circled flight, I am the soft stars that shine at night, Do not stand at my grave and cry, I am not there; I did not die! "
#Source: https://www.familyfriendpoems.com/poem/do-not-stand-by-my-grave-and-weep-by-mary-elizabeth-frye




def lines_printed_backward(txt):
    x = txt.split(", ")
    for word in reversed(x):
        print(word)





#def lines_printed_randomly(my_poem):
    #this function prints the powem in radnomly

print (lines_printed_backward(txt))
