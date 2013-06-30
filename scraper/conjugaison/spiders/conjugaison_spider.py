# -*- coding: utf-8 -*-
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from .verbs import VERBS
from conjugaison.items import ConjugaisonItem

class ConjugasionSpider(BaseSpider):
    def get_start_urls():
        url_base = 'http://www.collinsdictionary.com/dictionary/french-english/conjugation/{0}'
        urls = []
        for verb in VERBS:
            urls.append(url_base.format(verb))

        return urls

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        verbe = hxs.select('//div[@class="type"]')[0].select('ul/li/text()').extract()[0]
        conjugations = hxs.select('//div[@class="conjugation" or @class="conjugation nomargin"]')
        item = ConjugaisonItem()
        item['verbe'] = verbe
        temps = []
        for conjugation in conjugations:
            temp = conjugation.select('h3/text()').extract()[0]
            inflections = conjugation.select('ul/li/text()').extract()
            if inflections:
                mode, inflection = self.translate(temp)
                temp = { 'mode' : mode, 'inflection': inflection, 'inflections': inflections }
                temps.append(temp)
        
        item['temps'] = temps
        return item

    def translate(self, temp):
        # Indicatif
        if temp == 'Present Indicative':
            return u'indicatif', u'présent'
        elif temp == 'Past Historic':
            return u'indicatif', u'passé simple'
        elif temp == 'Imperfect':
            return u'indicatif', u'imparfait'
        elif temp == 'Future':
            return u'indicatif', u'futur simple'
        # Conditionnel
        elif temp == 'Conditional':
            return u'conditionnel', u'présent'
        if temp == 'Perfect Conditional':
            return u'conditionnel', u'passé'
        # Subjonctif
        elif temp == 'Imperfect Subjunctive':
            return u'subjonctif', u'imparfait'
        elif temp == 'Present Subjunctive':
            return u'subjonctif', u'présent'
        elif temp == 'Present Perfect Subjunctive':
            return u'subjonctif', u'passé'
        elif temp == 'Pluperfect Subjunctive':
            return u'subjonctif', u'plus-que-parfait'
        # Imperatif
        elif temp == 'Imperative':
            return u'impératif', u'présent'
        # Formes Composees
        elif temp == 'Pluperfect':
            return u'formes composées', u'plus-que-parfait'
        elif temp == 'Future Perfect':
            return u'formes composées', u'futur antérieur'
        elif temp == 'Present Perfect':
            return u'formes composées', u'passé composé'
        elif temp == 'Past Anterior':
            return u'formes composées', u'passé antérieur'

    name = 'conjugaison'
    start_urls = get_start_urls()
    download_delay = 2
