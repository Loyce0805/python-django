# Singer 타입의 객체 
# abc 라는 가수 객체

import pack3.test26_class

def process():

    abc = pack3.test26_class.Singer()
    print('타이틀 송 : ', abc.title_song)
    abc.sing()
    abc.hello()

if __name__ == '__main__':
    process()
