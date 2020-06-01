# -*- coding: utf-8 -*-
# 展会门户
import scrapy
import re
from ..items import ZhanhuimenhuItem


class ZhSpider(scrapy.Spider):
    name = 'zh'
    # allowed_domains = ['zhanhui.com']
    start_urls = ['http://zhanhui.com/']
    start_req = 'http://www.cnena.com/showroom/listall-htm-ordertype-id-page-1.html'
    base_url = 'http://www.cnena.com/showroom/'
    cat_req = 'http://www.cnena.com/showroom/listall-htm-ordertype-id-page-{}.html'

    def start_requests(self):
        # yield scrapy.Request(url=self.start_req, callback=self.parse)
        for page in range(1, 2284):
            yield  scrapy.Request(url=self.cat_req.format(page), callback=self.parse)

    def parse(self, response):
        url_lists = response.xpath('//div[@class="srpnel"]//td[@width="34%"]/a[1]/@href').extract()
        page = response.xpath('//div[@class="page"]/a/font/text()').extract_first()

        for next_url in url_lists:
            # print(next_url)
            meta = {
                'page': page
            }
            yield scrapy.Request(url=self.base_url + next_url, callback=self.parse_detial, meta=meta)
        # next_list = response.xpath('//a[@title="下一页"]/@href').extract_first()
        # yield scrapy.Request(url=self.base_url + next_list, callback=self.parse)

    def parse_detial(self, response):
        tishi = response.xpath('//td[@class="title"]/text()').extract_first()
        # print(tishi)
        if tishi != '温馨提示:':
            item = ZhanhuimenhuItem()
            print('来自第', response.meta['page'], '页面的信息')

            title = response.xpath('//h2/text()').extract_first()
            interest = response.xpath('//div[@class="headArea-main"]/p/b/text()').extract_first().strip()
            startData = re.findall(r'开幕日期：(.*?)<br>', response.text)[0]
            endData = re.findall(r'结束日期：(.*?)<br>', response.text)[0]
            # print(title, interest, startData, endData)

            organization = response.xpath('//div[@class="sub-info-2"][2]/div[2]//text()').extract()
            organize = ''
            for each_text in organization:
                if each_text != '\r\n':
                    organize += each_text.strip()

            release_platform = 'http://www.cnena.com/showroom'
            contacts = response.xpath('//div[@class="sub-info-2"][4]/p/text()').extract()
            contact = ' '.join(cont.strip() for cont in contacts)

            contents = response.xpath('//div[@class="area-main"]/div[@class="main-info"]/p/text()').extract()
            content = ' '.join(content_one.strip() for content_one in contents)

            item['title'] = title
            item['interest'] = interest
            item['startData'] = startData
            item['endData'] = endData
            item['organize'] = organize
            item['release_platform'] = release_platform
            item['contact'] = contact
            item['content'] = content

            yield item
