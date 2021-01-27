from datetime import datetime
from Model import longCalc
from Model import shortCalc

date_entry = input("Week of YYYY-MM-DD: ")
year, month, day = map(int, date_entry.split('-'))
currentDay = datetime(year, month, day)

longs = longCalc(currentDay, 5)
shorts = shortCalc(currentDay, 5)

print("-----TRADE OF THE WEEK-----")

if(shorts[2] > longs[2]):
	print("Put Option.")
	print("Strike:", round((shorts[3] + shorts[0]) / 2, 2))
	print("TP:", round(shorts[0], 2))
	print("SL:", round(shorts[1], 2))
else:
	print("Call Option.")
	print("Strike:", round((longs[3] + longs[0]) / 2, 2))
	print("TP:", round(longs[0], 2))
	print("SL:", round(longs[1], 2))

print("-----------")