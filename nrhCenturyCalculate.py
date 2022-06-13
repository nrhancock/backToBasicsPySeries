current_age = input("What is your current age?")
value_age = int(current_age)

years_toGo = 100 - value_age
weeks_toGo = years_toGo * 52
days_toGo = years_toGo * 365

time_to_hundred = f"You have {years_toGo} years, {weeks_toGo} weeks, and {days_toGo} until age 100."
print(time_to_hundred)
