from ovos_plugin_manager.templates.gui import GUIExtension
from ovos_utils.log import LOG


class PlasmoidExtension(GUIExtension):
    """ Plasmoid Platform Extension: This extension is responsible for managing the generic GUI behaviours
    for non specific platforms. The generic extension does optionally support Homescreen and Homescreen
    Management but it needs to be exclusively enabled in the configuration file.

    Args:
        bus: MessageBus instance
        gui: GUI instance
        preload_gui (bool): load GUI skills even if gui client not connected
        permanent (bool): disable unloading of GUI skills on gui client disconnections
    """

    def __init__(self, config, bus=None, gui=None,
                 preload_gui=False, permanent=True):
        # only thing this is really doing is changing default value of "permanent" flag
        LOG.info("Plasmoid: Initializing")
        super().__init__(bus, gui, config, preload_gui, permanent)
