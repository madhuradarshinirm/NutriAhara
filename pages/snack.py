import streamlit as st

# ---------------- PAGE ----------------

st.set_page_config(
page_title="Snack",
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

("Apple",80,100),
("Banana",100,120),
("Tea",70,200),
("Coffee",90,200),
("Juice",120,250),
("Chips",180,50),
("Milk",150,250),
("Sandwich",240,180)

]

# ---------------- STYLE ----------------

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

.card{

background:white;

padding:25px;

border-radius:20px;

margin-top:20px;

}

</style>

""",

unsafe_allow_html=True

)

# ---------------- TOP ----------------

c1,c2=st.columns([8,1])

with c1:

    if st.button(
    "← Snack"
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

placeholder=
"🔍 Search snack"

)

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

            st.subheader(
            meal
            )

            g=st.slider(

            "Serving",

            50,

            600,

            gram,

            key=f"{tab}_{meal}_{i}"

            )

            final=int(
            kcal*g/gram
            )

            st.success(
f"{final} kcal"
)

            if st.button(

            "Add Meal",

            key=f"add_{tab}_{meal}_{i}"

            ):

                st.session_state.meal_log[
                "Snack"
                ].append(

                (

                meal,

                final

                )

                )

                st.success(
                "Added ❤️"
                )

                st.switch_page(
                "pages/tracker.py"
                )

            st.markdown(
            "</div>",
            unsafe_allow_html=True
            )

# ----------------

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

    name=st.text_input(
    "Meal Name",
    key="own"
    )

    kcal=st.number_input(

    "Calories",

    0,

    3000,

    200

    )

    grams=st.number_input(

    "Grams",

    50,

    1000,

    100

    )

    if st.button(

    "Add Own Meal",

    key="ownmeal"

    ):

        st.session_state.meal_log[
        "Snack"
        ].append(

        (

        name,

        kcal

        )

        )

        st.success(
        "Own Meal Added ❤️"
        )

        st.switch_page(
        "pages/tracker.py"
        )

# ---------------- SUMMARY ----------------

st.divider()

st.subheader(
"Today's Snack"
)

total=0

for meal in st.session_state.meal_log[
"Snack"
]:

    st.write(
f"""
🍽 {meal[0]}
—
🔥 {meal[1]}
"""
)

    total+=meal[1]

st.metric(
"Snack Total",
total
)