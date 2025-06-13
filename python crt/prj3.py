n=int(input("how many food items you want to order:"))
menu=['tea','icecream','soda','pizza','biryani']
prices=(20,30,40,50,60)
total=0
for i in range(n):
  food=input(f"enter the food you want{i}:")
  if food in menu:
      print("confirm order")
      print("billing completed")
      phone_num=input("enter the phone number")
      feed_back=input("enter the feedback:")
      index = menu.index(food)
      price = prices[index]
      print(f"{food.capitalize()} is available at ₹{price}")
      total += price
  else:
      print("not available food")
print(f"the total bill amount is {total} ")
gst = total * 0.18
if gst!=0:
 print(f"the final bill amount after adding gst is is {gst}")
else:
 print("the amount is free")
    

