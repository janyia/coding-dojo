sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

test = [sI, mI, bI, eI, spI, sS, mS, bS, eS, aL, mL, lL, eL,spL]

for arg in test[0:14]:
    if isinstance(arg, int) ==True:
        if arg >= 100:
            print "Thats a big number!" ,arg
        else:
                print "That's a small number" ,arg
    if isinstance(arg, str) ==True:
        if len(arg) >= 50:
            print "Long sentence" ,arg
        else:
            print "Short sentence" ,arg
    if isinstance(arg, list) ==True:
        if len(arg) >= 10:
            print "Big list" ,arg
        else:
            print "Short list" ,arg 

