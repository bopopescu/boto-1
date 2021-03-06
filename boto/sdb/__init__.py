# Copyright (c) 2006-2009 Mitch Garnaat http://garnaat.org/
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#

from regioninfo import SDBRegionInfo


def regions():
    """
    Get all available regions for the SDB service.
        
    :rtype: list
    :return: A list of :class:`boto.sdb.regioninfo.RegionInfo`
    """
    return [SDBRegionInfo(name='us-east-1', endpoint='sdb.amazonaws.com'),
            SDBRegionInfo(name='eu-west-1', endpoint='sdb.eu-west-1.amazonaws.com'),
            SDBRegionInfo(name='us-west-1', endpoint='sdb.us-west-1.amazonaws.com')]

def connect_to_region(region_name):
    for region in regions():
        if region.name == region_name:
            return region.connect()
    return None
