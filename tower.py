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


class Bullet(arcade.Sprite):
	##tower = self.tower
	def __init__(self, x, y):
		self.x = x
		self.y = y
	##def animate(self, delta):
        ##        self.x = 165
	##        self.y = 365

	def update(self):
		self.tower.center_x += 5
		self.tower.center_y += 5
	def  hitMonster(self, other, hit_size):
                return (abs(self.x - other.x) <= hit_size) and (abs(self.y - other.y) <= hit_size)

	
