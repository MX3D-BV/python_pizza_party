import socket

# Some colors for convenience
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
RED = [255, 0, 0]
GREEN = [0, 255, 0]
BLUE = [0, 0, 255]
CYAN = [0, 255, 255]
MAGENTA = [255, 0, 255]
YELLOW = [255, 255, 0]


def send_pixel(s: socket.socket, x: int, y: int, color: list[int]) -> None:
    """
    Send a pixel to the pixelflut server
    s: socket connection object
    x: x coordinate
    y: y coordinate
    color: list of 3 integers (0-255) representing the color (RGB)
        eg; [255, 255, 255] for white, [0, 0, 0] for black, [255, 0, 0] for red
    """

    # convert color to hex (html color code)
    color_code = "".join("{:02x}".format(x) for x in color)

    # Create message
    # PX tells the server to set a pixel
    # x and y are the coordinates
    # color_code is the color
    # \n end package
    msg = f"PX {x} {y} {color_code}\n"

    # convert message to bytes and send it
    s.send(msg.encode())


# Screen size is x:800 y:600 pixels; 0,0 is top left corner

# Connect to pixelflut server on (ip, port)
s = socket.create_connection(("10.11.12.127", 1234))

# Set a pixel at (100, 200) to cyan
send_pixel(s, 100, 200, CYAN)

# One pixel is a bit hard to see, so let's draw a line
for x in range(100, 500):
    send_pixel(s, x, 200, CYAN)


# Inspiration:
# Can you draw a square?
# Can you draw a square that changes color?
# Can you draw a line over the screen that bounces back and forth?
# Can you draw a circle?
# What about an image? (hint: use PIL to open an image and get the pixels, then send them to the server)
