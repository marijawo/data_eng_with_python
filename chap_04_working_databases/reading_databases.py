import psycopg2 as db


conn_string = "dbname = 'dataengineeringdb' host='localhost' port='5437' user='postgres' password='MineOne'  "

conn = db.connect(conn_string)
cur=conn.cursor()

################## Query 2 ######################

query2 = "insert into users (id,name,street,city,zip) values(%s,%s,%s,%s,%s)"

data=(1,'Big Bird','Sesame Street','Fakeville','12345')

cur.mogrify(query2,data)

cur.execute(query2,data)
conn.commit()