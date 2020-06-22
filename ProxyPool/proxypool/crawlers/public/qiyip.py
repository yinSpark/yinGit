# import sys
# sys.path.append('.')

from proxypool.schemas.proxy import Proxy
from proxypool.crawlers.base import BaseCrawler
from pyquery import PyQuery as pq


BASE_URL = 'https://www.7yip.cn/free/?action=china&page={page}'
MAX_PAGE = 5


class QiyipCrawler(BaseCrawler):
    """
    齐云代理: https://www.7yip.cn/free/?action=china&page=1
    """
    urls = [BASE_URL.format(page=page) for page in range(1, MAX_PAGE + 1)]

    def parse(self, html):
        """
        parse html file to get proxies
        :return:
        """
        doc = pq(html)
        trs = doc('div.container table tbody  tr').items()
        for tr in trs:
            host = tr.find('td:nth-child(1)').text()
            port = int(tr.find('td:nth-child(2)').text())
            yield Proxy(host=host, port=port)


if __name__ == '__main__':
    print(__file__)
    crawler = QiyipCrawler()
    for proxy in crawler.crawl():
        print(proxy)