# 정규표현식 : 대량의 문자열에 대해 일정한 패턴을 부여해 원하는 문자열만 취할 수 있다.
import re

ss = "1234 abc가나다abcABCfun_123555_6'Python if fun'"
print(ss)
print(re.findall('123', ss))
aa = re.findall(r'123', ss)
print(aa[0])
print(re.findall('가나', ss))
print(re.findall('[12]', ss))
print(re.findall('[0-9]', ss))
print(re.findall('\d\d', ss)) # \D \s \S \w \W
print(re.findall('[0-9]+', ss))
print(re.findall('[0-9]?', ss))
print(re.findall('[0-9]*', ss))
print(re.findall('[0-9]{2}', ss))
print(re.findall('[0-9]{2,3}', ss))
print(re.findall('[a-z]', ss))
print(re.findall('[a-zA-Z ]', ss))
print(re.findall('[가-힣]', ss))
print(re.findall('[^가-힣]', ss)) # ^이게 아닌
print(re.findall('.bc', ss)) # 1번째 자리 아무거나
print(re.findall('a..', ss)) #2,3번째 자리는 아무거나
print(re.findall('^123', ss)) # ^로 시작되는
print(re.findall('fun$', ss)) # fun으로 끝나는
print(re.findall('12|34', ss)) # 12 또는 34
print(re.findall('(ab)+(c)', ss)) # 그룹화

p = re.compile('abc')
print(re.findall(p, ss))

p = re.compile('the', re.IGNORECASE) # IGNORECASE 로 인해 대소문자구분을 무시
print(p.findall('The DoG the dog'))















