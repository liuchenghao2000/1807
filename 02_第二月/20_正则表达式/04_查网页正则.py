import re
web_1='https://www.dadyface.com.das.aae.'
test = re.match('^https://w{3}\.\w*\.(com|cn)$',web_1)

print(test) 
web_2=[]
web_3=[]
web_2.append('http://www.interoem.com/messageinfo.asp?id=35')
web_2.append('http://3995503.com/class/class09/news_show.asp?id=14')
web_2.append('http://lib.wzmc.edu.cn/news/onews.asp?id=769')
web_2.append('http://www.zy-ls.com/alfx.asp?newsid=377&id=6')
web_2.append('http://www.fincm.com/newslist.asp?id=415')
for i in web_2:
	test_2 = re.sub('[^(https://w{3}\.\w*\.(com|cn)$)]\w+',' ',i)
	web_3.append(test_2)
print(web_3)
