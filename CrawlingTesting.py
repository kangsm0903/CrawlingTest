import csv
from konlpy.tag import Okt

okt = Okt()

f = open('C:/Users/ksm36/Desktop/dataset/review_dataset.csv','r', encoding='utf-8')

rdr=csv.reader(f)

def solution(k,rdr):
    result={}

    for line in rdr:

        if line[6]==str(k):
            target=okt.morphs(line[8]) # separate

            for i in target:
                if len(i)>1:    
                    if i in result: # 추가
                        result[i]+=1
                    else:           # 갱신
                        result[i]=1
            if str(k)==str(1):
                for i in result.items(): # ('A','b')
                    writer.writerow({'one_score': i[0],'one_value': i[1]})
            elif str(k)==str(2):
                for i in result.items(): # ('A','b')
                    writer.writerow({'two_score': i[0],'two_value': i[1]})
            elif str(k)==str(3):
                for i in result.items(): # ('A','b')
                    writer.writerow({'three_score': i[0],'three_value': i[1]})
            elif str(k)==str(4):
                for i in result.items(): # ('A','b')
                    writer.writerow({'four_score': i[0],'four_value': i[1]})
            elif str(k)==str(5):
                for i in result.items(): # ('A','b')
                    writer.writerow({'five_score': i[0],'five_value': i[1]})

with open('C:/Users/ksm36/Desktop/dataset/test.csv', 'w', newline='', encoding='utf-8-sig') as f2:
    fieldnames=['one_score','one_value','two_score','two_value','three_score','three_value','four_score','four_value','five_score','five_value']

# writer=csv.writer(f2)
    writer = csv.DictWriter(f2, fieldnames=fieldnames)
    writer.writeheader()

f.close()