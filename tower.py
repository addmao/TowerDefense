import arcade
	
class Tower(arcade.Sprite):
        def __init__(self, x, y):
                self.x = x
                self.y = y
	##	self.tower_list = arcade.SpriteList()
        def animate(self, delta):
                self.x = 650
                self.y = 700

        def hitEnemy(self, enemy, hit_size):
                return (abs(self.x - enemy.x) <= hit_size) and (abs(self.y - enemy.y) <= hit_size)

	##def on_key_press(self, key, key_modifiers):
	##	if key == arcade.key.SPACE:
	##		self.towerReady_sprite.draw()

	##def shootMonster():
		##Shoot Bullet



	 


	
