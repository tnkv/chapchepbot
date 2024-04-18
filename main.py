import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from src.handlers import msg, inline

import config

dp = Dispatcher()
bot = Bot(
    token=config.DANYA_TOKEN,
    default=DefaultBotProperties(
        parse_mode="HTML"
    )
)


async def main() -> None:
    dp.include_routers(
        msg.router,
        inline.router
    )

    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logging.getLogger("aiogram.event").setLevel(logging.WARNING)
    try:
        asyncio.run(main())
    except (SystemExit, KeyboardInterrupt):
        logging.warning('Bot stopped')
