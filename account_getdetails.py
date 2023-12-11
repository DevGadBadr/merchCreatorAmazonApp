
class Mydata:
    
    def getdata(self):
    
        with open('account_details.txt','r') as g:
            profiles=g.read()

            detials = profiles.split('//')

            a=[]

        for account in detials:

            l=account.split('*')

            m=l[0].split('\n')
            for i in m:
                if len(i) ==0:
                    m.remove(i)
            
            #first section extract
            email = m[0][7:]

            password = m[1][10:]

            secx = m[2][15:].replace(' ','')

            n=l[1].split('\n')

            #second section extract
            date_of_birth = n[1][15:]
            country=n[2][19:]

            full_name = n[3][11:]
            address_line_1 = n[4][15:]
            address_line_2 = n[5][15:]
            city= n[6][6:]
            state=n[7][23:]
            postal_code=n[8][13:]
            phone=n[9][7:]
            business_email=n[10][24:]

            o=l[2].split('\n')

            #third section extract
            bank_location = o[1][15:]
            account_holder_name=o[2][21:]
            iban_number=o[3][13:]
            bic_code=o[4][10:]

            p=l[3].split('\n')

            #fourth section extraction
            paragraph=p[1]

            account_details_list = [email,password,secx,date_of_birth,country,full_name,address_line_1,address_line_2,city,state,
                                postal_code,phone,business_email,bank_location,account_holder_name,iban_number,
                                bic_code,paragraph]
            
            a.append(account_details_list)
            
        return a
            



