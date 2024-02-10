import streamlit as st
import streamlit_lottie
from PIL import Image,ImageDraw,ImageOps
import copy
import json
import zipfile
from collections import defaultdict
st.set_page_config(layout="wide",page_title="Portfoliobuilder")
import io
# st.write("---")
welcome_note = "Welcome to MyPortfolioBuilder"

st.markdown(
    f'<div style="font-size: 40px; font-weight: bold; color: #7e22ce; padding-left: 20px; text-align: center; border: 2px solid #d1d5db; border-radius: 10px;">{welcome_note}</div>',
    unsafe_allow_html=True
)
# st.write("---")
heading="Empower Your Professional Presence"
st.markdown(
        f'<div style="font-size: 100px; font-weight: bold; color: black; padding: 10px; text-align: center;">{heading}</div>',
        unsafe_allow_html=True
    )

message='''Welcome to MyPortfolioBuilder, where your story takes center stage. Craft a stunning portfolio that showcases your skills, 
         experiences, and achievements. Whether you're a designer, developer, artist, or professional in any field, we provide the
          canvas for your narrative. Let your unique talents shine and create a lasting impression. Start building your personalized 
         portfolio today and make your mark in the digital world only in <span style="font-size: 40px; font-weight: bold;color: #ff5733;">3 Steps</span>.'''


st.write("##")
st.write("##")
st.markdown(
        f'<div style="font-size: 25px;  color: #7c7687; padding: 10px; text-align:center;">{message}</div>',
        unsafe_allow_html=True
    )


st.write("##")
st.write("##")

lott1,lott2,lott3=st.columns(3)
with lott1:
    st.markdown(
        f'<div style="font-size: 30px; font-weight: bold; color: #3c89d1; padding: 10px; text-align: center;">Step-1</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        f'<div style="font-size: 20px; font-weight: bold; color: #ff5733; padding: 10px; text-align: center;">Share Your Details</div>',
        unsafe_allow_html=True
    )
    anime_link = "https://lottie.host/d6088e55-0849-4340-be8f-8a0ab6907b9c/JaQkI6KLke.json"
    streamlit_lottie.st_lottie(anime_link, height=500, width=395)



with lott2:
    st.markdown(
        f'<div style="font-size: 30px; font-weight: bold; color: #3c89d1; padding: 10px; text-align: center;">Step-2</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        f'<div style="font-size: 20px; font-weight: bold; color: #ff5733; padding: 10px; text-align: center;">Download files</div>',
        unsafe_allow_html=True
    )
    anime_link = "https://lottie.host/b9b2a41c-5dd0-47c9-82bf-f4940bcb127f/t6X1cI6gAf.json"
    streamlit_lottie.st_lottie(anime_link, height=500, width=395)




with lott3:
    st.markdown(
        f'<div style="font-size: 30px; font-weight: bold; color: #3c89d1; padding: 10px; text-align: center;">Step-3</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        f'<div style="font-size: 20px; font-weight: bold; color: #ff5733; padding: 10px; text-align: center;">Deploy</div>',
        unsafe_allow_html=True
    )
    anime_link = "https://lottie.host/6d2acb34-458b-4d03-bd20-cf9506a99dc0/2fw3quubJU.json"
    streamlit_lottie.st_lottie(anime_link, height=500, width=395)
st.write("##")
sample_button = f'<a href="https://portfoliosagar.streamlit.app/"  target="_blank" style="display: flex; justify-content: center; padding:10px align-items: center; font-size: 40px; font-weight: bold; color: #3c89d1; text-decoration: none; cursor: pointer;">Sample</a>'
st.markdown(sample_button, unsafe_allow_html=True)


st.write("##")
st.write("##")

st.write("---")



st.markdown(
        f'<div style="font-size: 60px; font-weight: bold; color: #3498db; padding: 10px; text-align: center;">Personal-Details</div>',
        unsafe_allow_html=True
    )
_,r0c1,_,r0c2,_,r0c3=st.columns([.5,2,1,2,1,3])
with r0c1:
    name = st.text_input(label="Name")
    st.session_state['name']=name
with r0c2:
    mail = st.text_input(label="e-mail")
    st.session_state['mail'] = mail
with r0c3:
    resume = st.text_input(label="Link to your Resume")
    st.session_state['resume'] = resume


st.write("##")

_,r1c1,_=st.columns([1,6,1])
with r1c1:
    abt_me=st.text_area(label="Describe your self",height=300,placeholder="Describe about yourself")
    st.session_state['abt_me'] = abt_me


st.write("##")
st.write("##")

st.write("---")
st.markdown(
        f'<div style="font-size: 60px; font-weight: bold; color: #3498db; padding: 10px; text-align: center;">Links</div>',
        unsafe_allow_html=True
    )
r2c1,r2c2=st.columns(2)
links=[]
links_dic={}
with r2c1:
    links+=st.multiselect("Select the sites that need to included",
                   ["Git-hub","Leetcode","CodeChef","Code-forces","linked-In","Geeks-for-Geeks","Hacker-Rank"],
                   max_selections=5)
for i in links:
    temp=st.text_input(label=f"{i}",placeholder=f"Link to your {i} profile")
    links_dic[i]=temp

st.session_state['links'] = links
st.session_state['links_dic'] = links_dic
st.write("##")
st.write("##")
st.write("##")
st.write("##")
st.write("---")
st.markdown(
        f'<div style="font-size: 60px; font-weight: bold; color: #3498db; padding: 10px; text-align: center;">Project Details</div>',
        unsafe_allow_html=True
    )
st.markdown(
        f'<div style="font-size: 20px; font-weight: bold; color: #ff5733; padding: 10px; text-align: center;">(All the images must be in either landscape or a portrait orientation.)</div>',
        unsafe_allow_html=True
    )

projects_names={}
project_images=defaultdict(list)
projects_disc={}
no_of_projects=st.slider("select No of projects",min_value=1,max_value=6,value=3)
for i in range(no_of_projects):
    st.markdown(
        f'<div style="font-size: 30px; font-weight: bold; color: #3498db; padding: 10px; text-align: left;">Project{i+1}</div>',
        unsafe_allow_html=True
    )
    a,b=st.columns([1,2])
    with a:
        projects_names[i+1]=st.text_input(f"Enter the name of the project{i+1}")
    with b:
        projects_disc[i+1]=st.text_input(f"Describe Your project{i + 1}")
    uploaded_image=st.file_uploader(f"Upload an image of project{i+1}", type=["jpg", "png", "jpeg"])
    if uploaded_image:
        project_images[i+1]=uploaded_image



st.session_state['project_images'] = project_images
st.session_state['projects_names'] = projects_names
st.session_state['no_of_projects'] = no_of_projects
st.session_state['projects_disc'] = projects_disc
st.write("##")
st.write("##")
st.write("##")
st.write("##")
st.write("---")
st.markdown(
        f'<div style="font-size: 60px; font-weight: bold; color: #3498db; padding: 10px; text-align: center;">Your Skills</div>',
        unsafe_allow_html=True
    )

skills={}
no_of_skills=st.slider("Add skills",min_value=3,max_value=10,value=3)
sk,sk_info=st.columns(2)
with sk:
    for i in range(1,no_of_skills // 2 +1):
        ska,skb=st.columns(2)
        with ska:
            skills[i+i-1]=st.text_input(f"Skill{i+i-1}")
        with skb:
            skills[i+i]=st.text_input(f"Skill{i+i}")

    if no_of_skills%2!=0:
        ska,_=st.columns(2)
        with ska:
            skills[no_of_skills]=st.text_input(f"SKill{no_of_skills}")

with sk_info:
    st.markdown(
        f'<div style="font-size: 18px;  color: #7c7687; padding-left: 100px; text-align: left;">-->Mention languages you learned </div>',
        unsafe_allow_html=True
    )
    st.write("")

    st.markdown(
        f'<div style="font-size: 18px;  color: #7c7687; padding-left: 100px; text-align: left;">-->Maximum No.of Characters is 22  </div>',
        unsafe_allow_html=True
    )
    st.write("")

    st.markdown(
        f'<div style="font-size: 18px;  color: #7c7687; padding-left: 100px; text-align: left;">-->Use short-forms like DSA for Data structures and Algorithms  </div>',
        unsafe_allow_html=True
    )
    st.write("")
    ex="python , c++ , java , kotlin , DSA , competitive programming , Machine learning , OOPS , Socket programming , Computer Networks , html , css , javascript , etc"
    st.markdown(
        f'<div style="font-size: 18px;  color: #7c7687; padding-left: 100px; text-align: left;">-->These are the few Examples: </div>',
        unsafe_allow_html=True
    )
    st.write("")

    st.markdown(
        f'<div style="font-size: 15px;  color: #7c7687; padding-left: 140px; text-align: left;">{ex} </div>',
        unsafe_allow_html=True
    )
st.write("##")
st.write("##")
st.write("---")
st.markdown(
        f'<div style="font-size: 80px; font-weight: bold; color: #1D5C96;text-align: center;">Experience</div>',
        unsafe_allow_html=True
    )

st.session_state['no_of_skills'] = no_of_skills
st.session_state['skills'] = skills
no_of_interns=st.slider("Choose Text Areas",min_value=0,max_value=5,value=1)
st.session_state['no_of_interns'] = no_of_interns
exp_det=[]
for i in range(no_of_interns):
    exp=st.text_area(f"Describe your Experience{i+1}/internship{i+1}")
    exp_det.append(exp)
st.session_state['exp_det'] = exp_det
st.write("##")
st.write("##")
st.write("##")
st.write("##")
st.write("---")
st.markdown(
        f'<div style="font-size: 60px; font-weight: bold; color: #3498db; padding: 10px; text-align: center;">You</div>',
        unsafe_allow_html=True
    )

gender=st.radio(label="Select your Gender",options=["Male","Female"])
upl_img,prof=st.columns(2)
st.session_state['gender'] = gender

def imgtocir(original_image):
    mask = Image.new("L", original_image.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + mask.size, fill=255)
    circular_image = ImageOps.fit(original_image, mask.size, method=0, bleed=0.0, centering=(0.5, 0.5))
    circular_image.putalpha(mask)
    return circular_image

with upl_img:
    image = st.file_uploader(label="Upload your Profile Picture (Must be a Square)", type=["jpg", "png", "jpeg"])
    if image:
        st.session_state['profile_pic'] = image
        profile_pic = copy.copy(image)
        


with prof:
    _,temp=st.columns(2)
    with temp:
        if image:
            final_pic=imgtocir(Image.open(profile_pic))
            st.session_state['final_pic'] = final_pic
            st.image(final_pic, caption='Your Profile', use_column_width=True, width=40)

            with upl_img:
                st.markdown(
                    f'<div style="font-size: 20px; font-weight: bold; color: #ff5733; padding: 10px; text-align: left;">'
                    f'"If the image is not good, please crop it to a square"</div>',
                    unsafe_allow_html=True
                )



vars=[name,no_of_skills,no_of_projects,projects_names,projects_disc,skills,resume,mail,links,links_dic,abt_me,gender,exp_det]

def data_writing():
    st.sidebar.success("")

submit=st.button("Submit",on_click=data_writing)

st.markdown(
        f'<div style="font-size: 25px; font-weight: bold; color: #ff5733; padding: 10px; text-align: center;">'
        f'"After Submitting Open Slide-bar and click folio to check your portfolio"</div>',
        unsafe_allow_html=True
    )

st.write("##")
st.write("##")
st.write("##")
st.write("##")
st.write("##")
st.write("##")
st.write("##")


st.write("---")

me,m_det=st.columns([3,7])

with me:
    with open('Project_portfolio/WhatsApp Image 2023-12-19 at 16.56.45.jpeg','rb') as img:
        my_img=img.read()
        st.image(imgtocir(Image.open(io.BytesIO(my_img))),width=250)

with m_det:
    st.markdown(
        f'<div style="font-size: 30px; font-weight: bold; color: #687F8D; padding: 10px; text-align: left;">'
        f'By,</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        f'<div style="font-size: 30px; font-weight: bold; color: #687F8D; padding: 10px; text-align: left;">'
        f'SAGAR.E</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        f'<div style="font-size: 30px; font-weight: bold; color: #687F8D; padding: 10px; text-align: left;">'
        f'INDIAN INSTITUTE OF INFORMATION TECHNOLOGY PUNE</div>',
        unsafe_allow_html=True
    )


    l1,l2,l3,_,_=st.columns(5)
    with l1:
        label_as_button = f'<a href="https://github.com/sagareddum" target="_blank" style="font-size: 25px; font-weight: bold;  color: #687F8D; text-decoration: none; cursor: pointer;">Git-Hub</a>'
        st.markdown(label_as_button, unsafe_allow_html=True)

    with l2:
        label_as_button = f'<a href="https://drive.google.com/file/d/1f4hFTmV8uI8lR3gSgq6iZU0z5ytlJ7Cr/view?usp=drive_link" target="_blank" style="font-size: 25px; font-weight: bold;  color: #687F8D; text-decoration: none; cursor: pointer;">Resume</a>'
        st.markdown(label_as_button, unsafe_allow_html=True)

    with l3:
        label_as_button = f'<a href="https://www.linkedin.com/in/sagar-e-95ba80217/" target="_blank" style="font-size: 25px; font-weight: bold;  color: #687F8D; text-decoration: none; cursor: pointer;">Linkedin</a>'
        st.markdown(label_as_button, unsafe_allow_html=True)











