import arcade

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 600

class TowerDefense(arcade.Window):
	def __init__(self, width, height):
		super().__init__(width, height)

		arcade.set_background_color(arcade.color.BROWN)

	def on_draw(self):
		arcade.start_render()

if __name__ == '__main__':
	window = TowerDefense(SCREEN_WIDTH, SCREEN_HEIGHT)
	arcade.run()


