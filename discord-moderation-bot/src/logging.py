# logging.py (Python)

import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='moderation_bot.log',
                    filemode='a')

# Create a logger
logger = logging.getLogger('discord_moderation_bot')

def log_user_action(user_id, action):
    """Log user actions in the moderation bot log file"""
    logger.info(f'User ID: {user_id} - Action: {action}')

def log_server_changes(server_id, change):
    """Log server changes in the moderation bot log file"""
    logger.info(f'Server ID: {server_id} - Change: {change}')