"""
VideoPlayerBot, Telegram Video Chat Bot
Copyright (c) 2021  Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()

admins = {}
AUDIO_CALL = {}
VIDEO_CALL = {}
API_ID = int(getenv("API_ID", "8302428"))
API_HASH = getenv("API_HASH", "13dd80a1c8233942b0ca5b4b7373d29e")
BOT_TOKEN = getenv("BOT_TOKEN", "2034558488:AAFCVz6rjcXEu1Opzyfny2oSMIuphk2SUlQ")
SESSION_STRING = getenv("SESSION_STRING", "AQBCIm-6BaGp1OIR7kgblfVnqx3aYHr523MhQTtbrgZxT6faTTZyi0qLwUcA2pCBMCtf4AKrckWhjy963mZA-bY5Z8po2ziH4Pm_x5ZeXo1uKdLT5O_b9x_YOC65r03Av3femHe9rCmt4KIR9RB7CzTvpA_ygQp-j1yPqheEOhCjKFALvC7qJY1cTJuUf5Az263aSP4IZh03BlZBFZfI6sFFP_unVGa4caNewfBO6TFvRyQfU8NLkxN8bSHY4zUvJpj0lktCVS2LwAiJZCiUpEWKJhIgSovx4Xkq-FY2mKdq2alS1gSsRtXJqKSulGbWGDW1syUmKaj5z7Pdr2Bg6709fPxglgA")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "WorldWideChatsXd")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Sanki_BOTs")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "GalaxinaVcAssistant")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2067182444").split()))
REPLY_MESSAGE = getenv("REPLY_MESSAGE", "")
if REPLY_MESSAGE:
    REPLY_MESSAGE = REPLY_MESSAGE
else:
    REPLY_MESSAGE = None
