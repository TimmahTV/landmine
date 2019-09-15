#---------------------------------------
# Libraries and references
#---------------------------------------
import codecs
import json
import os
import re
#---------------------------------------
# [Required] Script information
#---------------------------------------
ScriptName = "boilerplate" #Change this
Website = "https://www.twitch.tv/Timmah_TV"
Creator = "Timmah_TV"
Version = "1.0.0"
Description = "description" #Change this
#---------------------------------------
# Versions
#---------------------------------------
"""
1.0.0 - Initial Release
"""
#---------------------------------------
# Variables
#---------------------------------------
settingsFile = os.path.join(os.path.dirname(__file__), "settings.json")
#---------------------------------------
# Classes
#---------------------------------------
class Settings:
    """" Loads settings from file if file is found if not uses default values"""

    # The 'default' variable names need to match UI_Config
    def __init__(self, settingsFile=None):
        if settingsFile and os.path.isfile(settingsFile):
            with codecs.open(settingsFile, encoding='utf-8-sig', mode='r') as f:
                self.__dict__ = json.load(f, encoding='utf-8-sig')

        else: #set variables if no custom settings file is found
            self.Command = "command" #Change this
            self.ResponseMessage = "Response Message" #Change this
            self.ErrorMessage = "Error Message" #Change this

    # Reload settings on save through UI
    def ReloadSettings(self, data):
        """Reload settings on save through UI"""
        self.__dict__ = json.loads(data, encoding='utf-8-sig')
        return

    # Save settings to files (json and js)
    def SaveSettings(self, settingsFile):
        """Save settings to files (json and js)"""
        with codecs.open(settingsFile, encoding='utf-8-sig', mode='w+') as f:
            json.dump(self.__dict__, f, encoding='utf-8-sig')
        with codecs.open(settingsFile.replace("json", "js"), encoding='utf-8-sig', mode='w+') as f:
            f.write("var settings = {0};".format(json.dumps(self.__dict__, encoding='utf-8-sig')))
        return

#---------------------------------------
# Settings functions
#---------------------------------------
def ReloadSettings(jsondata):
    """Reload settings on Save"""
    # Reload saved settings
    MySettings.ReloadSettings(jsondata)
    # End of ReloadSettings

def SaveSettings(self, settingsFile):
    """Save settings to files (json and js)"""
    with codecs.open(settingsFile, encoding='utf-8-sig', mode='w+') as f:
        json.dump(self.__dict__, f, encoding='utf-8-sig')
    with codecs.open(settingsFile.replace("json", "js"), encoding='utf-8-sig', mode='w+') as f:
        f.write("var settings = {0};".format(json.dumps(self.__dict__, encoding='utf-8-sig')))
    return

#---------------------------------------
# [Required] functions
#---------------------------------------
def Init():
    global MySettings
    # Load in saved settings
    MySettings = Settings(settingsFile)
    # Command #Change this
    global Command #Change this
    Command = MySettings.Command.lower() #Change this
    return


def Execute(data):
    if data.IsChatMessage():
        sendMessage = Parent.SendTwitchMessage if data.IsFromTwitch() else Parent.SendDiscordMessage
        if data.GetParam(0).lower() == Command: #Change this
            # Where we process the command
    return


def Tick():
    """Required tick function"""
    return
