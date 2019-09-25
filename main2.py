#Copy the contents from http://arcade.academy/examples/move_keyboard.html#move-keyboard and see if you can figure out what is going on. Add comments to any uncommented lines
"""
This simple animation example shows how to move an item with the keyboard.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.move_keyboard
"""

import arcade

SCREEN_WIDTH = 640 #screen width
SCREEN_HEIGHT = 480 #screen height
SCREEN_TITLE = "Move Keyboard Example" #title
MOVEMENT_SPEED = 3 #speed of ball movement 


class Ball: #creates the ball class
    def __init__(self, position_x, position_y, change_x, change_y, radius, color): #defines the parameters of hte initialization function

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x #variables for the ball #x position
        self.position_y = position_y #y position
        self.change_x = change_x #change in x
        self.change_y = change_y # change in y
        self.radius = radius #radius of the ball
        self.color = color #color of the ball

    def draw(self): #draws the ball
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)

    def update(self): #updates the position of the ball and adds the changes in position of the ball tot eh position of the ball
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction, # this is interesting
        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > SCREEN_WIDTH - self.radius: #keeps the ball on the screen in teh x axis
            self.position_x = SCREEN_WIDTH - self.radius

        if self.position_y < self.radius: 
            self.position_y = self.radius

        if self.position_y > SCREEN_HEIGHT - self.radius: #keeps the ball on the screen in the y direction
            self.position_y = SCREEN_HEIGHT - self.radius


class MyGame(arcade.Window): #game class

    def __init__(self, width, height, title): #parameters for initialization

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False) #gets rid of the cursor icon

        arcade.set_background_color(arcade.color.ASH_GREY) #sets background color

        # Create our ball
        self.ball = Ball(50, 50, 10, 5, 25, arcade.color.AUBURN) #creates the ball, color, radius, I do not know what the first two inegers do, but the third and fourth integers control horizontal movement, and verticle movement respectively.

    def on_draw(self): 
        """ Called whenever we need to draw the window. """#
        arcade.start_render()
        self.ball.draw()

    def update(self, delta_time):
        self.ball.update() #updates the ball

    def on_key_press(self, key, modifiers): #cahnges x and y movement speed with up down right and left key presses
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.ball.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.ball.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.ball.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.ball.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers): #sets the movement speed of the ball to 0 if none of the four buttons are being pressed
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ball.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.ball.change_y = 0


def main(): #main function
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__": #magic
    main()