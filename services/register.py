""" Endpoint api server registration."""

import endpoints
from .endpoint import EntityService

api = endpoints.api_server([EntityService],
                            restricted=False)
