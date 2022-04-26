import cgi

form = cgi.FieldStorage

name = form["name"].value
phone = form["phone"].value
gen = form["gen"].value

print('Content-Type:text/html; charset=utf-8\n')
print("""
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h2>친구 정보</h2>
이름은 {0}, 전화는 {1}, 성별은 {2}
<br>
<a href='../main.html'>메인으로</a>
</body>
</html>
""" .format(name, phone, gen))