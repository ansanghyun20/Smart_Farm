import serial
import time
import pymysql
import time



port = '/dev/ttyACM0'
brate = 9600
seria = serial.Serial(port, baudrate = brate, timeout=None)
#cmd = 'temp'

conn = pymysql.connect(host='localhost', user="root", password="0000" , db='AutoFarming', charset='utf8')

print(seria.name)

curs = conn.cursor()
#seri.write(cmd.encode())


#curs.execute(sql)
#


i=0
#try:
while(True):
    if seria.in_waiting != 0:
        time.sleep(2)
        now = time.localtime()
        content = seria.readline()
        Ctime = str(now.tm_hour)+str(now.tm_min)
        content.decode()[:len(content)-2]
        Temp =float(content.split()[0])
        print(Temp)
        humid =float(content.split()[1])
        print(humid)
        Light =int(content.split()[2])
        print(Light)
        print(Ctime)
        i=i+1
        print(i)
        val = (Temp,humid,Light,Ctime)
        sql = "INSERT INTO Status(Temp,Humid,Light,CTime) VALUES(%s,%s,%s,%s)"
        curs.execute(sql, val)
        conn.commit()
        
        

