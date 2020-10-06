import os
from dotenv import load_dotenv
import sqlite3
import psycopg2


class Vaishnadb:
    def __init__(self):
        self.conn = sqlite3.connect("vaishnadb.db")
        print(self.conn)
        self.cur = self.conn.cursor()

    def addEkadasiItem(self, name, day, month, year, start, end):
        self.cur.execute("""
            INSERT INTO ekadasi_dates  
            (name, day, month, year, start, end)
            VALUES (?, ?, ?, ?, ?, ?)""", (name, day, month, year, start, end))
        self.conn.commit()
        
             
    def addIskconEventItem(self, name, month, day, year):
        self.cur.execute("""
            INSERT INTO iskcon_events 
            (name, month, day, year)
            VALUES (?, ?, ?, ?)""", (name, month, day, year))
        self.conn.commit()



class VaishnadbPG:
    load_dotenv()
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname = os.getenv('PGDATABASE'),
            host = os.getenv('PGHOST'),
            port = os.getenv('PGPORT'),
            user = os.getenv('PGUSER'),
            password = os.getenv('PGPASSWORD')
        )
        self.cur = self.conn.cursor()

    def addEkadasiItem(self, name, day, month, year, starts, ends):
        self.cur.execute("""
            INSERT INTO ekadasi_events  
            (name, day, month, year, starts, ends)
            VALUES (%s, %s, %s, %s, %s, %s)""", (name, day, month, year, starts, ends))
        self.conn.commit()
        
             
    def addIskconEventItem(self, name, month, day, year):
        self.cur.execute("""
            INSERT INTO iskcon_events 
            (name, month, day, year)
            VALUES (%s, %s, %s, %s)""", (name, month, day, year))
        self.conn.commit()


