# Long Message Handler for Pyrogram

## Description

This project provides two methods for handling long messages in Telegram using the Pyrogram library. The methods allow you to send and edit long messages by splitting them into parts when the message length exceeds the allowed limit.

- `edit_long_message`: Method to edit an already sent long message.
- `send_long_message`: Method to send a new long message.

Both methods split long messages into multiple parts to avoid errors from exceeding the 4096 character limit and send or edit them with a delay between parts.

**Note:** Before using the methods in this project, make sure to import `monkeygram_patch` in your main file:

```python
import monkeygram_patch
```

## Functions

- **edit_long_message**: Edits a long message by splitting it into parts if it's too long.
- **send_long_message**: Sends a long message by splitting it into parts if it's too long.

Both functions support:
- Markdown or HTML parsing.
- Disabling web page previews.
- Preserving line formatting.
- Delay parameter between message parts.

## Installation

To use this code, you need to install the Pyrogram library and other dependencies:

```bash
pip install git+https://github.com/deadboizxc/monkeygram_patch.git
```

## Usage

### 1. `edit_long_message`

Method to edit a long message. First, make sure to import `monkeygram_patch` in your script:

```python
from pyrogram import Client
from pyrogram.types import Message
from typing import List, Optional

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
    """Method for editing long messages"""
    # Code as shown previously
```

Example usage:

```python
import monkeygram_patch
from pyrogram import Client

client = Client("my_bot")

async def main():
    message = await client.send_message(chat_id="chat_id", text="Some long text...")
    await message.edit_long_message("This is a very long message to be edited")

client.run(main())
```

### 2. `send_long_message`

Method to send a long message. Ensure that `monkeygram_patch` is imported at the beginning of your script:

```python
from pyrogram import Client

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
    """Method for sending long messages"""
    # Code as shown previously
```

Example usage:

```python
import monkeygram_patch
from pyrogram import Client

client = Client("my_bot")

async def main():
    await client.send_long_message(
        chat_id="chat_id",
        text="This is a very long message that exceeds the maximum length and needs to be split into multiple parts."
    )

client.run(main())
```

## Parameters

### `edit_long_message` and `send_long_message` take the following parameters:

- `text`: The text of the message to be sent or edited.
- `parse_mode`: The text formatting (e.g., `"markdown"` or `"html"`).
- `max_length`: The maximum length of a single message (default is 4096 characters).
- `delay`: The delay between sending each part of the message (in seconds).
- `preserve_lines`: If `True`, the line formatting will be preserved (default is `True`).
- `disable_web_page_preview`: Disables the web page preview (default is `True`).
- `reply_to_message_id`: The ID of the message to reply to (for the `send_long_message` method).

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
