import cgi

form = cgi.FieldStorage()
irum = form['name'].value
nai = form['age'].value
print(irum + " " + nai)
print('Content-Type:text/html;charset=utf-8\n')
print('''
<html>
<body>
이름 : {0} <br>
나이 : {1} <br>
<a href='../main.html'>메인으로</a>
</body>
</html>
'''.format(irum, nai))