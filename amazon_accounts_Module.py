
# This is a script to automate the creating of amazon accounts

from selenium import webdriver 
from selenium.webdriver.common.by import By
import os
import requests
import time
from ast import literal_eval
import pyotp
from account_getdetails import Mydata
from selenium.webdriver.support.ui import Select
import sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import datetime
from PyQt5.QtCore import *

class MainCode(QObject):
    
    status_message = pyqtSignal(str)
    
    def getname(self,idd):
        
        x = Mydata()
        y=x.getdata()
        d=y[idd]
        
        return d[5]
        
    def logTheResult(self,idd):
        timestamp=datetime.datetime.now()
        timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S')
        with open('Logging.txt','a') as l:
            name = self.getname(idd)
            l.write(f'Merch Account Created Successfully for\n\t{name}\n\t{timestamp}\n')
        l.close()

    def maincodeexcute(self,idd):
        
        print('...\nRunning main code')
                
        ex=0
        # user_number = 0
        # profile_id = 0
        # idd = 0


        x = Mydata()
        y=x.getdata()
        d=y[idd]

        current_dir = os.getcwd()

        with open('profile_ids.txt','r') as g:
            profiles=g.read()
            pros = profiles.split('\n')
        g.close()

        #account_data
        email = d[0]
        password= d[1]
        secret = d[2]

        url='https://www.amazon.com/'
        adspower_profile_id = pros[idd]

        ads_id = adspower_profile_id
        open_url = "http://local.adspower.net:50325/api/v1/browser/start?user_id=" + ads_id
        close_url = "http://local.adspower.net:50325/api/v1/browser/stop?user_id=" + ads_id

        print('Connecting to AdsPower Web Browser')

        resp = requests.get(open_url,60).json()
        if resp["code"] != 0:
            print(resp["msg"])
            print("please check ads_id")
            sys.exit()

        myservice = Service(executable_path=r"chromedriver.exe")
        chrome_driver = resp["data"]["webdriver"]
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", resp["data"]["ws"]["selenium"])
        # proxy = '192.168.185.33:30001'
        # chrome_options.add_argument('--proxy-server=%s' % proxy)
        driver = webdriver.Chrome(service=myservice, options=chrome_options)
        

        msg = 'Code Running...'
        print(msg)

        try :

            driver.get(url)

        except WebDriverException:
            
            print('Internet Problem')
            ex=1
            
        except UnboundLocalError:
            print('AdsPower failed to launch, Please try again')
            ex=1


        if ex == 1:
            raise SystemExit('The Main Code has Finished his task')

        wait = WebDriverWait(driver, 120)
        wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")

        #check if there is a captcha or not - wait until i see the search bar
        counter=1
        while True:
            try:
                #IF odd amazon home page it loads the website again
                driver.find_element(By.XPATH,'//*[@id="navbar-backup-backup"]/div/div[3]/a[1]')
                driver.get(url)
                
            except:
                time.sleep(1)
            
            try:
                driver.find_element(By.XPATH,'//*[@id="twotabsearchtextbox"]')
                print('Website Loaded Successfully')
                break
                # //*[@id="twotabsearchtextbox"]
                # /html/body/div/div[1]/div[3]/div/div/form/div[1]/div/div/div[2]/div/div[2]/a
        
            except UnboundLocalError:
                print('AdsPower Failed to launch,\nPlease make sure it opens correctly\nand Try again')
                break
                
            except:
                counter+=1
                time.sleep(5)
                print(f'Captcha Detected Please pass me to continue Trial {counter}, will abort on trial 60')
                
                try:
                    driver.current_url
                except:
                    break

                if counter==60:
                    ex=1
                    break
                
        if ex == 1:
            raise SystemExit('The Main Code has Finished his task')

        wait = WebDriverWait(driver, 120)
        wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")

        #Set language to English if in any other language
        site_language = driver.find_element(By.XPATH,'//*[@id="nav-link-accountList-nav-line-1"]')
        lang = site_language.text

        if 'Hello,' in lang:
            pass
        else:
            lang_but = driver.find_element(By.XPATH,'//*[@id="icp-nav-flyout"]/span/span[2]')
            lang_but.click()
            wait = WebDriverWait(driver, 120)
            wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")
            wait15 = WebDriverWait(driver,200).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="icp-language-settings"]/div[2]/div/label/i')))
            language_eng = driver.find_element(By.XPATH,'//*[@id="icp-language-settings"]/div[2]/div/label/i')
            language_eng.click()
            wait16 = WebDriverWait(driver,200).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="icp-save-button"]/span/input')))
            save_changes = driver.find_element(By.XPATH,'//*[@id="icp-save-button"]/span/input')
            save_changes.click()
            time.sleep(2)
            
        wait = WebDriverWait(driver, 120)
        wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")
        
        waittoload = WebDriverWait(driver,200).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="nav-link-accountList-nav-line-1"]')))
      
        while True:
            try:
                name = driver.find_element(By.XPATH,'//*[@id="nav-link-accountList-nav-line-1"]')
                user=name.text
                signed_in=False
                break
            except:
      
                time.sleep(2)
                try:
                    driver.current_url
                except:
                    break
                
        #check if already signed in     
        if 'Hello, sign in' in user:
                
            #step 1 sign in to amazon account
            wait2 = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="nav-link-accountList"]')))
            sign_in_button = driver.find_element(By.XPATH,'//*[@id="nav-link-accountList"]')
            sign_in_button.click()
            
            time.sleep(3)
            
            #check switch account case
            try:
                switch_account = driver.find_element(By.XPATH,'//*[@id="ap-account-switcher-container"]/div[1]/div/div/div[2]/h1')
                switch = switch_account.text
                
                if switch == 'Switch accounts':
                    
                    wait9 = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="ap-account-switcher-container"]/div[1]/div/div/div[2]/div[1]/div[2]/a/div/div/div/div/div[2]/div/div/div[1]/div[1]')))
                    curr=driver.find_element(By.XPATH,'//*[@id="ap-account-switcher-container"]/div[1]/div/div/div[2]/div[1]/div[2]/a/div/div/div/div/div[2]/div/div/div[1]/div[1]')
                    curr.click()
                    
                    time.sleep(3)
                    pas_box = driver.find_element(By.XPATH,'//*[@id="ap_password"]')
                    pas_box.send_keys(password)
                    curr=driver.find_element(By.XPATH,'//*[@id="signInSubmit"]')
                    curr.click()
                    signed_in = True
                    
            except:
                pass
            
            if not signed_in:
                
                # Normal Sign in Case #
                
                #type email
                wait = WebDriverWait(driver, 120)
                wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")
                wait10 = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="ap_email"]')))
                email_box = driver.find_element(By.XPATH,'//*[@id="ap_email"]')
                email_box.send_keys(email)

                #click sign in
                wait10 = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="continue"]')))
                sign_in = driver.find_element(By.XPATH,'//*[@id="continue"]')
                sign_in.click()


                #case password is required
                wait = WebDriverWait(driver, 120)
                wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")
                wait10 = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="ap_password"]')))
                case_pass = driver.find_element(By.XPATH,'//*[@id="authportal-main-section"]/div[2]/div/div[2]/div/form/div/div[1]/div[1]/div[1]/label')
                case_pass_text = case_pass.text
                
                if case_pass_text=='Password':
                    
                    #type password
                    pass_box = driver.find_element(By.XPATH,'//*[@id="ap_password"]')
                    pass_box.send_keys(password)
                    #check box remember me
                    check_box = driver.find_element(By.XPATH,'//*[@id="authportal-main-section"]/div[2]/div/div[2]/div/form/div/div[2]/div/div/label/div/label/input')
                    check_box.click()
                    #click sign in
                    check_box = driver.find_element(By.XPATH,'//*[@id="signInSubmit"]')
                    check_box.click()
                    
                    
                    # #Handle Important message
                    # try:
                    #     #Type Password
                    #     otp_box = driver.find_element(By.XPATH,'//*[@id="ap_password"]')
                    #     otp_box.send_keys(password)
                        
                    #     print('Hello, Please Enter Captcha and then Type any key in the box and hit Enter')
                    #     while True:
                    #         try:
                    #             siggi = driver.find_element(By.XPATH,'//*[@id="signInSubmit"]')
                    #             break

                    #         except:
                    #             time.sleep(2)
                                
                    #     #click sign in
                    #     siggi = driver.find_element(By.XPATH,'//*[@id="signInSubmit"]')
                    #     siggi.click()
                        
                    #     try:
                    #         siggi = driver.find_element(By.XPATH,' //*[@id="auth-error-message-box"]/div/h4')
                    #         #Type Password
                    #         otp_box = driver.find_element(By.XPATH,'//*[@id="ap_password"]')
                    #         otp_box.send_keys(password)
                    #         #click sign in
                    #         siggi = driver.find_element(By.XPATH,'//*[@id="signInSubmit"]')
                    #         siggi.click()
                    #     except:
                    #         pass
                        
                    # except:
                    #     pass
                    
                    wait = WebDriverWait(driver, 120)
                    wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")
                    myurl = driver.current_url
                    if 'mfa' in myurl:
                        enter_otp = True
                    else:
                        enter_otp = False
                        
                        
                    if enter_otp:
                        #check if already signed in or need to enter otp
                    
                        try:
                            sign_in_check = driver.find_element(By.XPATH,'//*[@id="nav-cart-count-container"]/span[2]')
                        except:
                            
                            # Create a new TOTP object
                            totp = pyotp.TOTP(secret)

                            # Generate a new OTP
                            otp = totp.now()
                            
                            #paste otp and click sign in
                            otp_box = driver.find_element(By.XPATH,'//*[@id="auth-mfa-otpcode"]')
                            otp_box.send_keys(otp)
                        
                            #checkbox for remember me
                            ch_otp = driver.find_element(By.XPATH,'//*[@id="auth-mfa-remember-device"]')
                            ch_otp.click()
                            
                            #click sign in for otp
                            sign_in_otp = driver.find_element(By.XPATH,'//*[@id="auth-signin-button"]')
                            sign_in_otp.click()
                            
                            time.sleep(3)
                            
                            # Case if the OTP is incorrect
                            try:
                                sign_in_otp = driver.find_element(By.XPATH,'//*[@id="auth-signin-button"]')
                                passed=False
                                while not passed:
                                           
                                    try:
                                        driver.find_element(By.XPATH,'//*[@id="nav-link-accountList"]')
                                        passed=True
                                        break
                                    except:
                                        pass
                            except:
                                pass
                            
                                
                    while True:
                        cururl = driver.current_url
                        if "https://www.amazon.com/?ref_=nav_ya_signin" in cururl:
                            skip_hackers = False
                            break
                            
                        elif "accountfixup" in cururl:
                            skip_hackers = True
                            break
                        
                        elif "request" in cururl:
                            skip_hackers = False
                            break
                        elif 'https://www.amazon.com/?language=en_US&currency=USD&ref_=nav_ya_signin' in cururl:
                            skip_hackers = False
                            break

                    if skip_hackers:
                        while True:
                            #skip hackers-out check
                            try:
                                wait = WebDriverWait(driver, 200)
                                wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")
                                hackers_out = driver.find_element(By.XPATH,'//*[@id="auth-account-fixup-phone-form"]/div/h1')
                                hackers_true = hackers_out.text
                                if 'Keep hackers out' in hackers_true:
                                    not_now = driver.find_element(By.XPATH,'//*[@id="ap-account-fixup-phone-skip-link"]')
                                    not_now.click() 
                                    
                                break
                            except:
                                time.sleep(1)
                                print('Skipping Hackers Out')
                    
                    counter=0
                    while True:
                        try:
                            driver.find_element(By.XPATH,'//*[@id="twotabsearchtextbox"]')
                            print('Passed, Website Loaded Successfully')
                            break
                            # //*[@id="twotabsearchtextbox"]
                            # /html/body/div/div[1]/div[3]/div/div/form/div[1]/div/div/div[2]/div/div[2]/a
                    
                        except UnboundLocalError:
                            print('AdsPower Failed to launch,\nPlease make sure it opens correctly\nand Try again')
                            break
                            
                        except:
                            counter+=1
                            time.sleep(5)
                            print(f'Waiting to Pass {counter}/60, Will abort on 60')
                            
                            if counter==60:
                                ex=1
                                break
                            
                            try:
                                driver.find_element(By.XPATH,'//*[@id="navbar-backup-backup"]/div/div[3]/a[1]')
                                driver.refresh()
                            except:
                                pass
                            
                            try:
                                driver.current_url
                            except:
                                break
                                                

                else:
                    otp_button = driver.find_element(By.XPATH,'//*[@id="continue"]')
                    otp_button.click()
            else:
                pass
        else:
            pass


        counter=0
        while True:
            try:
                driver.find_element(By.XPATH,'//*[@id="twotabsearchtextbox"]')
                print('Passed, Website Loaded Successfully')
                break
                # //*[@id="twotabsearchtextbox"]
                # /html/body/div/div[1]/div[3]/div/div/form/div[1]/div/div/div[2]/div/div[2]/a
        
            except UnboundLocalError:
                print('AdsPower Failed to launch,\nPlease make sure it opens correctly\nand Try again')
                break
                
            except:
                counter+=1
                time.sleep(5)
                print(f'Waiting to Pass {counter}/60, Will abort on 60')
                if counter==60:
                    ex=1
                    break
                
                try:
                    driver.current_url
                except:
                    break
                

        # Open a new tab
        driver.execute_script("window.open('');")

        # Switch to the new tab
        driver.switch_to.window(driver.window_handles[-1])

        # Navigate to another web page in the new tab
        driver.get('https://merch.amazon.com/landing')

        clicked=False
        while not clicked:
            try:       
                #click sign up for merch account
                wait11 = WebDriverWait(driver,90).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="invitation-button"]')))
                sign_in_merch = driver.find_element(By.XPATH,'//*[@id="invitation-button"]')
                sign_in_merch.click()
                break
            except:
                time.sleep(1)
                
                              
        try:
            #case password again

            #type password
            pass_box = driver.find_element(By.XPATH,'//*[@id="ap_password"]')
            pass_box.send_keys(password)
            #check box remember me
            check_box = driver.find_element(By.XPATH,'//*[@id="authportal-main-section"]/div[2]/div/div[2]/div/div/form/div/div[2]/div/div/label/div/label/input')
            check_box.click()
            #click sign in
            check_box = driver.find_element(By.XPATH,'//*[@id="signInSubmit"]')
            check_box.click()
            
            
        except:
            time.sleep(1)
        
        while True:
            url = driver.current_url
            if url in ['https://merch.amazon.com/sign-up/request/submitted','https://merch.amazon.com/sign-up/request','https://merch.amazon.com/terms','https://merch.amazon.com/sign-up/request/information-needed']:
                break

        #Case Created
        if url == 'https://merch.amazon.com/sign-up/request/submitted':
            try:
                created = driver.find_element(By.XPATH,'//*[@id="submitted-status-messaging"]/h1')
                created_t = created.text
                print('Merch Account Already Created and Pending Review')
                
                ex=1
            except:
                pass

        if ex == 1:
            raise SystemExit('The Main Code has Finished his task')
            
        # Case it heads directly to the last page
        if url== 'https://merch.amazon.com/sign-up/request':
            
            english = False
            while not english:
                
                try:   
                    heading = driver.find_element(By.XPATH,'/html/body/div[1]/div/app-root/div/div[2]/ng-component/div/div/request-invite-form/div/div/h1')
                    t = heading.text
                    
                    if 'Sign up Form' in t:
                        english=True
                        break
                    else:
                        #change to EN
                        EN = driver.find_element(By.XPATH,'//*[@id="header-links"]/lop-selector/div/button')
                        EN.click()
                        EN = driver.find_element(By.XPATH,'//*[@id="header-links"]/lop-selector/div/ul/li[1]/a')
                        EN.click()
                                        
                    en=False
                    while not en:
                        try:
                            heading = driver.find_element(By.XPATH,'/html/body/div[1]/div/app-root/div/div[2]/ng-component/div/div/request-invite-form/div/div/h1')
                            t=heading.text
                            if 'Sign up Form' in t:
                                en=True
                                break
                        except:
                            pass
                    english=True
                    break
                except:
                    time.sleep(1)
                    print("im stuck in languge")
                    pass
            
            try:     
                wait11 = WebDriverWait(driver,2).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="clear-button"]')))
                last_page_case = driver.find_element(By.XPATH,'//*[@id="clear-button"]')
                
                #choose industry 
                time.sleep(3)
                dropdown = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="industryType-field"]')))
                select = Select(dropdown)
                select.select_by_value("Other")

                #Type org name and additional information
                org_name = driver.find_element(By.XPATH,'//*[@id="orgName-field"]')
                org_name.send_keys(d[5])
                
                paragraph = driver.find_element(By.XPATH,'//*[@id="additionalInfo-field"]')
                paragraph.send_keys(d[17])
                
                print(True, '\nMerch Account Created Successfully')
                ex=1
            except:
                pass

        if ex == 1 :
            raise SystemExit('The Main Code has Finished his task')
            

        # Case it continues Normally with the merch sign up
        wait = WebDriverWait(driver, 120)
        wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")

        while True:
            try:
                current_url = driver.current_url
                if current_url in ['https://merch.amazon.com/terms','https://merch.amazon.com/sign-up/request/information-needed'] :
                    break
            except:
                pass

        if current_url == 'https://merch.amazon.com/terms':
            
            terms_button_clicked = False
            while not terms_button_clicked:
                try:
                    #click accept to terms
                    wait12 = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="accept-button"]')))
                    accept_terms = driver.find_element(By.XPATH,'//*[@id="accept-button"]')
                    accept_terms.click()
                    terms_button_clicked=True
                    break
                except:
                    pass
                
            continue_button_clicked = False
            while not continue_button_clicked:
                try:
                    #click continue for welcome message
                    wait13 = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="application-button"]')))
                    wel_msg = driver.find_element(By.XPATH,'//*[@id="application-button"]')
                    wel_msg.click()
                    continue_button_clicked=True
                    break
                except:
                    pass

        elif current_url == 'https://merch.amazon.com/sign-up/request/information-needed':
            continue_button_clicked = False
            while not continue_button_clicked:
                try:
                    #click continue for welcome message
                    wait13 = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="application-button"]')))
                    wel_msg = driver.find_element(By.XPATH,'//*[@id="application-button"]')
                    wel_msg.click()
                    continue_button_clicked=True
                    break
                except:
                    pass
        else:
            pass
        
        while True:
            urln = driver.current_url
            if urln in ['https://account-merch.amazon.com/']:
                
                case_otp = False
                break
            elif 'new-otp' in urln:
                
                try:
                    two_step = driver.find_element(By.XPATH,'//*[@id="authportal-main-section"]/div[2]/div/div/div/div/h1')
                    case_otp = True
                    break
                except:
                    time.sleep(2)
                    print('Facing some delay or problem')
                    
            elif 'signin' in urln:
                while True:
                    try:
                        
                        #Enter Password
                        passw = driver.find_element(By.XPATH,'//*[@id="ap_password"]')
                        passw.send_keys(otp)
                        time.sleep(1)
                        #Enter Sign IN
                        sign_in_otp_1 = driver.find_element(By.XPATH,'//*[@id="signInSubmit"]')
                        sign_in_otp_1.click()
                        while True:
                            urls = driver.current_url
                            if 'new-otp' in urls:
                                case_otp=True
                                break
                            elif 'https://account-merch.amazon.com/' in urls:
                                case_otp = False
                                break
                        break
                    except:
                        time.sleep(2)
                        print('Facing some delay or problem')
            elif 'mfa' in urln:
                 
                # Create a new TOTP object
                totp = pyotp.TOTP(secret)

                # Generate a new OTP
                otp = totp.now()
                
                #Enter OTP
                passw = driver.find_element(By.XPATH,'//*[@id="auth-mfa-otpcode"]')
                passw.send_keys(otp)
                time.sleep(1)
                #Enter Sign IN
                sign_in_otp_1 = driver.find_element(By.XPATH,'//*[@id="auth-signin-button"]')
                sign_in_otp_1.click()
                break
            
        if case_otp:
            while True:
                try:
                    time.sleep(1)
                    #case two step verification
                    two_step = driver.find_element(By.XPATH,'//*[@id="authportal-main-section"]/div[2]/div/div/div/div/h1')
                    case_two_step = two_step.text
                    if 'Two-Step Verification'in case_two_step:
                        #Check Send OTP on APP
                        try:
                            sign_in_otp_1 = driver.find_element(By.XPATH,'//*[@id="auth-select-device-form"]/div[1]/fieldset/div/label/span')
                            sign_in_otp_1.click()
                        except: 
                            sign_in_otp_2 = driver.find_element(By.XPATH,'//*[@id="auth-select-device-form"]/div[1]/fieldset/div[1]/label/span')
                            sign_in_otp_2.click()
                            
                        time.sleep(5)
                        #Case Send OTP Button
                        try:
                            #Click Send OTP
                            sign_in_otp = driver.find_element(By.XPATH,'//*[@id="auth-send-code"]')
                            sign_in_otp.click()
                            
                            time.sleep(2)
                            
                            totp = pyotp.TOTP(secret)
                            otp = totp.now()
                                        
                            #paste otp and click sign in
                            otp_box = driver.find_element(By.XPATH,'//*[@id="auth-mfa-otpcode"]')
                            otp_box.send_keys(otp)
                                        
                            #click sign in for otp
                            sign_in_otp = driver.find_element(By.XPATH,'//*[@id="auth-signin-button"]')
                            sign_in_otp.click()
                            
                        except:
                            pass
                        
                        # Case There was a problem message
                        errormsg = False
                        while True:
                            try:
                                ele = driver.find_element(By.XPATH,'//*[@id="auth-error-message-box"]/div/h4')
                                msge = ele.text
                                if 'There was a problem' in msge:
                                    errormsg = True
                                
                                if errormsg:
                                    time.sleep(2)
                            
                                    totp = pyotp.TOTP(secret)
                                    otp = totp.now()
                                                
                                    #paste otp and click sign in
                                    otp_box = driver.find_element(By.XPATH,'//*[@id="auth-mfa-otpcode"]')
                                    otp_box.send_keys(otp)
                                                
                                    #click sign in for otp
                                    sign_in_otp = driver.find_element(By.XPATH,'//*[@id="auth-signin-button"]')
                                    sign_in_otp.click()
                                    break
                                
                                else:
                                    break
           
                            except:
                                time.sleep(1)
                                break
                        break
                except:
                    time.sleep(1)


        #Author/Publisher information #

        wait = WebDriverWait(driver, 120)
        wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")

        not_loaded = True
        while not_loaded:
            try :
                heading = driver.find_element(By.XPATH,'//*[@id="payee-save-button"]')
                WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="payee-save-button"]')))
                not_loaded = False
                print('Data Page Loaded')
                break
            except:
                pass
            
        english = False
        while not english:
            try:   
                heading = driver.find_element(By.XPATH,'//*[@id="address"]/app-profile-edit/h2')
                t = heading.text
                if ('country/region' in t) or ('Creator Information' in t):
                    english=True
                    break
                else:
                    #change to EN
                    EN = driver.find_element(By.XPATH,'//*[@id="angular-page-container"]/div[1]/div[1]/div/div[2]/div/button')
                    EN.click()
                    EN = driver.find_element(By.XPATH,'//*[@id="lop-dropdown-container"]/div/a[1]')
                    EN.click()
                    time.sleep(2)
                    EN = driver.find_element(By.XPATH,'//*[@id="unsaved-changes-continue-without-saving-button"]')
                    EN.click()
                en=False
                while not en:
                    try:
                        lang_but = driver.find_element(By.XPATH,'//*[@id="angular-page-container"]/div[1]/div[1]/div/div[2]/div/button')
                        t=lang_but.text
                        if 'EN' in t:
                            en=True
                            break
                    except:
                        pass
                english=True
                break
            except:
                pass

        try:
            time.sleep(4)
            case_filled = driver.find_element(By.XPATH,'//*[@id="bank-account-header"]/button/span')
            case_filled_t = case_filled.text
            try:
                time.sleep(4)
                all_filled = driver.find_element(By.XPATH,'//*[@id="argon-tax-interview-button"]/span[1]/span')
                all_text = all_filled.text

                if 'Complete Tax Information' in all_text:

                    tax_filled=False

                else:
                    tax_filled=True
            except:
                tax_filled = False
                
            if tax_filled:
                save_and_cont = False
                while not save_and_cont:
                    try:
                        #Save and Continue
                        time.sleep(2)
                        wait = WebDriverWait(driver, 120)
                        wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")
                        wait13 = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="payee-save-and-continue-button"]')))
                        save_cont = driver.find_element(By.XPATH,'//*[@id="payee-save-and-continue-button"]')
                        save_cont.click()
                        save_and_cont=True
                        break
                    except:
                        time.sleep(1)
                
                wait = WebDriverWait(driver, 120)
                wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")
                
                #choose industry 
                we_are_in_last_page=False
                while not we_are_in_last_page:
                    try:
                        #choose industry 
                        time.sleep(3)
                        dropdown = WebDriverWait(driver, 180).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="industryType-field"]')))
                        select = Select(dropdown)
                        select.select_by_value("Other")
                        we_are_in_last_page=True
                        break
                    except:
                        time.sleep(1)

                
                time.sleep(2)

                #Type org name and additional information
                org_name = driver.find_element(By.XPATH,'//*[@id="orgName-field"]')
                org_name.send_keys(d[5])
                
                time.sleep(2)

                paragraph = driver.find_element(By.XPATH,'//*[@id="additionalInfo-field"]')
                paragraph.send_keys(d[17])

                print(True, '\nMerch Account Created Successfully')


                try:
                    fin = driver.find_element(By.XPATH,'//*[@id="submitted-status-messaging"]/h1')
                    fin_t = fin.text
                    if 'Your request is pending review.' in fin_t:
                        print('The Application is already Submitted')
                except:
                    print(False,'\nSomething Went wrong please check the web browser ')
                    
                ex=1
                
            try:
                smallscreen = driver.find_element(By.XPATH,'//*[@id="getting-paid"]/div[2]/h4')
                smallscreen_t = smallscreen.text
                if 'Your Bank Accounts' in smallscreen_t:
                    print('Small Screen Detected')
            except:
                pass
            
            
            if ex==1:
                raise SystemExit('The Main Code has Finished his task')
                
            
            elif case_filled_t == 'Expand Details' or 'Your Bank Accounts' in smallscreen_t:
                #Press Tax Information
                tax_but = driver.find_element(By.XPATH,'//*[@id="argon-tax-interview-button"]')
                tax_but.click()
                
        except:
            


            #check individual
            indvidual = driver.find_element(By.XPATH,'//*[@id="mat-radio-2"]/label')
            indvidual.click()
            
            #type fullname
            
            b3_box = driver.find_element(By.XPATH,'//*[@id="mat-input-1"]')
            b3_box.send_keys(d[5])
            
            #type phone
            
            b9_box = driver.find_element(By.XPATH,'//*[@id="mat-input-0"]')
            b9_box.send_keys(d[11])
            
            #type bussiness email address
            
            b10_box = driver.find_element(By.XPATH,'//*[@id="mat-input-2"]')
            b10_box.send_keys(d[12])


            #Click on add address button
            indvidual = driver.find_element(By.XPATH,'//*[@id="super-comp-2"]/div/div[3]/div/button')
            indvidual.click()
            
            while True:
                try:
                    #type country or region
                    
                    b2_box = driver.find_element(By.XPATH,'//*[@id="mat-input-3"]')
                    b2_box.send_keys(d[4].title().replace('And','and'))
                    time.sleep(1)
                    click_country = driver.find_element(By.CLASS_NAME,'mat-option-text')
                    click_country.click()
                    
                    break
                except Exception as e:
                    print(e)
                    time.sleep(1)
                    break
                
            #type Address Line 1
            b4_box = driver.find_element(By.XPATH,'//*[@id="mat-input-4"]')
            b4_box.send_keys(d[6])
            
            #type Address Line 2
            b5_box = driver.find_element(By.XPATH,'//*[@id="mat-input-5"]')
            b5_box.send_keys(d[7])
                        
            #type city
            b6_box = driver.find_element(By.XPATH,'//*[@id="mat-input-6"]')
            b6_box.send_keys(d[8])

            #type state/province/region
            b7_box = driver.find_element(By.XPATH,'//*[@id="mat-input-7"]')
            b7_box.click()
            time.sleep(1)
            b7_box.send_keys(d[9])
            time.sleep(1)
            while True:
                try:
                    provinza = driver.find_element(By.CLASS_NAME,'mat-option-text')
                    provinza.click()
                    break
                
                except:
                    
                    
                    b07_box = driver.find_element(By.XPATH,'//*[@id="mat-input-8"]')
                    b07_box.click()
                    
                    try:
                        error_msg = driver.find_element(By.XPATH,'//*[@id="mat-dialog-0"]/app-workflow-dialog/app-smooth-height/div/div/div/app-create-edit-address-form/form/mat-dialog-content/mat-form-field[5]/div/div[1]/div/div/span[1]')
                        err = error_msg.text
                        if 'State/Province/Region is required' in err:
                            print('error detected')
                            time.sleep(2)
                            b7_box = driver.find_element(By.XPATH,'//*[@id="mat-input-7"]')
                            b7_box.clear()
                            b07_box = driver.find_element(By.XPATH,'//*[@id="mat-input-7"]')
                            b07_box.click()
                            time.sleep(1)
                            provinza = driver.find_element(By.CLASS_NAME,'mat-option-text')
                            provinza.click()
                        break
                    except:
                        break
                            
                    
            # type postal code
            
            b8_box = driver.find_element(By.XPATH,'//*[@id="mat-input-8"]')
            b8_box.send_keys(d[10])
            
            # Press Use this address     
            use_But = driver.find_element(By.XPATH,'//*[@id="mat-dialog-0"]/app-workflow-dialog/app-smooth-height/div/div/div/app-create-edit-address-form/form/mat-dialog-actions/button')
            use_But.click()
            time.sleep(2)
            n=0
            check_address_xpath = '//*[@id="mat-radio-11"]/label/div[2]/app-html-string/span'
            check_xpath = '//*[@id="mat-checkbox-2"]/label/span'
            # ..
            switch_original_address_case = False
            try:
                original = driver.find_element(By.XPATH,'//*[@id="mat-radio-8"]/label/div[2]/div[1]')

                if 'Original Address' in original.text:
                    original.click()
                    check_xpath = '//*[@id="mat-checkbox-1"]/label/span'
                    check_address_xpath = '//*[@id="mat-radio-17"]/label/div[2]/app-html-string/span'
                    switch_original_address_case = True
                    
            except:
                pass
            
            while True:
                try:
                    driver.find_element(By.XPATH,'//*[@id="interview-bank-country"]')
                    break
                except:
                    time.sleep(1)
                    try:
                        use_But = driver.find_element(By.XPATH,check_xpath)
                        use_But.click()
                        time.sleep(1)
                        use_But = driver.find_element(By.XPATH,'//*[@id="mat-dialog-1"]/app-workflow-dialog/app-smooth-height/div/div/div/app-suggestions/form/mat-dialog-actions/button[1]')
                        use_But.click()
                        print('Address Confirmed')
                    except:
                        time.sleep(3)
                        print('Wrong Data please review to continue')
                        driver.set_window_size(900,700)
                
                    
            #Add Bank Details

            #Type bank location
            
            b11_box = driver.find_element(By.XPATH,'//*[@id="interview-bank-country"]')
            b11_box.send_keys(d[13])
            cont = driver.find_element(By.CLASS_NAME,'mat-option-text')
            cont.click()

            #Type Account holder details
            
            b12_box = driver.find_element(By.XPATH,'//*[@id="interview-bank-accountHolder"]')
            b12_box.send_keys(d[14])

            #Type IBAN Number
            
            b13_box = driver.find_element(By.XPATH,'//*[@id="interview-bank-iban"]')
            b13_box.send_keys(d[15])
            
            #Type Date of birth
            b013_box = driver.find_element(By.XPATH,'//*[@id="mat-input-13"]')
            b013_box.send_keys(d[3])
            
            # Select current address
            while True:
                try:
                    but1 = driver.find_element(By.XPATH,'//*[@id="super-comp-10"]/div/div[3]/div[1]/button')
                    but2 = driver.find_element(By.XPATH,'//*[@id="super-comp-10"]/div/div[3]/div[2]/button')
                    if 'Select Existing Address' in but1.text:
                        req_but = but1
                    else:
                        req_but = but2
                    break
                except:
                    time.sleep(1)
            
            req_but.click()
            time.sleep(1)
            # //*[@id="mat-radio-13"]/label/div[2]/app-html-string/span
            # //*[@id="mat-dialog-2"]/app-workflow-dialog/app-smooth-height/div/div/div/app-custom-address-sources/form/mat-dialog-actions/button[1]
            # //*[@id="super-comp-10"]/div/div[3]/div[1]/button
            # //*[@id="mat-radio-11"]/label/div[2]/app-html-string/span
            # //*[@id="mat-dialog-1"]/app-workflow-dialog/app-smooth-height/div/div/div/app-custom-address-sources/form/mat-dialog-actions/button[1]
            b013_box = driver.find_element(By.XPATH,check_address_xpath)
            b013_box.click()
            time.sleep(1)
            
            accurate_will_show=False
            while True:  
                n+=1 
                xpath = f'//*[@id="mat-dialog-{n}"]/app-workflow-dialog/app-smooth-height/div/div/div/app-custom-address-sources/form/mat-dialog-actions/button[1]'
                try: 

                    b26_box = driver.find_element(By.XPATH,xpath)
                    b26_box.click()
                    if n>1:
                        accurate_will_show=True
                    break
                except Exception as e:
                    time.sleep(1)
                    print('Pressing use this current address')
                    driver.set_window_size(900,700) 
                    

            time.sleep(1)
            #Case address not accurate 
            if accurate_will_show:
                while True:
                    if switch_original_address_case:
                        try:
                            #Check Original Address
                            original = driver.find_element(By.XPATH,'//*[@id="mat-radio-22"]/label/div[2]/div[1]')
                            original.click()
                            time.sleep(1)
                            check_xpath = '//*[@id="mat-checkbox-2"]/label/span'
                            #Select the confirm check box
                            use_But = driver.find_element(By.XPATH,check_xpath)
                            use_But.click()
                            # CLick the use address button
                            time.sleep(1)
                            use_But = driver.find_element(By.XPATH,'//*[@id="mat-dialog-3"]/app-workflow-dialog/app-smooth-height/div/div/div/app-suggestions/form/mat-dialog-actions/button[1]')
                            use_But.click()
                            print('Address Confirmed')
                            break
                        except:
                            time.sleep(1)
                            print('I Can"t Press')
                    else:
                        try: 
                            while True:
                                try:
                                    b013_box = driver.find_element(By.XPATH,'//*[@id="mat-checkbox-4"]/label/span')
                                    b013_box.click()
                                    time.sleep(1) 
                                    break
                                except:
                                    time.sleep(1)
                                    print('Checking Box')
                            while True:
                                try:
                                    b013_box = driver.find_element(By.XPATH,'//*[@id="mat-dialog-3"]/app-workflow-dialog/app-smooth-height/div/div/div/app-suggestions/form/mat-dialog-actions/button[1]')
                                    b013_box.click()
                                    break
                                except:
                                    time.sleep(1)
                                    print('Clicking Use Address')
                                    
                            break
                        except:
                            time.sleep(1)
        
        
            #Type BIC Code
            while True:
                try:
                    b14_box = driver.find_element(By.XPATH,'//*[@id="interview-bank-bic"]')
                    b14_box.send_keys(d[16])
                    break
                except:
                    time.sleep(2)
                    print('Trying to Type BIC code')
            
            
            
            #Click Add Bank Button
            while True:
                try:
                    time.sleep(1)
                    add_but = driver.find_element(By.XPATH,'//*[@id="super-comp-3"]/app-bank-account-form/div/form/div[3]/div/div[1]/button')
                    add_but.click()
                    break
                except:
                    time.sleep(1)

            time.sleep(5)
            
            tax_button_invisible = True
            while tax_button_invisible:
                
                try:
                    #Press Tax Information
                    tax_but = driver.find_element(By.XPATH,'//*[@id="argon-tax-interview-button"]')
                    tax_but.click()
                    tax_button_invisible=False
                    break
                except:
                    time.sleep(1)

            try:
                time.sleep(3)
                unsaved_but = driver.find_element(By.XPATH,'//*[@id="unsaved-changes-save-button"]')
                unsaved_but.click()
            except:
                pass


        wait = WebDriverWait(driver, 120)
        wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")

        started_nonus=False
        while not started_nonus:
            try:
                #Click Non Us
                wait13 = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="toggleButtonId_IsUSPersonIndividual_false"]/span/input')))
                nonus_but = driver.find_element(By.XPATH,'//*[@id="toggleButtonId_IsUSPersonIndividual_false"]/span/input')
                nonus_but.click()
                started_nonus = True
                break
            except:
                time.sleep(1)
            

        #Click agent no
        agent_but = driver.find_element(By.XPATH,'//*[@id="toggleButtonId_IsIntermediaryAgent_false"]/span/input')
        agent_but.click()


        #choose country
        c = driver.find_element(By.XPATH,'//*[@id="a-autoid-12-announce"]')
        c.click()
        dropdown = driver.find_element(By.CLASS_NAME,'a-popover-inner')
        print( d[4].title().replace('And','and'))
        print( d[4].title().replace('And','-').replace(' ',''))
        
        try:
            country = dropdown.find_element(By.LINK_TEXT,d[4].title().replace('And','and'))
        except:
            try:
                country = dropdown.find_element(By.LINK_TEXT,d[4].title().replace('And','-').replace(' ',''))
            except:
                
                country = dropdown.find_element(By.LINK_TEXT,d[4].title())
                
        country.click()
        

        time.sleep(1)
        #uncheck I have TIN number
        notin_but = driver.find_element(By.XPATH,'//*[@id="checkBoxDiv_NonUSHasForeignTINVisible"]/span/div/label/span/span')
        notin_but.click()

        time.sleep(1)
        #Check my country has no TIN
        notincont = driver.find_element(By.XPATH,'//*[@id="radioButtonVerticalDiv_NoTINProvidedReason"]/div[1]/label/i')
        notincont.click()

        #click continue
        time.sleep(1)
        cont = driver.find_element(By.XPATH,'//*[@id="a-autoid-22-announce"]')
        cont.click()


        #click save and preview

        time.sleep(1)
        cont = driver.find_element(By.XPATH,'//*[@id="a-autoid-86-announce"]')
        cont.click()
        counter2=0
        while True:
            try:
                check_sign = driver.find_element(By.XPATH,'//*[@id="checkBoxDiv_SignatureCapacityForIndividualW8Ben"]/span/div/label/i')
                valid_address_passed = True
                print('Valid Address')
                break
                
            except:
                try:
                    address_Valid = driver.find_element(By.XPATH,'//*[@id="checkBoxDiv_NonUSPermAddressOverride"]/span/div/label/span/span')
                    valid_address_passed = False
                    break
                except:
                    time.sleep(2)
                    print('Waiting Page')       
                    counter2+=1
                    print(f'Trial {counter2}/60 , will abort on 60')
                    if counter2==60:
                        ex=1
                        break
        if ex==1:
            raise SystemExit('Stopped due to an intrruption') 
        
        if not valid_address_passed:
            try:
                #Try to click address valid if it's shown
                address_Valid = driver.find_element(By.XPATH,'//*[@id="checkBoxDiv_NonUSPermAddressOverride"]/span/div/label/span/span')
                address_Valid.click()
                time.sleep(1)
                address_Valid = driver.find_element(By.XPATH,'//*[@id="button_NonUSTaxIdentityInformationSectionSaveButton"]/span/span/span/button')
                address_Valid.click()
                time.sleep(1)
                while True:
                    try:
                        cont = driver.find_element(By.XPATH,'//*[@id="button_SaveAndPreviewButtonW8Ben"]/span/span/span/button')
                        cont.click()
                        break
                    except:
                        time.sleep(1)
                        
            except:
                print('Valid Address')

        #signature
        while True:
            try:
                time.sleep(1)
                check_sign = driver.find_element(By.XPATH,'//*[@id="checkBoxDiv_SignatureCapacityForIndividualW8Ben"]/span/div/label/i')
                check_sign.click()
                signature_name = driver.find_element(By.XPATH,'//*[@id="textBoxSingleDiv_ElectronicSignatureW8BenName"]/input')
                signature_name.send_keys(d[5])
                break
            except:
                time.sleep(1)




        try:
            #Click Submit form
            save_preview = driver.find_element(By.XPATH,'//*[@id="button_SubmitButton"]/span/span/span/button')
            save_preview.click()
        except:
            print('Something is wrong with the information review it and try again')
            
        try:
            #Try to click address valid if it's shown
            address_Valid = driver.find_element(By.XPATH,'//*[@id="checkBoxDiv_NonUSPermAddressOverride"]/span/div/label/span/span')
            address_Valid.click()
            
            #click continue
            time.sleep(1)
            cont = driver.find_element(By.XPATH,'//*[@id="a-autoid-22-announce"]')
            cont.click()
            
            #click save and preview

            time.sleep(1)
            cont = driver.find_element(By.XPATH,'//*[@id="a-autoid-86-announce"]')
            cont.click()
            
            #signature
            while True:
                try:
                    time.sleep(1)
                    check_sign = driver.find_element(By.XPATH,'//*[@id="checkBoxDiv_SignatureCapacityForIndividualW8Ben"]/span/div/label/i')
                    check_sign.click()
                    signature_name = driver.find_element(By.XPATH,'//*[@id="textBoxSingleDiv_ElectronicSignatureW8BenName"]/input')
                    signature_name.send_keys(d[5])
                    break
                except:
                    pass

        except:
            print('Valid Address Passed')


        # submit_form_clicked=False
        # while not submit_form_clicked:
        #     try:
        #         time.sleep(4)
        #         wait = WebDriverWait(driver, 120)
        #         wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")

        #         #Click submit form
        #         wait13 = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="button_SubmitButton"]/span/span/span/button')))
        #         sub_form = driver.find_element(By.XPATH,'//*[@id="button_SubmitButton"]/span/span/span/button')
        #         sub_form.click()
        #         submit_form_clicked=True
        #         break
        #     except:
        #         pass

        exit_preview_clicked = False
        while not exit_preview_clicked:
            try:
                time.sleep(4)
                wait = WebDriverWait(driver, 120)
                wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")

                #Exit Interview
                wait13 = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="exit-button-id"]')))
                ex_inter = driver.find_element(By.XPATH,'//*[@id="exit-button-id"]')
                ex_inter.click()
                exit_preview_clicked=True
                break
                
            except:
                time.sleep(1)


        save_and_cont = False
        while not save_and_cont:
            
            try:
                #Save and Continue
                time.sleep(4)
                wait = WebDriverWait(driver, 120)
                wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")
                wait13 = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="payee-save-and-continue-button"]')))
                save_cont = driver.find_element(By.XPATH,'//*[@id="payee-save-and-continue-button"]')
                save_cont.click()
                save_and_cont=True
                break
            except:
                time.sleep(1)

        we_are_in_last_page=False
        while not we_are_in_last_page:
            try:
                #choose industry 
                time.sleep(3)
                wait = WebDriverWait(driver, 120)
                wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")
                dropdown = WebDriverWait(driver, 180).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="industryType-field"]')))
                select = Select(dropdown)
                select.select_by_value("Other")
                we_are_in_last_page=True
                break
            except:
                time.sleep(1)

        #Type org name and additional information
        org_name = driver.find_element(By.XPATH,'//*[@id="orgName-field"]')
        org_name.send_keys(d[5])

        paragraph = driver.find_element(By.XPATH,'//*[@id="additionalInfo-field"]')
        paragraph.send_keys(d[17])

        print(True, '\nMerch Account Created Successfully, Regards/ Dev Gad Badr')
        try:
            self.logTheResult(idd=idd)
        except:
            print("Can't be logged, something bad happened")


        '''''
        This 
        is to
        Certify 
        I'm Gad Badr
        Deveolper and 
        Engineer
        '''''
