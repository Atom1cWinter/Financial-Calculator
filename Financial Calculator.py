#Financial Calculator
##Rickey Glover's Financial calculator rewritten in Python

import math
print ("This is a financial calculator used to help calculate either mortgage, certificate of deposit, or annuity!\n")

calc = int(input("Which calculator would you like to use?\n (1)Mortgage/t (2)CD/t (3)Annuity/t\n"))


def present_value_annuity (monthly, interest, mature):
    PresentValue = monthly / ((1 + (interest/1200) ** (mature/12)))

def future_value_annuity (monthly, interest, mature):
    FutureValue = monthly * (((1 + r) ** (interest/1200) - 1) / (mature * 12))

def calculate_monthly_payment (principal, interest, length):
    monthly_payment = principal * ((interest/1200) * (1 + (interest/1200)) ** (length*12)) / ((1 + (interest/1200)) ** (length*12) - 1)

if calc == 1: ##The formula for mortgage calculation is definitely wrong
    print ("Welcome to the Mortgage Calculator!")
    principal = float(input("What is the principal on your loan?: "))
    interest = float(input("What is the interest on your loan as a percentage (i.e 4%)?: "))
    length = float(input("What is the length of your loan in years?: "))
    MonthlyPayment = calculate_monthly_payment (principal, interest, length)
    InterestPaid = (MonthlyPayment * (length * 12) - principal)
    roundedMonthly = round(MonthlyPayment, 2)
    roundedInterest = round(InterestPaid, 2)

    print ("Your monthly payment is ${}.".format(roundedMonthly))
    print ("Your total interest paid is ${}.".format(roundedInterest))

elif calc == 2:
    print ("Welcome to the Certificate of Deposit Calculator!")
    deposit = float(input("What is your deposit amount?: "))
    interest = float(input("What was the interest on your deposit?: "))
    years = float(input("The number of years?: "))
    Total = deposit * math.pow((interest/100) + 1, years)
    TotalInterest = Total - deposit
    roundedTotal = round(Total, 2)
    roundedTotalInterest = round(TotalInterest, 2)

    print ("Your ending balance is ${}.".format(roundedTotal))
    print ("Your total interest earned is ${}.".format(roundedTotalInterest))

elif calc == 3: ##The formula for annuity calculation is definitely wrong. 
    print ("Welcome to the Annuity Calculator!")
    monthly = float(input("What is your monthly payout?: "))
    interest = float(input("What is your expected interest rate?: "))
    mature = float(input("How many years to mature?: "))
    FutureValue = future_value_annuity(monthly, interest, mature)
    PresentValue = present_value_annuity(monthly, interest, mature)
    RoundedFutureValue = round(FutureValue, 2)
    RoundedPresentValue = round(PresentValue)

    print ("Present Value: ${}".format(RoundedPresentValue))
    print ("Future Value: ${}".format(RoundedFutureValue))