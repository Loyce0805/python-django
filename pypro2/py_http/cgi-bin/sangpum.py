# 웹 모듈 : DB 자료 출력

import MySQLdb
import pickle

with open('mydb.dat','rb') as obj:
    config= pickle.load(obj)
    
print('Content-Type:text/html;charset=utf-8\n')
print('<head><body>')
print('<h2>Product Info</h2>')
print('<table border="1"><tr><th>코드</th><th>상품명</th><th>수량</th><th>단가</th></tr>')
try:
    conn= MySQLdb.connect(**config) #dict 타입
    cursor= conn.cursor()
    
    cursor.execute("select * from sangdata")
    datas = cursor.fetchall()
    
    for code, sang, su, dan in datas:
        print('''
            <tr>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
            </tr>
        '''.format(code, sang, su, dan))
except Exception as e:
    print('err: ',e)
finally:
    cursor.close()
    conn.close()
print('</table>')
print("<br><a href='../main.html'>back to main</a>")
print('</body></head>')