import streamlit as st
import tensorflow as tf
import numpy as np

# --- Custom Glassmorphism CSS ---
st.markdown("""
    <style>
    /* General page setup */
    .stApp {
        background: linear-gradient(135deg, #a7d995, #e0f2f1, #c8e6c9);
        font-family: 'Poppins', sans-serif;
        color: #000000 !important; /* <-- CHANGED: Set default text to black */
    }

    /* Remove default white header gap */
    div.block-container {
        padding-top: 1rem !important;
    }

    /* Sidebar background and structure */
    [data-testid="stSidebar"] {
        background: rgba(255, 255, 255, 0.35);
        backdrop-filter: blur(12px);
        border-right: 1px solid rgba(255, 255, 255, 0.3);
        padding-top: 30px !important;
    }

    /* Target the button's *container* to force its width */
    [data-testid="stSidebar"] [data-testid="stButton"] {
        width: 100% !important;
        margin-bottom: 12px !important; 
    }

    /* Target the button *itself* */
    [data-testid="stSidebar"] [data-testid="stButton"] button {
        width: 100% !important;
        height: 45px !important;
        min-height: 45px !important;
        max-height: 45px !important;
        display: block !important;
        border-radius: 8px !important;
        background-color: rgba(255, 255, 255, 0.4) !important;
        border: 1px solid rgba(255, 255, 255, 0.3) !important;
        color: #000000 !important; /* <-- CHANGED: Button text to black */
        font-weight: 500 !important;
        transition: all 0.3s ease !important;
        text-align: center !important;
    }

    /* Force override Streamlit's default "primary" button style */
    [data-testid="stSidebar"] [data-testid="stButton"] button[kind="primary"] {
        background-color: rgba(255, 255, 255, 0.4) !important;
        border: 1px solid rgba(255, 255, 255, 0.3) !important;
        color: #000000 !important; /* <-- CHANGED: Button text to black */
    }

    /* Hover for *any* button (keeps green background, black text) */
    [data-testid="stSidebar"] [data-testid="stButton"] button:hover {
        background-color: rgba(85, 139, 47, 0.2) !important; 
        color: #000000 !important; /* <-- CHANGED: Hover text to black */
    }
    
    /* This active-button class (added by JS) is our main override */
    .active-button {
        background-color: rgba(85, 139, 47, 0.3) !important; 
        color: #000000 !important; /* <-- CHANGED: Active text to black */
        font-weight: 600 !important;
        border: 1px solid rgba(85, 139, 47, 0.4) !important;
    }

    /* Ensure active button *doesn't* change on hover */
    .active-button:hover {
        background-color: rgba(85, 139, 47, 0.3) !important; 
        color: #000000 !important; /* <-- CHANGED: Active text to black */
    }

    /* Glass panel for content */
    .glass-panel {
        background: rgba(255, 255, 255, 0.55);
        backdrop-filter: blur(10px);
        border-radius: 18px;
        padding: 30px 35px;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.05);
        margin-top: 10px;
    }

    /* Prediction result box */
    .result-box {
        background: rgba(255, 255, 255, 0.6);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(0,0,0,0.05);
        border-radius: 12px;
        padding: 18px;
        margin-top: 15px;
        text-align: left; /* <-- CHANGED: From center to left */
        font-weight: 600;
        color: #000000; /* <-- CHANGED: Result text to black */
        font-size: 18px;
    }

    h1, h2, h3 {
        color: #000000; /* <-- CHANGED: Headings to black */
    }

    p {
        color: #000000 !important; /* <-- CHANGED: Paragraphs to black */
    }
    </style>
""", unsafe_allow_html=True)


# --- TensorFlow Model Prediction ---
def model_prediction(test_image):
    model = tf.keras.models.load_model("trained_plant_disease_model.keras")
    image = tf.keras.preprocessing.image.load_img(test_image, target_size=(128, 128))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr])  # convert single image to batch
    predictions = model.predict(input_arr)
    return np.argmax(predictions)


# --- Sidebar Navigation ---
st.sidebar.title("Navigation")

if "page" not in st.session_state:
    st.session_state.page = "Home"

# Sidebar Buttons
home_btn = st.sidebar.button("Home")
about_btn = st.sidebar.button("About")
disease_btn = st.sidebar.button("Disease Recognition")

if home_btn:
    st.session_state.page = "Home"
elif about_btn:
    st.session_state.page = "About"
elif disease_btn:
    st.session_state.page = "Disease Recognition"

app_mode = st.session_state.page

# Highlight active button dynamically using JS injection
st.sidebar.markdown(f"""
    <script>
    var buttons = window.parent.document.querySelectorAll('[data-testid="stSidebar"] [data-testid="stButton"] button');
    buttons.forEach(btn => btn.classList.remove('active-button'));
    
    if ('{app_mode}' === 'Home') {{
        buttons[0].classList.add('active-button');
    }}
    if ('{app_mode}' === 'About') {{
        buttons[1].classList.add('active-button');
    }}
    if ('{app_mode}' === 'Disease Recognition') {{
        buttons[2].classList.add('active-button');
    }}
    </script>
""", unsafe_allow_html=True)


# --- HOME PAGE ---
if app_mode == "Home":
    st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
    st.header("Plant Disease Recognition System")
    st.image("home_page.jpeg", use_container_width=True)
    st.markdown("""
    Welcome to the **Plant Disease Recognition System**.

    Our goal is to assist farmers and researchers in quickly identifying plant diseases.  
    Upload a plant leaf image, and our AI model will analyze and classify it for you.

    ### How It Works
    1. Upload an image on the **Disease Recognition** page.
    2. The system processes it using deep learning.
    3. You receive the predicted disease instantly.

    ### Key Features
    - Accurate plant disease detection.
    - Simple and responsive design.
    - Fast predictions and clean UI.
    """)
    st.markdown('</div>', unsafe_allow_html=True)


# --- ABOUT PAGE ---
elif app_mode == "About":
    st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
    st.header("About the Project")
    st.markdown("""
    #### Dataset Overview
    The dataset is adapted from the **PlantVillage dataset** and enhanced using offline augmentation.

    - **Total images:** ~87,000  
    - **Categories:** 38 different plant and disease classes  
    - **Split:** 80% training, 20% validation, with an additional test set  

    The model has been trained on this dataset to achieve reliable plant disease classification using deep learning.
    """)
    st.markdown('</div>', unsafe_allow_html=True)


# --- DISEASE RECOGNITION PAGE ---
elif app_mode == "Disease Recognition":
    st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
    st.header("Disease Recognition")

    test_image = st.file_uploader("Upload a plant leaf image for analysis:")

    if st.button("Show Image") and test_image:
        st.image(test_image, use_container_width=True)

    if st.button("Predict") and test_image:
        st.snow()
        st.write("Processing image...")

        result_index = model_prediction(test_image)

        class_name = [
            'Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
            'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew',
            'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
            'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy',
            'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
            'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot',
            'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy',
            'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy',
            'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew',
            'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot',
            'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold',
            'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite',
            'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus',
            'Tomato___healthy'
        ]

        # --- This section splits the string for clean output ---
        prediction_string = class_name[result_index]
        
        parts = prediction_string.split('___')
        
        plant_name = parts[0].replace('_', ' ')
        disease_name = parts[1].replace('_', ' ')

        st.markdown(f'''
            <div class="result-box">
                <strong>Plant:</strong> {plant_name}<br>
                <strong>Disease:</strong> {disease_name}
            </div>
        ''', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)