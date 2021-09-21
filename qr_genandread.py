import qrcode
import cv2

data = input("Enter the data to be qr-ised")
qr_filename = 'qrsample.png'
img = qrcode.make(data)
img.save(qr_filename)

img_qr = cv2.imread('qrsample.png')
detector = cv2.QRCodeDetector()
qrdata, bbox, straight_qrcode = detector.detectAndDecode(img_qr)
if bbox is not None:
    print("The Data is:", qrdata)

    n_lines = len(bbox)
    print(bbox)
    for i in range(n_lines):
        point1 = tuple(bbox[i][0])
        point2 = tuple(bbox[(i+1) % n_lines][0])
        cv2.line(img_qr, point1, point2, color=(255, 0, 0), thickness=2)
