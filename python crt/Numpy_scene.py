#average for array
import numpy as np
revenue=np.array([20000,22000,21000,25000,24000])
avg=sum(revenue)/len(revenue)
print(avg)

#max and min
import numpy as np
temps=np.array([98.4,98.6,99.1,100.2,98.9,99.5,98.7])
Max=max(temps)
Min=min(temps)
print(Max)
print(Min)

#total orders recieved during a week
import numpy as np
orders=np.array([120,150,130,140,180,170])
total=sum(orders)
print(total)

#scored more than 60
import numpy as np
scores=np.array([45,67,89,76,55])
for i in scores:
    if i>60:
        print(i)
    else:
        print("")

#retail billing
import numpy as np
prices=np.array([50,20,30])
quantities=np.array([2,5,3])
bill=prices*quantities
print(bill)
print(sum(bill))

#feed back rating
import numpy as np
count=0
ratings=np.array([4,3,5,4,2,5,3,4,5,1])
for i in ratings:
    if i==5:
       print(i)
       count+=1
    else:
        print("")
print(count)

#house price data scenario
import numpy as np
house_price=np.array([45,50,48,52,47])
increase = house_price * 0.10
print("\n10% Increase for Each House:")
print(increase)

# Step 3: Add the increase to original prices
updated_price = house_price + increase
print("\nUpdated House Prices After 10% Increase:")
print(updated_price)

#avg goals
import numpy as np
goals=np.array([1,0,2,1,3])
Sum=sum(goals)
Len=len(goals)
Avg=Sum/Len
print(Avg)

#milage tracking scenario
import numpy as pandas
count=0
mileage=np.array([15.2,16.5,14.8,15.9,16.2,15.5])
for i in mileage:
    if i<15:
        count+=1
        print(i.index())
    else:
        print("")






