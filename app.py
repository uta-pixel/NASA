import streamlit as st
from pathlib import Path

# Set page configuration (optional)
st.set_page_config(page_title="فارسی وب اپ", page_icon="📊", layout="wide")

# Sidebar menu in Persian
with st.sidebar:
    selected_page = st.selectbox("منو", ["صفحه اصلی", "درباره ما"])

# Main content area
st.title("به برنامه من خوش آمدید")  # Welcome to my app

# Handle logo with error checking
try:
    logo_path = Path("logo.png")
    if logo_path.is_file():
        st.image("logo.png", width=200)  # Adjust width as needed
    else:
        st.warning("لوگو یافت نشد. لطفا فایل logo.png را در همان پوشه قرار دهید.")
        # Display placeholder if logo is missing
        st.image("https://via.placeholder.com/200x100?text=لوگوی+شما", 
                width=200,
                caption="لوگوی شما اینجا قرار می‌گیرد")
except Exception as e:
    st.error(f"خطا در نمایش لوگو: {e}")

# Page content based on selection
if selected_page == "صفحه اصلی":
    st.header("صفحه اصلی")
    st.write("این محتوای صفحه اصلی است.")
    
elif selected_page == "درباره ما":
    st.header("درباره ما")
    st.write("این بخش اطلاعات درباره ما را نمایش می‌دهد.")