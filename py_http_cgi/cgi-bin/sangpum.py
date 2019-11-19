# 원격 DB의 테이블 자료 출력
config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'kic1234',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}

import MySQLdb

print('Content-Type:text/html;charset=utf-8\n')
print('<html><body> <b> * 상품 정보 * </b><p/>')
print('<table border = "1">')
print('<tr><th>코드</th><th>품명</th><th>수량</th><th>단가</th></tr>')

try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    cursor.execute('select * from sangdata')
    
    for r in cursor:
        print('''
        <tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td></tr>
        '''.format(*r))
        
except Exception as e:
    print('err :',e)
finally:
    cursor.close()
    conn.close()
print('</table>')
print('</html></body>')