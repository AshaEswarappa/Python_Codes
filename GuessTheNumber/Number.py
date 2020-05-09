#Program to randomly generate a number between 0 and 20. 
#The user needs to guess what the number is. 
#If the user guesses wrong, tell them their guess is either too high, or too low. 

#Library to generate random number for the required range
from random import randrange

#Randomly generated number by the built-in function
Number = randrange(20)

#Prints the generated number
print("The Generated Number is ", Number)

#Checks if the generated number is 0 and generates again if its zero
if(Number == 0):

	print("Generated Number falls out of Range \n")
	
	#Randomly re-generates number by the built-in function
	Number = randrange(20)

	#Prints the generated number
	print("The Re-Generated Number is \n", Number)


#Say hello to user before staring with Guess
print( "Hello User, Welcome for guessing the number between 1 and 20 \n")

#Maximum Number of Guess Allowed
Max_Guess = 5

Guess = 0

#Checks if the number of guess is not excedded the maximum guesses
while(Guess <= Max_Guess):

	# An input is requested by user and stored in a variable, also type casting is done in case if user enters any other data type than the expected one
	User_Guess = int(input ("Enter a number: "))

	
	# Prints in the console the variable as requested
	print ("The number you guessed is: ", User_Guess)
	
	if (User_Guess < Number):
	
		print("The number you guessed is Smaller \n ")
	
	elif(User_Guess > Number):
	
		print("The number you guessed is Higher \n ")
		
	else:
	
		print(" Congratulations! You have guessed it Right")
		break;

	Guess = Guess + 1
	
	#Imdicated the user the number of trails left 
	Trails = Max_Guess - Guess
	
	print( "You are left with " , Trails, " Trails \n" )

