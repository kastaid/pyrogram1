#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from uuid import uuid4

import pyrogramv1
from pyrogramv1 import types
from ..object import Object

"""- :obj:`~pyrogramv1.types.InlineQueryResultCachedAudio`
    - :obj:`~pyrogramv1.types.InlineQueryResultCachedDocument`
    - :obj:`~pyrogramv1.types.InlineQueryResultCachedGif`
    - :obj:`~pyrogramv1.types.InlineQueryResultCachedMpeg4Gif`
    - :obj:`~pyrogramv1.types.InlineQueryResultCachedPhoto`
    - :obj:`~pyrogramv1.types.InlineQueryResultCachedSticker`
    - :obj:`~pyrogramv1.types.InlineQueryResultCachedVideo`
    - :obj:`~pyrogramv1.types.InlineQueryResultCachedVoice`
    - :obj:`~pyrogramv1.types.InlineQueryResultAudio`
    - :obj:`~pyrogramv1.types.InlineQueryResultContact`
    - :obj:`~pyrogramv1.types.InlineQueryResultGame`
    - :obj:`~pyrogramv1.types.InlineQueryResultDocument`
    - :obj:`~pyrogramv1.types.InlineQueryResultGif`
    - :obj:`~pyrogramv1.types.InlineQueryResultLocation`
    - :obj:`~pyrogramv1.types.InlineQueryResultMpeg4Gif`
    - :obj:`~pyrogramv1.types.InlineQueryResultPhoto`
    - :obj:`~pyrogramv1.types.InlineQueryResultVenue`
    - :obj:`~pyrogramv1.types.InlineQueryResultVideo`
    - :obj:`~pyrogramv1.types.InlineQueryResultVoice`"""


class InlineQueryResult(Object):
    """One result of an inline query.

    Pyrogram currently supports results of the following types:

    - :obj:`~pyrogramv1.types.InlineQueryResultArticle`
    - :obj:`~pyrogramv1.types.InlineQueryResultPhoto`
    - :obj:`~pyrogramv1.types.InlineQueryResultAnimation`
    """

    def __init__(
        self,
        type: str,
        id: str,
        input_message_content: "types.InputMessageContent",
        reply_markup: "types.InlineKeyboardMarkup"
    ):
        super().__init__()

        self.type = type
        self.id = str(uuid4()) if id is None else str(id)
        self.input_message_content = input_message_content
        self.reply_markup = reply_markup

    async def write(self, client: "pyrogramv1.Client"):
        pass
