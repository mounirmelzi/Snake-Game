
from random import randint
from Colors import *
from Directions import *
from OtherObjects import *
from time import sleep


class SnakeGame():

    def __init__(self, width=640, hight=480):
        self.w = width
        self.h = hight

        # init display
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Snake')
        self.clock = pygame.time.Clock()
        pygame.mixer.music.load('BackgroundSound.wav')
        pygame.mixer.music.play(-1)

        # Starting detection
        OutputMessage = 'Press any KEY to start'
        text = font.render(OutputMessage, True, GREEN)
        self.display.blit(text, [self.w//2-10*len(OutputMessage)//2, self.h//2])
        pygame.display.flip()
        while True:
            to_break = False
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    to_break = True
                    break
            if to_break :
                break

        # init game state
        self.direction = Direction.RIGHT

        self.head = Point( self.w/2 , self.h/2 )
        self.snake = [  self.head,
                        Point(self.head.x-BLOCK_SIZE, self.head.y), 
                        Point(self.head.x-(2*BLOCK_SIZE), self.head.y) ]

        self.score = 0
        self.food = None
        self._place_food()
    # END __INIT__
        
        

    def _place_food(self):
        x = randint(0, (self.w-BLOCK_SIZE )//BLOCK_SIZE )*BLOCK_SIZE
        y = randint(0, (self.h-BLOCK_SIZE )//BLOCK_SIZE )*BLOCK_SIZE
        self.food = Point(x, y)
        if self.food in self.snake: 
            self._place_food()



    def play_step(self):
        # 1. collect user input
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.direction = Direction.LEFT
                elif event.key == pygame.K_RIGHT:
                    self.direction = Direction.RIGHT
                elif event.key == pygame.K_UP:
                    self.direction = Direction.UP
                elif event.key == pygame.K_DOWN:
                    self.direction = Direction.DOWN

        # 2. move
        self._move(self.direction) # update the head
        self.snake.insert(0, self.head) 

        # 3. check if game over
        game_over = False
        if self._is_collision():
            game_over = True
            return game_over, self.score

        # 4. place new food or just move
        if self.head == self.food:
            pygame.mixer.Sound("Get_Feed_sound.wav").play()
            self.score += 1
            self._place_food()
        else:
            self.snake.pop()

        # 5. update ui and clock
        self._update_ui()
        self.clock.tick(SPEED)

        # 6. return game over and score
        return game_over, self.score



    def _is_collision(self):
        # hits boundary
        if self.head.x>self.w-BLOCK_SIZE or self.head.x<0 or self.head.y>self.h-BLOCK_SIZE or self.head.y<0 :
            pygame.mixer.Sound("Game_Over_sound.wav").play()
            sleep(1)
            return True
        # hits its self
        if self.head in self.snake[1:] :
            pygame.mixer.Sound("Game_Over_sound.wav").play()
            sleep(1)
            return True

        return False



    def _update_ui(self):
        self.display.fill(BLACK)

        for pt in self.snake:
            pygame.draw.rect(self.display, BLUE1, pygame.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.display, BLUE2, pygame.Rect(pt.x+4, pt.y+4, BLOCK_SIZE-8, BLOCK_SIZE-8))

        pygame.draw.rect(self.display, RED, pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))

        text = font.render("Score: " + str(self.score), True, WHITE)
        self.display.blit(text, [0, 0])
        pygame.display.flip()



    def _move(self, direction):
        x = self.head.x
        y = self.head.y

        if direction == Direction.RIGHT:
            x += BLOCK_SIZE
        elif direction == Direction.LEFT:
            x -= BLOCK_SIZE    
        elif direction == Direction.DOWN:
            y += BLOCK_SIZE 
        elif direction == Direction.UP:
            y -= BLOCK_SIZE 

        self.head = Point(x, y)
