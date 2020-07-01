from scrapy import Field, Item


class InfojobsItem(Item):
    url = Field()
    title = Field()
    company_name = Field()
    city = Field()
    salary = Field()
    experience = Field()
    tech_stack = Field()
    description = Field()
    vacancies = Field()
    level = Field()
    contract_type = Field()
    published = Field()
