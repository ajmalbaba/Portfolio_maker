import json
import copy
import streamlit as st

st.set_page_config(layout="wide")
from PIL import Image,ImageDraw,ImageOps
st.markdown(
        f'<div style="font-size: 60px; font-weight: bold; color: #3498db; padding: 10px; text-align: center;">Personal-Details</div>',
        unsafe_allow_html=True
    )
_,r0c1,_,r0c2,_,r0c3=st.columns([.5,2,1,2,1,3])
with r0c1:
    name = st.text_input(label="Name")
with r0c2:
    mail = st.text_input(label="e-mail")
with r0c3:
    resume = st.text_input(label="Link to your Resume")

st.write("##")

_,r1c1,_=st.columns([1,6,1])
with r1c1:
    abt_me=st.text_area(label="Describe your self",height=300,placeholder="Describe about yourself")


st.write("##")
st.write("##")
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
                   ["Git-hub","Leetcode","CodeChief","Code-forces","linked-In","Geeks-for-Geeks","Hacker-Rank"],
                   max_selections=5)
for i in links:
    temp=st.text_input(label=f"{i}",placeholder=f"Link to your {i} profile")
    links_dic[i]=temp

st.write("##")
st.write("##")
st.write("##")
st.write("##")
st.write("---")
st.markdown(
        f'<div style="font-size: 60px; font-weight: bold; color: #3498db; padding: 10px; text-align: center;">Project Details</div>',
        unsafe_allow_html=True
    )

projects_names={}
project_images={}
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
        f'<div style="font-size: 18px;  color: black; padding-left: 100px; text-align: left;">-->Mention languages you learnt </div>',
        unsafe_allow_html=True
    )
    st.write("")

    st.markdown(
        f'<div style="font-size: 18px;  color: black; padding-left: 100px; text-align: left;">-->Maximum No.of Charactors is 22  </div>',
        unsafe_allow_html=True
    )
    st.write("")

    st.markdown(
        f'<div style="font-size: 18px;  color: black; padding-left: 100px; text-align: left;">-->Use short-forms like DSA for Data structures and Algorithms  </div>',
        unsafe_allow_html=True
    )
    st.write("")
    ex="python , c++ , java , kotlin , DSA , compitative programing , Machine learning , OOPS , Socket programing , Computer Networks , html , css , javaskript , etc"
    st.markdown(
        f'<div style="font-size: 18px;  color: black; padding-left: 100px; text-align: left;">-->These are the few Examples: </div>',
        unsafe_allow_html=True
    )
    st.write("")

    st.markdown(
        f'<div style="font-size: 15px;  color: black; padding-left: 140px; text-align: left;">{ex} </div>',
        unsafe_allow_html=True
    )


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
        profile_pic = copy.copy(image)


with prof:
    _,temp=st.columns(2)
    with temp:
        if image:
            final_pic=imgtocir(Image.open(image))
            st.image(final_pic, caption='Circular Image', use_column_width=True, width=40)

            with upl_img:
                st.markdown(
                    f'<div style="font-size: 20px; font-weight: bold; color: #3498db; padding: 10px; text-align: left;">'
                    f'"If the image is not good please crop the image to Square"</div>',
                    unsafe_allow_html=True
                )



vars=[name,no_of_skills,no_of_projects,projects_names,projects_disc,skills,resume,mail,links,links_dic,abt_me,gender]

def data_writing():
    with open('Portfolio/D1/data.json', 'w') as file:
        for i in vars:
            json.dump(i, file)
            file.write('\n')
        file.close()

    for i in range(no_of_projects):
            output_folder = "Portfolio/D1/Projects_img/"


            image_path = output_folder + f"project_image_{i + 1}.jpg"
            with open(image_path, 'wb') as file:
                file.write(project_images[i+1].read())

    file.close()

    output_folder = 'Portfolio/D1/profile/'

    output_folder += "profile_img.jpg"

    with open(output_folder, 'wb') as f:
            f.write(profile_pic.read())
    f.close()



submit=st.button("Submit",on_click=data_writing)






