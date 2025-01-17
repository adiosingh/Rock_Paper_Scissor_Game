import random

lst=["rock","paper","scissor"]
round=1
score_comp=0
score_player=0
while round<6:
    print(f'''
          
          -----------Round {round}------------
          
          ''')
    ask=input("Choose between rock, paper and scissor: ").lower()

    while ask not in lst:
        ask=input("Choose only between rock, paper and scissor: ").lower()
        

    comp_choice=random.choice(lst)
    print(f"Comp chose  : {comp_choice}")
    print(f"You chose   : {ask}")

    if (comp_choice == ask):
        print(f"Game Drawn! Round {round} is completed.")

        score_comp+=0.5
        score_player+=0.5
        round+=1

        print(f"Your score          : {score_player}")
        print(f"Comp score          : {score_comp}")
    else:
        if (comp_choice=="rock"):
            if(ask=="paper"):
                print(f"Yay!!! you won. Round {round} is completed")
                score_player+=1
                round+=1
                print(f"Your score          : {score_player}")
                print(f"Comp score          : {score_comp}")


            else:
                print(f"Oops!!! you lost. Round {round} is completed.")
                score_comp+=1
                round+=1
                print(f"Your score          : {score_player}")
                print(f"Comp score          : {score_comp}")


        elif(comp_choice=="paper"):
            if(ask=="scissor"):
                print(f"Yay!!! you won. Round {round} is completed")
                score_player+=1
                round+=1
                print(f"Your score          : {score_player}")
                print(f"Comp score          : {score_comp}")



            else:
                print(f"Oops!!! you lost. Round {round} is completed.")
                score_comp+=1
                round+=1
                print(f"Your score          : {score_player}")
                print(f"Comp score          : {score_comp}")


        else:
            if(ask=="rock"):
                print(f"Yay!!! you won. Round {round} is completed")
                score_player+=1
                round+=1
                print(f"Your score          : {score_player}")
                print(f"Comp score          : {score_comp}")


            else:
                print(f"Oops!!! you lost. Round {round} is completed.")
                score_comp+=1
                round+=1
                print(f"Your score          : {score_player}")
                print(f"Comp score          : {score_comp}")


print('''
      
      ***************__FINAL_SOCRES__***************
      
      ''')
print(f"Your score          : {score_player}")
print(f"Comp score          : {score_comp}")
print('''

''')

if (score_comp == score_player):
    print("GAME DRAW!")
else:
    if(score_comp > score_player):
        print("COMP WON THE GAME!")

    else:
        print("YOU WON THE GAME!")






        







        
        
