import asyncio
import kasa
import time

bulb = kasa.SmartBulb('10.0.0.87')
bulb2 = kasa.SmartBulb('10.0.0.37')

async def rainbow():
    while True:
        for i in range(359):
            await bulb.update()
            await bulb2.update()
            await bulb.set_hsv(i, 100, 100,  transition= 50)
            await bulb2.set_hsv(i, 100, 100, transition= 50)


async def fade_rainbow():
    while True:
        for i in range(359):
            await bulb.update()
            await bulb2.update()
            await bulb.set_hsv(i, 100, 100)
            await bulb2.set_hsv(i, 100, 100)
            await bulb.turn_off(transition= 1000)
            await bulb2.turn_off(transition= 1000)
            i += 10

        

if __name__ == '__main__':
    #asyncio.run(rainbow())
    asyncio.run(fade_rainbow())
