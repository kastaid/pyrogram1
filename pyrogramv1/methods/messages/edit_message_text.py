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

from typing import Union, List, Optional

from pyrogramv1 import raw
from pyrogramv1 import types
from pyrogramv1 import utils
from pyrogramv1.scaffold import Scaffold


class EditMessageText(Scaffold):
    async def edit_message_text(
        self,
        chat_id: Union[int, str],
        message_id: int,
        text: str,
        parse_mode: Optional[str] = object,
        entities: List["types.MessageEntity"] = None,
        disable_web_page_preview: bool = None,
        reply_markup: "types.InlineKeyboardMarkup" = None
    ) -> "types.Message":
        """Edit the text of messages.

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).

            message_id (``int``):
                Message identifier in the chat specified in chat_id.

            text (``str``):
                New text of the message.

            parse_mode (``str``, *optional*):
                By default, texts are parsed using both Markdown and HTML styles.
                You can combine both syntaxes together.
                Pass "markdown" or "md" to enable Markdown-style parsing only.
                Pass "html" to enable HTML-style parsing only.
                Pass None to completely disable style parsing.

            entities (List of :obj:`~pyrogramv1.types.MessageEntity`):
                List of special entities that appear in message text, which can be specified instead of *parse_mode*.

            disable_web_page_preview (``bool``, *optional*):
                Disables link previews for links in this message.

            reply_markup (:obj:`~pyrogramv1.types.InlineKeyboardMarkup`, *optional*):
                An InlineKeyboardMarkup object.

        Returns:
            :obj:`~pyrogramv1.types.Message`: On success, the edited message is returned.

        Example:
            .. code-block:: python

                # Simple edit text
                app.edit_message_text(chat_id, message_id, "new text")

                # Take the same text message, remove the web page preview only
                app.edit_message_text(
                    chat_id, message_id, message.text,
                    disable_web_page_preview=True)
        """

        r = await self.send(
            raw.functions.messages.EditMessage(
                peer=await self.resolve_peer(chat_id),
                id=message_id,
                no_webpage=disable_web_page_preview or None,
                reply_markup=await reply_markup.write(self) if reply_markup else None,
                **await utils.parse_text_entities(self, text, parse_mode, entities)
            )
        )

        for i in r.updates:
            if isinstance(i, (raw.types.UpdateEditMessage, raw.types.UpdateEditChannelMessage)):
                return await types.Message._parse(
                    self, i.message,
                    {i.id: i for i in r.users},
                    {i.id: i for i in r.chats}
                )
