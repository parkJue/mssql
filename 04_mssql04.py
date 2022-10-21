from tkinter.tix import StdButtonBox
import dbconn as db

conn = db.dbconn()
cursor = conn.cursor()

sql = '''insert into blog values(?,?,?)'''
data = [('첫번째 글제목','첫번째 글내용','/static/blog/img/img01.png'),
        ('두번째 글제목','두번째 글내용','/static/blog/img/img02.png')]
cursor.executemany(sql, data)
conn.commit()
conn.close()