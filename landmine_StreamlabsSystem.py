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
ScriptName = "Land Mine" #Change this
Website = "https://www.twitch.tv/Timmah_TV"
Creator = "Timmah_TV"
Version = "1.0.1"
Description = "Chat whispers a message to the bot to lay a trap for the next chat member" #Change this
#---------------------------------------
# Versions
#---------------------------------------
"""
1.0.0 - Initial Release
1.0.1 - Figure out why broke
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
            self.Command = "!landmine" #Change this
            self.ResponseMessage = "Response Message" #Change this
            self.ErrorMessage = "Error Message" #Change this
            self.LandMine = ""

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

        # Check for whisper
        if data.IsWhisper():

            # Check to see if command was stated and the landmine value is blank
            if data.GetParam(0).lower() == Command and MySettings.LandMine == "":

                # set the landmine value to the message minus spaces and the command
                MySettings.LandMine = data.Message.replace(" ","").replace(Command, "").lower() # Set the landmine's value
                MySettings.LandMineMaker = data.UserName # The one who set the landmine

        else:

            # Check to see if landmine value is not blank
            if MySettings.LandMine != "":

                # see if regex of the landmine value matches anything in the message said
                if(re.search(MySettings.LandMine.lower(), data.Message.replace(" ",""))):
                    # Determine if twitch message or discord message
                    SendMessage = Parent.SendTwitchMessage if data.IsFromTwitch() else Parent.SendDiscordMessage
                    SendMessage("/timeout " + data.UserName + " 1")
                    SendMessage(replaceMessageWithInfo(MySettings.LandMine, MySettings.LandMineMaker, data.UserName))

                    # Set landmine back to blank
                    MySettings.LandMine = ""
                    MySettings.LandMineMaker = ""
    return


def Tick():
    """Required tick function"""
    return


def replaceMessageWithInfo(landmineMessage, landmineMaker, landmineVictim):

    # XXX = landmineMessage, YYY = landmineMaker, ZZZ = landmineVictim
    phrases = [
        "The phrase was XXX. ZZZ got got by YYY. 02Dab",
        "lol. YYY did it to ZZZ with XXX. get rekt my dude 02Dab",
        "Wow. Can't believe you said XXX in your message ZZZ. Didn't you know that YYY made that the landmine? Loser lmao.",
        "BRUH! CAN'T BELIEVE YOU SAID XXX IN YOUR MESSAGE ZZZ BRUH. bruh didn't you know? YYY set this up. bruh..."
    ]

    result = Parent.GetRandom(0,len(phrases))

    return phrases[result].replace('XXX', landmineMessage).replace('YYY', landmineMaker).replace('ZZZ', landmineVictim)
