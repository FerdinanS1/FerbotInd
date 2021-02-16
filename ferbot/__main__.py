# Ferbot, ini adalah bot untuk mengelola grup Anda.
# Copyright (C) 2021 FS Project <https://github.com/FS-Project/Ferbot.git>
# 
# UserindoBot
# Copyright (C) 2020  UserindoBot Team, <https://github.com/userbotindo/UserIndoBot.git>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import importlib
import traceback
from typing import Optional

from telegram import Message, Chat, User
from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.error import Unauthorized
from telegram.ext import (
    CommandHandler,
    Filters,
    MessageHandler,
    CallbackQueryHandler,
)
from telegram.ext.dispatcher import DispatcherHandlerStop
from telegram.utils.helpers import escape_markdown

from ferbot import (
    updater,
    TOKEN,
)

PM_START_TEXT = f"""
Hallo! Perkenalkan nama saya *{dispatcher.bot.first_name}*.

SAYA SEDANG DALAM PEMBUATAN JIKA SUDAH TERSEDIA MAKA AKAN DI BERITAHUKAN.
"""


buttons = [[InlineKeyboardButton(text="🔗 Tinjau Perkembangan",
                                  url=f"https://github.com/FS-Project/FerBotInd"),
             ]]


@typing_action
def start(update, context):
        else:
            update.effective_message.reply_photo(
                "https://i.ibb.co/nBwSNvN/Logo-header-ferbotind.jpg",
                PM_START_TEXT,
                reply_markup=InlineKeyboardMarkup(buttons),
                parse_mode=ParseMode.MARKDOWN,


if __name__ == "__main__":
    LOGGER.info("Successfully loaded modules: " + str(ALL_MODULES))
    main()
