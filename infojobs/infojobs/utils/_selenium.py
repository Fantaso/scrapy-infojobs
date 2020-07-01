import time
from pprint import pprint

from scrapy import Selector
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def open_browser_to_solve_captcha(url):
    # BROWSER_ZOOM_SETTING = "layout.css.devPixelsPerPx"
    # ZOOM_FACTOR = "0.4"
    TIME_SECS = 3
    options = Options()
    # options.add_argument("-headless")
    # profile = FirefoxProfile()
    # profile.set_preference(BROWSER_ZOOM_SETTING, ZOOM_FACTOR)
    browser = webdriver.Firefox(options=options)
    # browser = webdriver.Firefox(options=options, firefox_profile=profile)
    browser.maximize_window()
    browser.implicitly_wait(TIME_SECS)
    browser.get(url)
    try:
        time.sleep(15)
        return browser.current_url, browser.page_source

    finally:
        browser.quit()


def open_browser(url):
    # BROWSER_ZOOM_SETTING = "layout.css.devPixelsPerPx"
    # ZOOM_FACTOR = "0.4"
    TIME_SECS = 3
    options = Options()
    # options.add_argument("-headless")
    # profile = FirefoxProfile()
    # profile.set_preference(BROWSER_ZOOM_SETTING, ZOOM_FACTOR)
    browser = webdriver.Firefox(options=options)
    # browser = webdriver.Firefox(options=options, firefox_profile=profile)
    browser.maximize_window()
    browser.implicitly_wait(TIME_SECS)
    browser.get(url)

    time.sleep(15)
    return browser


def get_browser():
    # INIT
    secs = 3

    # CONFIG
    profile = webdriver.FirefoxProfile('/home/carlos/.mozilla/firefox/2qj7pfw0.infojobs')
    # profile = webdriver.FirefoxProfile('/home/carlos/.mozilla/firefox/se4tmv4c.nana')
    browser = webdriver.Firefox(firefox_profile=profile)
    time.sleep(1)
    # browser.implicitly_wait(secs)
    time.sleep(1)
    browser.maximize_window()
    return browser


def parse_jobs():
    keyword = 'devops'
    paginated = 2
    browser = get_browser()
    # browser.get(f'https://www.infojobs.net/jobsearch/search-results/list.xhtml?keyword={keyword}&page={page_num}')
    # for page_num in range(1, paginated):

    # PARSE JOBS
    time.sleep(1)
    browser.get(f'https://www.infojobs.net/jobsearch/search-results/list.xhtml?keyword={keyword}')
    time.sleep(15)
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(6)
    selector = Selector(text=browser.page_source)
    jobs = selector.css('.sui-AtomCard-link')
    jobs_ctx = ['https:' + job.css('.ij-OfferCardContent-description-title-link::attr(href)').get()
                for job in jobs]
    # for job in jobs:
    #     ctx = {'title': job.css('.ij-OfferCardContent-description-title-link::text').get(),
    #            'company': job.css('.ij-OfferCardContent-description-subtitle-link::text').get(),
    #            'city': job.css('.ij-OfferCardContent-description-list-item-truncate::text').get(),
    #            'url': 'https:' + job.css('.ij-OfferCardContent-description-title-link::attr(href)').get()}
    #     jobs_ctx.append(ctx)

    pprint(jobs_ctx)
    parse_job(jobs_ctx)


def parse_job(jobs_ctx):
    for job in jobs_ctx:
        browser = get_browser()
        browser.get(job.get('url'))
        time.sleep(2)
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(3)
        print(job.get('url'))
        time.sleep(3)


if __name__ == '__main__':
    def start():
        # get first page
        browser = get_browser()
        browser.get(f'https://www.infojobs.net/jobsearch/search-results/list.xhtml?keyword={"devops"}')
        parsing_jobs(browser)


    def parsing_jobs(browser):

        # wait for the results to appear. 'ofertas de trabajo de {devops} encontradas'
        try:
            search_text = WebDriverWait(browser, 25).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".ij-ResultsOverview"))
            )
        except Exception as e:
            print('ERR @ search text')
            print(e)

        # scroll down all the way
        height = browser.execute_script("return document.body.scrollHeight")
        # print(height, type(height))
        # scroll little by little
        times = height // 250
        print(times)
        current_height = 0
        for i in range(times):
            current_height += 250
            browser.execute_script(f"window.scrollTo(0,{current_height});")
            time.sleep(0.2)

        # wait for something to appear
        # get all job urls and save in a list
        selector = Selector(text=browser.page_source)
        jobs = selector.css('.sui-AtomCard-link')
        job_links = []
        for job in jobs:
            job_link = job.css('.ij-OfferCardContent-description-title-link::attr(href)').get()
            if job_link:
                url = f"https:{job_link}"
                print(url)
                job_links.append(url)

        print(len(job_links))
        pprint(job_links)

        # grab the next button and click it
        try:
            next_url = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Siguiente"))
            )
            print('next_url')
            print(next_url)
            next_url.click()
            parsing_jobs(browser)
        except Exception as e:
            print('ERR @ next url')
            print(e)

        try:
            next_url = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "SIGUIENTE"))
            )
            print('next_url')
            print(next_url)
            next_url.click()
            parsing_jobs(browser)
        except Exception as e:
            print('ERR @ next url')
            print(e)

        parsing_job(browser, job_links)


    def parsing_job(browser, job_links):
        for link in job_links:
            browser.get(link)
            time.sleep(4)
            selector = Selector(text=browser.page_source)
            title = selector.css('#prefijoPuesto::text').get()
            company_name = selector.css('.content-type-text .link::text').get()
            city = selector.css('#prefijoPoblacion::text').get()
            salary = selector.css('.list-bullet-default li~ li+ li span::text').get()
            experience = selector.css('h2+ .list-default li+ li .list-default-text::text').get()
            tech_stack = selector.css('.tag').getall()
            description = selector.css('#prefijoDescripcion1 p::text').getall()
            vacancies = selector.css('#prefijoVacantes::text').get()
            level = selector.css('#prefijoNivelLaboral::text').get()
            contract_type = selector.css('#prefijoJornada::text').get()
            published = selector.css('.marked::text').get()


    start()
