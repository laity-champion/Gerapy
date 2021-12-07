import scrapy


class DdwSpider(scrapy.Spider):
    name = 'ddw'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://search.dangdang.com/?key=python&act=input']

    def parse(self, response):
        lis = response.xpath('//ul[@id="component_59"]/li')
        item = {}
        for li in lis:
            item["name"] = li.xpath('./a[@class="pic"]/@title').get()
            item["author"] = li.xpath('./p/span[1]/a[1]/@title').get() if len(
                li.xpath('./p/span[1]/a[1]/@title')) > 0 else "无作者信息"
            item["introduction"] = li.xpath('./p[@class="detail"]/text()').get() if len(
                li.xpath('./p[@class="detail"]/text()')) else "无介绍信息"
            item["price"] = li.xpath('./p/span[@class="search_now_price"]/text()').get()
            item["press"] = li.xpath("./p[@class='search_book_author']/span[3]/a/text()").get() if len(
                li.xpath("./p[@class='search_book_author']/span[3]/a/text()")) else "无出版信息"
            item["time"] = li.xpath("./p[@class='search_book_author']/span[2]/text()").get().replace("/",
                                                                                                     '').strip() if len(
                li.xpath("./p[@class='search_book_author']/span[2]/text()")) > 0 else "无出版时间"
            item["comment"] = li.xpath("./p[@class='search_star_line']/a/text()").get().strip()
            # print(item)
            yield item
            
