# Copyright (c) 2015 Shotgun Software Inc.
# 
# CONFIDENTIAL AND PROPRIETARY
# 
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit 
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your 
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights 
# not expressly granted therein are reserved by Shotgun Software Inc.

"""
Populate Versions Hook

Called to modify or fill the versions list.
"""

import sgtk


class PopulateVersions(sgtk.Hook):
    """
    Hook to modify or fill the versions list.
    """

    def execute(self, versions, **kwargs):
        """
        The execute function of the hook will be called after the versions list
        was populated from the settings the first time.

        :param versions: (list) The initial versions populated by the settings.

        :returns: (list) Modified list.
        """

        # Modify or fill list here

        return versions
