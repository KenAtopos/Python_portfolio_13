import time
import pyautogui
from PIL import ImageGrab

# Coordinates of the dinosaur and the first cactus
dino_pos = (240, 346)
cactus_pos = (345, 364)

# Threshold for detecting obstacles
threshold = 50


# Press the space bar to jump
def jump():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    pyautogui.keyUp('space')


# Check if an obstacle is in the way
def is_obstacle():
    box = (cactus_pos[0], cactus_pos[1], cactus_pos[0] + 15, cactus_pos[1] + 30)
    image = ImageGrab.grab(box)
    gray_image = image.convert('L')
    pixels = gray_image.getdata()
    avg = sum(pixels) / len(pixels)
    if avg < threshold:
        return True
    return False


# Start the game
time.sleep(3)
while True:
    if is_obstacle():
        jump()
        time.sleep(0.1)
