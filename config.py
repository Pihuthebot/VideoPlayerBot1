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
API_ID = int(getenv("API_ID", "8755605"))
API_HASH = getenv("API_HASH", "9d067982dcaa2f7020957036e2a1cb89")
BOT_TOKEN = getenv("BOT_TOKEN", "2034558488:AAFCVz6rjcXEu1Opzyfny2oSMIuphk2SUlQ")
SESSION_STRING = getenv("SESSION_STRING", "BQB00zaLhBy1RZSOIz7X_R4R6bSwGIrV_qSCuwl1IcXEvxYDMwFF15l4eVq_RmWBI3kpz7nnK2BkevOzkad7mHVRSP_kvDnGwveKN7SsIDFwYsBZBKqoXC3wHm5hOf0IfOdOpkXWtWjJThj3jZ6AIo2c2r4048vg2VLqaB8pRC9wcm1WeXs9zPddd1iGSx7vBn2oxKD-i75JaoxQAyBawXwTRwSIH-d5WE5YBvAb0g3UGA8rDglJS9nqDtuTQ2QkWkby7CeKy7WmjJXdAcvBlQDb1nIQZotng419t7y1XX2bH3qvEzbQW603RCjGFe96Ae-uUxy9ClvIMVitbyNGzRBve27vYQA")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "WorldWideChatsXd")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Sanki_BOTs")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "GalaxinaVcAssistant")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2067182444").split()))
REPLY_MESSAGE = getenv("REPLY_MESSAGE", "")
if REPLY_MESSAGE:
    REPLY_MESSAGE = REPLY_MESSAGE
else:
    REPLY_MESSAGE = None
