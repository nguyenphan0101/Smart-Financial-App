import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from numpy import double

def saving_section():

	saving_money = input("Input the saving money you can save now: ")
	time = input("Input the saving duration: ")
	interest_rate = input("Input the interest rate: ")

	this_money_list = []


	for x in range(0,int(time)+1):
		saving_money_avaible =  double(double(saving_money)*pow(1+((double(interest_rate)/100))/12,double(x)*12))
		this_money_list.append(double(saving_money_avaible))
	print(this_money_list[-1])

	print("The total amount of money you own up to this point is " + str("%0.2f" %this_money_list[-1]))
	temp = double(this_money_list[-1])/double(saving_money)

	plt.plot(this_money_list)


	plt.xlabel('Time(s)')
	plt.ylabel('Values')
	plt.title("Your property value increases %s times" %("%.2f" %temp),loc='left')
	plt.grid()
	plt.scatter((range(0,int(time)+1)),this_money_list)
	plt.show()


def saving_section2():

	saving_money = input("Input the saving money you can save each month: ")
	time = input("Input the saving duration: ")
	interest_rate = input("Input the interest rate: ")

	this_money_list = []
	sum = saving_money
	this_money_list2 = []
	imtemp = 0

	for x in range(0,int(time)*12+1):
		saving_money_avaible =  double(((double(sum))+double(saving_money))*(1+((double(interest_rate)/100/12))))
		sum = double(saving_money_avaible)
		this_money_list.append(double(saving_money_avaible))
	print(this_money_list[-1])


	for x in range(0,int(time)*12+1):
		imtemp+=int(saving_money)
		this_money_list2.append(double(imtemp))



	print("The total amount of money you own up to this point is " + str("%0.2f" %this_money_list[-1]))
	temp = double(this_money_list[-1])/(double(saving_money)*int(time)*12+1)

	plt.plot(this_money_list)
	plt.plot(this_money_list2)

	plt.xlabel('Time(s)')
	plt.ylabel('Values')
	plt.title("Your property value is " +str("%0.2f" %this_money_list[-1]) + " after "  + str(time) + " years " ,loc='left')
	plt.grid()
	plt.show()

def required_savings():


	A = input("Input desire money you want in the future: ")
	P = input("Input your existing investment: ")
	r = input("Input the interest rate: ")

	t = input("Input the saving duration: ")
	n = double(t)
	temp = pow((1+(double(r)/100/double(n))),double(t)*double(n))
	Q = (((double(A) - (double(P) * double(temp)))) / (double(temp) - 1)) * ((double(r)) / 12) / 100



	print("You need to save money %s to get %s in the future!" %("%0.2f" %Q,A))
	#print("you need to save money x to get y in the future")

def double_up():
	print("The Rule of 72 is a simplified formula that calculates how long it'll take for an investment to double in value, based on its rate of return")
	interest_rate = input("Input the interest rate you are getting now: (included in %) ")
	duration = 72/int(interest_rate)

	print("You need %s year(s) to double up your money!" %("%.2f" %duration))


def investment_taste():
	print("Here are a few curated questions to find out what type of investment you are\n")
	print("Please choose 1 as true and 0 as false\n")
	x1 = input("If you own stocks, do you check stock prices daily or often?\n")
	x2 = input("When driving on the road, even when traffic and weather conditions are favorable, you never drive over the speed limit?\n")
	x3 = input("If the price of a stock falls, your first reaction is to sell?\n")
	x4 = input("Another stock market crash similar to 2007 could happen unexpectedly?\n")
	x5 = input("When flying in unfavorable weather conditions, you will be straight and worried about your safety?\n")
	x6 = input("If you sell the stock at a loss of more than 25%, you will seriously lose confidence in your ability to invest?\n")
	x7 = input("You hate pointless dates?\n")
	x8 = input("When you travel, you write a list to make sure you don't miss anything?\n")
	x9 = input("When traveling with other people, you prefer to drive by yourself?\n")
	x10 = input("Before buying stock, you want to talk to at least 2 more people to confirm your choice?\n")
	total = int(x1) + int(x2) + int(x3) + int(x4) + int(x5) + int(x6) + int(x7) + int(x8)+ int(x9)+ int(x10)
	print("You have %s points" %(total))

	if int(total) in range(0,4):
		print("Your risk appetite is suitable for single stock investing")
		return 0
	elif int(total) in range(4,7):
		print("You seem to be a sensitive investor, with more knowledge and experience you can raise your risk tolerance to a reasonable level")
	elif int(total) in range(7,11):
		print("You can be a very conservative and risk-averse investor, suitable for some long-term bond or bank interest portfolios")
	else:
		print("Cant solve this!")

print("Welcome to our SMART Financial App:")


member_choice = input("Choose the type you wanna chooose:\n"
	  "1. Compound interest\n"
	  "2. Saving per month with compound interest\n"
	  "3. Calculate the required savings\n"
	  "4. How long to double your money\n"
	  "5. Choosing suitable investment taste\n"
	"Put a number: "
	)



if int(member_choice) == 1:
	saving_section()
elif int(member_choice) == 2:
	saving_section2()
elif int(member_choice) == 3:
	required_savings()
elif int(member_choice) == 4:
	double_up()
elif int(member_choice) == 5:
	investment_taste()
else:
	print("You enter the wrong input, Please try again!")




