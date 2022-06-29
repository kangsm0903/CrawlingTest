import csv
from konlpy.tag import Okt

okt = Okt()

f = open('C:/Users/ksm36/Desktop/dataset/review_dataset.csv','r', encoding='utf-8')
f2= open('C:/Users/ksm36/Desktop/dataset/test2.csv', 'w', newline='', encoding='utf-8-sig')

rdr=csv.reader(f)
writer=csv.writer(f2)
result={}

for line in rdr:

    target=okt.morphs(line[8]) # separate

    for i in target:
        if len(i)>1:    
            if i in result: # 추가
                result[i]+=1
            else:           # 갱신
                result[i]=1

for i in result.items():
    writer.writerow([i[0],i[1]])

f.close()