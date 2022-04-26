# 웹용 파이썬 모듈
a = 10
b = 20
c = a + b
mbc = '파이썬 만세'
print('Content-Type:text/html;charset=utf-8\n') # 클라이언트 브라우져를 위한것 야 브라우져 내가 너한테 보내는 파일 타입은 text/html이야
print('<html><body>')
print('<b>안녕하세요</b> 파이썬 모듈로 작성한 문서입니다.<br>')   #여러칸 띄려면 \nbsp를 넣어야함
print('<hr>')
print('합은 %d'%c)
print('<br>메세지는 %s'%mbc)             #{}.format
print('<p>작성자 : 홍길동')
print('</body></html>')