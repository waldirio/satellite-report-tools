import xmlrpclib
import mainWindow

client=""
key=""

def connectServer(user, password):
    print 'Connecting RHNSatellite Server'
    # Global Vars
    global client
    global key
    global list
    
    
    # Satellite / Spacewalk Variables
    SATELLITE_URL = "http://10.1.1.254/rpc/api"      # The IP address of your RHN Satellite or Spacewalk
    SATELLITE_LOGIN = user                           # The admin account
    SATELLITE_PASSWD = password                      # The password of admin account

    
    # Conf to generate a Satellite List
    client = xmlrpclib.Server(SATELLITE_URL, verbose=0)
    key = client.auth.login(SATELLITE_LOGIN, SATELLITE_PASSWD)
    list = client.user.list_users(key)