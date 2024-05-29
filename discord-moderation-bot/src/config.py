config.py:

import os
from dotenv import load_dotenv

load_dotenv()

# Discord Bot Token
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Database Configuration
DATABASE_NAME = "discord_moderation.db"
DATABASE_PATH = os.path.join(os.path.dirname(__file__), DATABASE_NAME)

# Logging Configuration
LOG_FILE = "discord_moderation.log"
LOG_PATH = os.path.join(os.path.dirname(__file__), LOG_FILE)

# Webhooks Configuration
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

# OAuth2 Configuration
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")

# Other Configurations
PREFIX = "!"
OWNER_ID = os.getenv("OWNER_ID")
MODERATOR_ROLE = "Moderator"
ADMIN_ROLE = "Admin"