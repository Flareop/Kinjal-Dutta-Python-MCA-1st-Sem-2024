total_matchsticks = 21
print("wellcome to the matchstick game!")
print("Rules: there are 21 matchstick, you pick 1, 2, 3, or 4 matchsticks  on your turn.")
print("Whoever is forced to pick up the last matchstick loses the game.")

while total_matchsticks > 1:
    print("/nmatchstick remining:{total_matchstick}")
    user_pick = int(input("pick 1,2,3, or 4 : "))
    if user_pick < 1 or user_pick > 4:
        print("invalid choice! pick between 1 and 4.")
        continue

    total_matchsticks -= user_pick
    if total_matchsticks ==1:
        print("you picked the last matchstick. you lost!")
        break


    computer_pick = (5 - user_pick ) if total_matchsticks > 5 else  (total_matchsticks - 1)
    if(f"computer pick{computer_pick}matchstick"):
        total_matchsticks -= computer_pick

    if total_matchsticks == 1:
        print("computer pick the last matchstick . computer lost!")
   