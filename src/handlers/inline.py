import hashlib
from typing import Any

from aiogram import Router, F
from aiogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent

import config
from src import utils

router = Router()


@router.inline_query()
async def inline_handler(inline_query: InlineQuery):
    results = []
    text = inline_query.query or None
    if text is None:
        results.append(
            InlineQueryResultArticle(
                id='0',
                title='Необходимо ввести сообщение!!',
                input_message_content=InputTextMessageContent(
                    message_text=f"я не осилил написать ничего после меншона бота фиксируйте"
                )
            )
        )
    else:
        results.append(
            InlineQueryResultArticle(
                id=hashlib.md5(text.encode()).hexdigest(),
                title=utils.mediweitnuto('Отправить мейдвейтнутое сообщение'),
                input_message_content=InputTextMessageContent(
                    message_text=utils.mediweitnuto(text)
                )
            )
        )

    await inline_query.answer(
        results,
        is_personal=True,
        cache_time=0
    )