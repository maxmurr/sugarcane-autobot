import pyautogui as pt
from time import sleep
from pywinauto import application
import pynput

# Helper function
def nav_to_image(image, click,  off_x=0, off_y=0):
    position = pt.locateCenterOnScreen(image, confidence=0.5)

    if position is None:
        print(f'{image} not found...')
        return 0
    else:
        pt.moveTo(position, duration=0.1)
        pt.moveRel(off_x, off_y, duration=0.1)
        pt.click(clicks=click, interval=0.3)

def move_character(key_press, duration, action='walking'):
    pt.keyDown('a')
    pt.keyDown(key_press)

    if action == 'attack':
        pt.mouseDown(button='left')

    sleep(duration)
    pt.keyUp('x')
    pt.keyUp(key_press)

def move_character_a(key_press, duration, action='walking'):
    pt.keyDown(key_press)

    sleep(duration)
    pt.keyUp(key_press)

def move_character_d(key_press, duration, action='walking'):
    pt.keyDown(key_press)

    sleep(duration)
    pt.keyUp(key_press)

def locate_stuck():
    positon = pt.locateCenterOnScreen('C:\maxmurr\workspace\Minecraft\AutoMine\images\stuck.PNG', confidence=0.7)
    if positon is None:
        return False
    else:
        return True

def locate_netherwart():
    position = pt.locateCenterOnScreen('C:\maxmurr\workspace\Minecraft\AutoMine\images\wart.png', confidence=0.3)

    if position is None:
        return False
    else:
        return True


def locate_reconnect():
    position = pt.locateCenterOnScreen('C:\maxmurr\workspace\Minecraft\AutoMine\images\connect.PNG', confidence=0.8)

    if position is None:
        return False
    else:
        return True

def locate_bedrock():
    position = pt.locateOnScreen('C:\maxmurr\workspace\Minecraft\AutoMine\images\menu.PNG', confidence=0.4)

    if position is None:
        return False
    else:
        return True

def move_smooth(xm, ym, t):
    mouse = pynput.mouse.Controller()
    for i in range(t):
        if i < t/2:
            h = i
        else:
            h = t - i
        mouse.move(h*xm, h*ym)
        sleep(1/60)

def back_to_island():
    pt.press('/')
    pt.press('i')
    pt.press('s')
    pt.press('enter')

def set_home():
    pt.press('/')
    pt.press('s')
    pt.press('e')
    pt.press('t')
    pt.press('h')
    pt.press('o')
    pt.press('m')
    pt.press('e')
    pt.press('enter')

def back_to_skyblock():
    pt.press('/')
    pt.press('s')
    pt.press('k')
    pt.press('y')
    pt.press('b')
    pt.press('l')
    pt.press('o')
    pt.press('c')
    pt.press('k')
    pt.press('enter')

def autofarm_sugarcane():
    pt.keyDown('k')
    move_character_a('d', 18, 'attack')
    move_character_d('s', 18, 'attack')


def anti_stuck():
    pt.keyDown('space')
    pt.keyUp('space')
    pt.keyDown('space')
    pt.keyUp('space')
    pt.keyDown('ctrl')
    sleep(0.5)
    pt.keyUp('ctrl')

# Start the game
def main():
    
    print('Starting SugarCane Farming...')
    sleep(3)
    count = 0
    while True:
        if count % 4 == 0:
            back_to_island()
            set_home()
            back_to_skyblock()

        # Autofarm Wart
        pt.keyDown('k')
        autofarm_sugarcane()
        pt.keyDown('w')
        sleep(0.1)
        pt.keyUp('w')
        pt.keyDown('s')
        sleep(0.2)
        pt.keyUp('s')

        count += 1

main()

# Test
