import sqlite3

con = sqlite3.connect("teszt.db")

cur = con.cursor()

cur.execute("CREATE TABLE film(cim, ev, pont)")

cur.execute("""
    INSERT INTO film VALUES
        ('ben hur', 1975, 8.2),
        ('kingdom', 2021, 9.6)
""")

con.commit()

res = cur.execute("SELECT cim FROM film")
print(res.fetchall())
