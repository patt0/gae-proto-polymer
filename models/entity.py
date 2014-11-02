from google.appengine.ext import ndb
from endpoints_proto_datastore.ndb import EndpointsModel
from endpoints_proto_datastore.ndb import EndpointsAliasProperty
from protorpc import messages

class Entity(EndpointsModel):

    _message_fields_schema = ('id', 'uid', 'text', 'username', 'avatar', 'favorite')

    uid = ndb.StringProperty()
    text = ndb.StringProperty()
    username = ndb.StringProperty()
    avatar = ndb.StringProperty()
    favorite = ndb.BooleanProperty()

    def IdSet(self, value):
        if not isinstance(value, basestring):
            raise TypeError('ID must be a string.')
        self.uid = value
        self.UpdateFromKey(ndb.Key(Entity, value))

    @EndpointsAliasProperty(setter=IdSet, required=True)
    def id(self):
        if self.key is not None:
            return self.key.string_id()