import serial
import pandas as pd
##file1 = open('new.txt','w')
df = pd.DataFrame()
new = pd.DataFrame()
new2 = pd.DataFrame()
count1 = ['1','2','3','4','5','6','7','8','9','10']

count = 0

arduino = serial.Serial('COM14', 9600, timeout=.1)
while True:
   data = arduino.read() #the last bit gets rid of the new-line chars
   if data:
      
      data2 = data.decode('utf-8')
      newest = list(data2)
      df = pd.DataFrame(newest)
      
      if count >= 2 :
         if count < 12:
            new = new.append(df)
         else:
            new2 = new2.append(df)
            
         
         if count == 21:
            new.columns = ['1st']
            new2.columns = ['2nd']
            new.index = count1
            new2.index = count1
##            print('\n')
##            print(new2)
            merged = new.join(new2)
            print(merged)
####            new.to_csv('this2.csv', index = False, header = False)
####            new2.to_csv('this3.csv', index = False, header = False)
            merged.to_csv('this5.csv', index = False, header = False)
      count += 1
