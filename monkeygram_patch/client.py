from pyrogram import Client
from pyrogram.types import Message
from typing import List, Optional
import asyncio


async def edit_long_message(
    self: Message,
    text: str,
    *,
    parse_mode: Optional[str] = None,
    max_length: int = 4096,
    delay: float = 0.5,
    preserve_lines: bool = True,
    disable_web_page_preview: bool = True
) -> List[Message]:
    """
    Edits long messages in Telegram by splitting them into parts if they exceed the maximum length.

    Parameters:
    ------------
    text : str
        The text of the message to be edited. The message will be split into parts if its length
        exceeds max_length.

    parse_mode : Optional[str], default None
        The formatting of the text (e.g., "html" or "markdown").

    max_length : int, default 4096
        The maximum length of a single message. If the length of the text exceeds this limit,
        it will be split into several parts.

    delay : float, default 0.5
        The delay between sending each part of the message (in seconds).

    preserve_lines : bool, default True
        If True, the formatting of the lines will be preserved. Each line will be sent as a separate part.
        If False, the entire text will be split into parts based on the max_length.

    disable_web_page_preview : bool, default True
        Disables the web page preview in the message.

    Returns:
    -----------------------
    List[Message]
        A list of Message objects that were sent.
    """

    client = self._client  # Getting the client via _client since the message does not have a client attribute directly.

    # Splitting the text into parts while preserving lines
    if preserve_lines:
        parts = []
        current = ""
        for line in text.split('\n'):
            if len(current) + len(line) + 1 > max_length:
                if current:
                    parts.append(current)
                    current = line
                else:
                    parts.extend([line[i:i + max_length] for i in range(0, len(line), max_length)])
            else:
                current = '\n'.join([current, line]) if current else line
        if current:
            parts.append(current)
    else:
        parts = [text[i:i + max_length] for i in range(0, len(text), max_length)]

    # Sending/editing messages in parts
    messages = []
    for i, part in enumerate(parts):
        try:
            if i == 0:
                # Edit the first message
                msg = await client.edit_message_text(
                    chat_id=self.chat.id,
                    message_id=self.message_id,
                    text=part,
                    parse_mode=parse_mode,
                    disable_web_page_preview=disable_web_page_preview
                )
            else:
                # Send new messages for the remaining parts
                msg = await client.send_message(
                    chat_id=self.chat.id,
                    text=part,
                    parse_mode=parse_mode,
                    disable_web_page_preview=disable_web_page_preview
                )
            messages.append(msg)
            # Delay between sending parts
            if i < len(parts) - 1 and delay > 0:
                await asyncio.sleep(delay)
        except Exception as e:
            # If an error occurs, send the message normally
            msg = await client.send_message(
                chat_id=self.chat.id,
                text=part,
                parse_mode=parse_mode,
                disable_web_page_preview=disable_web_page_preview
            )
            messages.append(msg)

    return messages


async def send_long_message(
    self: Client,
    chat_id: int,
    text: str,
    *,
    parse_mode: Optional[str] = None,
    max_length: int = 4096,
    delay: float = 0.5,
    preserve_lines: bool = True,
    reply_to_message_id: Optional[int] = None,
    disable_web_page_preview: bool = True
) -> List[Message]:
    """
    Sends long messages in Telegram by splitting them into parts if they exceed the maximum length.

    Parameters:
    ------------
    chat_id : int
        The ID of the chat to send the message to.

    text : str
        The text of the message to be sent. The message will be split into parts if its length
        exceeds max_length.

    parse_mode : Optional[str], default None
        The formatting of the text (e.g., "html" or "markdown").

    max_length : int, default 4096
        The maximum length of a single message. If the length of the text exceeds this limit,
        it will be split into several parts.

    delay : float, default 0.5
        The delay between sending each part of the message (in seconds).

    preserve_lines : bool, default True
        If True, the formatting of the lines will be preserved. Each line will be sent as a separate part.
        If False, the entire text will be split into parts based on the max_length.

    reply_to_message_id : Optional[int], default None
        The ID of the message to reply to.

    disable_web_page_preview : bool, default True
        Disables the web page preview in the message.

    Returns:
    -----------------------
    List[Message]
        A list of Message objects that were sent.
    """

    # Splitting the text into parts while preserving lines
    if preserve_lines:
        parts = []
        current = ""
        for line in text.split('\n'):
            if len(current) + len(line) + 1 > max_length:
                if current:
                    parts.append(current)
                    current = line
                else:
                    parts.extend([line[i:i + max_length] for i in range(0, len(line), max_length)])
            else:
                current = '\n'.join([current, line]) if current else line
        if current:
            parts.append(current)
    else:
        parts = [text[i:i + max_length] for i in range(0, len(text), max_length)]

    # Sending messages in parts
    messages = []
    for i, part in enumerate(parts):
        try:
            if i == 0:
                # Send the first message
                msg = await self.send_message(
                    chat_id=chat_id,
                    text=part,
                    parse_mode=parse_mode,
                    disable_web_page_preview=disable_web_page_preview,
                    reply_to_message_id=reply_to_message_id
                )
            else:
                # Send the remaining messages
                msg = await self.send_message(
                    chat_id=chat_id,
                    text=part,
                    parse_mode=parse_mode,
                    disable_web_page_preview=disable_web_page_preview
                )
            messages.append(msg)
            # Delay between parts
            if i < len(parts) - 1 and delay > 0:
                await asyncio.sleep(delay)
        except Exception as e:
            # If an error occurs, send the message normally
            msg = await self.send_message(
                chat_id=chat_id,
                text=part,
                parse_mode=parse_mode,
                disable_web_page_preview=disable_web_page_preview
            )
            messages.append(msg)

    return messages
