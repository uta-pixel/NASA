import streamlit as st
import requests

st.title("💬 چت با پشتیبانی")

# دکمه لینک به تلگرام
st.markdown("""
<a href="https://t.me/HamPayamBot" target="_blank" 
   style="display: inline-block;
          background: #0088cc;
          color: white;
          padding: 10px 20px;
          text-decoration: none;
          border-radius: 5px;">
   💬 شروع چت در تلگرام
</a>
""", unsafe_allow_html=True)

# فرم تماس
with st.form("contact_form"):
    name = st.text_input("نام شما")
    message = st.text_area("پیام شما")
    submitted = st.form_submit_button("ارسال به تلگرام")
    if submitted:
        try:
            # ارسال پیام به ربات تلگرام
            bot_token = "8373221356:AAE3ucKVTKeGSdPnKQglSmc69nIu34qWIys"
            chat_id = "https://t.me/HamPayamBot"
            text = f"پیام جدید از {name}:\n{message}"
            url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={text}"
            requests.get(url)
            st.success("پیام شما ارسال شد!")
        except:
            st.error("خطا در ارسال پیام")
