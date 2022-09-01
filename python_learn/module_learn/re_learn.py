import re

# 下面讲解三个主要的re函数：re.match和re.search()以及re.compile()函数
# 下面的内容可以直接去看自己当时写过的博客
content = 'Hello 123 4567 World_This is a Regex Demo'
result1 = re.match('Hello\s\d{3}\s\d{4}\s\w{10}', content)
print(result1)
# group（）在正则表达式中用于获取分段截获的字符串
print(result1.group())
print(result1.span())

# 下面是re.search函数，改进了re.match只能从字符串的一开始进行查找匹配的字符串，
# 而re.search是从头开始，在整个字符串中查找，找到则立马停止。
line = "Cats are smarter than dogs"
matchObj1 = re.match(r'dogs', line, re.M | re.I)
if matchObj1:
    print(matchObj1.group())
else:
    print("No match!!")
matchObj2 = re.search(r'dogs', line, re.M | re.I)
print(matchObj2.group())

s = 'A B C D'
result2 = re.compile('\w+\s+\w?').findall(s)
print(result2)

result3 = re.compile('(\w+\s+)\w?').findall(s)
print(result3)

test_str = '''
<input type="hidden" name="lt" value="LT-2027101-wiAK5mdsf9uV1NVOJKcs7gSa6LaJcd1658484041159-4rcj-cas"/>
<input type="hidden" name="dllt" value="userNamePasswordLogin"/>
<input type="hidden" name="execution" value="e1s1"/>
<input type="hidden" name="_eventId" value="submit"/>
<input type="hidden" name="rmShown" value="1">
'''
# 想要得到上面name和value对的数据，使用正则表达式就非常容易得到了
result3 = re.compile('<input type="hidden" name="(\w+)" value="(\S+)"').findall(test_str)
print(result3)


# 下面是一些具体的例子
text = "文本最重要的来源无疑是网络。我们要把网络中的文本获取形成一个文本数据库。利用一个爬虫抓取到网络中的信息。爬取的策略有广度爬取和深度爬取。根据用户的需求，爬虫可以有主题爬虫和通用爬虫之分。"
# 假设我们想要找到关于爬虫的句子
regex = '爬虫?'
sentence_lst = text.split("。")
for line in sentence_lst:
    if re.search(regex, line) is not None:
        print(line)
# 下面是使用中括号匹配多个字符，且使用反斜杠作为转义字符
# "[bcr]at"代表的是匹配"bat""cat"以及"rat"
text_string = ['[重要的]今年第七号台风23日登陆广东东部沿海地区','上海发布车库销售监管通知：违规者暂停网签资格','[紧要的]中国对印连发强硬信息，印度急切需要结束对峙']
regex = '^\[[重紧]..'  # "[bcr]at"代表的是匹配"bat""cat"以及"rat"
for line in text_string:
    if re.search(regex,line) is not None:
        print(line)
    else:
        print('not match')

# 练习：下面我想要将年份1000-2999年之间的句子输出
strings = ['War of 1812','There are 5280 feet to a mile','Happy New Year 2016!']

# regex = '[12][0123456789][0123456789][0123456789]'
regex = '[1-2][0-9]{3}'
for string in strings:
    if re.search(regex, string) is not None:
        print(re.search(regex, string).group())
        print(string)

