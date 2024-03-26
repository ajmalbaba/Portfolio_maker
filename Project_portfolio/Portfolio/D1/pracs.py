import io
import json
import os
import streamlit as st
import webbrowser
import requests
import streamlit_lottie
from PIL import Image,ImageDraw,ImageOps
with open('D1/data.json', 'r') as file:
    name = json.loads(file.readline())
    no_of_skills = json.loads(file.readline())
    no_of_projects = json.loads(file.readline())
    projects_names = json.loads(file.readline())
    projects_disc = json.loads(file.readline())
    skills = json.loads(file.readline())
    resume = json.loads(file.readline())
    mail = json.loads(file.readline())
    links = json.loads(file.readline())
    links_dic = json.loads(file.readline())
    abt_me = json.loads(file.readline())
    gender = json.loads(file.readline())
    exp_det=json.loads(file.readline())
file.close()

gender_dic={'Female':"https://lottie.host/2ce8f458-d046-4796-bf3b-a4f66703bd35/E045iKYzlR.json","Male":"https://lottie.host/ded010c1-4656-4aee-bca9-cb0ad14d46cd/H1X9L3hTOp.json"}

# image=None
project_images={}
# vars=[name,no_of_skills,no_of_projects,projects_names,projects_disc,skills,resume,mail,links,links_dic,abt_me]


with open('D1/default_img_proj.jpg','rb') as dpi:
    project_img_default=dpi.read()
    
# file.close()
with open('D1/profileprofile_img.jpg','rb') as profile:
    image=profile.read()
profile.close()

for i in range(no_of_projects):
    image_path=f"D1/Projects_imgproject_image_{i+1}.jpg"
    with open(image_path,'rb') as f:
        project_images.update({i+1:f.read()})
f.close()


st.set_page_config(layout="wide",page_title=f"{name}")


def open_website(website_url):
    webbrowser.open_new_tab(website_url)



def lottie_loder(url):
        r=requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
# Create columns
r0c0, r0c1 = st.columns([1, 5])

with r0c0:
    st.markdown(
        f'<div style="font-size: 30px; font-weight: bold; color: #F86D4E; padding: 10px; text-align: left;">Quick-Links</div>',
        unsafe_allow_html=True
    )

with r0c1:
     top_links=st.columns(5)
     for i in range(len(links)):
         with top_links[-(i+1)]:
             label_as_button = f'<a href="{links_dic[links[i]]}" target="_blank" style="font-size: 35px; font-weight: bold;  color: #3498db; text-decoration: none; cursor: pointer;">{links[i]}</a>'
             st.markdown(label_as_button, unsafe_allow_html=True)

st.write("---")
st.markdown(
        f'<div style="font-size: 80px; font-weight: bold; color: #1D5C96;text-align: center;">{name}</div>',
        unsafe_allow_html=True
    )
#----------------------------------------------about-me----------------------------
r1c0,_,r1c1=st.columns([1.7,0.3,1])

with r1c0:
    st.markdown(
        f'<div style="font-size: 24px;padding-top:70px;color: #687F8D;font-family: Pacifico, cursive;">{abt_me}</div>',
        unsafe_allow_html=True
    )

with r1c1:
    anime_link=gender_dic[gender]
    streamlit_lottie.st_lottie(anime_link,height=500,width=450)

st.write('##')
st.write("---")
st.write('##')
#---------------------------------------------projects-------------------------------------------
st.markdown(
        f'<div style="font-size: 80px; font-weight: bold; color: #1D5C96;text-align: center;">My Projects</div>',
        unsafe_allow_html=True
    )

if no_of_projects > 3:
    projects1 = st.columns(3)
    for i in range(3):
        with projects1[i]:
            if project_images[i+1]:
                img=project_images[i+1]
            else:
                img=project_img_default
            st.image(img)
            st.markdown(
                f'<div style="font-size: 30px; font-weight: bold; color: #1D5C96;text-align: center;">{projects_names[str(i+1)]}</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                f'<div style="font-size: 15px; color: #3498db;text-align: left;padding-left:10px;padding-right:30px;">{projects_disc[str(i+1)]}</div>',
                unsafe_allow_html=True
            )
    st.write("##")
    st.write("##")

    projects2 = st.columns(3)
    for i in range(no_of_projects - 3):
        with projects2[i]:
            if project_images[i+1]:
                img=project_images[i+1]
            else:
                img=project_img_default
            st.image(img)
            st.markdown(
                f'<div style="font-size: 30px; font-weight: bold; color: #1D5C96;text-align: center;">{projects_names[str(i+1)]}</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                f'<div style="font-size: 15px; color: #3498db;text-align: left;padding-left:10px;padding-right:30px;">{projects_disc[str(i+1)]}</div>',
                unsafe_allow_html=True
            )
else:
    rem_projects = st.columns(no_of_projects)
    for i in range(no_of_projects):
        with rem_projects[i]:
            if project_images[i+1]:
                img=project_images[i+1]
            else:
                img=project_img_default
            st.image(img)
            st.markdown(
                f'<div style="font-size: 30px; font-weight: bold; color: #1D5C96;text-align: center;">{projects_names[str(i+1)]}</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                f'<div style="font-size: 15px; color:#3498db;text-align: left;padding-left:30px;padding-right:30px;">{projects_disc[str(i+1)]}</div>',
                unsafe_allow_html=True
            )

st.write("##")
st.write("---")

#---------------------------------------------skills-------------------------------------------
st.markdown(
        f'<div style="font-size: 80px; font-weight: bold; color: #1D5C96;text-align: left;">Skills</div>',
        unsafe_allow_html=True
    )
st.write("##")

skills1=st.columns(5)

if no_of_skills>5:
    for i in range(5):
        skills1[i].markdown(
            f'<div style="font-size: 30px; font-weight: bold; color: #3498db;text-align: left;">{skills[str(i+1)]}</div>',
            unsafe_allow_html=True
        )
    skills2 = st.columns(5)
    for i in range(no_of_skills-5):
        skills2[i].markdown(
            f'<div style="font-size: 30px; font-weight: bold; color: #3498db;text-align: left;">{skills[str(i+6)]}</div>',
            unsafe_allow_html=True
        )
else:
    for i in range(no_of_skills):
        skills1[i].markdown(
            f'<div style="font-size: 30px; font-weight: bold; color: #3498db;text-align: left;">{skills[str(i+1)]}</div>',
            unsafe_allow_html=True
        )
#---------------------------------------------Interns-------------------------------------------------
if exp_det:
    st.write("##")
    st.write("##")
    st.write("---")
    st.write("##")
    st.markdown(
        f'<div style="font-size: 80px; font-weight: bold; color: #1D5C96;text-align: center;">My Experience</div>',
        unsafe_allow_html=True)

    for i in exp_det:
        st.markdown(
              f'<div style="font-size: 25px;  color: #7c7687;text-align: left;">{i}</div>',
              unsafe_allow_html=True)
        st.write("")


#---------------------------------------------Contact-me-------------------------------------------

st.write("##")
st.write("---")
_,hi_anime=st.columns([1.5,2])
with hi_anime:
    streamlit_lottie.st_lottie("https://lottie.host/7e7689a0-6c4a-4d6d-b25d-99016cae33a8/RGFcDNJt2d.json"
                               , width=200, height=200)


_,_,Img,_,_=st.columns(5)
def imgtocir(original_image):
    mask = Image.new("L", original_image.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + mask.size, fill=255)
    circular_image = ImageOps.fit(original_image, mask.size, method=0, bleed=0.0, centering=(0.5, 0.5))
    circular_image.putalpha(mask)
    return circular_image
with Img:
    if image:
        final_pic = imgtocir(Image.open(io.BytesIO(image)))
        st.image(final_pic, caption='Circular Image', use_column_width=True, width=40)

st.write("##")


con_det=st.columns([5,.2,5])
with con_det[0]:
    label_as_button = f'<a href="{resume}" target="_blank" style="font-size: 35px; font-weight: bold;padding-left: 500px;  color: #1D5C96; text-decoration: none; cursor: pointer;">Resume</a>'
    st.markdown(label_as_button, unsafe_allow_html=True)
with con_det[1]:
    st.markdown(
        f'<div style="font-size: 30px; font-weight: bold; color: black;text-align: center;">|</div>',
        unsafe_allow_html=True
    )
with con_det[2]:
    st.markdown(
        f'<div style="font-size: 35px; font-weight: bold; color: #1D5C96;text-align: left;">{mail}</div>',
        unsafe_allow_html=True
    )

