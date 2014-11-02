import endpoints
from protorpc import remote

from models import Entity

api_root = endpoints.api(name='myApi', version='v1.0b')

@api_root.api_class(resource_name='entity', path='entity')
class EntityService(remote.Service):

    @Entity.method(path='/entity/{id}', http_method='POST', name='insert')
    def insert(self, entity):
        entity.put()
        return entity

    @Entity.method(path='/entity/{id}', http_method='GET', name='get')
    def get(self, entity):
        if not entity.from_datastore:
            raise endpoints.NotFoundException('Entity not found.')

        return entity

    @Entity.method(path='/entity/{id}', http_method='DELETE', name='delete')
    def delete(self, entity):
        if not entity.from_datastore:
            raise endpoints.NotFoundException('Entity not found.')

        entity.key.delete()
        return entity

    @Entity.query_method(query_fields=('limit', 'order', 'pageToken'),
                         path='/entity', name='list')
    def list(self, query):
        return query
