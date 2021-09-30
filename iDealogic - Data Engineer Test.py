# import json lib for parse json to object
import json

#open json file
file1 = open("E:\\Dropbox\\Idealogic\\20190207_transactions.json", 'r')
# Read all lines in file
Lines = file1.readlines()
 
count = 0
arr = []
# for each lines of file
for line in Lines:
    count += 1
    #parse each line
    data = json.loads(line) 
   # add data to arr
    arr.append(data)

# count frequences of product in arr
freq = {}
for data in arr:
   products = data["products"]
   for item in products:
       if (item in freq):
            freq[item] += 1
       else:
            freq[item] = 1
         
# Sort count of product descending
sort_orders = sorted(freq.items(), key=lambda x: x[1], reverse=True)
print(sort_orders )

# Write output to file
f = open("myfile.txt", "w")
for data in sort_orders :
  f.write ("% d : % d\r" % (data[0], data[1]))
