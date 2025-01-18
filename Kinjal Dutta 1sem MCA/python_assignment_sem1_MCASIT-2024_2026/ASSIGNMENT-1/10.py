poputation=80000
popmen=(52*poputation)/100
popwomen=poputation-popmen
poplit=(48*poputation)/100
litmen=(35*popmen)/100
litwomen= poplit-litmen
unlitmen=popmen-litmen
unlitwomen=popwomen-litwomen
print("Total Population          : ",poputation)
print("Total Mens                : ",popmen)
print("Total Womens              : ",popwomen)
print("Total Literacy            : ",poplit)
print("Total Literacy Mens       : ",litmen)
print("Total Literacy Womens     : ",litwomen)
print("Total Not Literacy Mens   : ",unlitmen)
print("Total Not Literacy Womens : ",unlitwomen)