num_days=int(input("Enter number of days: "))
temp=[]
total = 0
for i in range(num_days):
    nextday = int(input("Day"+str(i+1)+"'s high temperature: "))
    temp.append(nextday)
    total += temp[i]

avg = round(total / num_days, 2)
print("Average Temperature:", avg)

above = 0
for i in temp:
    if i > avg:
        above += 1
print(str(above)+" Day's temperature is above average temperature")
