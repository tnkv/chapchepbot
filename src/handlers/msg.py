from typing import Any

from aiogram import Router, F
from aiogram.enums import ChatType
from aiogram.filters import CommandStart
from aiogram.types import Message

import config
from src import utils

router = Router()


@router.message(CommandStart(), F.chat.type == ChatType.PRIVATE)
async def command_start(message: Message) -> Any:
    return await message.answer(
        text=utils.mediweitnuto(
            "Напиши мне любое сообщение и оно будет мейдветуно"
        )
    )


@router.message(F.from_user.id == config.DANYA_ID)
async def reply_to_danya(message: Message) -> Any:
    if len(message.text) > 600:
        return
    return await message.reply(
        f"<blockquote>{utils.mediweitnuto(message.html_text)}</blockquote>"
    )


@router.message(F.chat.type == ChatType.PRIVATE)
async def danyaficirovat(message: Message) -> Any:
    return await message.reply(
        utils.mediweitnuto(message.html_text[:2048]),
    )
