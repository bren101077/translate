import streamlit as st
from PIL import Image
import pytesseract
from googletrans import Translator

# Path to Tesseract executable (set to your installation path)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Title of the app
st.title("Thai Text Extraction and Translation")

# Upload image file
uploaded_file = st.file_uploader("Upload an image with Thai text", type=["png", "jpg", "jpeg"])

# Process the image if uploaded
if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Extract text using Tesseract OCR
    st.write("Extracting text...")
    extracted_text = pytesseract.image_to_string(image, lang="tha")
    st.text(f"Extracted Thai Text:\n{extracted_text}")

    # Translate the extracted text into English
    st.write("Translating text...")
    translator = Translator()
    try:
        translated_text = translator.translate(extracted_text, src="th", dest="en")
        st.text(f"Translated English Text:\n{translated_text.text}")
    except Exception as e:
        st.error("An error occurred during translation. Please try again.")

# Footer
st.write("---")
st.write("Made with ❤️ using Streamlit")
