from pynput.keyboard import Controller
import time

keyboard = Controller()


def attack():
    keyboard.type("rpg hunt\n")
    # time.sleep(1.2)
    # keyboard.type("rpg heal\n")
    time.sleep(61)


def drill():
    keyboard.type("rpg drill\n")
    time.sleep(1.2)
    attack()
    attack()
    attack()
    attack()
    attack()


# def heal():
#     keyboard.type("rpg heal\n")
#     time.sleep(1.5)
#
#
# def attack():
#     keyboard.type("rpg hunt\n")
#     time.sleep(60.2)
#
#
# def pickaxe():
#     keyboard.type("rpg pickaxe\n")
#     time.sleep(1.2)
#     attack()
#     attack()
#     heal()
#     attack()
#     attack()
#     heal()
#     attack()
#
#
# def pickaxe2():
#     keyboard.type("rpg pickaxe\n")
#     time.sleep(1.2)
#     attack()
#     heal()
#     attack()
#     attack()
#     heal()
#     attack()
#     attack()
#     heal()


def craft_dismantle():
    keyboard.type("rpg craft epic log all\n")
    time.sleep(1.5)
    keyboard.type("rpg dismantle epic log all\n")
    time.sleep(1.5)


time.sleep(3)
while True:
    keyboard.type("rpg farm\n")
    time.sleep(1.5)
    drill()
    drill()
    time.sleep(1.5)
    # craft_dismantle()
