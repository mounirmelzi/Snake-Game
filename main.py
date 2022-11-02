
import pygame
from GameClass import SnakeGame
import OtherObjects
from os import system
pygame.init()
system("cls")




if __name__ == "__main__":

    print("Welcome to the Snake game BY Mounir!!")
    user_name = input("Dear Player, Enter your name: ")
    Difficulty = input("Enter the difficulty : easy | normal | hard \n-->")
    OtherObjects.SPEED = OtherObjects.set_difficulty(Difficulty)

    game = SnakeGame()
    # game loop
    while True:
        game_over, score = game.play_step()
        # break if game over
        if game_over == True:
            break
    pygame.quit()

    # print the best score
    best_info = OtherObjects.best_score()
    if score > best_info['score'] :
        print("\nCONGRATS!! YOU Beat The Best Score...")
        print(f"Your final score is: {score}")
    else:
        print(f"\nYour Final score is: {score}")
        print(f"Our best score is {best_info['score']} achieved by {best_info['name']}, in the {best_info['Difficulty']} difficulty")

    # data base management:
    # user_name, Difficulty, score !!
    OtherObjects.save_progress(user_name, Difficulty, score)


    input("\nThis is the END of the game\nThank you for playing\nPress ENTER to exit...")
    quit()
