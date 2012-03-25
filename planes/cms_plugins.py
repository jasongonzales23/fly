from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from planes.models import Fleet, Plane
from planes.models import FleetPlugin as FleetPluginModel
from django.utils.translation import ugettext as _

import admin

class FleetPlugin(CMSPluginBase):
    model = FleetPluginModel
    name = _("Fleet")
    render_template = "fleet.html"
    
    def render(self, context, instance, placeholder):
        context.update({
            'fleet':instance.fleet,
            'object':instance,
            'placeholder':placeholder
        })
        return context
    
plugin_pool.register_plugin(FleetPlugin)