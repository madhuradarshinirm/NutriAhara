import streamlit as st

# ---------------- PAGE ----------------

st.set_page_config(
    page_title="Breakfast",
    layout="centered"
)

# ---------------- SESSION ----------------

if "meal_log" not in st.session_state:

    st.session_state.meal_log={

        "Breakfast":[],

        "Lunch":[],

        "Dinner":[],

        "Snack":[]
    }

# ---------------- DATA ----------------

meals=[

("Idli",60,100),
("Dosa",150,150),
("Masala Dosa",250,200),
("Poha",180,180),
("Upma",200,180),
("Oats",170,120),
("Pongal",300,250),
("Fruit Bowl",90,100)

]

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
#FFD6E8,
#E6D6FF
);
}

.block-container{
max-width:850px;
}

.card{
background:white;
padding:25px;
border-radius:20px;
margin-top:20px;
margin-bottom:20px;
}

.title{
font-size:28px;
font-weight:700;
color:#6B4F4F;
}

</style>

""",

unsafe_allow_html=True

)

# ---------------- TOP ----------------

c1,c2=st.columns([8,1])

with c1:

    if st.button(
        "← Breakfast"
    ):

        st.switch_page(
            "pages/tracker.py"
        )

with c2:

    st.button(
        "☰",
        key="menu"
    )

# ---------------- SEARCH ----------------

search=st.text_input(

"",
placeholder="🔍 Search meal"

)

# ---------------- TABS ----------------

tab1,tab2,tab3,tab4=st.tabs(

[

"❤️ Fav",

"🍱 My Foods",

"📖 My Meals",

"➕ Create Own Meal"

]

)

# ---------------- SHOW ----------------

def show(tab):

    for i,(meal,kcal,gram) in enumerate(meals):

        if search.lower() in meal.lower():

            st.markdown(
                "<div class='card'>",
                unsafe_allow_html=True
            )

            st.markdown(

f"""

<div class='title'>
{meal}
</div>

""",

unsafe_allow_html=True

)

            g=st.slider(

                "Serving",

                50,

                500,

                gram,

                key=f"slider_{tab}_{meal}_{i}"

            )

            final=int(
                kcal*g/gram
            )

            st.caption(
                f"{g} g"
            )

            st.success(
                f"{final} kcal"
            )

            if st.button(

                "Add Meal",

                key=f"add_{tab}_{meal}_{i}"

            ):

                st.session_state.meal_log[
                    "Breakfast"
                ].append(

                    (

                        meal,

                        final

                    )

                )

                st.success(
                    "Meal Added ❤️"
                )

                st.switch_page(
                    "pages/tracker.py"
                )

            st.markdown(
                "</div>",
                unsafe_allow_html=True
            )

# ---------------- TABS ----------------

with tab1:

    show("fav")

with tab2:

    show("food")

with tab3:

    show("meal")

# ---------------- CREATE OWN ----------------

with tab4:

    st.subheader(
        "Create Own Meal"
    )

    meal_name=st.text_input(

        "Meal Name",

        key="own_name"

    )

    meal_kcal=st.number_input(

        "Calories",

        0,

        3000,

        200,

        key="own_kcal"

    )

    meal_gram=st.number_input(

        "Grams",

        50,

        1000,

        100,

        key="own_gram"

    )

    st.caption(
        f"{meal_gram} g"
    )

    if st.button(

        "Add Own Meal",

        key="own_breakfast"

    ):

        if meal_name.strip():


            st.session_state.meal_log[
                "Breakfast"
            ].append(

                (

                    meal_name,

                    meal_kcal

                )

            )

            st.success(
                "Own Meal Added ❤️"
            )

            st.switch_page(
                "pages/tracker.py"
            )

        else:

            st.warning(
                "Enter meal name"
            )

# ---------------- SUMMARY ----------------

st.divider()

st.subheader(
"Today's Breakfast"
)

total=0

for meal in st.session_state.meal_log[
"Breakfast"
]:

    st.write(

f"""

🍽 {meal[0]}

🔥 {meal[1]} kcal

"""

)

    total+=meal[1]

st.metric(

"Breakfast Total",

total

)