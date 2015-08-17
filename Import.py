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
        another script to call the importer via ``Import. AAA``.
        """
        print("importing:", mod_name)
        e = None
        try:
            __import__(mod_name)
            sys.modules[mod_name] =
            print("Imported", mod_name, "successfully")
        except ImportError as E:
            e = E
        except Exception as E:
            e = E
            log.debug("Error importing '%s': %s" % (mod_name, E))
        else:
            return

        print('error', e)



sys.modules[__name__] = Importer()
