import random
import time
import os
def zombie_survival_game():
    print("Loading........")
    time.sleep(2)
    os.system('clear')
    userName = input("Enter your name:")
    print(f"Hello, {userName}, welcome to Zombie survival game!")
    print("A zombie is walking straight on a road...")
    attempts = 0
    press = input("press 'y' to start game or press 'q' to quite a game.")
    if press == "y":
         time.sleep(2)
         os.system('clear')
         while True:
              print("Which direction should the zombie move?")
              print("Right (enter a jungle and get lost)")
              print("Straight (fall into a pothole and die.)")
              print("Left (find a human or fight with enemy and find a human and win the game)")
      
              direction = input("Enter 1, 2, or 3 to choose the direction or 'q' to quit")
              if direction == 'q':
                  print("Exiting the game...")
                  break
            
              if direction not in ['1', '2', '3']:
                  print("Invalid choice! Please enter 1, 2, or 3.")
                  continue
              
              direction = int(direction)
              attempts += 1
              
              if direction == 1:
                      print("The zombie moves straight and falls into a pothole... GAME OVER!")
              elif direction == 2:
                  print("The zombie moves right into a jungle and gets lost... GAME OVER!")
              elif direction == 3:
                  direction = random.choice(['enemy', 'human'])
                  if(direction == 'enemy'):
                       direction = random.choice(['die','kill'])
                       if(direction == 'kill'):
                            print("Zombie find enemy.")
                            print("zombie defect enemy, find a human and win a game")
                            print(f"Congratulations! The zombie has won the game in {attempts} attempts.")
                            
                       elif(direction == 'die'):
                         print("Enemy kill the zombie... GAME OVER! ")

                  elif direction == 'human':
                        print("The zombie moves left and finds a human!")
                        print(f"Congratulations! The zombie has won the game in {attempts} attempts.")
                        
              if direction == 1 or direction == 2 or direction == 'die' or direction == 'human' or direction == 'kill':
                  time.sleep(2)
                  os.system('clear')
                  x  = input('Want to try again? press "y"  to continue... or "q" to quite')
                  if x == 'y':
                   time.sleep(2)
                   os.system('clear')
                   continue
                  elif x == 'q':
                       print("Exiting the game...")
                       break
    elif press == "q":
         print("Exiting the game...")
zombie_survival_game()
