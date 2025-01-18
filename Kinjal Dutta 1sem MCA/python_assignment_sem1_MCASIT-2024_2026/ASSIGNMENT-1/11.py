amt = int(input("enter the amount to be withdrwn : "))  #amt = amount
hundred = amt //100
amt = amt % 100
fifty = amt //50
amt = amt % 50
ten = amt // 10
amt = amt % 10

print("number of hundred notes : ", hundred)
print("numner of fifty notes : ", fifty)
print("number of ten notes : ", ten)
