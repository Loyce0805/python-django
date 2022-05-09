import pickle

dictData = {'tom':'111-1111', 'james':'222-2222'} # 데이터 분석가도 이런거 써먹음 파일에 딕트저장
listData = ['채원', '해승']
tupleData = (dictData, listData)

with open(file = 'bread1.csv', mode ='wb') as ff3:
    pickle.dump(tupleData, ff3)   # 저장할때 씀 객체변수는 ff3
    pickle.dump(listData, ff3)