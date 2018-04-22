"""
HTML下载器用于从URL管理器中获取未爬取的URL链接并下载HTML阿页。
"""
import requests


class HtmlDownloader:

    def download(self, url):
        if url is None:
            return None
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                     'Chrome/64.0.3282.140 Safari/537.36'
        headers = {'User-Agent': user_agent}
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            res.encoding = 'utf-8'
            return res.text
        return None