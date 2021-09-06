import pymysql
import time
import serial
import time
connect = pymysql.connect(host='localhost', user='root', password='0000', db='AutoFarming',charset='utf8')
cur = connect.cursor()
arduino = serial.Serial('/dev/ttyACM0', 9600)
i=0
print("a")
ok_LED =0;
ok_Cooler = 0;
ok_Humid = 0;
while 1:
    query = "SELECT * FROM Status ORDER BY ID DESC LIMIT 1;"
    query2 = "SELECT * FROM Sen_set ORDER BY ID DESC LIMIT 1;"
    cur.execute(query)
    connect.commit()
    status = cur.fetchall()   # current status
    cur.execute(query2)
    connect.commit()
    sen_set = cur.fetchall() # user custom data
    time.sleep(1)
    for sta in status:
        print("Current_Light : ",sta[3])
        print("Current_TEMP : ",sta[1])
        print("Current_Humid : ",sta[2])
    for sen in sen_set:
        print("Hope_Light : ", sen[3])
        print("Hope_TEMP : ",sen[1])
        print("Hope_Humid : ",sen[2])
    if(int(sen[3])>sta[3] and ok_LED==0):         #
        print("LED ON")
        c = "1"
        c= c.encode('utf-8')
        arduino.write(c)
        i=i+1
        time.sleep(1)
        if(i==3):
            ok_LED=1
            i=0
            print("break")
    elif(int(sen[3])<=sta[3] and ok_LED ==1):
        print("LED OFF")
        c = "0"
        c= c.encode('utf-8')
        arduino.write(c)
        i=i+1
        time.sleep(1)
        if(i==3):
            ok_LED=0
            i=0
            print("break")

    if(int(sen[1])>sta[1] and ok_Cooler ==0):
        print("Cooler OFF")
        c = "2"
        c= c.encode('utf-8')
        arduino.write(c)
        i=i+1
        time.sleep(1)
        if(i==3):
            ok_Cooler=1
            i=0
            print("break")
    elif(int(sen[1])<=sta[1] and ok_Cooler ==1):
        print("Cooler ON")
        c = "3"
        c= c.encode('utf-8')
        arduino.write(c)
        i=i+1
        time.sleep(1)
        if(i==3):
            ok_Cooler=0
            i=0
            print("break")
    if(int(sen[2])>sta[2] and ok_Humid ==0):
        print("Water ON")
        c = "5"
        c= c.encode('utf-8')
        arduino.write(c)
        i=i+1
        time.sleep(1)
        if(i==3):
            ok_Humid=1
            i=0
            print("break")
    elif(int(sen[2])<=sta[2] and ok_Humid ==1):
        print("Water OFF")
        c = "4"
        c= c.encode('utf-8')
        arduino.write(c)
        i=i+1
        time.sleep(1)
        if(i==3):
            ok_Humid=0
            i=0
            print("break")
