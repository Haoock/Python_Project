from lxml import etree
import requests

BASE_URL = 'https://www.zhihu.com/billboard'


def getHTML(url):
    ''' 获取网页 HTML 返回字符串
    Args:
        url: str, 网页网址
    Returns:
        HTML 字符串
    '''
    # Cookie 有效期至2023-02-10
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/84.0.4147.125 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    return response.text

# 使用 xpath 解析 HTML
def parseHTMLByXPath(content):
    html = etree.HTML(content)
    titles = html.xpath('//div[@class="Card"]/a[@class="HotList-item"]/div[@class="HotList-itemBody"]/div['
                        '@class="HotList-itemTitle"]/text()')
    hots = html.xpath('//div[@class="Card"]/a[@class="HotList-item"]/div[@class="HotList-itemBody"]/div['
                        '@class="HotList-itemMetrics"]/text()')
    print(titles)
    print(hots)


print(getHTML(BASE_URL))
parseHTMLByXPath(getHTML(BASE_URL))
