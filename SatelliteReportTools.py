# 
# Date ........: 05/22/2013
# Developer ...: Waldirio M. Pinheiro <waldirio.pinheiro@iesbrazil.com.br>
# Purpose .....: Cod to collect information from RHNSatellite / Spacewalk, generating 
#                a custom report.
# Changelog ...: 
# 
# 

import mainWindow


def openWindow():
    w = mainWindow.SatReport()
    mainWindow.gtk.main()

openWindow()