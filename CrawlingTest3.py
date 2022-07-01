# Rating, Content, Count 순으로 정렬
import csv
from konlpy.tag import Okt

okt = Okt()

f = open('C:/Users/ksm36/Desktop/dataset/review_dataset.csv','r', encoding='utf-8')
f2= open('C:/Users/ksm36/Desktop/dataset/test2.csv', 'w', newline='', encoding='utf-8-sig')

rdr=csv.reader(f)
writer=csv.writer(f2)

result={}
rating={}

for line in rdr:
    target=okt.morphs(line[8]) # separate

    for i in target:
        if len(i)>1:
            if i in result: # 추가
                result[i]+=1
            else:           # 갱신
                result[i]=1
                rating[i]=line[6]

def classify():
    Content=[]
    Count=[]

    Content2=[]
    Count2=[]

    Content3=[]
    Count3=[]

    Content4=[]
    Count4=[]

    Content5=[]
    Count5=[]
    for i in result.items():
        if rating[i[0]]=='1':
            Content.append(i[0])
            Count.append(i[1])
        elif rating[i[0]]=='2':
            Content2.append(i[0])
            Count2.append(i[1])
        elif rating[i[0]]=='3':
            Content3.append(i[0])
            Count3.append(i[1])
        elif rating[i[0]]=='4':
            Content4.append(i[0])
            Count4.append(i[1])
        elif rating[i[0]]=='5':
            Content5.append(i[0])
            Count5.append(i[1])

    for i in range(len(result)):
        try:
            writer.writerow([Content[i],Count[i],"",Content2[i],Count2[i],"",Content3[i],Count3[i],"",Content4[i],Count4[i],"",Content5[i],Count5[i]])
        except IndexError:
            continue

result.pop('content')
# for i in result.items():
#     writer.writerow([rating[i[0]],i[0],i[1],'',''])

classify()
f.close()