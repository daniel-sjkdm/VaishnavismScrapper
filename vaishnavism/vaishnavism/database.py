import sqlite3


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
