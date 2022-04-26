# 우편번호 data 파일 사용
# 키보드로 동이름을 입력해서 해당 동이름의 자료만 읽기
# 아스키코드 기억해야할거
try:
    dong = input('동이름 입력 :')
    #dong = '개포'
    #print(dong)
    
    with open(file = r'zipcode.txt', mode='r', encoding = 'euc-kr') as f:
        line = f.readline()
        #print(line)
        
        while line:
            # lines = line.split('\t')  # tap 을 기준으로 자른다
            lines = line.split(chr(9))
            
            #print(lines) 
            if lines[3].startswith(dong):
                print('[' + lines[0] + '] ' + lines[1] + ' ' + \
                        lines[2] + ' ' + lines[3] + ' ' + lines[4])
            line = f.readline()
    
    
except Exception as e:
    print('err : ', e)