fruit_list = ["apple", "banana", "cherry", "guva"]                    # this lines stores lists of fuits

#to assign fuits quantity
apple_size = 100
banana_size = 100
cherry_size = 100
guva_size = 100

"""
 name          : AnandhS
 created       : 17.11.2023
 last modified : 22.11.2023
 version       : pycharm 2022.2.2
"""

print(f"""fruits list :
           apple , banana , cherry , guva """)            # printing the list
fruit = input("enter fruit : ")                         # asking to user for which fruit he asking
while fruit not in fruit_list :                         # asking to user until user tells a fruit name in our list
    print(f" sorry , we didn't have that fruit")
    fruit = input(f"enter fruit : ")
else:
    print(f"yeah we have {fruit} ")

if fruit == "apple":                                             # to print fuits quantity with kilograms
    print(f" {fruit} 1 kilogram : 80rs ")
if fruit == "banana":
    print(f" {fruit} 1 kilogram : 30rs ")
if fruit == "cherry":
     print(f" {fruit} 1 kilogram : 50rs ")
if fruit == "guva":
    print(f" {fruit} 1 kilogram : 60rs ")


fruit_quantity = int(input("how many kilograms sir ?  "))                     # asking size of the fruit
while fruit_quantity >= 6:
    print("sir maximum is 5 kg sir .")
    fruit_quantity = int(input("how many kilograms sir ? (pls enter 5 or below 5 kilograms sir ): "))
if fruit == "apple":                                                          # subracting the value from fuit quantity
    apple_size = apple_size - fruit_quantity
if fruit == "banana":
    banana_size = banana_size - fruit_quantity
if fruit == "cherry":
    cherry_size = cherry_size - fruit_quantity
if fruit == "guva":
    guva_size = guva_size - fruit_quantity

price = 0                                                                   # calculating the value of fruit
if fruit == "apple" and fruit_quantity == 1:
    price = price+80
if fruit == "apple" and fruit_quantity == 2:
    price = price+160
if fruit == "apple" and fruit_quantity == 3:
    price = price+240
if fruit == "apple" and fruit_quantity == 4:
    price = price+320
if fruit == "apple" and fruit_quantity == 5:
    price = price+400
if fruit == "banana" and fruit_quantity == 1:
    price = price+30
if fruit == "banana" and fruit_quantity == 2:
    price = price+60
if fruit == "banana" and fruit_quantity == 3:
    price = price+90
if fruit == "banana" and fruit_quantity == 4:
    price = price+120
if fruit == "banana" and fruit_quantity == 5:
    price = price+150
if fruit == "cherry" and fruit_quantity == 1:
    price = price+50
if fruit == "cherry" and fruit_quantity == 2:
    price = price+100
if fruit == "cherry" and fruit_quantity == 3:
    price = price+150
if fruit == "cherry" and fruit_quantity == 4:
    price = price+200
if fruit == "cherry" and fruit_quantity == 5:
    price = price+250
if fruit == "guva" and fruit_quantity == 1:
    price = price+60
if fruit == "guva" and fruit_quantity == 2:
    price = price+120
if fruit == "guva" and fruit_quantity == 3:
    price = price+180
if fruit == "guva" and fruit_quantity == 4:
    price = price+240
if fruit == "guva" and fruit_quantity == 5:
    price = price+300

print(f"""here's your order sir/madam                                            
     
     fruit     : {fruit}
     kilograms : {fruit_quantity}Kg
     price     : {price}Rs
     
     Thank you visiting our shop ! """)                    # finalizing the values
print("____"*7, end="")
print("""
    """)
print(f"""balance quantity of products :                    
                apple  : {apple_size}kg
                banana : {banana_size}kg
                cherry : {cherry_size}kg
                guva   : {guva_size}kg   """)                # printing the balance quantity of the fruits





