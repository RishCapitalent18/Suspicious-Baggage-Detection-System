import streamlit as st
import torch
from pathlib import Path
import pathlib
import time  

pathlib.PosixPath = pathlib.WindowsPath

# Class labels mapping
CLASS_LABELS = {
    0: "Scissors",
    1: "Folding Knife",
    2: "Straight Knife",
    3: "Utility Knife",
    4: "Multitool Knife"
}

# Load YOLO model with caching
@st.cache_resource
def load_model(weights_path):
    with st.spinner("🔄 Loading model..."):
        time.sleep(1)  # Simulate a loading animation
        model = torch.hub.load('ultralytics/yolov5', 'custom', path=weights_path, force_reload=True)
    return model

# Detection function
def detect_objects(model, img_path):
    results = model(img_path)
    results.save()  # YOLOv5 automatically saves in runs/detect/exp*
    return results

# Streamlit app
def main():
    # Page Configuration
    st.set_page_config(page_title="Suspicious Item Detection and Classification", layout="wide", initial_sidebar_state="expanded")

    # Main Title and Description
    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Suspicious Item Detection and Classification</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align: center;'>Upload an image to detect and classify objects!</p>",
        unsafe_allow_html=True,
    )

    # File Uploader
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Save uploaded image
        upload_path = Path("uploads")
        upload_path.mkdir(exist_ok=True)
        img_path = upload_path / uploaded_file.name
        with open(img_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Display an upload animation
        with st.spinner("🔄 Uploading image..."):
            time.sleep(2)

        # Display side-by-side images
        col1, col2 = st.columns(2)

        # Column 1: Uploaded Image
        with col1:
            st.image(str(img_path), caption="Uploaded Image", use_container_width=True)

        # Load Model and Perform Detection
        model_path = "best.pt"  # Path to your YOLOv5 weights
        with st.spinner("🔄 Running YOLOv5, please wait..."):
            model = load_model(model_path)
            results = detect_objects(model, str(img_path))

        # Column 2: Detected Image
        with col2:
            detect_path = Path("runs/detect")
            latest_exp = sorted(detect_path.glob("exp*"))[-1]  # Get the most recent `exp` folder

            # Dynamically locate the result image in the latest experiment folder
            result_files = list(latest_exp.glob("*.jpg"))  # Find all .jpg files in the folder
            if result_files:
                result_image = result_files[0]  # Use the first detected result image
                st.image(str(result_image), caption="Detected Objects", use_container_width=True)
            else:
                st.error("Result image not found. Please check the YOLO output.")

        # Display detected classes below images
        detected_classes = results.pandas().xyxy[0]['class'].unique().tolist()
        st.markdown("### Detected Classes:")
        if detected_classes:
            for cls in detected_classes:
                label = CLASS_LABELS.get(cls, "Unknown")
                st.markdown(f"- **{cls} - {label}**")
        else:
            st.warning("No objects detected.")

# Entry Point
if __name__ == "__main__":
    main()
