from huxiu.items import HuxiuItem
import scrapy


class HuXiuSpider(scrapy.Spider):
    name = 'huxiu'
    allowed_domains = ['huxiu.com']
    start_urls = ['https://www.huxiu.com/index.php/']

    def parse(self, response):
        for sel in response.xpath("//div[@class='mod-info-flow']/div[@class='mod-b mod-art clearfix ']"):
            item = HuxiuItem()
            title_datas = sel.xpath("div[@class='mob-ctt index-article-list-yh']/h2/a/text()")
            item['title'] = title_datas[0].extract() if title_datas else ''
            link_datas = sel.xpath("div[@class='mob-ctt index-article-list-yh']/h2/a/@href")
            item['link'] = link_datas[0].extract() if link_datas else ''
            url = response.urljoin(item['link'])
            desc_datas = sel.xpath("div[@class='mob-ctt index-article-list-yh']/div[@class='mob-sub']/text()")
            item['desc'] = desc_datas[0].extract() if desc_datas else ''
            yield scrapy.Request(url, callback=self.parse_article)

    def parse_article(self, response):
        try:
            detail = response.xpath('//div[@class="article-wrap"]')
            item = HuxiuItem()
            item['title'] = detail.xpath('h1/text()')[0].extract().strip()
            item['link'] = response.url
            item['post_time'] = detail.xpath(
                "div[@class='article-author']/div[@class='column-link-box']/"
                "span[@class='article-time pull-left']/text()")[0].extract()
            yield item
        except IndexError:
            yield scrapy.Request(response.url, callback=self.parse_article)
