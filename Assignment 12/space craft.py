import random
import math
import time
import arcade


class Enemy(arcade.Sprite):
    def __init__(self ,w , h):
        super().__init__(":resources:images/space_shooter/playerShip2_orange.png")
        self.speed = 3
        self.width = 50
        self.height = 50
        self.center_x = random.randint(0 , w)
        self.center_y = h
        self.angle = 180
        self.start_timer = time.time()

    def move(self):
        self.center_y -= self.speed

    def increase_speed(self):
        self.end_timer = time.time()
        if self.end_timer - self.start_timer > 10 : 
            self.speed += 1

        


class Bullet(arcade.Sprite):
    def __init__(self, host):
        super().__init__(":resources:images/space_shooter/laserRed01.png")
        self.speed = 5
        self.angle = host.angle
        self.center_x = host.center_x
        self.center_y = host.center_y

    def move(self):
        angle_radians = math.radians(self.angle)
        self.center_x -= self.speed * math.sin(angle_radians)
        self.center_y += self.speed * math.cos(angle_radians)



class Spacecraft(arcade.Sprite):
    def __init__(self,w,h):
        super().__init__(":resources:images/space_shooter/playerShip1_blue.png")
        self.width = 50
        self.height = 50
        self.center_x = w//2
        self.center_y = 50
        self.angle = 0
        self.change_angle = 0
        self.bullets_list = []
        self.speed = 3
        self.score = 0

    def rotate(self):
        self.angle += self.change_angle * self.speed

    def fire(self):
        self.bullets_list.append(Bullet(self)) 

    def add_score(self):
        self.score +=1


class Game(arcade.Window):
    def __init__(self):
        self.w = 800
        self.h = 600
        super().__init__(self.w,self.h,"Super Space Craft")
        arcade.set_background_color= arcade.color.BLACK
        self.background_image = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.myspaceship = Spacecraft(self.w , self.h)
        self.enemy_list = []
        self.start_time = time.time()
        self.hearts = arcade.load_texture("heart.png")
        self.lives = 3
        self.enter_time = random.randint(1,6)
        self.flag = 0
        self.bullet_sound = arcade.sound.load_sound(":resources:sounds/laser2.wav")
        self.explosion_sound = arcade.sound.load_sound(":resources:sounds/explosion2.wav")


    def on_draw(self):
        arcade.start_render()
        

        if self.lives > 0 :
            arcade.draw_lrwh_rectangle_textured(0 , 0 , self.w , self.h , self.background_image)
            self.myspaceship.draw()

            
        
        for i in range(len(self.myspaceship.bullets_list)):
            self.myspaceship.bullets_list[i].draw()

        for i in range(len(self.enemy_list)):
            self.enemy_list[i].draw()

        

        arcade.draw_text(
            f"score:{self.myspaceship.score}", 650 , 50 , arcade.color.WHITE, 20
        )

        if self.lives == 3:    
            for i in range(10,120,40):
                arcade.draw_lrwh_rectangle_textured(i , 10 , 30 , 30 , self.hearts)
        elif self.lives == 2:    
            for i in range(40,120,40):
                arcade.draw_lrwh_rectangle_textured(i , 10 , 30 , 30 , self.hearts) 
        elif self.lives == 1:    
            for i in range(80,120,40):
                arcade.draw_lrwh_rectangle_textured(i , 10 , 30 , 30 , self.hearts)           
        elif self.lives < 1 :
            arcade.draw_text('Game Over', self.w//4, self.h//2, arcade.color.red, width=400 ,font_size = 45, align='center')

    def on_update(self, delta_time):
        self.end_time = time.time()
        if self.end_time - self.start_time > self.enter_time:
            self.enemy_list.append(Enemy(self.w , self.h)) 
            self.start_time = time.time()


        self.myspaceship.rotate()


        for i in range(len(self.myspaceship.bullets_list)):
            self.flag = 1
            self.myspaceship.bullets_list[i].move()
              


        for i in range(len(self.enemy_list)):
            self.enemy_list[i].move()

            

        for e in self.enemy_list:
            for b in self.myspaceship.bullets_list:
                if arcade.check_for_collision(e ,b):
                    self.enemy_list.remove(e)
                    self.myspaceship.bullets_list.remove(b)
                    arcade.play_sound(self.explosion_sound)
                    self.myspaceship.score +=1
                    print(self.myspaceship.score)


        for en in self.enemy_list:
            if en.center_y == 0:
                self.enemy_list.remove(en)
                self.lives -= 1

    def on_key_press(self , key , modifiers):
        if key ==  arcade.key.RIGHT:
            self.myspaceship.change_angle = -1
        elif key == arcade.key.LEFT:
            self.myspaceship.change_angle = 1
        elif key == arcade.key.SPACE:
            self.myspaceship.fire()
            if self.flag >= 1:
                arcade.play_sound(self.bullet_sound)
                self.flag = 0  

    def on_key_release(self, symbol ,modifiers):
        self.myspaceship.change_angle = 0



game = Game()
arcade.run()