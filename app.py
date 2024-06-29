import json
import requests
import streamlit as st
from streamlit_lottie import st_lottie

# Function to load Lottie animation from a URL
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load Lottie animations from URLs
lottie_hello = load_lottieurl("https://lottie.host/eb0a14ca-59bb-4ad8-9768-c050b750dab7/RDOP76Vkps.json")
lottie_hello_1 = load_lottieurl("https://lottie.host/2ac78d97-f9af-4e57-b892-8020074e471f/zd15pdSa75.json")
if lottie_hello is not None:
    st_lottie(lottie_hello, speed=1, reverse=False, loop=True, quality="high", key="hello")

if lottie_hello_1 is not None:
    st_lottie(lottie_hello_1, speed=1, reverse=True, loop=True, quality="high", key="hello_1")
else:
    st.error("Failed to load Lottie animation from URL")

# Display introduction
st.title(" I'm Ritwick Mondal")
st.subheader("Machine Learning Enthusiast")

# Contact number
st.write("<h3>Contact Number: 7063536185</h3>",unsafe_allow_html=True)

# LinkedIn link
linkedin_url = "linkedin.com/in/ritwick-mondal-ba4937251"
linkedin_logo="/content/linkedin.png"
st.markdown(f'<h3>Here is my linkedin profile <a href="{linkedin_url}" target="_blank"><img src="{linkedin_logo}" width="30" style="vertical-align: middle; margin-right: 10px;" />linkedin.com/in/ritwick-mondal-ba4937251</a></h3>', unsafe_allow_html=True)
email_url = "ritwickmondal874@gmail.com"
email_logo="/content/email.png"
st.markdown('<h3>Here is my email id: <a href="{email_url}" target="_blank"><img src="{email_logo}" width="30" style="vertical-align: middle; margin-right: 10px;" />ritwickmondal874@gmail.com</a></h3>', unsafe_allow_html=True)





# Instagram link
# instagram_url = "https://www.instagram.com/your-instagram-url"
# st.image("instagram_logo.png", width=30)
# st.markdown(f"[Instagram]({instagram_url})")

# Display Lottie animations if loaded successfully
