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
from macpath import split

# Global Vars
global list
nameFileOut=""
nameFileIn=""

def defineInPutFile():
    global nameFileIn
    nameFileIn = raw_input('Inform the list file name with cve/rhsa: ')
    

def defineOutPutFile():
    global nameFileOut
    nameFileOut = raw_input('inform the output file name: ')
    fileRef = open(nameFileOut,'w')
    fileRef.write('NODE;CVE;RHSA\n')
    fileRef.close()

def dumpOutFile(params_nodes):
    fileRef = open(nameFileOut,'a')
    fileRef.write(params_nodes)
    fileRef.close()

def findSystemCve(cveCode):
    ErrataFindCve = config.client.errata.findByCve(config.key,cveCode)
    AdvCode=ErrataFindCve[0].get('advisory_name')
    
    for b in [AdvCode]:
        ErrataAffectedSystems = config.client.errata.listAffectedSystems(config.key,b)
       
        for x in range(len(ErrataAffectedSystems)):
            dumpOutFile(ErrataAffectedSystems[x].get('system_name') + ";" + cveCode + ";" + "-" + ";" +"\n")
        

def findSystemAdv(advCode):
    ErrataFindAdv = config.client.errata.listAffectedSystems(config.key,advCode)
    for x in range(len(ErrataFindAdv)):
        dumpOutFile(ErrataFindAdv[x].get('system_name') + ";" + "-" + ";" + advCode + ";" + "\n")
    
def listCveRhsa():
    fileRef=open(nameFileIn, 'r')
    
    for b in fileRef:
    	typeAdv=b[0:3]
    	if typeAdv == 'RHS':
#            print 'Security Advisory - ' + b
            # Add .rstrip to remove '\n' char
            findSystemAdv(b.rstrip())
    	elif typeAdv == 'CVE':
#            print 'CVEs - ' + b
            findSystemCve(b)
        else:
            print 'discarding ...., comments or blank line'

def listUsers():
    for user in config.list:
        print user.get('login')

def menu():
    while True:
#        os.system('cls')
        print '##################################'
        print '# 0. List users from RHNSatellite'
        print '# 1. Define the output file name'
        print '# 2. Define the CVEs/RHSA file name'
        print '# 3. Check CVE/RHSA from file'
        print '#'
        print '# 9. Exit'
        print '##################################'
        opc = raw_input('Option: ')


        if opc == '0':
            listUsers()
        elif opc == '1':
            defineOutPutFile()
        elif opc == '2':
            defineInPutFile()
        elif opc == '3':
            listCveRhsa()
        elif opc == '9':
            print 'Sair ...'
            exit()
        else:
            print 'opcao invalida'
            
            
# Main Menu from Apps            
menu()