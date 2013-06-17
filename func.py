import sys
import config
from macpath import split

nameFileOut=""
nameFileIn=""



def defineOutPutFile(nameFileOutTemp):
    global nameFileOut
    nameFileOut = nameFileOutTemp
    print 'Output file ' + nameFileOut
    fileRef = open(nameFileOut,'w')
    fileRef.write('NODE;CVE;RHSA\n')
    fileRef.close()

def dumpOutFile(params_nodes):
    fileRef = open(nameFileOut,'a')
    fileRef.write(params_nodes)
    fileRef.close()

def defineInPutFile(nameFileInTemp):
    global nameFileIn
    nameFileIn = nameFileInTemp
    print 'List File ' + nameFileIn

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
    
    print 'Finished'