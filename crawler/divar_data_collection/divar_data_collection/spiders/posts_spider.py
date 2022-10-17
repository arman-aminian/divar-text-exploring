import scrapy
from divar_data_collection.utils.get_tokens import get_tokens
url = 'https://divar.ir/v/-/{post_token}'


class PostsSpider(scrapy.Spider):
    name = 'divar'
    # start_urls = [url.format(post_token=token) for token in ['asfsadf', 'asdfaf']]
    start_urls = [url.format(post_token=token) for token in get_tokens(1650392836073764, 1, n_pages=2)]

    def parse(self, response, **kwargs):
        informations = response.css('div span.kt-group-row-item__value::text')

        area = int(informations[0].extract())
        construction = int(informations[1].extract())
        rooms = int(informations[2].extract())

        warehouse = False if 'ندارد' in informations[3].extract() else True
        parking = False if 'ندارد' in informations[4].extract() else True
        elevator = False if 'ندارد' in informations[5].extract() else True

        address = response.css('div div.kt-page-title__subtitle--responsive-sized::text').extract()
        price = response.css('div p.kt-unexpandable-row__value::text').extract_first()

        description = response.css('div p.kt-description-row__text--primary').extract_first()

        yield {
            'Area': area,
            'Construction': construction,
            'Room': rooms,
            'Warehouse': warehouse,
            'Parking': parking,
            "Elevator": elevator,
            'Address': address,
            'Price': price,
            'Description': description
        }
