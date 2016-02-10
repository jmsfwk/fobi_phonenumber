===============================================
fobi_phonenumber
===============================================
A ``Fobi`` PhoneNumber form field plugin. Makes use of the
``phonenumber_field.formfields.PhoneNumberField`` and
``phonenumber_field.widgets.PhoneNumberPrefixWidget``.

Installation
===============================================
1. Add ``fobi.contrib.plugins.form_elements.fields.text`` to the
   ``INSTALLED_APPS`` in your ``settings.py``.

.. code-block:: python

    INSTALLED_APPS = (
        # ...
        'fobi_phonenumber',
        # ...
    )

2. In the terminal type:

.. code-block:: none

    $ ./manage.py fobi_sync_plugins

3. Assign appropriate permissions to the target users/groups to be using
   the plugin if ``FOBI_RESTRICT_PLUGIN_ACCESS`` is set to True.
