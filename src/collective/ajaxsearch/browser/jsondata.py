# -*- coding: utf-8 -*-
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.memoize.instance import memoize
from Products.CMFCore.utils import getToolByName
from zope.component import getUtility, queryUtility
from collective.ajaxsearch.interfaces.interfaces import IAjaxsearchSettings
from plone.registry.interfaces import IRegistry
import json

types = {}

class AjaxSearchView(BrowserView):
    """
    class to create json search result
    """
    template = ViewPageTemplateFile('templates/searchresult.pt')

    @memoize
    def __call__(self):
        """
        """
        # get groups config
        registry = queryUtility(IRegistry)
        settings = registry.forInterface(IAjaxsearchSettings, check=False)

        for config in settings.group_info:
            types[config.group_name] = config.group_types

        # remove livesearch product
        livesearch = getToolByName(self.context, 'portal_javascripts')
        livesearch.getResource('livesearch.js').setEnabled(False)
        livesearch.cookResources()

        output = {}
        query = self.request['query']

        # do request for de query in the catalog
        ct = self.context.portal_catalog
        rs = ct.searchResults(SearchableText=query,
                              portal_type=sum([types[k] for k in types], []))

        # create output object
        for current_type in types:
            output[current_type] = [{'url': brain.getPath(), 'titulo': brain.Title}
                                    for brain in rs if brain.Type in types[current_type]]

        # return json
        return json.dumps(output)
