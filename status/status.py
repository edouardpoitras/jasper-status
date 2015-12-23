# -*- coding: utf-8-*-
import re
import psutil
import platform
import datetime
from client import plugin

class StatusPlugin(plugin.SpeechHandlerPlugin):
    def get_phrases(self):
        return ["STATUS"]

    def is_valid(self, text):
        """
            Returns True if the text is related to Jasper's status.

            Arguments:
            text -- user-input, typically transcribed speech
        """
        return bool(re.search(r'\b(status)\b', text, re.IGNORECASE))

    def handle(self, text, mic):
        os, name, version, _, _, _ = platform.uname()
        version = version.split('-')[0]
        cores = psutil.cpu_count()
        cpu_percent = psutil.cpu_percent()
        memory_percent = psutil.virtual_memory()[2]
        disk_percent = psutil.disk_usage('/')[3]
        boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
        running_since = boot_time.strftime("%A %d. %B %Y")
        response = []
        response.append("I am currently running on %s version %s.  " %
                        (os, version))
        response.append("This system is named %s and has %s CPU cores.  " %
                        (name, cores))
        response.append("Current CPU utilization is %s percent.  " %
                        cpu_percent)
        response.append("Current memory utilization is %s percent." %
                        memory_percent)
        self.invoke_all('StatusPlugin_modify_response', response)
        mic.say('\n'.join(response))
