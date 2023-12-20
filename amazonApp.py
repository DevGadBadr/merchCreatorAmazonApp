from PyQt5 import QtCore, QtGui, QtWidgets 
from appUI import Ui_amazonaccount
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QThread , pyqtSignal
from amazon_accounts_Module import MainCode
from selenium.common.exceptions import NoSuchWindowException,InvalidSessionIdException,WebDriverException,NoSuchElementException
from urllib3.exceptions import ProtocolError
import time
from PyQt5.QtCore import Qt
import datetime

class worker_1(QThread):
    
    finished = pyqtSignal(str,str,str)
    profile = 'Profile 1'
    def run(self):
        try:
            name = main_code.getname(0)
            main_code.maincodeexcute(0)
            self.finished.emit(name,'success','Some Message')
                
        except SystemExit:
            msg = f'Code Finished Running, {self.profile}'
            print(msg)
            self.finished.emit('','Finished',msg)
        except NoSuchWindowException or InvalidSessionIdException or WebDriverException:
            msg = f'Oops ,Browser Window was closed please try again, {self.profile}'
            print(msg)
            self.finished.emit('','fail',msg)
        except UnboundLocalError:
            msg = f'Problem with Browser, Consider Changing the Proxy, {self.profile}'
            print(msg)
            self.finished.emit('','fail',msg)
        except ConnectionAbortedError:
            msg = f'Connection Aborted! Please Try Connecting again after closing Antivirus or firewall, {self.profile}'
            print(msg)
            self.finished.emit('','fail',msg)
        except ProtocolError:
            msg = f'Protocol Error! Please Try Connecting again, {self.profile}'
            print(msg)
            self.finished.emit('','fail',msg) 
        except NoSuchElementException:
            msg = f'Problem with Browser, Please try Again, {self.profile}'
            print(msg)
            self.finished.emit('','fail',msg)
        except WebDriverException:
            msg = f'Please check the version of SunPower Browser in Ads Power, {self.profile}'
            print(msg)
            self.finished.emit('','fail',msg)
        except :
            msg = f'Open Ads work Program and try again, {self.profile}'
            print(msg)
            self.finished.emit('','fail',msg)
        
                        

class Worker_2(QThread):
    
    finished = pyqtSignal(str,str,str)
    profile = 'Profile 2'
    def run(self):
        try:
            time.sleep(2)
            name = main_code.getname(1)
            main_code.maincodeexcute(1)
            self.finished.emit(name,'success','Some Message')
                
        except SystemExit:
            msg = f'Code Finished Running 1 {self.profile}'
            print(msg)
            self.finished.emit('','Finished',msg)
        except NoSuchWindowException or InvalidSessionIdException or WebDriverException:
            msg = f'Oops ,Browser Window was closed please try again, {self.profile}'
            print(msg)
            self.finished.emit('','fail',msg)
        except UnboundLocalError:
            msg = f'Problem with Browser, Consider Changing the Proxy, {self.profile}'
            print(msg)
            self.finished.emit('','fail',msg)
        except ConnectionAbortedError:
            msg = f'Connection Aborted! Please Try Connecting again after closing Antivirus or firewall, {self.profile}'
            print(msg)
            self.finished.emit('','fail',msg)
        except ProtocolError:
            msg = f'Protocol Error! Please Try Connecting again, {self.profile}'
            print(msg)
            self.finished.emit('','fail',msg) 
        except NoSuchElementException:
            msg = f'Problem with Browser, Please try Again, {self.profile}'
            print(msg)
            self.finished.emit('','fail',msg)
        except WebDriverException:
            msg = f'Please check the version of SunPower Browser in Ads Power, {self.profile}'
            print(msg)
            self.finished.emit('','fail',msg)
        except :
            msg = f'Open Ads work Program and try again, {self.profile}'
            print(msg)
            self.finished.emit('','fail',msg)
            
            
class Worker_3(QThread):
    
    finished = pyqtSignal(str,str,str)
    profile = 'Profile 3'
    def run(self):
        try:
            time.sleep(4)
            name = main_code.getname(2)
            main_code.maincodeexcute(2)
            self.finished.emit(name,'success','Some Message')
                
        except SystemExit:
            msg = f'Code Finished Running, {self.profile}'
            print(msg)
            self.finished.emit('','Finished',msg)
        except NoSuchWindowException or InvalidSessionIdException or WebDriverException:
            msg = f'Oops ,Browser Window was closed please try again, {self.profile}'
            print(msg)
            self.finished.emit('','fail',msg)
        except UnboundLocalError:
            msg = f'Problem with Browser, Consider Changing the Proxy, {self.profile}'
            print(msg)
            self.finished.emit('','fail',msg)
        except ConnectionAbortedError:
            msg = f'Connection Aborted! Please Try Connecting again after closing Antivirus or firewall, {self.profile}'
            print(msg)
            self.finished.emit('','fail',msg)
        except ProtocolError:
            msg = f'Protocol Error! Please Try Connecting again, {self.profile}'
            print(msg)
            self.finished.emit('','fail',msg) 
        except NoSuchElementException:
            msg = f'Problem with Browser, Please try Again, {self.profile}'
            print(msg)
            self.finished.emit('','fail',msg)
        except WebDriverException:
            msg = f'Please check the version of SunPower Browser in Ads Power, {self.profile}'
            print(msg)
            self.finished.emit('','fail',msg)
        except :
            msg = f'Open Ads work Program and try again, {self.profile}'
            print(msg)
            self.finished.emit('','fail',msg)
            

class Worker_4(QThread):
    
    finished = pyqtSignal(str,str,str)
    profile = 'Profile 4'
    def run(self):
        try:
            time.sleep(6)
            name = main_code.getname(3)
            main_code.maincodeexcute(3)
            self.finished.emit(name,'success','Some Message')
                
        except SystemExit:
            msg = f'Code Finished Running, {self.profile}'
            print(msg)
            self.finished.emit('','Finished',msg)
        except NoSuchWindowException or InvalidSessionIdException or WebDriverException:
            msg = f'Oops ,Browser Window was closed please try again, {self.profile}'
            print(msg)
            self.finished.emit('','fail',msg)
        except UnboundLocalError:
            msg = f'Problem with Browser, Consider Changing the Proxy, {self.profile}'
            print(msg)
            self.finished.emit('','fail',msg)
        except ConnectionAbortedError:
            msg = f'Connection Aborted! Please Try Connecting again after closing Antivirus or firewall, {self.profile}'
            print(msg)
            self.finished.emit('','fail',msg)
        except ProtocolError:
            msg = f'Protocol Error! Please Try Connecting again, {self.profile}'
            print(msg)
            self.finished.emit('','fail',msg) 
        except NoSuchElementException:
            msg = f'Problem with Browser, Please try Again, {self.profile}'
            print(msg)
            self.finished.emit('','fail',msg)
        except WebDriverException:
            msg = f'Please check the version of SunPower Browser in Ads Power, {self.profile}'
            print(msg)
            self.finished.emit('','fail',msg)
        except :
            msg = f'Open Ads work Program and try again, {self.profile}'
            print(msg)
            self.finished.emit('','fail',msg)
            
            
class Worker_5(QThread):
    
    finished = pyqtSignal(str,str,str)
    profile = 'Profile 5'
    def run(self):
        try:
            time.sleep(8)
            name = main_code.getname(4)
            main_code.maincodeexcute(4)
            self.finished.emit(name,'success','Some Message')
                
        except SystemExit:
            msg = f'Code Finished Running, {self.profile}'
            print(msg)
            self.finished.emit('','Finished',msg)
        except NoSuchWindowException or InvalidSessionIdException or WebDriverException:
            msg = f'Oops ,Browser Window was closed please try again, {self.profile}'
            print(msg)
            self.finished.emit('','fail',msg)
        except UnboundLocalError:
            msg = f'Problem with Browser, Consider Changing the Proxy, {self.profile}'
            print(msg)
            self.finished.emit('','fail',msg)
        except ConnectionAbortedError:
            msg = f'Connection Aborted! Please Try Connecting again after closing Antivirus or firewall, {self.profile}'
            print(msg)
            self.finished.emit('','fail',msg)
        except ProtocolError:
            msg = f'Protocol Error! Please Try Connecting again, {self.profile}'
            print(msg)
            self.finished.emit('','fail',msg) 
        except NoSuchElementException:
            msg = f'Problem with Browser, Please try Again, {self.profile}'
            print(msg)
            self.finished.emit('','fail',msg)
        except WebDriverException:
            msg = f'Please check the version of SunPower Browser in Ads Power, {self.profile}'
            print(msg)
            self.finished.emit('','fail',msg)
        except :
            msg = f'Open Ads work Program and try again, {self.profile}'
            print(msg)
            self.finished.emit('','fail',msg)
            

class AppUI(Ui_amazonaccount):
    
    def myui(self,appwindow):
        super().setupUi(appwindow)
        # with open('style.css','r') as sh:
        #     appwindow.setStyleSheet(sh.read())
        self.myedit()
        self.counter = 0
        today = datetime.date.today()
        year = today.year
        self.label = QtWidgets.QLabel(appwindow)
        self.label.setGeometry(280,330,500,60)
        self.label.setText(f'Dev Gad Badr © All Rights Reserved {year}, For Mr Mounir')
        
    def myedit(self):

        appwindow.setFixedSize(855,404)
        appwindow.setWindowIcon(QtGui.QIcon('icon.png'))
        appwindow.setWindowFlags(appwindow.windowFlags() | Qt.WindowMinimizeButtonHint)
        self.start_button.clicked.connect(self.maincode)
        self.browse_button.clicked.connect(self.open_data)
        self.close_button.clicked.connect(self.close_window)
        self.profiles_button.clicked.connect(self.profiles)
        self.openLogbut.clicked.connect(self.openLog)
        self.start_button.setCursor(Qt.PointingHandCursor)
        main_code.status_message.connect(self.takingShots)
        
    def openLog(self):
        QDesktopServices.openUrl(QtCore.QUrl.fromLocalFile('Logging.txt'))
        
    def read_profiles(self):
        with open('profile_ids.txt','r') as h :
            ids = h.readlines()
        h.close()
        
        #cleaning
        clean_ids=[]
        for i in ids:
            l=i.replace('\n','')
            clean_ids.append(l)
                   
    def maincode(self):
       
        self.worker_1 = worker_1()
        self.worker_2 = Worker_2()
        self.worker_3 = Worker_3()
        self.worker_4 = Worker_4()
        self.worker_5 = Worker_5()
        
        self.worker_1.finished.connect(self.codefinish)
        self.worker_2.finished.connect(self.codefinish)
        self.worker_3.finished.connect(self.codefinish)
        self.worker_4.finished.connect(self.codefinish)
        self.worker_5.finished.connect(self.codefinish)

        start_list=[
            self.worker_1,
            self.worker_2,
            self.worker_3,
            self.worker_4,
            self.worker_5
        ]
        
        with open('profile_ids.txt','r') as p:
            m = p.readlines()
            # print(m)
            cleanm=[]
            for item in m:
                nitem = item.replace('\n','')
                if len(nitem)==7:
                    cleanm.append(nitem)
                else:
                    pass
        p.close()
        print(cleanm)
        
        for pro in range(0,len(cleanm)):
            start_list[pro].start()
                      
        
    def open_data(self):
        QDesktopServices.openUrl(QtCore.QUrl.fromLocalFile('account_details.txt'))
        
    def close_window(self):
        app.closeAllWindows()    
        
    def progress_bar(self):
        pass
    
    def codefinish(self,name,status,message):
        
        if status == 'success':
            self.msg = QtWidgets.QMessageBox()
            self.msg.setText(f'Merch Account Created Successfully for\n{name}')
            self.msg.setWindowIcon(QtGui.QIcon('icon.png'))
            self.msg.setWindowTitle('Success')
            self.msg.exec()
        if status=='fail':
            self.msg = QtWidgets.QMessageBox()
            self.msg.setText(message)
            self.msg.setWindowIcon(QtGui.QIcon('icon.png'))
            self.msg.setWindowTitle('Failed')
            self.msg.exec()
        if status=='Finished':
            self.msg = QtWidgets.QMessageBox()
            self.msg.setText(message)
            self.msg.setWindowIcon(QtGui.QIcon('icon.png'))
            self.msg.setWindowTitle('Finished')
            self.msg.exec()
            
            
    def takingShots(self,msg):
        print(f'Oh, Im here taking shots like this one {msg}')
        
        
    def profiles(self):
        QDesktopServices.openUrl(QtCore.QUrl.fromLocalFile('profile_ids.txt'))
        
        
if __name__ == '__main__':
    main_code = MainCode()
    app =QtWidgets.QApplication([])
    appwindow = QtWidgets.QDialog()
    mydialog = AppUI()
    mydialog.myui(appwindow)
    appwindow.show()
    app.exec_()