import csv

#reading the stock values from Day1 to Day10 (stored in csv format)
reader = csv.reader(open(r"Stocks.csv"))   
d = {}
val_list_of_floats = []

#as the first line is header want to ignore the first input
next(reader)              

#reading the values one by one and storing them in dictonary 
for row in reader:
   k, v = row
   d[k] = v

#print(d)
#creating list of all the keys
key_list = list(d.keys())

#creating list of all the values
val_list = list(d.values())

#converting the string values to float
for item in val_list:
    val_list_of_floats.append(float(item))

vmin = val_list_of_floats[0]
dmax = float(0)

#comparing the stock price from day1 to day10 for lost price and highest price
for i in range(len(val_list_of_floats)):
   if (val_list_of_floats[i] < vmin):
       vmin = val_list_of_floats[i]
   elif (val_list_of_floats[i] - vmin > dmax):
       dmax = val_list_of_floats[i] - vmin
       key_min_index = val_list_of_floats.index(vmin)
       key_min = key_list[key_min_index]
       min_stock_value = vmin
       key_max_index = val_list_of_floats.index(val_list_of_floats[i])
       key_max = key_list[key_max_index]
       max_stock_value = val_list_of_floats[i]
       
print('The best day to buy stock: %s at price %f' %(key_min,min_stock_value))
print('The best day to sell stock: %s at price %f' %(key_max,max_stock_value))
print('The max profit from the transcation:',dmax)




