#
# Import.py
#
"""
Hijack the python import system.
"""

import sys
import ast
import logging

log = logging.getLogger('Import')
log.setLevel(logging.DEBUG)


class Importer:
    """
    Class whose instance will be used as the module.
    """

    def __getattr__(self, mod_name):
        """
        Allows access to an 'attribute' of the module. This really allows
        another script to call the importer via ``Import. XXX``.
        """

        log.debug("importing:", mod_name)
        e = None
        try:
            sys.modules[mod_name] = __import__(mod_name)
        except ImportError as E:
            e = E
        except Exception as E:
            e = E
        else:
            return

        log.info('error', e)


sys.modules[__name__] = Importer()
