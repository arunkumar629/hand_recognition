from PIL import Image 
from ludwig.api import LudwigModel
import streamlit as st
def deploy_model():
    st.title("Gesture classification example")
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
        st.write(str(prediction[0]["label_predictions"].values[0]))
if __name__=="__main__":
    deploy_model()