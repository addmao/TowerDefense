import arcade

class Model:
	def __init__(self, world, x, y, angle):
		self.world = world		
		self.x = x
		self.y = y
		self.angle = 0
	
	def hit(self, other, hit_size):
		return (abs(self.x - other.x) <= hit_size) and (abs(self.y - other.y) <= hit_size)



class Monster(Model):
	def __init__(self, x, y):
		super().__init__(world, x, y, 0)
		##self.monster_list = arcade.SpriteList()
		
		self.x = x
		self.y = y 
		for i in range(100):
			monster = arcade.Sprite("assets/Monster_easy1.png")
			monster.center_x = x
			monster.center_y = y

			self.all_sprites_list.append(monster)
			self.monster_list.append(monster)
	
	def animate(self, delta):
		##easyMonster = self.easyMonster
		##self.x += 5
		if self.x <= 800 :
			self.x += 5
			print(self.x, self.y)	
	
		if self.x >= 175 and self.y < 265:
			self.y += 5
			self.x = 175
			print(self.x, self.y)   	
	##	self.x += 5
		
		if self.x > 265 and self.y != 365:
			self.y += 5
			self.x = 270
			print(self.x, self.y)
	
	##	self.x -= 5
		if self.x <= 270 and self.x > 120 and self.y == 365:
			self.x -= 10
			##self.y = 425	
			print(self.x, self.y)
			
		if self.x > 120 and self.y > 365 and self.y <= 450 :
			self.y += 5
			self.x = 120

	def aliveMonster(self, x, y):
		self.aliveImage = arcade.Sprite("assets/clearMonster.png")

class Tower(Model):
	def __init__(self, world, x, y):
		super().__init__(world, x, y, 0)

	def buy():
		self.money -= 100


class Bullet(Model):
	def __init__(self, world, x, y):
		super().__init__(world, x, y, 0)
	def update(self):
		self.center_x += 5
		self.center_y += 5

class World:
	NUMBER_OF_MONSTER = 100
	NUMBER_OF_BULLET = 50
		
	def __init__(self, width, height):
		self.width = width
		self.height = height

		##self.monster = Monster(self, 50, 175)
		self.tower = Tower(self, 500, 500)
		self.monsters = []
		self.bullet_list = arcade.SpriteList()
		
		for i in range(NUMBER_OF_BULLET):
			bullet = Bullet(self, 0, 0, 0, 0)
			self.bullet_list.append(bullet)

		for i in range(NUMBER_OF_MONSTER):
			monster = Monster(self, 0, 0, 0, 0)
			self.monsters.append(monster)

		self.money = 100

	def animate(delta):
		self.text_angle += 1
		self.time_elapsed += delta
		
		for bullet in self.bullet_list:
			bullet.animate(delta)
			if self.bullet.hit(monster, 10):
				self.monster.aliveMonster()
				self.money += 20
	
		for monster in self.monsters:
			monster.animate(delta)
			
	def on_mouse_motion(self, x, y, button, modifiers):
		self.tower_sprite.center_x = x
		self.tower_sprite.center_y = y

	def on_mouse_press(self, x, y, button, modifiers):
		print(button)
		if money == 100 and arcade.MOUSE_BUTTON_LEFT:
			self.tower.buy()
	
























