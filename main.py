from aiosmtpd.controller import Controller
import handler


async def main(loop):
    my_controller = Controller(handler.MailHandler(), hostname='127.0.0.1', port=10025)
    my_controller.start()


if __name__ == '__main__':
    loop = handler.asyncio.get_event_loop()
    loop.create_task(main(loop=loop))
    loop.run_forever()
