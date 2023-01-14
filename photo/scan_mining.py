import scan
import mining



scan_photo=scan.Scan(r'D:\2work\programing\1stleader\input\data\scan','w1.jpg',"test.xlsx")
table=scan.Scan(r'D:\programing\1stleader\input\data\scan\dts','1-Export-XPS.pdf',"tds.csv")
#for scan text 
#scan_photo.text_ar()
table.pdf_extract_table()



#tests
#scan_photo.hand_writing_digit()
#scan_photo.all_boxes()
#scan_photo.boxes()      #scan boinding box

#scan_photo.line_detection()
#scan_photo.spilt_cells_of_table()
#for scan 

#for select any image by your self
#scan_photo.select_box()

#scan_photo.decode_predictions()

import test
scan_photo_test=test.Scan(r'D:\2work\programing\1stleader\files\scan','test_numbers_en.JPG',"test.xlsx")

#scan_photo_test.text_en()
