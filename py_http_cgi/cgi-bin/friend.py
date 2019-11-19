import cgi

form = cgi.FieldStorage()
name = form['name'].value
phone = form['phone'].value
gender = form['gen'].value

print('Content-Type:text/html;charset=utf-8\n')
print('''
<html>
<body>
이름 : {0} <br>
전화 : {1} <br>
성별 : {2} <br>
<a href='../main.html'>메인으로</a>
</body>
</html>
'''.format(name, phone, gender))