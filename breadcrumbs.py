import time
import sys

#************
#This function, "output", can output the sentence in animation.
# If the line is longer than the seting, it also do backspce animation
# and print in next line.
#************
def output(string,re=0): # recursive method 

	#******************************
	str_limit=60 #Default number: 60; It is the number of characters in one line.
	p_blank=0 #position of blank
	i=1 #Count the number of string has be printed.
	j=0 #Count the loop in the backspace animation
	#blank string: To cover the previous string in backspace amimation
	string_="                                                               " 
	#******************************

	while (i <= len(string)):# i=1 ~ x

		#string[0:1]=0,string[0:2]=0~1 ...string[0:x]=0~(x-1)
		sys.stdout.write("\r"+string[0:i])
		sys.stdout.flush()
		time.sleep(0.06) #delay time add every new character

		if (string[i-1]==" "): #Save the position of the blank in the string.
			p_blank=i-1

		if (i>str_limit): # When the number of characters in a line is larger than 60.

			#Backspace animation: #print string[0~60] (61c) to 
			# string[0~p_blank](character_+1 blank)			
			for j in range(i,p_blank,-1):#61 ~ (p_blank+1)
				sys.stdout.write("\r"+string[0:j]) 
				sys.stdout.flush()
				#print string[0~60] (61c) to string[0~p_blank](character_+1 blank)
				time.sleep(0.06)
				sys.stdout.write("\r"+string_[0:61]) #Cover the previous string in blank.
				sys.stdout.flush()

			sys.stdout.write("\r"+string[0:j]+"\n") #To next line
			sys.stdout.flush()
			new_string=string[p_blank+1:len(string)] #Set that is not outputed
			output(new_string,1) #recursion
			i=len(string) #Exit loop.
		i=i+1
	if (re==0):
		sys.stdout.write("\n")
		sys.stdout.flush()
		sys.stdout.write("\n")
		sys.stdout.flush()
		time.sleep(0.02)

