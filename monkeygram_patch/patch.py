from pyrogram import Client
from pyrogram.types import Message
from .client import send_long_message, edit_long_message


def apply_patch():
    print("[pyrogram_patch] Applying monkey patch to Pyrogram Client...")
    # Добавляем метод в класс Client
    Client.send_long_message = send_long_message
    # Добавляем метод в класс Message
    Message.edit_long_message = edit_long_message
