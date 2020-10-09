import psycopg2


class Vaishnadb:

    def __init__(self, dbname, host, port, user, password):
        self.dbname = dbname
        self.host = host
        self.port = port
        self.user = user
        self.password = password


    def get_connection(self):
        conn = psycopg2.connect(
            dbname=self.dbname,
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password
        )
        if conn.status == 1:
            return conn
        else:
            raise Exception("The connection to the database failed")


    def add_ekadasi(self, name, description, return_id=False):
        with self.get_connection() as conn:
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO ekadasi (name, description)
                VALUES (%s, %s)
            """, (name, description))

            conn.commit()

            if return_id:
                cur.execute("SELECT id FROM ekadasi WHERE name=%s", (name,))
                return cur.fetchone() 


    def add_ekadasi_date(self, ekadasi_id, country, event_date, starts, ends):
        with self.get_connection() as conn:
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO ekadasi_date (ekadasi_id, country, event_date, starts, ends)
                VALUES (%s, %s, %s, %s, %s)
            """, (ekadasi_id, country, event_date, starts, ends))
            conn.commit()


    def add_iskcon_event(self, name, description, event_date):
        with self.get_connection() as conn:
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO iskcon_event (name, description, event_date)
                VALUES (%s, %s, %s)
            """, (name, description, event_date))
            conn.commit()