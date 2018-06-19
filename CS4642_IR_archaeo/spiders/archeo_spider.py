import scrapy


class ArcheoSpider(scrapy.Spider):
    name = "archeo"

    def start_requests(self):
        urls = [
            'https://www.archaeology.lk/category/excavation',
            'https://www.archaeology.lk/category/exploration',
            'https://www.archaeology.lk/category/maritime-archaeology',
            'https://www.archaeology.lk/category/books',
            'https://www.archaeology.lk/category/research-paper'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)