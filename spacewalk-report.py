
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

# Global Vars
global list

def findSystemCve(cveCode):
    print cveCode

def findSystemAdv(advCode):
    print advCode
    
def listCveRhsa():
    file=open('list.txt', 'r')
    
    for b in file:
    	typeAdv=b[0:3]
    	if typeAdv == 'RHS':
            print 'Security Advisory - ' + b
            findSystemAdv(b)
    	elif typeAdv == 'CVE':
            print 'CVEs - ' + b
            findSystemCve(b)

def listUsers():
    for user in config.list:
        print user.get('login')

def menu():
    while True:
        os.system('cls')
        print '##################################'
        print '# 0. List users from RHNSatellite'
        print '# 1. Check CVE/RHSA from file'
        print '#'
        print '# 9. Exit'
        print '##################################'
        opc = raw_input('Option: ')


        if opc == '0':
            listUsers()
        elif opc == '1':
            listCveRhsa()
        elif opc == '9':
            print 'Sair ...'
            exit()
        else:
            print 'opcao invalida'
            
            
# Main Menu from Apps            
menu()