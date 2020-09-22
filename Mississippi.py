input_string = "Mississippi"
d= {} 
for char in input_string: 
   if char in d: 
      d[char] += 1
   else: 
      d[char] = 1
sort1=list(set(sorted(d.values())))
for x in sort1: 
    for key, value in d.items(): 
        if value == x:
            print(key,":", value)
