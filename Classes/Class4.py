message = "Hello World"
print(message[::-1])

new_message = "ORANGE"

print(new_message[3:0:-1])

#Exercise 1
#Replace English by Spanish from the following
astrng= "I know English, And I can speak too!"
 
astrng = astrng.replace("English", "Spanish")

astrng= "I know English, And I can speak too!"

ind = astrng.find["English"]
astrng[:ind]+" Spanish "+astrng[:ind+len("English"):]

