s1 = 'data 1'
s2 = '파이썬 변수에 값 저장'
print('Content-Type:text/html;charset=utf-8\n')
print('''
<html>
<body>
자료 출력 : {0}, {1} <br>
<img src='../images/aa.png' width = '60%' />
<br>
<a href='../main.html'>메인으로</a>
</body>
</html>
'''.format(s1, s2))