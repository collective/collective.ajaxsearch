from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile

from zope.configuration import xmlconfig

class CollectiveAjaxsearch(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import collective.ajaxsearch
        xmlconfig.file('configure.zcml',
                       collective.ajaxsearch,
                       context=configurationContext)


    def setUpPloneSite(self, portal):
        pass

COLLECTIVE_AJAXSEARCH_FIXTURE = CollectiveAjaxsearch()
COLLECTIVE_AJAXSEARCH_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(COLLECTIVE_AJAXSEARCH_FIXTURE, ),
                       name="CollectiveAjaxsearch:Integration")