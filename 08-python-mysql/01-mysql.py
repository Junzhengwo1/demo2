import pymysql

# with pymysql.connect(host='localhost',
#                      user='root',
#                      password='123',
#                      database='python',
#                      port=3306,
#                      charset='utf8') as db:
#     with db.cursor() as cur:
#         cur.execute('select * from t_user')
#         db.commit()
#         cur.close()
#         print(cur.fetchone())

db = pymysql.connect(host='localhost',
                     user='root',
                     password='123',
                     database='python',
                     port=3306,
                     charset='utf8')
cur = db.cursor()
cur.execute('select * from t_user')
db.commit()
cur.close()
print(cur.fetchone(),type(cur.fetchone()))
