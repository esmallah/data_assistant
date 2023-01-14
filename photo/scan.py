from PIL import Image
import pytesseract
import os
import openpyxl as xl
from pytesseract import Output
from pytesseract import pytesseract as pt
import numpy as np
        
from matplotlib import pyplot as plt

import cv2
from imutils.object_detection import non_max_suppression

class Scan():
    def __init__(self,folder,readfile,writefile):
        self.folder=folder
        self.readfile=readfile
        self.writefile=writefile
                
    def text_en(self):
        os.chdir(self.folder)
        img = Image.open(self.readfile)
        im.load()
        text = pytesseract.image_to_string(im,lang='eng')
        print(text)
        text.save(self.writefile)
    def text_ar(self):
        os.chdir(self.folder)
        img = Image.open(self.readfile)
        img.load()
        text = pytesseract.image_to_string(im,lang='ara')
        print(text)
        wb2 = xl.load_workbook(self.writefile)
        ws2 = wb2.get_sheet_by_name("Sheet1") 
        for row in ws2:
            for cell in row:
                ws2[cell.coordinate].value = text
        wb2.save(self.writefile)
    def pdf_extract_table(self):
        import camelot
        os.chdir(self.folder)
        #table file must be pdf file
        tables = camelot.read_pdf(self.readfile)

        #TableList 
        #self.writefile must be csv file
        n=1
        tables.export(self.writefile, f='csv', compress=True) # json, excel, html,csv
        tables[1]
        Table_shape=(7, 7)
        tables[1].parsing_report
        {
            'accuracy': 99.02,
            'whitespace': 12.24,
            'order': 1,
            'page': 1}
        tables[1].to_csv(self.writefile) # to_json, to_excel, to_html,to_csv


    def boxes(self):
        os.chdir(self.folder)
            # read the image and get the dimensions
        img = cv2.imread(self.readfile)

        h, w, _ = img.shape # assumes color image

        # run tesseract, returning the bounding boxes
        boxes = pytesseract.image_to_boxes(img) # also include any config options you use

    # draw the bounding boxes on the image
        for b in boxes.splitlines():
            b = b.split(' ')
            img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)
        cv2.imshow('img', img)
        cv2.waitKey(0)
        
    def all_boxes(self):
        os.chdir(self.folder)
            # read the image and get the dimensions
        img = cv2.imread(self.readfile)

        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        contours,hierarchy = cv2.findContours(gray,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
        idx =0 
        for cnt in contours:
            idx += 1
            x,y,w,h = cv2.boundingRect(cnt)
            roi=img[y:y+h,x:x+w]
            cv2.imwrite(str(idx) + '.jpg', roi)
            #cv2.rectangle(im,(x,y),(x+w,y+h),(200,0,0),2)
        cv2.imshow('img',img)
        cv2.waitKey(0)    

    def select_box(self):
        '''this function is very useful for corp images then press ctrl+c the past it in iny place by ctrl+v'''
        os.chdir(self.folder)
            # read the image and get the dimensions
        
        # Read image
        
        img = cv2.imread(self.readfile)
        # Select ROI
        showCrosshair = False   #to hide the rectangle selection line when select
        fromCenter = True      # true for corss line # false for triangle
        r = cv2.selectROI('image',img, fromCenter, showCrosshair)       #to select from center
        
        
        # Crop image
        imCrop = img[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
    
        # Display cropped image
        cv2.imshow("Image", imCrop)
        cv2.waitKey(0)
    def hand_writing_digit(self):
        os.chdir(self.folder)
            #by knn technices
        img = cv2.imread(self.readfile)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        # Now we split the image to 5000 cells, each 20x20 size
        cells = [np.hsplit(row,100) for row in np.vsplit(gray,50)]

        # Make it into a Numpy array. It size will be (50,100,20,20)
        x = np.array(cells)

        # Now we prepare train_data and test_data.
        train = x[:,:50].reshape(-1,400).astype(np.float32) # Size = (2500,400)
        test = x[:,50:100].reshape(-1,400).astype(np.float32) # Size = (2500,400)

        # Create labels for train and test data
        k = np.arange(10)
        train_labels = np.repeat(k,250)[:,np.newaxis]
        test_labels = train_labels.copy()

        # Initiate kNN, train the data, then test it with test data for k=1
        knn = cv2.KNearest()
        knn.train(train,train_labels)
        ret,result,neighbours,dist = knn.find_nearest(test,k=5)

        # Now we check the accuracy of classification
        # For that, compare the result with test_labels and check which are wrong
        matches = result==test_labels
        correct = np.count_nonzero(matches)
        accuracy = correct*100.0/result.size
        print (accuracy)
        # save the data
        np.savez('knn_data.npz',train=train, train_labels=train_labels)

        # Now load the data
        with np.load('knn_data.npz') as data:
            print (data.files)
            train = data['train']
            train_labels = data['train_labels']
    def line_detection(self):
        #Reading the required image in  
        # which operations are to be done.  
        # Make sure that the image is in the same  
        # directory in which this python program is 
        os.chdir(self.folder)
            #by knn technices
        img = cv2.imread(self.readfile)
                
        # Convert the img to grayscale 
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
        
        # Apply edge detection method on the image 
        edges = cv2.Canny(gray,50,150,apertureSize = 3) 
        
        # This returns an array of r and theta values 
        lines = cv2.HoughLines(edges,1,np.pi/180, 200) 
        
        # The below for loop runs till r and theta values  
        # are in the range of the 2d array 
        for r,theta in lines[0]: 
            
            # Stores the value of cos(theta) in a 
            a = np.cos(theta) 
        
            # Stores the value of sin(theta) in b 
            b = np.sin(theta) 
            
            # x0 stores the value rcos(theta) 
            x0 = a*r 
            
            # y0 stores the value rsin(theta) 
            y0 = b*r 
            
            # x1 stores the rounded off value of (rcos(theta)-1000sin(theta)) 
            x1 = int(x0 + 1000*(-b)) 
            
            # y1 stores the rounded off value of (rsin(theta)+1000cos(theta)) 
            y1 = int(y0 + 1000*(a)) 
        
            # x2 stores the rounded off value of (rcos(theta)+1000sin(theta)) 
            x2 = int(x0 - 1000*(-b)) 
            
            # y2 stores the rounded off value of (rsin(theta)-1000cos(theta)) 
            y2 = int(y0 - 1000*(a)) 
            
            # cv2.line draws a line in img from the point(x1,y1) to (x2,y2). 
            # (0,0,255) denotes the colour of the line to be  
            #drawn. In this case, it is red.  
            cv2.line(img,(x1,y1), (x2,y2), (0,0,255),2) 
            
        # All the changes made in the input image are finally 
        # written on a new image houghlines.jpg 
        cv2.imwrite('linesDetected.jpg', img) 
        cv2.imshow('img', img)
        cv2.waitKey(0)
    def spilt_cells_of_table(self):
        os.chdir(self.folder)
            #by knn technices
        img = cv2.imread(self.readfile)
 
        # find edges in the image
        edges = cv2.Laplacian(img, cv2.CV_8U)
        # kernel used to remove vetical and small horizontal lines using erosion
        kernel = np.zeros((5, 11), np.uint8)
        kernel[2, :] = 1
        eroded = cv2.morphologyEx(edges, cv2.MORPH_ERODE,
                                kernel)  # erode image to remove unwanted lines

        # find (x,y) position of the horizontal lines
        indices = np.nonzero(eroded)
        # As indices contain all the points along horizontal line, so get unique rows only (indices[0] contains rows or y coordinate)
        rows = np.unique(indices[0])
        # now you have unique rows but edges are more than 1 pixel thick
        # so remove lines which are near to each other using a certain threshold
        filtered_rows = []
        for ii in range(len(rows)):
            if ii == 0:
                filtered_rows.append(rows[ii])
            else:
                if np.abs(rows[ii] - rows[ii - 1]) >= 10:
                    filtered_rows.append(rows[ii])

        print(filtered_rows)
        # crop first row of table
        first_cropped_row = img[filtered_rows[0]:filtered_rows[1], :, :]
        #cv2.resize(img, (960, 540)
        cv2.imshow('Image', eroded)
        cv2.imshow('Cropped_Row', first_cropped_row)
        cv2.waitKey(0)
    