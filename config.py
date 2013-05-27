import xmlrpclib
import mainWindow

serverName=""
userName=""
passWord=""
client=""
key=""

def connectServer():
    print 'Connecting RHNSatellite Server'
    # Global Vars
    global serverName
    global userName
    global passWord
    global client
    global key
    global list
    
#    serverName = raw_input('Informe the RHNSatellite Server, like http://server/rpc/api: ')
#    userName = raw_input('Inform the user name: ')
#    passWord = raw_input('Inform the password: ')
    
    # Satellite / Spacewalk Variables
    SATELLITE_URL = "http://10.1.1.254/rpc/api"     # The IP address of your RHN Satellite or Spacewalk
    SATELLITE_LOGIN = "admin"                       # The admin account
    SATELLITE_PASSWD = "redhat"                     # The password of admin account
    serverName="http://10.1.1.254/rpc/api"
    userName="admin"
    passWord="redhat"
#    SATELLITE_URL = serverName                      # The IP address of your RHN Satellite or Spacewalk
#    SATELLITE_LOGIN = userName                      # The admin account
#    SATELLITE_PASSWD = passWord                     # The password of admin account
    
    # Conf to generate a Satellite List
    client = xmlrpclib.Server(SATELLITE_URL, verbose=0)
    key = client.auth.login(SATELLITE_LOGIN, SATELLITE_PASSWD)
    list = client.user.list_users(key)
    

"""    
    print 'INICIO VALORES CONFIG'
    print serverName
    print userName
    print passWord
    print client
    print key
    print 'FIM VALORES CONFIG'
""" 