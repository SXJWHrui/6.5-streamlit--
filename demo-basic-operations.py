import streamlit as st
st.title("Hello,2208!")
st.header("You need to learn some basic operations")
st.subheader("eg,Visual StdioCode")
st.text('It')
st.markdown("this is an image:\n\
            ![](https://www.tjnu.edu.cn/images/24/04/28/6k5d17bn3r/07.jpg)")
if st.checkbox("show/Hide"):
    st.text("You checked the box")
status=st.radio("select gender:",("Male","Female"))
if status=='Male':
    st.success('Male')
else:
    st.success('Female')
hobbies=st.multiselect("Hobbies:",['Reading','Writing','Coding','Traveling'])
st.write("You selected:",hobbies)
if st.button("about"):
    st.text("Streamlit is a great tool")
name=st.text_input("Enter your name:")
if st.button("Submit"):
    st.write("Hello,",name)

level=st.slider("Select your level",1,5)
st.write("You selected!",level)

from fastai.vision.all import *
upload_img=st.file_uploader("Upload an image",type=['jpg','png'])
if upload_img is not None:
    img=PILImage.create(upload_img)
    st.image(img.to_thumb(256,256),caption="Uploaded Image")