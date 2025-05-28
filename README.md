# 🎯 Suspicious Baggage Detection System

A real-time baggage screening solution powered by **YOLOv5**, this project detects and classifies potentially dangerous items in security X-ray or baggage images. Built with a web-friendly UI using **Streamlit**, it’s a tool designed for rapid deployment and intuitive use in real-world scenarios.

---

## 🚀 Features
- 🔍 Real-time object detection with YOLOv5
- 🌐 Web-based interface using Streamlit
- 📦 Multi-class suspicious item detection:
  - Scissors ✂️
  - Folding Knives
  - Straight Knives
  - Utility Knives
  - Multitool Knives
- 🖼️ Interactive image upload and processing
- 🧠 Visual results: bounding boxes + class labels

---

## 🛠️ Installation
1. **Clone the repository**:
```bash
git clone https://github.com/yourusername/Suspicious_Baggage_Detection_ECE5554_Final_Project.git
cd Suspicious_Baggage_Detection_ECE5554_Final_Project
```

2. **Install required dependencies**:
```bash
pip install -r requirements.txt
```

---

## 📁 Project Structure
```
Suspicious_Baggage_Detection_ECE5554_Final_Project/
├── app.py                            # Streamlit app interface
├── best.pt                           # Trained YOLOv5 weights
├── requirements.txt                  # Python dependencies
├── Dataset/                          # Training and validation dataset
├── uploads/                          # Temporary image uploads
├── runs/                             # Detection output
└── Abhi_Suspicious_Item_Detection_CNN_ECE5554.ipynb  # Training notebook
```

---

## 💻 Usage
1. **Launch the application**:
```bash
streamlit run app.py
```
2. Open browser at the local URL (typically `http://localhost:8501`)
3. Upload a baggage scan image
4. View:
   - Original image
   - Annotated image with detections
   - List of detected items

---

## 🧠 Model Training
- Based on YOLOv5 architecture
- Trained on a custom dataset of suspicious items
- See `Abhi_Suspicious_Item_Detection_CNN_ECE5554.ipynb` for:
  - Dataset prep + augmentation
  - Model configuration + tuning
  - Training pipeline
  - Model export

---

## 🧾 Dependencies
- streamlit
- torch
- torchvision
- opencv-python-headless
- matplotlib
- pillow

Install via:
```bash
pip install -r requirements.txt
```

---

## 📌 Notes
- Powered by YOLOv5 (Ultralytics)
- Optimized for fast, accurate predictions
- Frontend via Streamlit = no extra setup needed
- Detection results saved in `runs/detect` for reference

---

## 🤝 Contributing
We welcome contributions! Fork the repo, suggest enhancements, or submit a PR.

---

## 🪪 License
Licensed under the MIT License – see the [LICENSE](LICENSE) file.

---

> 🔒 *Enhancing security through smart, accessible AI.*
