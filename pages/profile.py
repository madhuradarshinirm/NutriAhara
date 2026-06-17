import streamlit as st

st.set_page_config(
page_title="Profile",
layout="centered"
)

# ----------

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
max-width:700px;
}

.card{

background:white;

padding:30px;

border-radius:24px;

}

</style>

""",

unsafe_allow_html=True

)

# ----------

c1,c2=st.columns([8,1])

with c2:

    if st.button("←"):

        st.switch_page(
        "app.py"
        )

# ----------

name=st.session_state.get(
"name",
"Guest"
)

age=st.session_state.get(
"age",
0
)

height=st.session_state.get(
"height",
0
)

weight=st.session_state.get(
"weight",
0
)

bmi=0

if height:

    bmi=round(
weight/
(
(height/100)**2
),
1
)

# ----------

st.title(
"👤 Profile"
)

st.markdown(
"<div class='card'>",
unsafe_allow_html=True
)

st.subheader(
name
)

st.write(
f"Age: {age}"
)

st.write(
f"Height: {height} cm"
)

st.write(
f"Weight: {weight} kg"
)

st.metric(
"BMI",
bmi
)

st.progress(
min(
weight/100,
1.0
)
)

st.markdown(
"</div>",
unsafe_allow_html=True
)