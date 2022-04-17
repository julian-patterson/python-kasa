import asyncio
import kasa
import time

async def rainbow():
    bulb = kasa.SmartBulb('10.0.0.87')
    bulb2 = kasa.SmartBulb('10.0.0.37')
    while True:
        for i in range(359):
            await bulb.update()
            await bulb2.update()
            await bulb.set_hsv(i, 100, 100)
            await bulb2.set_hsv(i, 100, 100)
            await bulb.update()
            await bulb2.update()
            time.sleep(1/1000)


            

async def main():
    bulb = kasa.SmartBulb('10.0.0.87')
    bulb2 = kasa.SmartBulb('10.0.0.37')
    while True:
        await bulb.update()
        await bulb2.update()
        await bulb.set_hsv(180, 100, 88)
        await bulb2.set_hsv(180, 100, 88)
        time.sleep()


if __name__ == '__main__':
    asyncio.run(rainbow())
