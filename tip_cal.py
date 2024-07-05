#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator")
print("Enter the total bill amount in USD")
bill = float(input())
print("Enter how much tip you want to give? 10, 12 or 15")
tip_percent = int(input())
print("How many people to split the bill?")
people = int(input())
tip = (bill/people) * ((tip_percent+100)/100)
#tips = round(tip, 2)
tips = "{:.2f}".format(tip)
print(f"Each person should pay: ${tips}")



#if(bill==150.0){
#  float pay = (150.00/5) * 1.12;
#}
#if(pay[3]>5){
#  pay[2]=pay[2]+1;
#else
#pay[2]=pay[2]-1;
#}
#print("Each person should pay: " + pay)
