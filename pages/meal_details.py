import streamlit as st

st.set_page_config(
page_title="Meal Details"
)

meal=st.session_state.get(
"selected",
"Unknown Meal"
)

st.title(
"🍽 Meal Details"
)

st.subheader(
meal
)

st.write(
"Calories : 320 kcal"
)

st.write(
"Protein : 6 g"
)

st.write(
"Serving : 250 g"
)

if st.button(
"Add Meal"
):

    st.session_state.calories=(
        st.session_state.get(
        "calories",
        0
        )
        +
        320
    )

    st.success(
    "Meal Added"
    )

if st.button(
"← Tracker"
):

    st.switch_page(
    "pages/tracker.py"
    )