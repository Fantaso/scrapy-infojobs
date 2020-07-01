<!-- logo -->
<a href="https://www.fantaso.de">
<img src="/readme/fantaso.png" align="right" />
</a>

<!-- header -->
<h1 style="text-align: left; margin-top:0px;">
  Jobs Scraper for infojobs.net
</h1>

> Jobs scraper app with Scrapy and Selenium.


<!-- build -->
<!-- [![Build Status][travis-image]][travis-link] -->


Project consists to allow a user to scrape the "devops" jobs in
infojobs.net (platform for spain) and use the data for analysis.

<br><br>

---
## Index:
- #### Usage
    0. Before it can be used some configuration is required as we are using Selenium with Firefox
    1. Clone and Run it
    2. What data are we scraping and where is stored

- #### Information:
- #### Maintainer

<br><br>


---
## Usage

#### 0. Before it can be used some configuration is required as we are using Selenium with Firefox
- Install firefox and the webdriver and add the path of your firefox into the spider where the selenium is configured
- Once Firefox is installed. create a profile for firefox. (in linux you can run `firefox -p`) or in your browser url write `about:profiles`
- Once profile is created. get the path and added to the the selenium configuration in the spider also.


#### 1. Clone and Run it

image is hosted in docker hub registry freely available [fantaso/scrapy_tradefest](https://hub.docker.com/repository/docker/fantaso/scrapy_tradefest)

cloning repo
    
```sh
git clone https://github.com/Fantaso/scrapy_infojobs/tree/master/infojobs
```

enter into the scrapy project

```sh
cd scrapy_infojobs/infojobs
```

run the scraper with

```sh
scrapy crawl infojob
```



---
#### 2.  What data are we scraping and where is stored
  
Output folder contains:
    
- `feeds` contains all the scraped data in different formats (csv, xml, json)
          
**NOTE:** all data files generated in `feeds/` are named or formatted
with the current time when the docker image is run. `e.g: "2020-06-28 23:47:18.csv"`

Fields to be scraped from each event or expo:
- `url`: url of the detailed job
- `title`: name of the job
- `company_name`: company posting the job
- `city`: city where the job is offered
- `salary`: salary for the job
- `experience`: 
- `tech_stack`: technologies required for the job
- `description`: detailed description of the job
- `vacancies`: number of people needed for this job
- `level`: could be employee, specialist, internship (there is no a sane pattern)
- `contract_type`: could be full-time job and indefinite contract 
- `published`: when was the job posted


<br>

## Information:
| Technology Stack |  |  |
| :- | :-: | :- |
| Python                    | ![back-end][python]                   | Back-End |
| Scrapy                    | ![scraper framework][scrapy]          | Scraper Framework |
| Selenium                  | ![browser automation][selenium]       | Browser Automation |

<br><br>


## Maintainer
Get in touch -–> [fantaso][fantaso]



<!-- Links -->
<!-- Profiles -->
[github-profile]: https://github.com/fantaso/
[linkedin-profile]: https://www.linkedin.com/
[fantaso]: https://github.com/fantaso/
<!-- Extra -->

<!-- Repos -->
[github-repo]: https://github.com/Fantaso/scrapy_infojobs

<!-- Builds -->
[travis-link]: https://travis-ci.org/
[travis-image]: https://travis-ci.org/

<!-- images -->
[python]: readme/python.png
[scrapy]: readme/scrapy.png
[selenium]: readme/selenium.png
