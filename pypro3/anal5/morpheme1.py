'''
Created on 2022. 4. 26. 형태소(morpheme)
'''
# 형태소 분석 : 자연어 처리를 목적으로 언어적 속성의 구조를 파악
# konlpy 라이브러리를 사용

from konlpy.tag import Kkma, Okt, Komoran

kkma = Kkma()
print(kkma.sentences('한글 데이터 형태소 분석을 위한 라이브러리 설치를 합니다. 잘되길 바랍니다')) # 마침표(.)를 찍으니까 2개의 문장으로 나눠짐.
print(kkma.nouns('한글데이터형태소분석을위한라이브러리설치를합니다. Good job 123'))  # 한글은 붙여도 읽을 수 있지만, 영어는 붙이면 못 읽는다. 영어는 버리고 숫자랑 한글만 나옴.
print(kkma.pos('한글데이터형태소분석을위한라이브러리설치를합니다. Good job 123')) #  [('한글', 'NNG'), ('데이터', 'NNG'), ('형태소', 'NNG'), ('분석', 'NNG'), ...
print(kkma.morphs('한글데이터형태소분석을위한라이브러리설치를합니다. Good job 123')) # ['한글', '데이터', '형태소', '분석', '을', '위하', 'ㄴ', '라이브러리', '설치', '를'....

print()
okt = Okt()
print(okt.nouns('한글데이터형태소분석을위한라이브러리설치를합니다. Good job 123'))
print(okt.pos('한글데이터형태소분석을위한라이브러리설치를합니다. Good job 123'))
print(okt.pos('한글데이터형태소분석을위한라이브러리설치를합니다. Good job 123', stem = True)) # 원형 어근 추출
print(okt.morphs('한글데이터형태소분석을위한라이브러리설치를합니다. Good job 123'))
print(okt.phrases('한글데이터형태소분석을위한라이브러리설치를합니다. Good job 123')) # 어절 추출

print()
ko = Komoran()
print(ko.nouns('한글데이터형태소분석을위한라이브러리설치를합니다. Good job 123'))
print(ko.pos('한글데이터형태소분석을위한라이브러리설치를합니다. Good job 123'))
print(ko.morphs('한글데이터형태소분석을위한라이브러리설치를합니다. Good job 123'))

















