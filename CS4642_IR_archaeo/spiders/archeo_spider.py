import scrapy


class ArcheoSpider(scrapy.Spider):
    name = "archeo"

    def start_requests(self):
        urls = [
            'https://www.archaeology.lk'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for a in response.css('a.tag-cloud-link'):
            yield response.follow(a, callback=self.parse_article)

    def parse_article(self, response):
        for post in response.css('article.post'):
            yield {
                'title': str(post.css('h2.entry-title a::text').extract_first()),
                'link': str(post.css('h2.entry-title a::attr(href)').extract_first()),
                'tags': post.css('a[rel="tag"]::text').extract(),
            }
