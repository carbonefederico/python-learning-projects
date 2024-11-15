investment = float(input ("Initial investement: "))
rate = float(input ("Rate (%): "))
years = int(input ("Years: "))

for year in range(years):
    investment = investment * (1 + rate / 100)
    print (f"Investment after {year + 1} years: {round(investment,0)}")

print (f"***** 10Final value: {round(investment,0)}")