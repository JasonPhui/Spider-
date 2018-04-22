"""
HTML解析器用于从HTML下载器中获取己经 下载的HTML网页， 并从中解析出新
的URL链接交给URL管理器 ,解析出有效数据交给数据存储器。
"""
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin


class HtmlParse:

    def parser(self, page_url, html_cont):
        """
        解析下载器下载的网页，抽取url和数据
        :param page_url:下载页面的url
        :param html_cont:下载的网页内容
        :return:返回url和数据
        """
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'lxml')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_date(page_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        """
        抽取新的url集合
        :param page_url: 下载页面的url
        :param soup:soup
        :return:返回新的url集合
        """
        new_urls = set()
        links = soup.find_all('a', attrs={'href': re.compile(r'/item/.*?')})
        for link in links:
            new_url = link.get('href')
            # 拼接成完整网址
            new_full_url = urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_date(self, page_url, soup):
        """
        抽取有效数据
        :param page_url:
        :param soup:
        :return: 返回有效数据
        """
        data = {}
        data['url'] = page_url
        title = soup.find('dd', attrs={'class': 'lemmaWgt-lemmaTitle-title'}).find('h1')
        data['title'] = title.text
        summary = soup.find('div', attrs={'class': 'lemma-summary'})
        data['summary'] = summary.get_text()
        return data