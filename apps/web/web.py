# control web pages by pyautogui or sellenium
import os
import webbrowser
import socket
import pyautogui
import time
import pyperclip
items=('MFZ65333701','MFZ65333801','MFZ65914801','MFZ66333001','mfz66236501','MFZ65262201',
        'MFZ66151901','MFZ66236701','MFZ66236702','3920EZ2058A','3920FZ3114C','AGG76599801')
class Connection():
    '''
    in filling 
    standard_spec=True      for print the specification only 
    standard_spec=Flse      for generate false data
    vertically=True        for print in column , Flase for rows
    '''
    def __init__(self):
        self.site_connection()
       # self.past_form()
    def site_connection(self,webSite):
        # Using Chrome to access web
        #import selenium
        #from selenium import webdriver
        #from selenium.webdriver.common.keys import Keys
        
        #print (browser.current_url)

        # Open the website by selenium for control
    
        #driver = webdriver.Chrome('C:\manual_install\chromedriver.exe') 
        #driver.get(self.website)
        #driver.get("http://dmzpuscs.lge.com:6101/com.cer.CER01Login.laf")
        #print("__________________________test____________________________________")
        #print(driver.current_url)        

        
        webbrowser.open(webSite)
        #webbrowser.open("https://www.lgesuppliers.com/index.dev")     
        #elem = driver.find_element_by_css_selector('tr.td partNo')
        #elem.send_keys('a')
        
        #open in specific time in dufing day
        
        #ID=blockeg
        #Password=Blockeg123

    def ip_show(self):
        
        ip=socket.gethostbyname(self.website)
        print(ip)

class AutomatedFilling():
    '''
    in filling 
    standard_spec=True      for print the specification only 
    standard_spec=Flse      for generate false data
    vertically=True        for print in column , Flase for rows
    '''
    def __init__(self):
        self.site_connection()
       # self.past_form()
    
    def past_form(itemSelection,standard_spec=True,vertically=True):
        #self.itemSelection=itemSelection
        from random import randint,seed
        time.sleep(0.007*60)
        
        #lock at the object
        
        #lock at the buttons and text boxes
        #pyautogui.locateOnScreen('main_text01.png')
        #pyautogui.locateOnScreen('submit.png')

        #data for entry
              #"mma" classification
        
        LG_43UJ63="MFZ65333701"
        LG_43UJ63_high=[1049,141,183,187,1049,141,183,161.72]
        LG_43UJ63_low=[1042,136,177,164,1042,136,177,142]
        MFZ65333701=[LG_43UJ63_high,LG_43UJ63_low]

        LG_49UJ63="MFZ65333801"
        LG_49UJ63_high=[1182,147,210,246,1182,147,183,187.42]
        LG_49UJ63_low=[1175,142,204,216,1175,142,177,164.67]
        MFZ65333801=[LG_49UJ63_high,LG_49UJ63_low]

        
        lg_55UK630="MFZ65914801"
        lg_55UK630_high=[1345,160,231,326,1345,160,211,280]
        lg_55UK630_low=[1338,155,227,287,1338,155,207,246]
        MFZ65914801=[lg_55UK630_high,lg_55UK630_low]

        lg_LG32LM55="MFZ66333001"
        lg_LG32LM55_high=[801,131,130,96,801,131,128,88]
        lg_LG32LM55_low=[794,127,124,84,794,127,122,75]
        MFZ66333001=[lg_LG32LM55_high,lg_LG32LM55_low]

        lg_LG43LM63="mfz66236501"
        lg_LG43LM63_high=[1049,141,183,198.14,1049,141,183,161.72]
        lg_LG43LM63_low=[1042,136,177,174.09,1042,136,177,142.09]
        mfz66236501=[lg_LG43LM63_high,lg_LG43LM63_low]

        lg_MFZ65262201="MFZ65262201"
        lg_MFZ65262201_high=[1027,190,18,39.78]
        lg_MFZ65262201_low=[1020,185,14,31.99]
        MFZ65262201=[lg_MFZ65262201_high,lg_MFZ65262201_low]


        lg_MFZ66151901="MFZ66151901"
        lg_MFZ66151901_high=[1019,211,23,49]
        lg_MFZ66151901_low=[1012,206,19,41]
        MFZ66151901=[lg_MFZ66151901_high,lg_MFZ66151901_low]

        lg_MFZ66236701="MFZ66236701"
        lg_MFZ66236701_high=[791.5,175,283,628.68,792,161,283,509]
        lg_MFZ66236701_low=[784.5,170,277,552.37,785,156,277,447]
        MFZ66236701=[lg_MFZ66236701_high,lg_MFZ66236701_low]

        lg_MFZ66236702="MFZ66236702"
        lg_MFZ66236702_high=[421,180,169,203.49]
        lg_MFZ66236702_low=[416,175,164,178.79]
        MFZ66236702=[lg_MFZ66236702_high,lg_MFZ66236702_low]

        lg_LG43UP77="AGG76599801"#LG43UP77
        LG43UP77_high=[1044,131,204,181,1044,131,201,138.16]
        LG43UP77_low=[1037,127,199,159.3,1037,127,196,121.39]
        MFZ67209801=[LG43UP77_high,LG43UP77_low]


        LG65UP775Front="MFZ67225101"#Lg65UP7750PVB
        LG65UP775Front_high=[1555,265,38,110.3]
        LG65UP775Front_low=[154,260,34.5,96.9]
        MFZ67225101=[LG65UP775Front_high,LG65UP775Front_low]

        lg_65UP7750PVB="MFZ67207701"#Lg65UP7750PVB
        lg_65UP7750PVB_high=[1584,157,351,513,1585,157,354,508.7]
        lg_65UP7750PVB_low=[1577,152,345,450.7,1577,152,348,446.9]
        MFZ67207701=[LGlg_65UP7750PVB_high,LGlg_65UP7750PVB_low]

        lg_65UP8140PVA="MFZ66236601"#lg65UP8140PVA
        lg_65UP7750PVB_high=[791.5,192,321,975,178,281,638]
        lg_65UP7750PVB_low=[784.5,316,857,173,276,560]
        MFZ66236601=[LGlg_65UP7750PVB_high,LGlg_65UP7750PVB_low]

        lg_65UP81Side="MFZ67207602"#lg65UP8140PVA
        lg_65UP81Side_high=[]
        lg_65UP81Side_low=[]
        MFZ67207602=[lg_65UP81Side_high,lg_65UP81Side_low]

        lg_75UP77FRONT="MFZ65917901"#lg75up77Front
        lg_75UP77FRONT_high=[]
        lg_75UP77FRONT_low=[]
        MFZ65917901=[lg_75UP77FRONT_high,lg_75UP77FRONT_low]

        lg_75UP77="MFZ67207201"#lg65UP8140PVA
        lg_75UP77_high=[]
        lg_75UP77_low=[]
        MFZ67207201=[lg_75UP77_high,lg_75UP77_low]

        lg_75UP77FRONT="MFZ65917901"#lg75up77Front
        lg_75UP77FRONT_high=[]
        lg_75UP77FRONT_low=[]
        MFZ65917901=[lg_75UP77FRONT_high,lg_75UP77FRONT_low]

        lg_43UP81="MFZ67209701"#lg43UP81
        lg_43UP81_high=[1064,176,246,320.23,1064,176,181,198.14]
        lg_43UP81_low=[1057,171,241,281.36,281.36,171,171,174.09]
        MFZ67209701=[lg_43UP81_high,lg_43UP81_low]

            # "mmf" classification
        LG_cover="3920EZ2058A"# الكفر
        LG_cover_high=[106,71.4,643.5,261.7]
        LG_cover_low=[97,68.6,638.5,258.3]
        LG_3920EZ2058A=[LG_cover_high,LG_cover_low]
        lG_zayaza="3920FZ3114C"#الزوايا=
        lG_zayaza_high=[57.24,185.7,542.5]
        lG_zayaza_low=[50.76,182.3,537.5]
        LG_3920FZ3114C=[lG_zayaza_high,lG_zayaza_low]
        lg_kaeda="AGG76599801"#القاعده
        lg_kaeda_high=[276,640,645,100]
        lg_kaeda_low=[267,637.5,642.5,98.9]
        AGG76599801=[lg_kaeda_high,lg_kaeda_low]


        #second version
        #time recorded for fill     30minint    #the time not accurecy because intenet speed defirince between time to time
        items=(MFZ65333701,MFZ65333801,MFZ65914801,MFZ66333001,mfz66236501,MFZ65262201,
                MFZ66151901,MFZ66236701,MFZ66236702,MFZ67209801,MFZ67225101,
                MFZ67207701,MFZ66236601,MFZ67207602,MFZ65917901,MFZ67207201,MFZ67209701,
                LG_3920EZ2058A,LG_3920FZ3114C,AGG76599801)
        #item=items[0]
        item=items[itemSelection]

        #s=slice(items.lengh(),int(itemSelection))
        #item=items[int(itemSelection)]#type the varibale item______________________________
        
        lg_item=item
        specification_no_high=lg_item[0]
        #specification_no_high=lg_43LH51_high
        specification_no_low=lg_item[1]
        #specification_no_low=lg_43LH51_low
        lg_range=len(specification_no_high)
        s=0
        pyautogui.hotkey('alt', 'tab', interval=0.1)    #for tab to website to write the window must be on website befor bress on fill

        if standard_spec:
            printRange=lg_range
        else:
            printRange=5
        #git id_javascript

        #pyautogui.getWindow("music").maximize()

        #get #partNo (foradding lg pfoduct code)
        for s in range(lg_range):
            #i=1
            for i in range(printRange):
                seed(i)
                #distribution=specification_no_high[s]
                low_value=int(round(specification_no_low[s],0))+1 #approximat to higher value and convert to in
                high_value=int(specification_no_high[s])
                random_value = randint(low_value,high_value)        
                #print(distribution)
                if standard_spec:#for print the standard only
                    distribution=str(lg_item[s][i])
                else:
                    distribution=str(random_value)
                pyautogui.typewrite(distribution)
                if vertically:
                    pyautogui.typewrite(['enter'])  #for write vertically
                else:
                    pyautogui.typewrite(['tab'])
            #for move to next posision
            for i in range(4):
                pyautogui.typewrite(['tab'])
    def pastNames(itemSelection):
        item=items[itemSelection]
        pyautogui.hotkey('alt', 'tab', interval=0.1)    #for tab to website to write the window must be on website befor bress on fill
        pyautogui.typewrite(item)