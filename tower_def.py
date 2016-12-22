import arcade
from models import EasyMonster
from tower import Tower
from tower import Bullet

SCREEN_WIDTH = 750
SCREEN_HEIGHT = 550

class TowerDefense(arcade.Window):
	def __init__(self, width, height):
		super().__init__(width, height, title="Tower Defense")
		
		self.all_sprites_list = arcade.SpriteList()
		self.monster_list = arcade.SpriteList()
		self.bullet_list = arcade.SpriteList()		
		self.tower_list = arcade.SpriteList()

		arcade.set_background_color(arcade.color.WHITE)
		
		self.text_angle = 0
		self.time_elapsed = 0
		self.money = 0

		##self.tower = Tower(300, 400)
		self.tower_sprite = arcade.Sprite("assets/Tower1.png")
		self.tower_sprite.center_x = 500
		self.tower_sprite.center_y = 450	
		self.all_sprites_list.append(self.tower_sprite)		


		##self.bullet_list.append(self.tower_sprite)
		##self.easyMonster = EasyMonster(50, 175)
		self.monster = arcade.Sprite("assets/Monster_easy1.png")
		self.monster.center_x = 50
		self.monster.center_y = 175
		self.all_sprites_list.append(self.monster)

		self.monster_list.append(self.monster)
		self.bullet_list.append(self.tower_sprite)

		##self.monster_list.append()
		##self.tower = Tower(300, 400)
		##self.tower_sprite = arcade.Sprite("assets/Tower1.png")

		##self.bulletOne = Bullet(165, 175)
		##self.bulletOne_sprite = arcade.Sprite("assets/bulletOne.png")
		
		self.gameBoard = arcade.Sprite("assets/gameBoard.png")
		self.gameBoard.set_position(350, 300)	
	
	def animate(self, delta):
		self.text_angle += 1
		self.time_elapsed += delta
	
		self.all_sprites_list.update()	
		##bullet = self.bullet
		##monster = self.easyMonster
		##tower = self.tower
		
			
		
	
		
		self.money += 10

	def on_draw(self):
		arcade.start_render()

		self.all_sprites_list.draw()
		##tower = self.tower
		self.gameBoard.draw()
		
		arcade.draw_text("Time: {:5.1f}".format(self.time_elapsed), 500, 30, arcade.color.BLACK, 20)
		arcade.draw_text("MONEY: {:5d}".format(self.money), 100, 75, arcade.color.YELLOW)
		
		##self.easyMonster_sprite.draw()
		

		##if self.time_elapsed % 5 == 0:
			##self.sprite_list.append(self.easyMonster)
		

		##self.bulletOne_sprite.draw()
		##self.bulletOne_sprite.set_position(Bullet.x, Bullet.y)	

		self.tower_sprite.draw() 
		self.tower_sprite.set_position(tower.x, tower.y)
		self.money += 10

	def on_mouse_motion(self, x, y, button, modifiers):
		self.tower_sprite.center_x = x
		self.tower_sprite.center_y = y
	
	def on_mouse_press(self, x, y, button, modifiers):
		print(button)
		self.tower_sprite = arcade.Sprite("assets/Tower1.png")
		self.tower_sprite.center_x = 500
		self.tower_sprite.center_y = 450
		if money == 100:
			self.all_sprites_list.append(self.tower_sprite)
			self.tower_list.append(self.tower_sprite)	
		##bullet = Bullet("assets/bulletOne.png", 0.5 * 1.5)
	##	bullet.angle = 90

		##bullet.center_x = self.tower_sprite.center_x
		##bullet.bottom = self.tower_sprite.top

		##self.all_sprites_list.append(bullet)
		##self.bullet_list.append(bullet)

	##def on_mouse_release():
	##	self.all_sprites_list.pop(self.tower_sprite)
	##def on_key_press(self, key, key_modifiers):
	##	self.towerReady.on_key_press(key, key_modifiers)		

if __name__ == '__main__':
		window = TowerDefense(SCREEN_WIDTH, SCREEN_HEIGHT)	
		arcade.run()


