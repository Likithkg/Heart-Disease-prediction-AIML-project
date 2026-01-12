from flask import session
import mysql.connector
from config import config

Host, Database, Password, User = config.get_db_config()

class FeedBack():
    def __init__(self):
        self.db = mysql.connector.connect(
            host=Host,
            user=User,
            password=Password,
            database = Database
        )

    def submit_feedback(self, name, email, phone, message):
        cursor = self.db.cursor()
        try:
            cursor.execute('INSERT INTO feedback (name,email,phone,message) VALUES (%s,%s,%s,%s)', (name, email, phone, message))
            self.db.commit()
            cursor.close()
            print("test")
            return True
        except Exception as e:
            print(f"Error submitting feedback: {e}")
            self.db.rollback()
            cursor.close()
            return False