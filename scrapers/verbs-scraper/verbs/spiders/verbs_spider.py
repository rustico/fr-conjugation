# -*- coding: utf-8 -*-
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from verbs.items import VerbsItem

class VerbsSpider(BaseSpider):
    name = 'verbs'
    start_urls = ['http://leconjugueur.lefigaro.fr/frlistedeverbe.php']

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        verbs = hxs.select('//li/a/text()').extract()
        items = []
        for verb in verbs:
            item = VerbsItem()
            item['name'] = verb
            items.append(item)

        return items
