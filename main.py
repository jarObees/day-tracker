import sqlite3

conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute("""CREATE TABLE activities (
            action_type text,
            date integer,
            start_time integer,
            end_time integer
            )""")
