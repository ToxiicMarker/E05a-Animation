#Copy the contents from http://arcade.academy/examples/move_mouse.html#move-mouse and see if you can figure out what is going on. Add comments to any uncommented lines
"""
This simple animation example shows how to move an item with the mouse, and
handle mouse clicks.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.move_mouse
"""

import arcade #imports arcade

SCREEN_WIDTH = 640 #horizontal
SCREEN_HEIGHT = 480 #vertical 
SCREEN_TITLE = "Move Mouse Example" #name of window


class Ball: #ball class is estblished
    def __init__(self, position_x, position_y, radius, color): # ball size position, and color parameters

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color 

    def draw(self): #ball is drawn with this
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)


class MyGame(arcade.Window): #window/game is established

    def __init__(self, width, height, title): #parameters for initialization

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False) #makes coursor disapear

        arcade.set_background_color(arcade.color.ASH_GREY) #background color

        # Create our ball
        self.ball = Ball(50, 50, 15, arcade.color.AUBURN) #not sure what the three intergers do. The last oen seesm to change the size of the ball

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.ball.draw() #calls on the ball

    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects. Happens approximately 60 times per second."""
        self.ball.position_x = x #updates the x and y positions apparently 60 times per second^
        self.ball.position_y = y

    def on_mouse_press(self, x, y, button, modifiers): # wow a buton!
        """
        Called when the user presses a mouse button.
        """
        print(f"You clicked button number: {button}")
        if button == arcade.MOUSE_BUTTON_LEFT: #this checks to see if the left mouse button is pressed down or not
            self.ball.color = arcade.color.BLACK # color of clicked button

    def on_mouse_release(self, x, y, button, modifiers):
        """
        Called when a user releases a mouse button.
        """
        if button == arcade.MOUSE_BUTTON_LEFT: # this checks to see if the left mouse button is not being pressed and changes the color to Auburn
            self.ball.color = arcade.color.AUBURN


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE) #Main fuction that defines the window and uses the parameters from the top of the page to set the size of the window
    arcade.run()


if __name__ == "__main__": #Still unsure about this is, magic?
    main()