import streamlit as st
import requests
from PIL import Image
import io

st.set_page_config(page_title="Human Pose Estimator", layout="wide")

st.title("🏃 Human Pose Estimation App")
st.write("Upload an image to detect human pose landmarks.")

# Sidebar for options
st.sidebar.header("Options")
source_option = st.sidebar.selectbox("Select Input Source", ("Upload Image", "Camera"))

input_image = None

# Handle Image Upload
if source_option == "Upload Image":
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        input_image = uploaded_file.getvalue()
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

# Handle Camera Input
elif source_option == "Camera":
    camera_input = st.camera_input("Take a picture")
    if camera_input is not None:
        input_image = camera_input.getvalue()

# Send to Backend
if input_image is not None:
    if st.button("Estimate Pose"):
        with st.spinner('Processing...'):
            try:
                # Send image to FastAPI backend
                files = {"file": input_image}
                response = requests.post("http://backend:8000/predict", files=files)
                
                if response.status_code == 200:
                    output_image = Image.open(io.BytesIO(response.content))
                    st.success("Pose Detected!")
                    # CHANGED: use_column_width -> use_container_width
                    st.image(output_image, caption="Pose Estimation Result", use_container_width=True)
                else:
                    st.error("Error processing image.")
            except Exception as e:
                st.error(f"Connection Error: {e}")