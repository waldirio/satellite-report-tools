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

class SatReport:

    def __init__(self):

        # Window definition
        self.gladefile = "glade/main.glade"
        self.xmlMain = gtk.glade.XML(self.gladefile)

#    self.gladelogin = "glade/login.glade"
#    self.xmlLogin = gtk.glade.XML(self.gladelogin)
    
        self.gladeListFileRhsaCve = "glade/chooseListFileRhsaCve.glade"
        self.xmlChooseListFileRhsaCve = gtk.glade.XML(self.gladeListFileRhsaCve)
        
#        self.xmlChooseListFileRhsaCveWindow = self.xmlChooseListFileRhsaCve.get_widget('filechooserdialog1')

        dic = { "on_btnListFileRhsaCve_clicked" : self.btnListFileRhsaCve_clicked,
                "on_MainWindow_destroy" : gtk.main_quit }
    
        self.xmlMain.signal_autoconnect(dic)
    
    
    def btnListFileRhsaCve_clicked(self, widget):
        print "hello mundo"
 #       self.xmlChooseListFileRhsaCveWindow.show()
        
    # Button definition
    # self.btnLogin = self.xml.get_widget('btnLogin')
    # self.LabelTitle = self.xml.get_widget('LabelTitle')

    # self.btnListFileRhsaCve = self.xml.get_widget('btnListFileRhsaCve')

    # self.Login = self.xmlLogin.get_widget('login')
    # self.WinChooseListFileRhsaCve = self.xmlChooseListFileRhsaCve.get_widget('winChooseListFileRhsaCve')

    #    self.btnLogin.connect('clicked', self.on_btnLogin_clicked)
    # self.btnLogin.connect('clicked', self.on_btnLocal_clicked)
    # self.btnListFileRhsaCve.connect('clicked', self.on_btnListFileRhsaCve_clicked)


  # def on_btnListFileRhsaCve_clicked(self, widget):
  #  self.xmlChooseListFileRhsaCve.show()

  # def on_btnLocal_clicked(self, widget):
#    self.LabelTitle.set_text('xxxxx')
  #  self.Login.show()


#    self.mainWindow = self.wTree.get_widget('Principal')
#    self.mainWindow.set_title("teste")

#    self.mainWindow.connect('destroy', gtk.main_quit)


if __name__ == "__main__":
    w = SatReport()
    gtk.main()

