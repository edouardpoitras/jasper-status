"""
The following methods can be used in any Jasper plugin to modify the status
module's response to the user.

Simply copy-and-paste the example in your plugin class and change the response
as necessary.
"""

def StatusPlugin_modify_response(self, response):
    """
    In future versions of this plugin, the response parameter will be a dict
    where you can store status messages in different categories.  For example,
    system status messages, jasper status messages, plugin status messages,
    voice/speaker status messages, network status messages,
    misc status messages, etc.

    Until this logic has been implemented and the user can choose which type
    of status to hear, response is simply a list of strings that will be
    spoken in it's entirety everytime the user requests the status.
    """
    response.append('My plugin\'s custom status message here')
    response.append('The stock trader plugin claims you have 3 active trades')
    response.append('The family GPS plugin says your wife is on her way home')
