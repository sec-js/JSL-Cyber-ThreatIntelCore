# -*- coding: utf-8 -*-

import scrapy
import re
import json
import csv
import socket
from socket import getaddrinfo  #use to check for valid domain   => i.e. result = getaddrinfo("www.google.com", None)
from scrapy import Spider
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.http import Request
from blacklist_enrichment.items import MayhemListItem



class MayhemSpider(CrawlSpider):
    name = "sagadc"

    def start_requests(self):
        url  = 'http://dns-bh.sagadc.org/20160219.txt'
        yield Request(url, callback=self.parse_sagadc)

      
    def parse_sagadc(self, response):
        get_url = response #this gets us current URL crawling!
        url = re.match('<200\s*(.*?)>', str(get_url)).group(1) #some tidying up

        getall = response.xpath('//body').extract()
        getrows = getall[0].split('\n')
        #clean
        clean = [e.split('\t') for e in getrows]
        clean = [[f for f in e if f != ''] for e in clean]
        erase = [[e[i].replace(re.match('(<.*?>(?:<.*?>)?(?:<.*?>)?).*', e[i]).group(1), '') if re.match('<.*?>(?:<.*?>)?(?:<.*?>)?', e[i]) else f for i, f in enumerate(e)] for e in clean]


        domains = [e[0] for e in erase]

        
        for i, e in enumerate(domains):
            item = MayhemListItem()
            domain_name = domains[i]

            try:
                ip_address = socket.gethostbyname(str(domain_name))
            except socket.gaierror:
                ip_address = ''

                
            item['Address_IP'] = ip_address
            item['Domain_Name'] = domains[i]
            
        

            yield item

            #scrapy crawl sagadc -o dns_bh_sagadc_SA.csv