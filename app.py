import streamlit as st 
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

## Funciton to get response from llma2 model

def getllmaResponse(input_text, no_words, blog_style):
    prompt_template = """
    Write a blog for {blog_style} about {input_text} with {no_words} words.
    """

    prompt = PromptTemplate(input_variables=["blog_style","input_text",'no_words'], template = prompt_template)
    
    llma = CTransformers(model ='llama-2-7b-chat.ggmlv3.q8_0.bin', model_type='llama', temperature=0.7, 
                         max_tokens=512 )
    response = llma(prompt.format(blog_style = blog_style, input_text=input_text, no_words=no_words))
    return response


st.set_page_config(page_title="Generate blogs", 
                   page_icon=":robot:",
                   layout="centered",
                   initial_sidebar_state="collapsed")

st.header("Generate Blogs")

input_text=st.text_input("Enter your Blog here")

##creating 2 more columns for additional tokens

col1, col2 = st.columns([5,5])

with col1:
    no_words = st.text_input('No of Words')
with col2:
    blog_style = st.selectbox('Writing the blog for', ('Reserachers', 'Data scientist', 'leyman'), index=0)
    
submit=st.button("Generate Blog")

##Final response
if submit:
    st.write(getllmaResponse(input_text, no_words, blog_style))