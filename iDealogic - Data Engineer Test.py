import json

file1 = open("E:\\Dropbox\\Idealogic\\20190207_transactions.json", 'r')
Lines = file1.readlines()
 
count = 0
arr = []
# Strips the newline character
for line in Lines:
    count += 1
    data = json.loads(line) 
    arr.append(data)
#print (arr)

freq = {}
for data in arr:
   products = data["products"]
   for item in products:
       if (item in freq):
            freq[item] += 1
       else:
            freq[item] = 1
            #for key, value in freq.items():
      #print ("% d : % d"%(key, value))
#sort_orders = sorted(freq.items(), key=lambda x: x[1])
print(freq)

sort_orders = sorted(freq.items(), key=lambda x: x[1], reverse=True)
print(sort_orders )

f = open("myfile.txt", "w")
for data in sort_orders :
  f.write ("% d : % d\r" % (data[0], data[1]))
