🌿 Plant Disease Detection System

![WhatsApp Image 2025-10-29 at 00 43 19_bb151f09](https://github.com/user-attachments/assets/d84b4115-fc09-4e28-aa73-36b46084e818)

🚀 Features

🌿 Upload or capture a leaf image for real-time disease detection

🤖 CNN / Transfer Learning (MobileNetV2 or ResNet50)

⚡ Fast and lightweight inference

📊 Displays disease name and prediction confidence

🧩 Simple, farmer-friendly web interface


🧠 Overview

A Deep Learning–based web app that detects plant diseases from leaf images in seconds using a CNN model trained on the PlantVillage Dataset.
Built with TensorFlow/Keras and Streamlit, it aims to assist farmers and researchers in diagnosing crop diseases quickly and accurately.

🌄 Preview
🖼️ App Interface

![WhatsApp Image 2025-10-29 at 00 43 18_153b08af](https://github.com/user-attachments/assets/5653966e-7827-4505-a513-d77697029c8f)




🌱 Sample Prediction
Input Leaf Image	Model Prediction	Confidence

	Tomato___Late_blight	0.97 ✅


🚀 Features

🌿 Upload or capture a leaf image for real-time disease detection

🤖 CNN / Transfer Learning (MobileNetV2 or ResNet50)

⚡ Fast and lightweight inference

📊 Displays disease name and prediction confidence

🧩 Simple, farmer-friendly web interface

🧠 Overview

Early and accurate plant disease detection helps reduce yield losses and pesticide misuse.
This project leverages AI-driven image classification to automate the diagnosis process — turning smartphones and laptops into plant health scanners.


🗂️ Project Structure
plant-disease-detection-system/
│
├── app.py                 # Web app (Streamlit/Flask)
├── model/                 # Trained model file (.h5 / .pth)
├── dataset/               # Image dataset
├── static/ or templates/  # UI files (for Flask)
├── requirements.txt       # Dependencies
└── README.md              # Documentation


💾 Installation
git clone https://github.com/akshataundhekar23/plant-disease-detection-system.git
cd plant-disease-detection-system
pip install -r requirements.txt

▶️ Run the App

For Streamlit:

streamlit run app.py


For Flask:

python app.py


Then open your browser at http://localhost:8501 or the link shown in the terminal.


🌱 Dataset & Model

Dataset: PlantVillage Dataset (Kaggle)

Classes: Healthy + multiple crop disease types

Model: CNN / Transfer Learning (e.g., MobileNetV2)

Accuracy: 96–98%

Training Details:

Optimizer: Adam

Epochs: 30

Batch Size: 32

📊 Results

✅ Model Accuracy: 96%

🧩 High precision and recall

⚙️ Inference Time: <1s on CPU

🖼️ Supports both upload and live capture


👤 Contributor

Akshat Aundhekar

🏅 Internship Context

This project was created as part of an internship task, demonstrating the use of AI in agricultural health monitoring and automation.

