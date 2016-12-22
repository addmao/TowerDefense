import arcade

class Model:
	def __init__(self, world, x, y, angle):
		self.x = x
		self.y = y
		self.angle = 0



class EasyMonster(Model):
	def __init__(self, x, y):
		self.sprite_list = arcade.SpriteList()
	
		self.x = x
		self.y = y 

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


