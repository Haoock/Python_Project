from lxml import etree
import requests

BASE_URL = 'https://s.weibo.com'
JSON_DIR = './raw'
ARCHIVE_DIR = './archives'


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
                      'Chrome/84.0.4147.125 Safari/537.36',
        'Cookie': 'SUB=_2AkMVWDYUf8NxqwJRmP0Sz2_hZYt2zw_EieKjBMfPJRMxHRl-yj9jqkBStRB6PtgY-38i0AF7nDAv8HdY1ZwT3Rv8B5e5'
                  '; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WFencmWZyNhNlrzI6f0SiqP '
    }
    response = requests.get(url, headers=headers)
    return response.text


# 使用 xpath 解析 HTML
def parseHTMLByXPath(content):
    """ 使用 xpath 解析 HTML, 提取榜单信息
    Args:
        content: str, 待解析的 HTML 字符串
    Returns:
        榜单信息的字典 字典
    """
    html = etree.HTML(content)
    # 下面是我之前的写法，还是挺麻烦的
    # hots = html.xpath('//div[@class="data"]//tbody/tr[position()>1]/td[@class="td-02"]/a[not(contains(@href, "javascript:void(0);"))]/../span/text()')
    # 这边加上javascript:void(0);的原因主要是因为有推荐的一个条目的时候会出现问题，所以要排除这个条目（not contains）。
    titles = html.xpath('//tr[position()>1]/td[@class="td-02"]/a[not(contains(@href, "javascript:void(0);"))]/text()')
    hrefs = html.xpath('//tr[position()>1]/td[@class="td-02"]/a[not(contains(@href, "javascript:void(0);"))]/@href')
    hots = html.xpath(
        '//tr[position()>1]/td[@class="td-02"]/a[not(contains(@href, "javascript:void(0);"))]/../span/text()')
    titles = [title.strip() for title in titles]
    hrefs = [BASE_URL + href for href in hrefs]
    for i in range(len(titles)):
        print("%20s" % titles[i], end=" ")
        print("%20s" %hrefs[i], end=" ")
        print(hots[i])
    hots = [int(hot.strip().split(' ')[-1]) for hot in hots]  # 该处除了热度还会返回大致分类，形如 `剧集 53412536`，前为分类，后为热度


def main():
    url = '/top/summary'

    content = getHTML(BASE_URL + url)
    parseHTMLByXPath(content)


if __name__ == '__main__':
    main()
