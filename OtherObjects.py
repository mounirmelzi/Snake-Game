
import pygame
import csv
pygame.init()

font = pygame.font.Font('arial.ttf', 25)
# font = pygame.font.SysFont('arial', 25)

SAVE_FILE = 'players_progress.csv'  # path to the file

BLOCK_SIZE = 20
SPEED = 15



def set_difficulty(difficulty):
    difficulties = {
        'easy': 15,
        'normal': 20,
        'hard': 25,
    }
    if type(difficulty) == str:
        if difficulty in difficulties:
            return difficulties[difficulty]
    print("You entered invalid difficulty level !!")
    print("Difficulty level defaults to normal...")
    return difficulties['normal']



def save_progress(name:str, difficulty:str, score:int, file=SAVE_FILE):
    with open(file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([name, difficulty, score])
    f.close()



def best_score(file=SAVE_FILE):
    best = {
        'name': '',
        'Difficulty': '',
        'score': 0,
    }
    with open(file, 'r') as f:
        csvfile = csv.DictReader(f)
        for row in csvfile :
            if int(row['score']) > best['score']:
                best['name'] = row['name']
                best['Difficulty'] = row['Difficulty']
                best['score'] = int(row['score'])
    f.close()
    return best

