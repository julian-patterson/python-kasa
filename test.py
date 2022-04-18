import asyncio
import kasa
from time import sleep

bulb = kasa.SmartBulb('10.0.0.87')
bulb2 = kasa.SmartBulb('10.0.0.37')


async def rainbow():  # an effect
    while True:
        for i in range(359):
            await bulb.update()
            await bulb2.update()
            await bulb.set_hsv(i, 100, 100,  transition=50)
            await bulb2.set_hsv(i, 100, 100, transition=50)


async def nightmode():  # a scene
    while True:
        await bulb.update()
        await bulb2.update()
        await bulb.set_color_temp(2700, brightness=10)
        await bulb2.set_color_temp(2700, brightness=10)


async def scene(color):  # a scene // rotate through colors using a range
    if color == 'blue':
        await bulb.update()
        await bulb2.update()
        await bulb.set_hsv(300, 100, 100, transition=50)
        await bulb2.set_hsv(256, 100, 83, transition=50)

    if color == 'green':
        await bulb.update()
        await bulb2.update()
        await bulb.set_hsv(110, 100, 96, transition=50)
        await bulb2.set_hsv(51, 99, 96, transition=50)

    if color == 'red':
        await bulb.update()
        await bulb2.update()
        await bulb.set_hsv(0, 100, 88, transition=50)
        await bulb2.set_hsv(326, 86, 100, transition=50)


# a scene // time is seconds for user simplicity
async def gradual_light(time: int):
    await bulb.update()
    await bulb2.update()
    await bulb.set_color_temp(2700, transition=(time*1000))
    await bulb2.set_color_temp(2700, transition=(time*1000))


async def set_brightness(percentage):
    await bulb.update()
    await bulb2.update()
    await bulb.set_brightness(percentage)
    await bulb2.set_brightness(percentage)


async def off():
    await bulb.update()
    await bulb2.update()
    await bulb.turn_off(transition=2000)
    await bulb2.turn_off(transition=2000)


if __name__ == '__main__':
    asyncio.run(off())
