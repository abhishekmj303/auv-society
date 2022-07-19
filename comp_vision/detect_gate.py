import cv2

capture = cv2.VideoCapture("6.m4v")

while True:
    # reading frame by frame from the video
    ret, gate = capture.read()
    if ret == False:
        break
    
    # threshold and grayscale the image to get only red color gates
    gate_thresh1 = cv2.threshold(gate, 106, 255, cv2.THRESH_BINARY)[1]
    gate_gray1 = cv2.cvtColor(gate_thresh1, cv2.COLOR_BGR2GRAY)
    gate_thresh2 = cv2.threshold(gate_gray1, 127, 255, cv2.THRESH_BINARY_INV)[1]

    #extracting the contours of the object
    contours,_ = cv2.findContours(gate_thresh2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #sorting the contour based of area
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    
    if len(contours) >= 2:
        #if contours are found we take the 2 biggest contour and get bounding box
        (x1_min, y1_min, box1_width, box1_height) = cv2.boundingRect(contours[0])
        (x2_min, y2_min, box2_width, box2_height) = cv2.boundingRect(contours[1])
        #drawing a rectangle around the object with 15 as margin
        cv2.rectangle(gate, (x1_min - 15, y1_min -15),
                      (x1_min + box1_width + 15, y1_min + box1_height + 15),
                      (0,255,0), 4)
        
        cv2.rectangle(gate, (x2_min - 15, y2_min -15),
                      (x2_min + box2_width + 15, y2_min + box2_height + 15),
                      (0,255,0), 4)


    # show the video with the bounding box
    cv2.imshow("Video", gate)
    
    # checking if q key is pressed to break out of loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()

cv2.destroyAllWindows()