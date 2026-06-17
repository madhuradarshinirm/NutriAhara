import streamlit as st
from datetime import datetime

# ---------------- PAGE ----------------

st.set_page_config(
page_title="Tracker",
layout="centered"
)

# ---------------- SESSION ----------------

if "target" not in st.session_state:
    st.session_state.target=2000

if "meal_log" not in st.session_state:
    st.session_state.meal_log={

    "Breakfast":[],

    "Lunch":[],

    "Dinner":[],

    "Snack":[]

}

# NEW FIX
if "calories" not in st.session_state:
    st.session_state.calories=0

# ---------------- CALORIES ----------------

meal_total=0

for section in st.session_state.meal_log:

    for meal in st.session_state.meal_log[section]:

        meal_total+=meal[1]

# FIX → sync checker calories
total=max(
meal_total,
st.session_state.calories
)

# store back
st.session_state.calories=total

progress=min(
total/
st.session_state.target,
1.0
)

# ---------------- STYLE ----------------

st.markdown("""

<style>

#MainMenu{
visibility:hidden;
}

header{
visibility:hidden;
}

footer{
visibility:hidden;
}

.stApp{

background:
linear-gradient(
180deg,
#FFD8EC,
#EAD8FF
);

}

.big{

font-size:34px;

font-weight:700;

color:#6B4F4F;

}

.card{

background:white;

padding:22px;

border-radius:22px;

margin-top:15px;

margin-bottom:15px;

}

</style>

""",

unsafe_allow_html=True

)

# ---------------- TOP ----------------

c1,c2,c3=st.columns([1,6,1])

with c1:

    if st.button("←"):

        st.switch_page(
        "app.py"
        )

with c2:

    st.markdown(
"""
<div class='big'>
🔥 Kcal
</div>
""",

unsafe_allow_html=True

)

with c3:

    if st.button("☰"):

        st.switch_page(
        "pages/profile.py"
        )

# ---------------- DATE ----------------

today=datetime.now()

st.caption(
f"📅 {today.strftime('%d %B %Y')}"
)

# ---------------- CARD ----------------

st.metric(

"Calories",

f"{total}/{st.session_state.target}"

)

st.progress(
progress
)

# FIX TARGET RANGE
st.caption(

f"Target Range : 1400 - {st.session_state.target}"

)

# ---------------- AI ----------------

remain=(
st.session_state.target
-
total
)

if remain>1200:

    ai="""
🤖 AI Suggestion

You need a heavier meal

Try:
Rice
Protein
Vegetables
"""

elif remain>700:

    ai="""
🥗 AI Suggestion

Balanced lunch recommended
"""

elif remain>300:

    ai="""
🍎 AI Suggestion

Light snack recommended
"""

else:

    ai="""
🎉 AI

Target almost completed
"""

st.info(
ai
)

# ---------------- CELEBRATE ----------------

if total>=st.session_state.target:

    st.balloons()

    st.success(
    "Daily Goal Completed ❤️"
    )

# ---------------- LOG ----------------

st.divider()

st.markdown(
"""
<div class='big'>
🍽 Log Meal
</div>
""",

unsafe_allow_html=True

)

# ---------------- BUTTONS ----------------

if st.button(
"🍞 Breakfast",
use_container_width=True
):

    st.switch_page(
    "pages/breakfast.py"
    )

if st.button(
"🍱 Lunch",
use_container_width=True
):

    st.switch_page(
    "pages/lunch.py"
    )

if st.button(
"🍲 Dinner",
use_container_width=True
):

    st.switch_page(
    "pages/dinner.py"
    )

if st.button(
"🍎 Snack",
use_container_width=True
):

    st.switch_page(
    "pages/snack.py"
    )

# ---------------- SUMMARY ----------------

st.divider()

st.subheader(
"Today's Meals"
)

empty=True

for sec in st.session_state.meal_log:

    if st.session_state.meal_log[sec]:

        empty=False

        st.markdown(
f"### {sec}"
)

        for meal in st.session_state.meal_log[sec]:

            st.write(
f"""
🍽 {meal[0]}

🔥 {meal[1]} kcal
"""
)

if empty:

    st.info(
    "No meals added"
    )

# ---------------- AI ANALYSIS ----------------

st.divider()

st.subheader(
"🤖 AI Nutrition Analysis"
)

if total<800:

    st.warning(
"""
You consumed too little.

Eat balanced meals.
"""
)

elif total<1500:

    st.success(
"""
Healthy intake ❤️
"""
)

elif total<2200:

    st.warning(
"""
Near target.
"""
)

else:

    st.error(
"""
High calorie intake.
"""
)

# ---------------- FOOTER ----------------

st.divider()

st.caption(
"Made with ❤️ using NutriAhara"
)