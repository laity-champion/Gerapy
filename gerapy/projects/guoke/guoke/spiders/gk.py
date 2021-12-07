import scrapy


class GkSpider(scrapy.Spider):
    name = 'gk'

    # allowed_domains = ['www.xxx.com']
    start_urls = [
        f'https://www.guokr.com/apis/minisite/article.json?ukey=bkfczo&offset=8&limit={page}&retrieve_type=by_ukey' for
        page in range(0, 89, 8)]

    # def start_requests(self):
    #     yield scrapy.Request(
    #         url='https://www.guokr.com/apis/minisite/article.json?ukey=bkfczo&offset=8&limit=8&retrieve_type=by_ukey')

    def parse(self, response):
        resp = response.json()
        results = resp['result']
        item = {}
        for result in results:
            item['title'] = result['title']  # 标题
            item['url'] = result['url']  # 文章url
            item['summary'] = result['summary']  # 文章封面内容
            print(item)
            yield item
            # url = result['url']
