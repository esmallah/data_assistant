# control web pages by pyautogui or sellenium
import webbrowser
import socket
import pyautogui
import time

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
        self.past_form()
                
    def past_form(itemSelection,standard_spec=True,vertically=True,insert_name=True,fill_data=True):
        #self.itemSelection=itemSelection
        from random import randint
        time.sleep(0.007*60)
        
        #lock at the object
        
        #lock at the buttons and text boxes
        #pyautogui.locateOnScreen('main_text01.png')
        #pyautogui.locateOnScreen('submit.png')

        #data for entry
              #"mma" classification
        
        LG43UJ63="MFZ65333701"
        LG43UJ63_high=[1049,141,183,187,1049,141,183,161.72]
        LG43UJ63_low=[1042,136,177,164,1042,136,177,142]
        MFZ65333701=[LG43UJ63_high,LG43UJ63_low]

        LG49UJ63="MFZ65333801"
        LG49UJ63_high=[1182,147,210,246,1182,147,183,187.42]
        LG49UJ63_low=[1175,142,204,216,1175,142,177,164.67]
        MFZ65333801=[LG49UJ63_high,LG49UJ63_low]

        
        LG55UK630="MFZ65914801"
        LG55UK630_high=[1345,160,231,326,1345,160,211,280]
        LG55UK630_low=[1338,155,227,287,1338,155,207,246]
        MFZ65914801=[LG55UK630_high,LG55UK630_low]

        LGLG32LM55="MFZ66333001"
        LGLG32LM55_high=[801,131,130,96,801,131,128,88]
        LGLG32LM55_low=[794,127,124,84,794,127,122,75]
        MFZ66333001=[LGLG32LM55_high,LGLG32LM55_low]

        LGLG43LM63="mfz66236501"
        LGLG43LM63_high=[1049,141,183,198.14,1049,141,183,161.72]
        LGLG43LM63_low=[1042,136,177,174.09,1042,136,177,142.09]
        mfz66236501=[LGLG43LM63_high,LGLG43LM63_low]

        lg_43LM63FRONT ="MFZ66151901"#FRONT 43LM63

        lg_MFZ65262201_high=[1027,190,18,39.78]
        lg_MFZ65262201_low=[1020,185,14,31.99]
        MFZ66151901=[lg_MFZ65262201_high,lg_MFZ65262201_low]


        lg_43LM55FRONT="MFZ65262201"#FRONT 43LM5
        lg_MFZ66151901_high=[1019,211,23,49]
        lg_MFZ66151901_low=[1012,206,19,41]
        MFZ65262201=[lg_MFZ66151901_high,lg_MFZ66151901_low]

        LG65UM73up="MFZ66236701"#LG65UM73up&down
        LG65UM73up_high=[791.5,175,283,628.68,792,161,283,509]
        LG65UM73up_low=[784.5,170,277,552.37,785,156,277,447]
        MFZ66236701=[LG65UM73up_high,LG65UM73up_low]

        LG65UM73LR="MFZ66236702"#LG65UM73LR
        LG65UM73LR_high=[421,180,169,203.49]
        LG65UM73LR_low=[416,175,164,178.79]
        MFZ66236702=[LG65UM73LR_high,LG65UM73LR_low]

        LG43UP77="MFZ67209801"#LG43UP77
        LG43UP77_high=[1044,131,204,181,1044,131,201,138.16]
        LG43UP77_low=[1037,127,199,159.3,1037,127,196,121.39]
        MFZ67209801=[LG43UP77_high,LG43UP77_low]


        LG65UP775Front="MFZ67225101"#Lg65UP77_front
        LG65UP775Front_high=[1555,247,38,110.3]
        LG65UP775Front_low=[1547,241,34.5,96.9]
        MFZ67225101=[LG65UP775Front_high,LG65UP775Front_low]

        LG65UP77set="MFZ67207701"#Lg65UP77_set
        LG65UP77set_high=[1584,157,351,513,1585,143,354,508.7]
        LG65UP77set_low=[1577,152,345,450.7,1577,139,348,446.9]
        MFZ67207701=[LG65UP77set_high,LG65UP77set_low]

        LG65UP81set="MFZ67207601"#lg65UP81set       #last modification in 9/6/2021
        LG65UP81set_high=[1585,213,351,1001.3,1585,199,356,662.949]
        LG65UP81set_low=[1577,208,345,879.8,1577,195,350,582.479]
        MFZ67207601=[LG65UP81set_high,LG65UP81set_low]

        LG65UP81Side="MFZ67207602"#lg65UP81sides
        LG65UP81Side_high=[251,207,133,131.9]
        LG65UP81Side_low=[246,202,129,115.9]
        MFZ67207602=[LG65UP81Side_high,LG65UP81Side_low]

        LG75UP77FRONT="MFZ65917901"#lg75up77Front
        LG75UP77FRONT_high=[1308,529,62.73,322.37]
        LG75UP77FRONT_low=[1301,524,58.73,283.24]
        MFZ65917901=[LG75UP77FRONT_high,LG75UP77FRONT_low]

        LG75UP77Set="MFZ67207201"#lg65UP8140PVA
        LG75UP77Set_high=[902,185,281,688.6,902,171,281,666.1]
        LG75UP77Set_low=[895,180,276,605.6,895,166,276,585.3]
        MFZ67207201=[LG75UP77Set_high,LG75UP77Set_low]
        
        LG75UP77Side="MFZ67207202"#lg65UP8140PVA
        LG75UP77Side_high=[536,179,187.5,147.8]
        LG75UP77Side_low=[530,174,183.5,129.8]
        MFZ67207202=[LG75UP77Side_high,LG75UP77Side_low]

        LG43UP81="MFZ67209701"#lg43UP81
        LG43UP81_high=[1064,176,246,320.23,1064,176,181,198.14]
        LG43UP81_low=[1057,171,241,281.36,1057,171,176,174.09]
        MFZ67209701=[LG43UP81_high,LG43UP81_low]

        LGNano80set="MFZ67212201"#LGNano80set

        LGNano80set_high=[1585,157,351,650,1585,143,354,520.51	]
        LGNano80set_low=[1577,152,345,492,1577,139,348,457.33]
        MFZ67212201=[LGNano80set_high,LGNano80set_low]

        LGNano80side="MFZ67212202"#LGNano80side
        LGNano80side_high=[251.8,151,133,111.38]
        LGNano80side_low=[246.8,147,129,97.86]
        MFZ67212202=[LGNano80side_high,LGNano80side_low]

        LGOLED65A26LA_set="MFZ67319401"#LGNano80side
        LGOLED65A26LA_set_high=[1584,156,283,717.57	,1584,142,274,621.18]
        LGOLED65A26LA_set_low=[1578,154,280,630.47,1578,140,271,545.78]
        MFZ67319401=[LGOLED65A26LA_set_high,LGOLED65A26LA_set_low]

        OLED65A26LAside="MFZ67319402"#LGNano80side
        OLED65A26LAside_high=[373.8	,150,260,359.85	]
        OLED65A26LAside_low=[369.8,146,257,316.17]
        MFZ67319402=[OLED65A26LAside_high,OLED65A26LAside_low]

        lg70UQ980updown="MFZ67207501"#LGNano80side
        lg70UQ980updown_high=[841.5,171,280,605.11,841.5,157,280,563.346]
        lg70UQ980updown_low=[836.5,168,277,531.66,836.5,154,277,494.966]
        MFZ67207501=[lg70UQ980updown_high,lg70UQ980updown_low]

        lg70UQ980sides="MFZ67207502"#LGNano80side
        lg70UQ980sides_high=[491,165,160,220.62	]
        lg70UQ980sides_low=[486,162,157,193.84]
        MFZ67207502=[lg70UQ980sides_high,lg70UQ980sides_low]

        #OLED65CS
        lg_OLED65CS_set="mfz66237401"#OLED65CS
        lg_OLED65CS_set_high=[877.1,192,223,759.33,784.6,178,306,805.39]
        lg_OLED65CS_set_low=[870.1,187,219,667.16,777.6,173,301,707.63]
        mfz66237401=[lg_OLED65CS_set_high,lg_OLED65CS_set_low]

        #lg_OLED65CS_set
        
        lg_OLED65CS_sides="mfz66237402"#LGNano80side
        lg_OLED65CS_sides_high=[383.2,185.8,165,213.12]
        lg_OLED65CS_sides_low=[378.2,180.8,159,187.25]
        mfz66237402=[lg_OLED65CS_sides_high,lg_OLED65CS_sides_low]

        #OLED55CS
        #mma
        #set
        #
        OLED55CS_set="mfz66237601"#OLED55CS_set
        OLED55CS_set_high=[1330,192,265,627.84,1330,177,244,499.22]
        OLED55CS_set_low=[1323,187,260,552.96,1323,174,239,439.68]
        mfz66237601=[OLED55CS_set_high,OLED55CS_set_low]

        #side
        #mfz66237602
        OLED55CS_side="mfz66237602"#OLED55CS_side
        OLED55CS_side_high=[283,186,117,151.51]
        OLED55CS_side_low=[280,182,117,133.44]
        mfz66237602=[OLED55CS_side_high,OLED55CS_side_low]
            # "mmf" classification
        LG_cover="3920EZ2058A"# LGwasher machine cover
        LG_cover_high=[106,71.4,643.5,261.7]
        LG_cover_low=[97,68.6,638.5,258.3]
        LG_3920EZ2058A=[LG_cover_high,LG_cover_low]
        lG_angels="3920FZ3114C"#LGwasher machine-angels=
        lG_angels_high=[57.24,185.7,542.5]
        lG_angels_low=[50.76,182.3,537.5]
        LG_3920FZ3114C=[lG_angels_high,lG_angels_low]
        lg_kaeda="AGG76599801"#LGwasher machine-base
        lg_kaeda_high=[276,640,100,645]
        lg_kaeda_low=[267,637.5,98.9,642.5]
        AGG76599801=[lg_kaeda_high,lg_kaeda_low]

        lg_base_VIV="AGG76599802"#LGwasher machine base VIVACHE
        lg_base_VIV_h=[294,642.5,101.4,647.5]
        lg_base_VIV_l=[266,637.5,98.6,642.5]
        AGG76599802=[lg_base_VIV_h,lg_base_VIV_l]

        lg_slides_50UQ75="MFZ67452601"#LGwasher machine base VIVACHE
        lg_slides_50UQ75_h=[1164.00,312,196,162,127.5,206,24]
        lg_slides_50UQ75_l=[1156,308,194,158,112.03,204,22]
        MFZ67452601=[lg_slides_50UQ75_h,lg_slides_50UQ75_l]
        
        #second version
        #time recorded for fill     30minint    #the time not accurecy because intenet speed defirince between time to time
        
        
        
        #s=slice(items.lengh(),int(itemSelection))
        #item=items[int(itemSelection)]#type the varibale item______________________________
        if fill_data:
            items=[MFZ65333701,MFZ65333801,MFZ65914801,MFZ66333001,mfz66236501,MFZ65262201,
                MFZ66151901,MFZ66236701,MFZ66236702,MFZ67209801,MFZ67225101,
                MFZ67207701,MFZ67207601,MFZ67207602,MFZ65917901,MFZ67207201,MFZ67207202,MFZ67209701,
                MFZ67212201,MFZ67212202,MFZ67319401,MFZ67319402,MFZ67207501,MFZ67207502,mfz66237401,mfz66237402,mfz66237601,mfz66237602,
                LG_3920EZ2058A,LG_3920FZ3114C,AGG76599801,AGG76599802,MFZ67452601]
            
            item=items[itemSelection]
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
                for i in range(3):
                    pyautogui.typewrite(['tab'])
        if insert_name:
            items=[LG43UJ63,LG49UJ63,LG55UK630,LGLG32LM55,LGLG43LM63,lg_43LM63FRONT,lg_43LM55FRONT,
                    LG65UM73up,LG65UM73LR,LG43UP77,LG65UP775Front,LG65UP77set,LG65UP81set,
                    LG65UP81Side,LG75UP77FRONT,LG75UP77Set,LG75UP77Side,LG43UP81,
                    LGNano80set,LGNano80side,LGOLED65A26LA_set,OLED65A26LAside,lg70UQ980updown,lg70UQ980sides
                    ,lg_OLED65CS_set,lg_OLED65CS_sides,OLED55CS_set,OLED55CS_side
                    ,LG_cover,lG_angels,lg_kaeda,lg_base_VIV,lg_slides_50UQ75]
            
            item=items[itemSelection]
            print(item)
            pyautogui.hotkey('alt', 'tab', interval=0.1)    #for tab to website to write the window must be on website befor bress on fill
            pyautogui.typewrite(str(item))