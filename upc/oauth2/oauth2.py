from Products.CMFCore.utils import getToolByName
from pas.plugins.preauth.interfaces import IPreauthTask, IPreauthHelper
from zope.interface import implements
from zope.component import adapts

import requests
import json


class oauthTokenRetriever(object):
    implements(IPreauthTask)
    adapts(IPreauthHelper)

    def __init__(self, context):
        self.context = context

    def execute(self, credentials):
        user = credentials.get('login')
        password = credentials.get('password')

        if user == "admin":
            return

        payload = {"grant_type": "password",
                   "client_id": "MAX",
                   "scope": "widgetcli",
                   "username": user,
                   "password": password
                   }

        r = requests.post('https://oauth.upc.edu/token', data=payload, verify=False)
        response = json.loads(r.text)
        oauth_token = response.get("oauth_token")

        pm = getToolByName(self.context, "portal_membership")
        member = pm.getMemberById(user)
        member.setMemberProperties({'oauth_token': oauth_token})
