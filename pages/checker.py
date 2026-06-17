import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

st.set_page_config(
page_title="Meal Calories Checker",
layout="centered"
)

# ----------------

st.markdown("""

<style>

.stApp{
background:
linear-gradient(
180deg,
#FFD6E8,
#E6D6FF
);
}

.block-container{
max-width:780px;
}

</style>

""",

unsafe_allow_html=True

)

# ----------------

if "calories" not in st.session_state:
    st.session_state.calories=0

if "target" not in st.session_state:
    st.session_state.target=2000

if "meal_added" not in st.session_state:
    st.session_state.meal_added=False

# ----------------

classes=[

"burger",
"butter_naan",
"chai",
"chapati",
"chole_bhature",
"dal_makhani",
"dhokla",
"fried_rice",
"idli",
"jalebi",
"kaathi_rolls",
"kadai_paneer",
"kulfi",
"masala_dosa",
"momos",
"paani_puri",
"pakode",
"pav_bhaji",
"pizza",
"samosa"

]

nutrition={

"idli":[120,4,90],
"burger":[350,18,45],
"pizza":[420,14,40],
"chapati":[140,3,88],
"fried_rice":[340,7,70],
"masala_dosa":[280,8,82],
"paani_puri":[250,8,80]

}

# ----------------

@st.cache_resource

def load():

    return tf.keras.models.load_model(
    "models/food_model.keras"
    )

model=load()

# ----------------

def detect(img):

    img=img.convert(
    "RGB"
    )

    img=img.resize(
    (224,224)
    )

    arr=np.array(
    img
    )

    arr=(
    arr/127.5
    )-1

    arr=np.expand_dims(
    arr,
    0
    )

    pred=model.predict(
    arr,
    verbose=0
    )[0]

    idx=np.argmax(
    pred
    )

    return classes[idx]

# ----------------

c1,c2=st.columns([8,1])

with c2:

    if st.button("←"):

        st.switch_page(
        "app.py"
        )

# ----------------

st.title(
"🔥 Meal Calories Checker"
)

st.write(
"Calories"
)

st.write(
f"""
{st.session_state.calories}
/
{st.session_state.target}
"""
)

st.progress(
st.session_state.calories/
st.session_state.target
)

# ----------------

up=st.file_uploader(
"📷 Upload Meal"
)

if up:

    st.session_state.meal_added=False

    img=Image.open(
    up
    )

    st.image(
    img,
    width=260
    )

    food=detect(
    img
    )

    c,p,h=nutrition.get(
food,
[250,8,80]
)

    a,b,d=st.columns(3)

    a.metric(
    "Calories",
    c
    )

    b.metric(
    "Protein",
    f"{p} g"
    )

    d.metric(
    "Health",
    f"{h}%"
    )

    meal=st.selectbox(

    "Add To",

    [

"Breakfast",
"Lunch",
"Dinner"

]

)

    if st.button(
    "Add To Meal"
    ):

        if not st.session_state.meal_added:

            st.session_state.calories+=c

            st.session_state.meal_added=True

            st.success(
f"""
Added to {meal}
"""
)

        else:

            st.warning(
"Meal already added"
)