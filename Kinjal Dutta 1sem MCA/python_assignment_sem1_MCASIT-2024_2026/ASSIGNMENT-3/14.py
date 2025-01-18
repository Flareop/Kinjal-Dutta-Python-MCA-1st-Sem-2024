cost = 6000
salvage = 2000
annual_earnings = 1000
alternative_rate = 0.12

minimum_life = 0
while True:
    minimum_life +=1
    pv_earnings = sum(annual_earnings/ (1 + alternative_rate) ** t for t in range (1, minimum_life + 1))
    pv_earnings += salvage / (1 + alternative_rate) ** minimum_life

    if pv_earnings >= cost:
        break

print(f"The minimum life of the machine to make it a more attractive investment is {minimum_life} years.")