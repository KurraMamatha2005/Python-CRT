# program to
# add confirmed  guest
#remove who cancels it
# check wether the guest is in the list
#sort and print the final guest list

Guest_list=[]
while(True):
    print("************Menu*************")
    print("1.add the Guest")
    print("2.remove the guest who cances")
    print("3.check if frnd attending the party or not")
    print("4.View the final guest list")
    print("5.Exit")
    choice=int(input("enter your choice:"))
    if(choice>=1 and choice<=5):
       if(choice==1):
           Guest_name=(input("enter the guest name"))
           Guest_list.append(Guest_name)
           print(f"{Guest_name} is added to guest list")
       elif(choice==2):
           cancelledguest=(input("enter the cancelled guest list"))
           if cancelledguest in Guest_list:
              Guest_list.remove(cancelledguest)
              print(f"{cancelledguest} is removed from the guestlist")
           else:
              print(f"{cancelledguest} is not in guestlist")
       elif(choice==3):
           checkguest=input("enter the guest name to check")
           if checkguest in Guest_list:
              print("the guest is attending the party")
           else:
              print(f"{checkguest} is not attending the party")
       elif(choice==4):
           if(len(Guest_list)==0):
               print("guest list is empty......")
           else:
               Guest_list.sort()
               print("hurray here is youer final  guest list")
               print(Guest_list)
       else:
           print("enjoy the party")
           break
    else:
        print("in valid input")