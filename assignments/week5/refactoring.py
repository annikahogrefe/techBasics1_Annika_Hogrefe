# refactored code of week 4

#import
import random
import turtle

# global constants (uppercase)
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800
TRIANGLE_SIZE = 50
INITIAL_NOISE = 1
NUM_CIRCLES = 15
BG_COLOR = "black"
TRIANGLE_COLOR = "red"
CIRCLE_COLOR = "yellow"


# functions
def draw_single_triangle(size, noise_level):
    angle = random.uniform(-noise_level, noise_level)
    turtle.right(angle)
    # draw triangle
    for _ in range(6):
        turtle.forward(size)
        turtle.right(120)
    return angle


def draw_triangle_grid(): #adding noise
    turtle.color(TRIANGLE_COLOR)
    current_noise = INITIAL_NOISE
    for y in range(20):
        for x in range(15):
            turtle.penup()
            grid_x = -SCREEN_WIDTH / 2 + (x * TRIANGLE_SIZE)
            grid_y = SCREEN_HEIGHT / 2 - (y * TRIANGLE_SIZE)
            turtle.goto(grid_x, grid_y)
            turtle.pendown()

            applied_angle = draw_single_triangle(TRIANGLE_SIZE, current_noise)
            turtle.left(applied_angle)

        current_noise += 8


def draw_random_circles(count):
    turtle.fillcolor(CIRCLE_COLOR)
    for _ in range(count):
        # random positions
        rand_x = random.randint(-SCREEN_WIDTH // 2, SCREEN_WIDTH // 2)
        rand_y = random.randint(-SCREEN_HEIGHT // 2, SCREEN_HEIGHT // 2)
        rand_radius = random.randint(10, 50)
        # move to position
        turtle.penup()
        turtle.goto(rand_x, rand_y)
        turtle.pendown()
        # filled circle
        turtle.begin_fill()
        turtle.circle(rand_radius)
        turtle.end_fill()

# main function
def main():
    # general setup
    turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    turtle.tracer(0, 0)  # disable animation
    turtle.bgcolor(BG_COLOR)

    # rendering
    draw_triangle_grid()
    draw_random_circles(NUM_CIRCLES)

    # end
    turtle.penup()
    turtle.update()
    turtle.done()

if __name__ == "__main__":
    main()

    # global constants done completely by myself
    # had some help with the functions from gemini, but mostly let it create a general structure I could "fill in" because I always struggle with where and how to start
    # + asked questions if something did not work / calmed me down when I panicked about a terminator error lol


