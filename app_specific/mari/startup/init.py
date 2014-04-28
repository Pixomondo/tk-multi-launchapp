# Copyright (c) 2013 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

"""
Set up the Tank context and prepares the Tank Mari engine.
"""

import os
import mari


def log_warn(msg):
    print msg
    mari.utils.message(msg)
    return


def bootstrap_tank():

    try:
        import tank
    except Exception, e:
        msg = "Shotgun: Could not import sgtk! Disabling for now: %s" % e
        log_warn(msg)
        return

    if not "TANK_ENGINE" in os.environ:
        msg = "Shotgun: No Engine specified via environment! Disabling for now."
        log_warn(msg)
        return

    engine_name = os.environ.get("TANK_ENGINE")
    try:
        context = tank.context.deserialize(os.environ.get("TANK_CONTEXT"))
    except Exception, e:
        msg = "Shotgun: Could not create context! "
        msg += "Shotgun Pipeline Toolkit will be disabled. Details: %s" % e
        log_warn(msg)
        return

    try:
        engine = tank.platform.start_engine(engine_name, context.tank, context)
    except Exception, e:
        msg = "Shotgun: Could not start engine: %s" % e
        log_warn(msg)
        return

    # clean up temp env vars
    for var in ["TANK_ENGINE", "TANK_CONTEXT", "TANK_FILE_TO_OPEN"]:
        if var in os.environ:
            del os.environ[var]


bootstrap_tank()
