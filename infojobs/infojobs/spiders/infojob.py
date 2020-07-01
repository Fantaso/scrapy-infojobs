import time
from pprint import pprint

import scrapy
from scrapy import Selector
from selenium import webdriver

from ..loaders import InfojobsLoader


class InfojobSpider(scrapy.Spider):
    name = 'infojob'
    allowed_domains = ['infojobs.net']
    job_keyword = 'devops'
    job_page = 2

    # CAPTCHA
    # https://www.infojobs.net/distil_r_captcha.html?requestId=b363052e-3c3b-4e49-96da-04ec24e37d43&httpReferrer=%2Fjobsearch%2Fsearch-results%2Flist.xhtml%3Fkeyword%3Ddevops'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        profile = webdriver.FirefoxProfile('/home/carlos/.mozilla/firefox/2qj7pfw0.infojobs')
        # profile = webdriver.FirefoxProfile('/home/carlos/.mozilla/firefox/se4tmv4c.nana')
        self.browser = webdriver.Firefox(firefox_profile=profile)
        time.sleep(1)
        self.browser.maximize_window()

    def start_requests(self):
        start_urls = [
            scrapy.Request(
                url=f"https://www.infojobs.net/jobsearch/search-results/list.xhtml?keyword=devops&page={page_num}",
                callback=self.parse_jobs,
            )
            for page_num in range(1, self.job_page)
        ]
        return start_urls

    def parse_jobs(self, response):
        self.browser.get(response.url)
        time.sleep(2)
        if 'captcha' in self.browser.current_url:
            self.logger.info(f'Captcha found: {response.url}')
            # time to solve the captcha
            time.sleep(12)

        # scroll down all the way
        height = self.browser.execute_script("return document.body.scrollHeight")
        # scroll little by little
        times = height // 250
        current_height = 0
        for i in range(times):
            current_height += 250
            self.browser.execute_script(f"window.scrollTo(0,{current_height});")
            time.sleep(0.2)

        selector = Selector(text=self.browser.page_source)
        jobs = selector.css('.sui-AtomCard-link')
        print(f'----len(jobs): {len(jobs)}')
        for job in jobs:
            url = job.css('.ij-OfferCardContent-description-title-link::attr(href)').get()
            if url:
                url = 'https:' + url
                yield scrapy.Request(url=url, callback=self.parse_job)

        # image_urls = selector.css('.sui-AtomImage-image::attr(src)').getall()

    def parse_job(self, response):
        loader = InfojobsLoader(response=response)
        loader.add_value('url', response.url)

        if 'captcha' in response.url:
            self.logger.info(f'----Captcha found: {response.url}')
            self.browser.get(response.url)
            # time to solve the captcha
            time.sleep(12)
            selector = Selector(text=self.browser.page_source)
            loader = InfojobsLoader(selector=selector)
            loader.add_value('url', self.browser.current_url)

        loader.add_css('title', '#prefijoPuesto::text')
        loader.add_css('company_name', '.content-type-text .link::text')
        loader.add_css('city', '#prefijoPoblacion::text')
        loader.add_css('salary', '.list-bullet-default li~ li+ li span::text')
        loader.add_css('experience', 'h2+ .list-default li+ li .list-default-text::text')
        loader.add_css('tech_stack', '.tag::text')
        loader.add_css('description', '#prefijoDescripcion1 p::text')
        loader.add_css('vacancies', '#prefijoVacantes::text')
        loader.add_css('level', '#prefijoNivelLaboral::text')
        loader.add_css('contract_type', '#prefijoJornada::text')
        loader.add_css('published', '.marked::text')
        pprint(loader.load_item())

        yield loader.load_item()
