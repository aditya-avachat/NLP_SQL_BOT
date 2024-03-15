import psycopg2
import csv
# conn = psycopg2.connect("dbname=train user=postgres password=passmein@16")
# cur = conn.cursor()
# cur.execute('SELECT * FROM TRAINS')
# out = cur.fetchall()
# for i in out:
# 	print(i)
# cur.close()
# conn.close()

data = open(r"C:\Users\Shela\Downloads\All_Indian_Trains.csv")
csvreader = csv.reader(data)
next(csvreader)
count = 0
for i in csvreader:
	count += 1
	conn = psycopg2.connect("dbname=train user=postgres password=passmein@16")
	cur = conn.cursor()
	train_num = int(i[1])
	train_name = i[2]
	start = i[3]
	ends = i[4]
	sql = "INSERT INTO TRAINS(TRAINUM,TRAINAME,START,ENDS) VALUES (%s,%s,%s,%s);"
	
	cur.execute(sql,(train_num,train_name,start,ends))
	conn.commit()
	print("printing .."+ str(count))
	cur.close()
	conn.close()


