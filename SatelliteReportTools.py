# 
# Date ........: 05/22/2013
# Developer ...: Waldirio M. Pinheiro <waldirio.pinheiro@iesbrazil.com.br>
# Purpose .....: Cod to collect information from RHNSatellite / Spacewalk, generating 
#                a custom report.
# Changelog ...: 
# 
# 
import os
import config
import mainWindow
from macpath import split
#from config import *

# Global Vars
nameFileOut=""
nameFileIn=""



def openWindow():
    w = mainWindow.SatReport()
    mainWindow.gtk.main()

openWindow()