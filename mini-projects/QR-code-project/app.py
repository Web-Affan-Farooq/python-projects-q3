import qrcode
import streamlit as st
import cv2
import numpy as np

st.title("QR code generator application")

generate_tab_1 , scan_tab_2 = st.tabs(["Generate QR code ", "Scan qr code"])

with generate_tab_1:
    data = st.text_area("Enter link to generate QR code ")
    count = 0
    if st.button("Generate code "):
        qrcode.make(data).save(f"./images/qrcode.png")
        st.image(f"./images/qrcode.png")
        with open("./images/qrcode.png","rb") as f:
            content = f.read()
            st.download_button("Download QR code ",content, mime="image/png")

with scan_tab_2:
    st.subheader("Scan QR code ")
    file = st.file_uploader("Choose image ", type=["png","svg","jpeg","jpg","avif"])
    if file != None:
        img = np.asarray(bytearray(file.read()), dtype=np.uint8)
        image = cv2.imdecode(img,cv2.IMREAD_COLOR)
        detector = cv2.QRCodeDetector()
        converted = detector.detectAndDecode(image)
        # print("Conveted :" , converted)
        st.text_area("Scanned Link ", value=converted[0])
        
        
        
        # img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # st.image(img_rgb)
    # img = cv2.imread(file)
    # st.write(img)
    
# 0346-2803108

# import qrcode  # ___For creating qrcodes 
# import streamlit as st
# from numpy import ndarray
# from PIL import Image
# import base64

# import cv2
# def generate_code_for_file(file):
#     if(file.type == "image/png"):
#         binary = file.read() # converts into binary
#         base64_string = base64.b64encode(binary).decode('utf-8')
#         print(Image(base64_string))
    
# st.title(" QR code generator and decoder app")

# st.write("Enter data to be decoded in QR code ")
# # data = st.text_area("Enter your data ")
# # st.write("Or ")
# file = st.file_uploader("Select file", type=["txt","jpg","jpeg","png","pdf"])
# st.button("Generate ", on_click=generate_code_for_file(file))
# # import cv2

# # img = cv2.imread("./qrcode.png")
# # image_detector = cv2.QRCodeDetector()

# # converted = image_detector.detectAndDecode(img)
# # print("Found link in QR code :  ", converted[0])

# # # qrcode.make("https://www.freecodecamp.org/news/python-projects-for-beginners/#heading-mad-libs-python-project").save("qrcode.png")