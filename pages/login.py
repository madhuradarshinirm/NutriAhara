import streamlit as st

st.set_page_config(
page_title="Login",
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
max-width:650px;
}

</style>

""",

unsafe_allow_html=True

)

# ----------

if "name" not in st.session_state:
    st.session_state.name=""

if "age" not in st.session_state:
    st.session_state.age=19

if "height" not in st.session_state:
    st.session_state.height=155

if "weight" not in st.session_state:
    st.session_state.weight=68

# ----------

c1,c2=st.columns([8,1])

with c2:

    if st.button("←"):

        st.switch_page(
        "app.py"
        )

# ----------

st.title(
"👤 Login"
)

name=st.text_input(

"Name",

value=
st.session_state.name

)

age=st.number_input(

"Age",

1,
100,

st.session_state.age

)

height=st.number_input(

"Height (cm)",

100,
220,

st.session_state.height

)

weight=st.number_input(

"Weight (kg)",

20,
200,

st.session_state.weight

)

# ----------

if st.button(
"Save Profile"
):

    st.session_state.name=name

    st.session_state.age=age

    st.session_state.height=height

    st.session_state.weight=weight

    st.success(
"Profile Updated ❤️"
    )