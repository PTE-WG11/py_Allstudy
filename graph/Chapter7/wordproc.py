f = open("rawwords.txt", "r")
wl = []
for aline in f:
    l = aline.split()
    wl.append(l[0])
print(wl[:10])
    
    
of = open("fourletterwords.txt", "w")

for w in wl:
   of.write(w+'\n')
    