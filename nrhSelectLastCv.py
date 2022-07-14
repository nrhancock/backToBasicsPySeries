selection = pm.ls(sl=True)[0]
count = 0

degree = pm.getAttr( selection+'.degree' )
print(degree)
spans = pm.getAttr( selection+'.spans' )
print (spans)

cv_count= degree + spans

list = []

for n in range(cv_count):
    count_up = str(count)
    string_up = pm.format(selection+".cv["+count_up+"]")
    print(string_up)
    list.append(string_up)
    count+=1
    print(count)
   
print(list)

last_cv = pm.select(list[-1])
