#  lxml是使用xpath语法来进行文件格式解析，与Beautiful相比，效率更高。

from lxml import etree

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">第一个</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0"><a href="link5.html">a属性</a>
     </ul>
 </div>
'''

# 下面是读取文本解析节点
tree_object = etree.HTML(text)  # 初始化生成一个XPath解析对象（树对象）
result = etree.tostring(tree_object, encoding='utf-8')  # 解析对象输出代码
print(type(tree_object))
print(type(result))
print(result.decode('utf-8'))

"""
/                     ：从当前节点选取直接子节点
//                    ：从当前节点选取子孙节点
.                     ：选取当前节点
..                    ：选取当前节点的父节点
@                     ：选取属性
*                     ：通配符，选择所有元素节点与元素名
@*                    ：选取所有属性
[@attrib]             ：选取具有给定属性的所有元素
[@attrib='value']     ：选取给定属性具有给定值的所有元素
[tag]                 ：选取所有具有指定元素的直接子节点
[tag='text']          ：选取所有具有指定元素并且文本内容是text节点
"""

# 读取Html文件进行解析，即使用xpath来提取字符串或者子节点：results = tree_object.xpath('')
result1 = tree_object.xpath('//*')  # //代表获取子孙节点，*代表获取所有
print(result1)
result2 = tree_object.xpath('//li')  # 获取所有子孙节点的li节点
print(result2)
result3 = tree_object.xpath('//li/a')  # 通过追加/a选择所有li节点的所有直接a节点，因为//li用于选中所有li节点，/a用于选中li节点的所有直接子节点a
print(result3)

text2 = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">第一个</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
     </ul>
 </div>
'''

# 我们知道通过连续的/或者//可以查找子节点或子孙节点，那么要查找父节点可以使用..来实现也可以使用parent::来获取父节点
# 使用@符号即可获取节点的属性，如下：@class表示获取class属性
html = etree.HTML(text2, etree.HTMLParser())
result = html.xpath('//a[@href="link2.html"]/../@class')
result1 = html.xpath('//a[@href="link2.html"]/parent::*/@class')
print(result)
print(result1)

# 我们用XPath中的text()方法获取节点中的文本
html = etree.HTML(text2, etree.HTMLParser())
result = html.xpath('//li[@class="item-1"]/a/text()')  # 获取a节点下的内容
result1 = html.xpath('//li[@class="item-1"]//text()')  # 获取li下所有子孙节点的内容

print(result)
print(result1)


# 属性多值匹配：
text1 = '''
<div>
    <ul>
         <li class="aaa item-0"><a href="link1.html">第一个</a></li>
         <li class="bbb item-1"><a href="link2.html">second item</a></li>
     </ul>
 </div>
'''

html = etree.HTML(text1, etree.HTMLParser())
result = html.xpath('//li[@class="aaa"]/a/text()')
result1 = html.xpath('//li[contains(@class,"aaa")]/a/text()')

# 结果如下：通过第一种方法没有取到值，通过contains（）就能精确匹配到节点了
print(result)
print(result1)

# 多属性匹配：
text1='''
<div>
    <ul>
         <li class="aaa" name="item"><a href="link1.html">第一个</a></li>
         <li class="aaa" name="fore"><a href="link2.html">second item</a></li>
     </ul>
 </div>
'''

html=etree.HTML(text1,etree.HTMLParser())
result=html.xpath('//li[@class="aaa" and @name="fore"]/a/text()')
result1=html.xpath('//li[contains(@class,"aaa") and @name="fore"]/a/text()')


print(result)
print(result1)
