# -*- coding: utf-8 -*-
from plone.theme.interfaces import IDefaultPloneLayer
from z3c.form import interfaces
from zope import schema
from zope.interface import Interface
from plone.registry.field import PersistentField
from collective.ajaxsearch import ajaxsearchMessageFactory as _

class IThemeSpecific(IDefaultPloneLayer):
    """
    interface for search viewlet
    """


class PersistentObject(PersistentField, schema.Object):
    """
    create a persistent object
    """
    pass


class IAjaxsearchGroup(Interface):
    """
    interface for group of types
    """
    group_name = schema.TextLine(title=_(u"Group Name"),
                                 description=_(u"Name for the group"),
                                 required=True,
                                 default=u'',)

    group_types = schema.List(title=_(u"Portal Types"),
                              description=_(u"Portal Types to search in this group"),
                              value_type=schema.Choice(
                              title=_(u"Portal Types"),
                              vocabulary=u"plone.app.vocabularies.ReallyUserFriendlyTypes",
                              required=False,
                              ),
                              required=True,)


class IAjaxsearchSettings(Interface):
    """
    interface for settings
    """
    group_info = schema.Tuple(title=_(u"Group Info"),
                              description=_(u"Informations of the group"),
                              value_type=PersistentObject(
                              IAjaxsearchGroup, required=False),
                              required=False,)
