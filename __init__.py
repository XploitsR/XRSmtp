#!/usr/bin/env python3
# -*- coding: utf-8 -*-
##################################################################################
# MIT License                                                                    #
# Copyright (c) 2019 XploitsR                                                    #
#                                                                                #
# Permission is hereby granted, free of charge, to any person obtaining a copy   #
# of this software and associated documentation files (the "Software"), to deal  #
# in the Software without restriction, including without limitation the rights   #
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell      #
# copies of the Software, and to permit persons to whom the Software is          #
# furnished to do so, subject to the following conditions:                       #
#                                                                                #
# The above copyright notice and this permission notice shall be included in all #
# copies or substantial portions of the Software.                                #
#                                                                                #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR     #
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,       #
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE    #
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER         #
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,  #
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE  #
# SOFTWARE.                                                          #############
#                                                                    #
# Coded by Solomon Narh (::XploitsR Author::)                        #
# Github: https://github.com/XploitsR/XRSmtp                         #
# Facebook: https://facebook.com/RXploits                            #
# Twitter: https://twitter.com/RXploits                              #
# Telegram: https://t.me/RXploits                                    #
# Website: https://xploitsr.tk                                       #
#                                                                    #
#             ::PERSONAL ME::                                        #
# Github: https://github.com/Solomon97062                            #
# Facebook: https://facebook.com/solomon.narh.311                    #
# Twitter: https://twitter.com/Solomon97062                          #
# Instagram: @_xploitsr_author_1                                     #
# Email: solomonnarh97062@gmail.com                                  #
######################################################################

# =begin == 
"""""""""""""""""""""""""""""""""""""""""
XRSmtp is a module to auto fetch any smtp 
server details by just knowing the smtp 
providers name.
"""""""""""""""""""""""""""""""""""""""""
# XRSwitch
def XRSwitch(provider):
    ext = provider.lower()
    comb = {
        "gmail" : "smtp.gmail.com",
        "yahoo" : "smtp.mail.yahoo.com",
        "outlook" : "smtp-mail.outlook.com",
        "hotmail" : "smtp.live.com",
        "office365" : "smtp.office365.com",
        "aim" : "smtp.aim.com",
        "aol" : "smtp.aol.com",
        "yandex" : "smtp.yandex.com",
        "icloud" : "smtp.mail.me.com",
        "zoho" : "smtp.zoho.com",
        "godaddy" : "smtpout.secureserver.net",
        "yahoo plus" :"plus.smtp.mail.yahoo.com",
        "mail" : "smtp.mail.com",
        "hushmail" : "smtp.hushmail.com",
        "gmx" : "smtp.gmx.com",
        "verizon" : "smtp.verizon.net",
        "at&t" : "smtp.mail.att.net",
        "airmail" : "smtp.airmail.net",
        "lycos" : "smtp.mail.lycos.com",
        "rediff" : "smtp.rediffmail.com",
        "rediff pro" : "smtp.rediffmailpro.com",
    }
    return comb.get(ext, "[!] SMTP provider not found")
class XRSmtp:
  # ssl port
  def smtp_portSSL(self,provider):
      arr = ["lycos","rediff"]
      port =  465
      try:
        if str(provider) is not None and len(str(provider)) > 0 and type(provider) == str:
           if XRSwitch(provider) == "[!] SMTP provider not found":
              print("[!] XRSmtpError: SMTP provider not found or not included.")
              quit()
           if str(provider.lower()) in arr:
              server,port = XRSwitch(provider),25
           else:
              server,port = XRSwitch(provider),port
        else:
           print("[!] Don't be silly, string expected... str()")
           quit()
      except:
        raise
        quit()
      return [server,port]
  # tls port
  def smtp_portTLS(self,provider):
      arr = ["lycos","rediff"]
      port =  587
      try:
        if str(provider) is not None and len(str(provider)) > 0 and type(provider) == str:
           if XRSwitch(provider) == "[!] SMTP provider not found":
              print("[!] XRSmtpError: SMTP provider not found or not included.")
              quit()
           if str(provider.lower()) in arr:
              server,port = XRSwitch(provider),25
           else:
              server,port = XRSwitch(provider),port
        else:
           print("[!] Don't be silly, string expected... str()")
           quit()
      except:
        raise
        quit()
      return [server,port]
  # list all smtp provider names
  def smtp_listAll(self):
      smtp_servers = []
      smtp_servers.append("Gmail")
      smtp_servers.append("Yahoo")
      smtp_servers.append("Yahoo Plus")
      smtp_servers.append("Hotmail")
      smtp_servers.append("Outlook")
      smtp_servers.append("Office365")
      smtp_servers.append("Yandex")
      smtp_servers.append("AIM")
      smtp_servers.append("AOL")
      smtp_servers.append("iCloud")
      smtp_servers.append("ZOHO")
      smtp_servers.append("GoDaddy")
      smtp_servers.append("Mail")
      smtp_servers.append("GMX")
      smtp_servers.append("Verizon")
      smtp_servers.append("AT&T")
      smtp_servers.append("Airmail")
      smtp_servers.append("Lycos")
      smtp_servers.append("Rediff")
      smtp_servers.append("Rediff Pro")
      return smtp_servers
