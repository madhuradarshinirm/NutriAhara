import streamlit as st

# -------------------
# PAGE
# -------------------

st.set_page_config(
    page_title="NutriAhara",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# -------------------
# SESSION
# -------------------

if "target" not in st.session_state:
    st.session_state.target = 2000

if "calories" not in st.session_state:
    st.session_state.calories = 0

progress = min(
    st.session_state.calories /
    st.session_state.target,
    1
)

# -------------------
# STYLE
# -------------------

st.markdown("""

<style>

#MainMenu,
header,
footer{
visibility:hidden;
}

[data-testid="stSidebar"]{
display:none;
}

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

/* TITLE */

.title{

text-align:center;

font-size:52px;

font-weight:700;

color:#6B4F4F;

margin-bottom:20px;

}

/* CARD */

.card{

background:white;

border-radius:28px;

padding:32px;

margin-top:10px;

margin-bottom:18px;

box-shadow:
0 10px 30px
rgba(0,0,0,.06);

font-size:24px;

color:#6B4F4F;

}

/* ROW */

.row{

display:flex;

justify-content:
space-between;

align-items:center;

}

/* CLICK BOX */

.stButton>button{

width:26px;

height:26px;

border-radius:10px;

border:none;

background:#FFFDF7;

margin-left:-60px;

box-shadow:
0 2px 8px
rgba(0,0,0,.05);

}

/* ICONS */

.float{

font-size:70px;

animation:
float 2s infinite;

}

.rotate{

font-size:60px;

animation:
rotate 3s infinite;

}

.bounce{

font-size:60px;

animation:
bounce 2s infinite;

}

@keyframes float{

50%{
transform:
translateY(-10px);
}

}

@keyframes rotate{

50%{
transform:
rotate(10deg);
}

}

@keyframes bounce{

50%{
transform:
translateY(-10px);
}

}

</style>

""",
unsafe_allow_html=True
)

# -------------------
# TITLE
# -------------------

st.markdown(
"""
<div class='title'>
NutriAhara
</div>
""",
unsafe_allow_html=True
)

# -------------------
# TOP ICONS
# -------------------


c1,c2,c3 = st.columns([6.5,0.45,0.45])

with c2:

    if st.button(
          "👤",
          key="profile"
    ):

        st.switch_page(
            "pages/login.py"
        )

with c3:

    if st.button(
          "⚙️",
          key="setting"
    ):

        st.switch_page(
            "pages/settings.py"
        )

# -------------------
# CARD 1
# -------------------

if st.button(
"",
key="cal"
):

    st.switch_page(
        "pages/tracker.py"
    )

progress_html = f"""

<div class='card'>

<div class='row'>

<div>

<div style="font-size:28px">

🔥 {st.session_state.calories} / {st.session_state.target}

</div>

<div style="
margin-top:10px;
font-size:20px;
color:#8A7A7A;
">

kcal

</div>

<div style="
margin-top:18px;
width:260px;
height:12px;
background:#F7F4F8;
border-radius:40px;
overflow:hidden;
">

<div style="
width:{progress*100}%;
height:100%;
background:#FFD6E8;
border-radius:40px;
">

</div>

</div>

</div>

<div class='float'>

🥗

</div>

</div>

</div>

"""

st.markdown(
progress_html,
unsafe_allow_html=True
)

# -------------------
# CARD 2
# -------------------

if st.button(
"",
key="meal"
):

    st.switch_page(
        "pages/checker.py"
    )

st.markdown(
"""

<div class='card'>

<div class='row'>

Meal Calories Checker

<div class='rotate'>

🍴

</div>

</div>

</div>

""",
unsafe_allow_html=True
)

# -------------------
# CARD 3
# -------------------

if st.button(
"",
key="cook"
):

    st.switch_page(
        "pages/cook.py"
    )

st.markdown(
"""

<div class='card'>

<div class='row'>

Cook with NutriAhara

<div class='bounce'>

🍳

</div>

</div>

</div>

""",
unsafe_allow_html=True
)