dinar = float(input("pls enter the amount of dinar: "))
if dinar == 0:
    print("can not change")
dollar = dinar/ 129
pound = dinar/ 176
euro =  dinar/ 152

result = str(input("pls enter the currency you want to change to: "))

if result == "dollar":
    print(dollar)
elif result == "pound":
    print(pound)
elif result == "euro":
    print(euro)