import server
            #connect server ( server name , latidure  coordinates on earch,longitude coordinate,)

train=server.Connect("http://api.open-notify.org","37.78","-122.41")
qc_server=server.Connect("http://ahmed-rashad:8069",37.78,-122.41)
sm_obour_server=server.Connect("http://safety_egypt:8069",30.013055700000002,31.2088526)
contact=server.Connect("192.168.1.221",37.78,-122.41)
#status
sm_obour_server.status()
#coordinates 
#sm_obour_server.location()
#sm_obour_server.content_type
#sm_obour_server.count_people