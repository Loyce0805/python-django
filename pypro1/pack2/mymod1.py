# 사용자 정의 모듈 : 독립적으로 사용하지 않고 다른 모듈에서 호출될 대상
price = 12345

def listHap(*ar):
    print(ar)
    
    if __name__ == '__main__':
        print('이 파일이 메인이야~~')
    
def kbs():
    print('대한민국 대표방송')
    
def mbc():
    print('문화방송 : 11')