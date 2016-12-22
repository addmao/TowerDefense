import arcade

from models import World, Tower, Bullet

SCREEN_WIDTH = 750
SCREEN_HEIGHT = 550

class Model(arcade.Sprite):
	def __init__(self, *args, **kwargs):
		self.model = kwargs.pop('model', None)
		super().__init__(*args, **kwargs)

	def sync_with_model(self):
		if self.model:
			self.set_position(self.model.x, self.model.y)
			self.angle = self.model.angle

	def draw(self):
		self.sync_with_model()
		super().draw()

class TowerDefense(arcade.Window):
	def __init__(self, width, height):
		super().__init__(width, height, title="Tower Defense")
		
		self.bullet_list = arcade.SpriteList()		

		arcade.set_background_color(arcade.color.WHITE)
		
		self.text_angle = 0
		self.time_elapsed = 0
		self.money = 0

		self.world = World(width, height)

		self.tower_sprite = Model("assets/Tower1.png", model=self.world.tower)
		self.monster_sprite = []
		for monster in self.world.monsters:
			self.monster_sprites.append(ModelSprite("assets/Monster_easy1.png", scale=0.5, model=monster))
	
		self.bullet_sprite = []
		for bullet in self.world.bullets:
			self.monster_sprites.append(ModelSprite("assets/bulletOne.png", scale=0.5, model=bullet))

		for i in range(100):
			self.monster = arcade.Sprite("assets/Monster_easy1.png")
			self.monster.center_x = 50
			self.monster.center_y = 175
			self.all_sprites_list.append(self.monster)
			self.monster_list.append(self.monster)


		
		bullet = Bullet("assets/bulletOne.png", 0.5 * 1.5)

		bullet.center_x = self.tower_sprite.center_x
		bullet.center_y = self.tower_sprite.center_y

		self.all_sprites_list.append(bullet)
		self.bullet_list.append(bullet)
		
		##self.tower = Tower(300, 400)
		##self.tower_sprite = arcade.Sprite("assets/Tower1.png")

		##self.bulletOne = Bullet(165, 175)
		##self.bulletOne_sprite = arcade.Sprite("assets/bulletOne.png")
		
		self.gameBoard = arcade.Sprite("assets/gameBoard.png")
		self.gameBoard.set_position(350, 300)
	
	def animate(self, delta):
		self.world.animate(delta)
		
	
		self.all_sprites_list.update()	
		
		for bullet in self.bullet_list:
			hit_list = arcade.check_for_collision_with_list(bullet, self.monster_list)		
		if len(hit_list) > 0:
			bullet.kill()

		for monster in self.monster_list:
			monster.kill()
			self.money += 20
		
##		if bullet.bottom > SCREEN_HEIGHT:
##			bullet.kill()

	def on_draw(self):
		arcade.start_render()

		self.all_sprites_list.draw()
		self.gameBoard.draw()
		
		self.tower_sprite.draw()
		self.monster_sprite.draw()
		self.bullet.draw()
		for sprite in  self.monster_sprites:
			sprite.draw()

		arcade.draw_text("Time: {:5.1f}".format(self.time_elapsed), 500, 30, arcade.color.BLACK, 20)
		arcade.draw_text("MONEY: {:5d}".format(self.money), 100, 75, arcade.color.YELLOW)
		
		##if self.time_elapsed % 5 == 0:
			##self.sprite_list.append(self.easyMonster)

		self.money += 10
	
				
##class Tower:




class Monster:
	def animate(delta):
		if self.x <= 800:
			self.x += 5
			print(self.x, self.y)
		
		if self.x >= 175 and self.y < 265:
			self.y += 5
			self.x = 175
			print(self.x, self.y)
		
		if self.x > 265 and self.y != 365:
			self.y += 5
			self.x = 270
			print(self.x, self.y)

		if self.x <= 270 and self.x > 120 and self.y == 365:
			self.x -= 10
			print(self.x, self.y)

		if self.x > 120 and self.y > 365 and self.y <= 450 :
			self.y += 5
			self.x = 120

class Bullet(arcade.Sprite):
        def update(self):
                self.center_x += 5
                self.center_y += 5


if __name__ == '__main__':
		window = TowerDefense(SCREEN_WIDTH, SCREEN_HEIGHT)	
		arcade.run()


