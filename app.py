from utils import summarize, generate_image
import streamlit as st
st.title('Text to summary to Image')
st.header('This is a sample web app that summarizes text and generates an image of summary')
text=st.text_area('Enter your text below','Astraunut riding a bicycle in the beach')
if st.button('Summarize and generate image'):
    if not text:
        st.error('Please input a text in the text box')
    else:
        with st.spinner('Summarizing....'):
            summary=summarize(text)
        with st.spinner('Generating image....'):
            image =generate_image(summary)
        st.info(f'Summary:{summary}')
        st.image(image)

