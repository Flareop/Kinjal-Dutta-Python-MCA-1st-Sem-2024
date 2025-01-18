cost_price = int(input("enter the price cost :"))
selling_price = float(input("enter the selling cost :"))
if  cost_price > selling_price:
       profit =(cost_price -  selling_price)
       print("profit", profit)
else:
       loss =(selling_price - cost_price)
       print("loss", loss)