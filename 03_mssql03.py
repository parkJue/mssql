from tkinter.tix import StdButtonBox
import dbconn as db

conn = db.dbconn()
cursor = conn.cursor()

sql = ''' insert into blog values
(N'첫번째 글제목',N'첫번째 글내용',N'/static/blog/img/img01.png'),
(N'두번째 글제목',N'두번째 글내용',N'/static/blog/img/img02.png')
'''
cursor.execute(sql)
conn.commit()
conn.close()