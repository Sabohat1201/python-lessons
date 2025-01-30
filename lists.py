mevalar=['olma','anjir','shaftoli','o\'rik']
narhlar=[12000,18000,10900,20000]
print(mevalar[0])
print("Birinchi meva",mevalar[0])
print("Oxirgi meva", mevalar[-1])
mevalar[0]="banan"
#print(mevalar)
mevalar.append('olma')
#print(mevalar)
mevalar.insert(0,'gilos')
#print(mevalar)
del mevalar[0]
#print(mevalar)
mevalar.remove("olma")
print(mevalar)

print("Men",mevalar.pop(2), "mevani sotib oldim.")