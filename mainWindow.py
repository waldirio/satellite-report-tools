import sys
import xmlrpclib
try:
    import pygtk
    pygtk.require("2.0")
except:
    pass
try:
    import gtk
    import gtk.glade
except:
    sys.exit(1)

import func
import config


class SatReport:

    def __init__(self):

        # Window definition
        self.gladefile = "glade/satellite-report-tools.glade"
        self.xml = gtk.glade.XML(self.gladefile)


        dic = { "on_btnLogin_clicked" :                 self.btnLogin_clicked,
                "on_btnListFileRhsaCve_clicked":        self.btnListFileRhsaCve_clicked,
                "on_btnOutPutFileRhsaCve_clicked":      self.btnOutPutFileRhsaCve_clicked,
                "on_btnRunRhsaCve_clicked":             self.btnRunRhsaCve_clicked,
                "on_btnSendLogin_clicked":              self.btnSendLogin_clicked,
                "on_btnCleanLogin_clicked":             self.btnCleanLogin_clicked,
                "on_btnCloseLogin_clicked":             self.btnCloseLogin_clicked,
                "on_btnAbout_clicked":                  self.btnAbout_clicked,
                "on_btnCloseAbout_clicked":             self.btnCloseAbout_clicked,
                "on_Main_destroy" :                     self.main_quit,
                }
    
        self.xml.signal_autoconnect(dic)
        

    def btnCloseAbout_clicked(self, widget):
        self.xml.get_widget('about').hide()
        
    
    def btnAbout_clicked(self, widget):
        self.xml.get_widget('about').show()
    
    def btnLogin_clicked(self, widget):
        self.xml.get_widget('login').show()
        #config.connectServer()
        print "Login"
        
    def btnListFileRhsaCve_clicked(self, widget):
        dialog = gtk.FileChooserDialog('Choose the File list with RHSA and CVEs codes',
                                       None,
                                       gtk.FILE_CHOOSER_ACTION_OPEN,
                                       (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                                        gtk.STOCK_OPEN, gtk.RESPONSE_OK))
        dialog.set_default_response(gtk.RESPONSE_OK)
        response = dialog.run()
        
        if response == gtk.RESPONSE_OK:
            func.defineInPutFile(dialog.get_filename())
            #print pathFile
            #func.defineOutPutFile(pathFile)
        elif response == gtk.RESPONSE_CANCEL:
            print 'closed, no files selected'
        dialog.destroy()

        print 'ListFile RHSA CVE'
        
    def btnOutPutFileRhsaCve_clicked(self, widget):
        dialog = gtk.FileChooserDialog('Choose the File list with RHSA and CVEs codes',
                                       None,
                                       gtk.FILE_CHOOSER_ACTION_SAVE,
                                       (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                                        gtk.STOCK_SAVE, gtk.RESPONSE_OK))
        dialog.set_default_response(gtk.RESPONSE_OK)
        response = dialog.run()
        
        if response == gtk.RESPONSE_OK:
            pathFile = dialog.get_filename()
            print pathFile
            func.defineOutPutFile(pathFile) 
            print dialog.get_filename()
        elif response == gtk.RESPONSE_CANCEL:
            print 'closed, no files selected'
        dialog.destroy()

        print 'OutPut File RHSA CVE'
        
    def btnRunRhsaCve_clicked(self, widget):
        func.listCveRhsa()
        print 'Run RHSA CVE'
        
    def btnSendLogin_clicked(self, widget):
        config.connectServer(self.xml.get_widget('txUser').get_text(),self.xml.get_widget('txPass').get_text())
        if config.key != "":
            self.xml.get_widget('lbStatus').set_text('connected')
        print 'Send Login'
        
    def btnCloseLogin_clicked(self,widget):
        self.xml.get_widget('login').hide()
        
    def btnCleanLogin_clicked(self, widget):
        self.xml.get_widget('txUser').set_text('')
        self.xml.get_widget('txPass').set_text('')
        print 'Clean Login'

    def main_quit(self,widget):
        sys.exit()

if __name__ == "__main__":
    w = SatReport()
    gtk.main()

