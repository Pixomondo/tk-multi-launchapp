import os
import sys


def main():

    # Fix for Cinema Bug (<15.0.3.7):
    # Python plugins are not being loaded when C4D_PLUGINS_DIR
    # has multiple paths. The path are not being splitted.
    # This is the proposed fix by the MAXON technical support.
    plugin_paths = os.environ.get('C4D_PLUGINS_DIR')
    if plugin_paths:
        plugin_path_list = plugin_paths.split(';')
        for plugin_path in plugin_path_list:
            sys.plugin_path.append(plugin_path)


if __name__ == '__main__':
    main()
