#core concept of python with module are using in the Project:-)

#Modules Used:-)
#Emoji Module: Used to display different emojis for a better user experience.
#Colorama (Fore) Module: Used to change the color of the text in the console output.
#Datetime Module: Used to display and record the current date and time.

#Dictionary:-)
#A dictionary is used to store all the food items along with their respective prices.

#Loop:-)
#Loops are used along with dictionary methods to calculate the total amount based on the ordered food items and their quantities.

#Conditional Statements:-)
#Conditional statements are used to determine whether the user wants to order additional food items or not.

#Text File Handling:-)
#A text file is used to store the ordered food items along with the date and time for record-keeping purposes.

##         working of cafe food menu ordering system:-
#First, I welcome the customer with a smile emoji
#and display the café menu using fork and knife emojis.
#Then, I show a message to the customer requesting
# them to order food only from the menu.
#After that, I ask the user to select a food item.
#If the ordered food item is available in the café menu,
# I display a message saying that the ordered item has been added to their order.
#Next, I ask the user how many quantities of the selected food item they want to order.

#After that, I again ask the user whether they want to order another food item.
#If the user refuses, I display the ordered food items with their prices and
#Thank the customer for visiting the café.

#If the user agrees to order another food item, the same process is repeated.
# Finally, I display all the ordered food items with the total amount and
# thank the customer for visiting our restaurant with a smile emoji.

import emoji
from colorama import Fore
from datetime import datetime

smile_em = emoji.emojize(":grinning_face:")
print(smile_em*23+" "+"welcome to my cafe"+" "+smile_em*23)

dic={"tea":50,
"coffee":100,
"cold drink":50,
"samosa":30,
"chicken butter":600,
"chicken biryani":250,
"burger":30,
"pasta":80,
"chilli potato":100,
"pastry":50,
"chapati":60,
 "water":50,
 "momo":300,
 "cold_drink":50,
 "testy_flavor":300}

print()
print()

em = emoji.emojize(":fork_and_knife:")
print(Fore.YELLOW +em*26 +" "+"cafe menu"+" "+em*26)
print(f"{dic}")
print(em*57)
print(Fore.WHITE)

total_amount=0
print("please order food item only from cafe menu")
order1=input("what food item would you like to order from cafe menu=")

if order1 in dic:
    items1=int(input(f"how many quantities of {order1} do you want to order="))
    for i in range(items1):
        total_amount+=dic[order1]
    print(f"your {order1} has been added in your order")

else:
    print(f"{order1} item is not available yet")

order2=input("would you like to order another item=")

if order2=="yes":
    order_item=input("chose your another food_item from cafe menu=")
    item2=int(input(f"how many {order_item} do you want to order="))
    for i in range(item2):
        total_amount += dic[order_item]
    print(f"you ordered {order1} and {order_item}")
    print(f"your total_amount is {total_amount}")
    print(smile_em * 10 + " " + "thanks to visit our cafe,have a sweet day" + " " + smile_em * 10)

    now1 = datetime.now() # print now date and time
    now  = now1.strftime("%d-%m-%y %S:M%:H% %p")
    items_date = f"this is food items: {order1},{order_item}  datetime of ordered food_items: {now}"
    with open("stored_data", "w") as f:
        f.write(items_date)


elif order2=="no":
    print(f"you ordered {order1}")
    print(f"your total_amount is {total_amount}")
    print(smile_em*10+" "+"thanks to visit our cafe,have a sweet day"+" "+smile_em*10)

    now1 = datetime.now() #print now date and time
    now = now1.strftime("%d-%m-%y %M:%H:%S %p")
    items_date = f"this is food item: {order1} \ndatetime of ordered food_time:{now}"
    with open("stored_data", "w") as f:
        f.write(items_date)


