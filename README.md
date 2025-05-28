# Suspicious Baggage Detection System

This project implements a real-time suspicious item detection system using YOLOv5 for security screening applications. The system can detect and classify various potentially dangerous items in baggage or security screening images.

## Features

- Real-time object detection using YOLOv5
- Web-based interface using Streamlit
- Detection of multiple suspicious items:
  - Scissors
  - Folding Knives
  - Straight Knives
  - Utility Knives
  - Multitool Knives
- Interactive image upload and analysis
- Visual results with bounding boxes and class labels

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/Suspicious_Baggage_Detection_ECE5554_Final_Project.git
cd Suspicious_Baggage_Detection_ECE5554_Final_Project
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Project Structure

- `app.py`: Main Streamlit application for the web interface
- `best.pt`: Trained YOLOv5 model weights
- `requirements.txt`: Python dependencies
- `Dataset/`: Training and validation dataset
- `runs/`: Directory containing detection results
- `uploads/`: Temporary storage for uploaded images
- `Abhi_Suspicious_Item_Detection_CNN_ECE5554.ipynb`: Jupyter notebook containing model training code

## Usage

1. Start the Streamlit application:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the provided local URL (typically http://localhost:8501)

3. Upload an image using the file uploader

4. The system will process the image and display:
   - The original uploaded image
   - The processed image with detected objects
   - A list of detected suspicious items

## Model Training

The model was trained using YOLOv5 on a custom dataset of suspicious items. The training process and code can be found in the Jupyter notebook `Abhi_Suspicious_Item_Detection_CNN_ECE5554.ipynb`. The training process includes:

- Dataset preparation and augmentation
- Model configuration and hyperparameter tuning
- Training and validation
- Model export and optimization

## Dependencies

- streamlit
- torch
- torchvision
- opencv-python-headless
- matplotlib
- pillow

## Notes

- The system uses YOLOv5, a state-of-the-art object detection model
- The model is optimized for real-time detection
- The web interface is built using Streamlit for easy deployment and use
- Detection results are saved in the `runs/detect` directory

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.