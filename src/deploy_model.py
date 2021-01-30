from PIL import Image 
from ludwig.api import LudwigModel
import streamlit as st
def deploy_model():
    st.title("Gesture Classification Example \n Author: Arunkumar")
    upload_file= st.file_uploader("Give an image", type="jpg")
    if upload_file is not None:
        image = Image.open(upload_file)
        image.save("../infer/uploaded_image.jpg","JPEG")
        st.image(image,caption="upload_image", use_column_width=True)
        st.write("classifying image...")
        trained_model = LudwigModel.load("results/exp_run/model")
        prediction = trained_model.predict(
            {"image_path": ["D:\programs\python\exampl\hand_recognition/infer/uploaded_image.jpg" ],

            "label":[-1]
            }
        )
        label_identified=str(prediction[0]["label_predictions"].values[0])
        if label_identified=='0':
            st.write("Left")
        if label_identified=='1':
            st.write("Palm")
        if label_identified=='2':
            st.write("Peace")
        if label_identified=='3':
            st.write("Right")
if __name__=="__main__":
    deploy_model()