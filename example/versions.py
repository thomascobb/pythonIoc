'''Version definitions for softIOC.  This is normally the first module
imported, and should only be used to establish module versions.'''

from pkg_resources import require

require('cothread==2.0')
require('iocbuilder==3.18')
