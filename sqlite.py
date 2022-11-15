"""
year;programming language;first name; last name of chief developer
1972;C;Dennis; Ritchie
1964;BASIC;John George;Kemeny
1964;BASIC;Thomas Eugene;Kurtz
1995;Java;James;Gosling
1983;C++;Bjarne;Stroustrup
1987;Perl;Larry;Wall
1995;JavaScript;Brendan;Eich
1970;Pascal;Niklaus; Wirth
1946;ENIAC Short Code;Richard; Clippinger
1946;ENIAC Short Code;John;von Neumann
1995;PHP;Rasmus;Lerdorf
1989;Python;Guido;Van Rossum
2000;C#;Anders;Hejlsberg
1970;Pascal;Kathleen;Jensen
"""


import sqlite3

con = sqlite3.connect("sulipy.db")

cur = con.cursor()

cur.execute("CREATE TABLE sulipy(year, programming_language, first_name, last_name)")

cur.execute("""
    INSERT INTO sulipy VALUES
        (1972,"C","Dennis", "Ritchie"),
        (1964,"BASIC","John George","Kemeny")
""")


data = [
    (1972,"C","Dennis", "Ritchie"),
    (1964,"BASIC","John George","Kemeny"),
    (1964,"BASIC","Thomas Eugene","Kurtz"),
    (1995,"Java","James","Gosling"),
    (1983,"C++","Bjarne","Stroustrup"),
    (1987,"Perl","Larry","Wall"),
    (1995,"JavaScript","Brendan","Eich"),
    (1970,"Pascal","Niklaus", "Wirth"),
    (1946,"ENIAC Short Code","Richard", "Clippinger"),
    (1995,"PHP","Rasmus","Lerdorf"),
    (1989,"Python","Guido","Van Rossum"),
    (2000,"C","Anders","Hejlsberg"),
    (1970,"Pascal","Kathleen","Jensen"),
    
    
    
]
cur.executemany("INSERT INTO sulipy VALUES(?,?,?,?)", data)

con.commit()

for sor in cur.executemany("SELECT year, last_name FROM sulipy ORDER BY year"):
    print(sor)

con.close()