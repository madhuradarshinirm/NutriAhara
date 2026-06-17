import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

st.set_page_config(
page_title="Cook with NutriAhara",
layout="centered"
)

# -----------------

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
max-width:760px;
}

</style>

""",

unsafe_allow_html=True

)

# -----------------

classes=[

"burger",
"idli",
"pizza",
"chapati",
"fried_rice",
"masala_dosa"

]

@st.cache_resource

def load():

    return tf.keras.models.load_model(
    "models/food_model.keras"
    )

model=load()

# -----------------

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

    return classes[
    np.argmax(
    pred
    )
]

# -----------------

recipes={

"burger":[

"Toast bun",
"Prepare filling",
"Serve"

],

"idli":[

"Soak",
"Steam",
"Serve"

],

"pizza":[

"Prepare base",
"Bake",
"Serve"

]

}

# -----------------

c1,c2=st.columns([8,1])

with c2:

    if st.button("←"):

        st.switch_page(
        "app.py"
        )

# -----------------

st.title(
"🍳 Cook with NutriAhara"
)

up=st.file_uploader(
"📷 Upload Ingredients"
)

if up:

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

    st.info(

f"""
From uploaded ingredients
AI suggests:

You can prepare
healthy versions
of this meal.
"""

)

    st.subheader(
"👩🏻‍🍳 Procedure"
)

    for i,x in enumerate(

recipes.get(
food,
[
"Prepare",
"Cook",
"Serve"
]

)

):

        st.write(
f"{i+1}. {x}"
)

    st.success(

"""
Health Tip:

Use less oil
Increase vegetables
"""
)