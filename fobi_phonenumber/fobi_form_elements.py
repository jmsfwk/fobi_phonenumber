__title__ = 'fobi_phonenumber.fobi_form_elements'
__author__ = 'James Fenwick <jfenwick@tecaz.com'
__copyright__ = 'Copyright (c) 2016 Tecaz Ltd'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('PhoneNumberPlugin',)

from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.utils.translation import ugettext_lazy as _

from fobi.base import FormFieldPlugin, form_element_plugin_registry, get_theme

from . import UID
from .forms import PhoneNumberForm

theme = get_theme(request=None, as_instance=True)

class PhoneNumberPlugin(FormFieldPlugin):
    """
    PhoneNumber field plugin.
    """
    name = _("PhoneNumber")
    group = _("Fields")
    form = PhoneNumberForm
    uid = UID

    def get_form_field_instances(self, request=None):
        """
        Get form field instances.
        """
        widget_attrs = {
            'class': theme.form_element_html_class,
            'placeholder': self.data.placeholder,
        }

        kwargs = {
            'label': self.data.label,
            'help_text': self.data.help_text,
            'initial': self.data.initial,
            'required': self.data.required,
            'widget': PhoneNumberPrefixWidget(attrs=widget_attrs),
        }
        if self.data.max_length:
            kwargs['max_length'] = self.data.max_length

        return [(self.data.name, PhoneNumberField, kwargs)]


form_element_plugin_registry.register(PhoneNumberPlugin)
