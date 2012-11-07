from zope import component
from Products.Five import BrowserView


class Example(BrowserView):
    """example"""
    def get_path(self):
        """taken from http://developer.plone.org/serving/traversing.html"""
        portal_state = component.getMultiAdapter((self.context, self.request),
                                                 name=u'plone_portal_state')
        site = portal_state.portal()

        # Both of these are tuples
        site_path = site.getPhysicalPath();
        context_path = self.context.getPhysicalPath()

        relative_path = context_path[len(site_path):]

        return "/" + "/".join(relative_path)
