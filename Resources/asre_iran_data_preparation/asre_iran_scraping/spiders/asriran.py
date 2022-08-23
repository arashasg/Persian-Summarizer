import csv

import scrapy

archive_url = 'https://www.asriran.com/fa/archive?service_id=1&sec_id=-1&cat_id=-1&rpp=100&from_date=1384/01/01&to_date=1401/05/27&p={}'

with open('output.csv', 'a', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['متن خبر', 'خلاصه خبر احتمالی 2', 'خلاصه خبر احتمالی 1', 'عنوان خبر', 'دسته بندی خبر'])


class AsrIranSpider(scrapy.Spider):
    name = 'AsrIran'

    @staticmethod
    def get_news_absolute_url(relative_url):
        return 'https://www.asriran.com' + relative_url

    @staticmethod
    def build_body_form_multiple_p_tags(text_list):
        return '\n'.join(text.strip() for text in text_list)

    def start_requests(self):
        for page_num in range(1, 1501):
            yield scrapy.Request(url=archive_url.format(page_num), callback=self.parse)

    def parse(self, response, **kwargs):
        news_urls = map(self.get_news_absolute_url, response.css('a.vizhe_title::attr(href)').getall())
        for url in news_urls:
            yield scrapy.Request(url=url, callback=self.parse_news_page)

    def parse_news_page(self, response):
        category = response.css('div.news_path a::text').getall()[1].strip()
        title = response.css('h1.title a::text').get().strip()
        gray_section = response.css('div.subtitle::text')
        if gray_section:
            possible_summary_1 = gray_section.get().strip()
        else:
            possible_summary_1 = 'خالی'
        body = response.css('div.body p::text').getall()
        if body:
            possible_summary_2 = body[0].strip()
            with open('output.csv', 'a', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([body, possible_summary_2, possible_summary_1, title, category])
