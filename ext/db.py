import logging
import sqlite3

class Database:
    global logger
    logger = logging.getLogger(__name__)

    def __init__(self, database='data/db.sqlite3'):
        self.database = database
        self.conn = None

    def connect(self):
        """
        Connects to the database and creates the `points` table if it doesn't
        already exist.
        """
        logger.debug('Starting the database module.')
        self.conn = sqlite3.connect(self.database)
        with self.conn as conn:
            cur = conn.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS `points`
                (key text NOT NULL UNIQUE, value int NOT NULL)""")
        return self.conn