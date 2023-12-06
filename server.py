# gunicorn
# fastapi or flask or aiohttp or sarlette
# Django

# Model -> View -> Template -> Response
from models import Offer
from urls import url_handlers


def app(environ, start_response):
    offer = Offer()
    #load input.json
    offer_dict = offer.offer_data
    return url_handlers(environ, start_response,offer_dict)
    