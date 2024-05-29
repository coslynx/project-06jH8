# database.py (Python)

import sqlite3

class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS server_config (
                                server_id TEXT PRIMARY KEY,
                                prefix TEXT,
                                log_channel_id TEXT,
                                welcome_message TEXT
                            )''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS moderation_logs (
                                log_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                server_id TEXT,
                                user_id TEXT,
                                action TEXT,
                                reason TEXT,
                                timestamp TEXT
                            )''')
        self.connection.commit()

    def add_server_config(self, server_id, prefix, log_channel_id, welcome_message):
        self.cursor.execute('''INSERT INTO server_config (server_id, prefix, log_channel_id, welcome_message)
                            VALUES (?, ?, ?, ?)''', (server_id, prefix, log_channel_id, welcome_message))
        self.connection.commit()

    def update_server_config(self, server_id, prefix, log_channel_id, welcome_message):
        self.cursor.execute('''UPDATE server_config
                            SET prefix=?, log_channel_id=?, welcome_message=?
                            WHERE server_id=?''', (prefix, log_channel_id, welcome_message, server_id))
        self.connection.commit()

    def get_server_config(self, server_id):
        self.cursor.execute('''SELECT * FROM server_config WHERE server_id=?''', (server_id,))
        return self.cursor.fetchone()

    def add_moderation_log(self, server_id, user_id, action, reason, timestamp):
        self.cursor.execute('''INSERT INTO moderation_logs (server_id, user_id, action, reason, timestamp)
                            VALUES (?, ?, ?, ?, ?)''', (server_id, user_id, action, reason, timestamp))
        self.connection.commit()

    def get_moderation_logs(self, server_id):
        self.cursor.execute('''SELECT * FROM moderation_logs WHERE server_id=?''', (server_id,))
        return self.cursor.fetchall()

    def close_connection(self):
        self.connection.close()