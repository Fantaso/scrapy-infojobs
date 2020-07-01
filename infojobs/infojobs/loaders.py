from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join

from .items import InfojobsItem


class InfojobsLoader(ItemLoader):
    default_item_class = InfojobsItem
    default_input_processor = MapCompose(str.strip)
    default_output_processor = TakeFirst()

    tech_stack_out = Join(', ')
    description_out = Join(', ')
