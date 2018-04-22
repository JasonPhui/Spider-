from python爬虫.MyScrapy.HTML下载器 import HtmlDownloader
from python爬虫.MyScrapy.HTML解析器 import HtmlParse
from python爬虫.MyScrapy.URL管理器 import UrlManage
from python爬虫.MyScrapy.数据存储器 import DataOutput


class SpiderMan:
    def __init__(self):
        self.downloder = HtmlDownloader()
        self.parser = HtmlParse()
        self.manager = UrlManage()
        self.output = DataOutput()

    def crawl(self, root_url):
        # 添加入口url
        self.manager.add_new_url(root_url)
        # 判断url管理器中是否有新的url,同时判断抓取了多少个url
        while self.manager.has_new_url() and self.manager.old_url_size() < 100:
            try:
                # 从url管理器中获取新的url
                new_url = self.manager.get_new_url()
                # HTML下载器下载网页
                html = self.downloder.download(new_url)
                # HTML解析器抽取网页数据
                new_urls, data = self.parser.parser(new_url, html)
                # 将抽取的url添加到url管理器中
                self.manager.add_new_urls(new_urls)
                # 数据存储器存储数据
                self.output.store_data(data)
                print('已经抓取%s个链接' % self.manager.old_url_size())
            except Exception as e:
                print('crawl failed')
        self.output.output_html()


if __name__ == '__main__':
    spider_man = SpiderMan()
    spider_man.crawl('https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711?fr=aladdin')