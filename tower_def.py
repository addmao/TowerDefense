import arcade

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 600

class TowerDefense(arcade.Window):
	def __init__(self, width, height):
		super().__init__(width, height, title="Tower Defense")

		arcade.set_background_color(arcade.color.CYAN)
		
		self.text_angle = 0
		self.time_elapsed = 0
	
	##	self.xPosition = xPosition	
    	##	self.yPosition = yPosition

	##	self.deltaX = 0
	##	self.deltaY = 0

		self.easyMonster1 = arcade.Sprite("assets/Monster_easy1.png")
		self.easyMonster1.set_position(100, 200)
		
	def animate(self, delta_time):
		self.text_angle += 1
		self.time_elapsed += delta_time

	def canMove(self):
		self.xPos += deltaX
		self.yPos += deltaY

		

	def on_draw(self):
		arcade.start_render()

		start_x = 100
		start_y = 100
		arcade.draw_point(start_x, start_y, arcade.color.BLACK, 5)
		arcade.draw_text("TOWER DEFENSE!!!", start_x, start_y, arcade.color.BLACK, 14, width=100, align="center", anchor_x="center", anchor_y="center", rotation=0.0)
		
		start_x = 400
		start_y = 200
		arcade.draw_text("Time: {:5.1f}".format(self.time_elapsed), start_x, start_y, arcade.color.BLACK, 30)

		self.easyMonster1.draw()

if __name__ == '__main__':
	window = TowerDefense(SCREEN_WIDTH, SCREEN_HEIGHT)	
	arcade.run()


