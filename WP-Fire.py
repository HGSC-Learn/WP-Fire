# code by HGSC
# Author: Team of HGSC <dev/>
# Date: 4/12/23

# imports
import requests
from bs4 import BeautifulSoup
import os
import sys
import re
import time

red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
magenta = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m"
bright_black = "\033[0;90m"
bright_red = "\033[0;91m"
bright_green = "\033[0;92m"
bright_yellow = "\033[0;93m"
bright_blue = "\033[0;94m"
bright_magenta = "\033[0;95m"
bright_cyan = "\033[0;96m"
bright_white = "\033[0;97m"

def ps(ban):
    for char in ban:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

if os.name == 'nt':
    os.system('cls')
elif os.name == 'posix':
    os.system('clear') 
else:
    pass

banner = f"""{bright_blue}
{bright_blue}  _      __  ___         {bright_red} ____  _            
{bright_blue} | | /| / / / _ \ {bright_cyan} ____  {bright_red}/ __/ (_) ____  ___ 
{bright_blue} | |/ |/ / / ___/ {bright_cyan}/___/ {bright_red}/ _/  / / / __/ / -_)
{bright_blue} |__/|__/ /_/          {bright_red}/_/   /_/ /_/    \__/ 
                                            {yellow} Author{bright_blue}: {green}Team of HGSC                                                                                                                                                                                                                                                                                      
"""
print(banner)


uses = f"""
{green}Uses {green}:------------------------------------:
     {green}:          {bright_white}-{white}h ---->for help          {green}:
     {green}:          {bright_blue}-u ---->for URL           {green}:
     {green}:  {bright_red}-v ---->for get WP site verssion  {green}:
     {green}:  {bright_yellow}-p ---->for get WP site plugin    {green}:
     {green}:  {bright_white}-t ---->for get WP site themes    {green}:
     {green}:  {bright_blue}-e ---->for get WP site extract V {green}:
     {green}:------------------------------------: 
"""


discription = f"""{bright_green}
WP-Fire is a simple WordPress Penetration testing tool by HGSC.
WP-Fire verssion V 0.1
"""

example = f"""
{bright_blue}Example : {bright_cyan}python {green}WP-Fire.py {bright_blue}-u {bright_yellow}https://HGSC.in {bright_magenta}-v{bright_green}
{bright_green}"""




if len(sys.argv) == 1:
    ps(discription)
    print(uses)
    ps(example)

if '-h' in sys.argv:
    print("""
   Uses :------------------------------------:
        :          -h ---->for help          :
        :          -u ---->for URL           :
        :  -v ---->for get WP site verssion  :
        :  -p ---->for get WP site plugin    :
        :  -t ---->for get WP site themes    :
        :  -e ---->for get WP site extract V :
        :------------------------------------: 
    """)


for i in range(1, len(sys.argv)):
    if sys.argv[i] == "-u" and i < len(sys.argv) - 1:
        url = sys.argv[i+1]
        if "http://" not in url and "https://" not in url:
            print('use http:// like a (python W* -u http://HGSC.in -v)')
            break
        else:
            if '-v' in sys.argv:
                #get verssion
                getVerssion = url
                getVerssion = requests.get(getVerssion)
                if getVerssion.status_code ==200:
                    html = getVerssion.text
                    fd = BeautifulSoup(html, "html.parser")
                    tags = fd.find("meta", {"name": "generator"})
                    if tags and tags["content"].startswith("WordPress"):
                        version = tags["content"].split(" ")[1]
                        print("WordPress version:", version)
                        break
                    else:
                        ps("WordPress Version not found on this website.")
                        break
                    
            #get plugin
            if '-p' in sys.argv:
                getPlugin = url
                getPlugin = requests.get(getPlugin)
                if getPlugin.status_code == 200:
                    html_content = getPlugin.text
                    plug = r'wp-content/plugins/.*?[\'"]'
                    plugin = re.findall(plug, html_content)
                    for match in plugin:
                        print(match.strip("'"))
                else:
                    ps("WordPress Plugin get problem!!")
                
            #get themes
            if '-t' in sys.argv:
                getThemes = url
                getThemes = requests.get(getThemes)
                if getThemes.status_code ==200:
                    html_content = getThemes.text
                    playdThim = r'wp-content/themes/.*?[\'"]'
                    theme = re.findall(playdThim, html_content)
                    for match in theme:
                        print(match.strip("'"))
                else:
                    ps("WordPress Themes get problem!!")
            #get extra versions
            if '-e' in sys.argv:
                getExtra = url
                getExtra = requests.get(getExtra)
                if getExtra.status_code == 200:
                    html_content = getExtra.text
                    exta = r'http.*?ver=.*?[\'"]'
                    extra = re.findall(exta, html_content)
                    for match in extra:
                        print(match.strip("'"))
                else:
                    ps("WordPress extract versions in general get problem!!")

