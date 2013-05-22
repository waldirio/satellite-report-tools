
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

def findSystemCve(cveCode):
#    print cveCode
    
    ErrataFindCve = config.client.errata.findByCve(config.key,cveCode)
    
    AdvCode=ErrataFindCve[0].get('advisory_name')
    print AdvCode
    
    for b in [AdvCode]:
        ErrataAffectedSystems = config.client.errata.listAffectedSystems(config.key,b)
#        print ErrataAffectedSystems[0].get('system_name')
        print len(ErrataAffectedSystems)
        
        for x in range(len(ErrataAffectedSystems)):
            print ErrataAffectedSystems[x].get('system_name')
        
#$PreCommand errata.findByCve "%session%" $CodCve                                                      > $LOG
#AdvCode=$(grep advisory_name $LOG |awk -F"=>" '{print $2}'|sed -e "s/'//g"|sed -e "s/,//g"|sed -e "s/^ //g")

#for b in $AdvCode
#do
#  echo "CVE Cod. $b"
#  $PreCommand errata.listAffectedSystems "%session%" $b                                               > $LOG
#  grep system_name $LOG|awk -F"=>" '{print $2}'|sed -e "s/'//g"|sed -e "s/,//g"|sed -e "s/^ //g"      > $LOG1

#  while read line
#  do
#    echo "$line;$CodCve;$b;$(date +%d/%m/%Y)"                                >> $LOGDIR/$LOGNAMEFILE
#  done < $LOG1

#done
    
    
    

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
#        os.system('cls')
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