from plone.app.users.userdataschema import IUserDataSchemaProvider
from plone.app.users.userdataschema import IUserDataSchema
from zope.interface import implements
from zope import schema
from upc.oauth2 import _


class IEnhancedUserDataSchema(IUserDataSchema):
    """ Use all the fields from the default user data schema, and add various
    extra fields.
    """
    token = schema.TextLine(
        title=_(u'label_token', default=u'Token'),
        description=_(u'help_token',
                      default=u"oAuth2 Token"),
        required=False,
        )


class UserDataSchemaProvider(object):
    implements(IUserDataSchemaProvider)

    def getSchema(self):
        """
        """
        return IEnhancedUserDataSchema
