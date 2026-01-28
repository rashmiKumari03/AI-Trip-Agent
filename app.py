# ==================================================
# ENV & RUNTIME CONFIG
# ==================================================
import os

os.environ["CREWAI_TELEMETRY"] = "false"
os.environ["CREWAI_DISABLE_TELEMETRY"] = "true"
os.environ["OTEL_SDK_DISABLED"] = "true"


# ==================================================
# STANDARD LIBRARY
# ==================================================
from datetime import date
import time


# ==================================================
# THIRD PARTY
# ==================================================
from dotenv import load_dotenv
import streamlit as st


# ==================================================
# INTERNAL
# ==================================================
from src.crew import TripCrew


# ==================================================
# LOAD ENV
# ==================================================
load_dotenv(override=True)


# ==================================================
# PAGE CONFIG
# ==================================================
st.set_page_config(
    page_title="TripSathi AI",
    layout="wide",
    page_icon="🌍",
)


# ==================================================
# GLOBAL STYLES
# ==================================================
st.markdown(
    """
    <style>

    /* MAIN BACKGROUND */
    .stApp {
        background: linear-gradient(180deg,#050816,#0b122a,#0f172a);
    }

    /* SIDEBAR */
    section[data-testid="stSidebar"] {
        width:360px !important;
        background: linear-gradient(180deg,#020617,#0a043c);
        border-right:3px solid #22d3ee;
        box-shadow:0 0 20px rgba(34,211,238,.35);
        padding-top:1rem;
    }

    section[data-testid="stSidebar"] * {
        color:white !important;
    }

    section[data-testid="stSidebar"] input,
    section[data-testid="stSidebar"] textarea,
    section[data-testid="stSidebar"] select {
        background:rgba(255,255,255,0.07) !important;
    }

    /* NEON SECTION TITLE */
    .sidebar-section-title {
        font-size:15px;
        font-weight:700;
        color:#67e8f9;
        margin-top:1rem;
        margin-bottom:.4rem;
        border-bottom:1px solid #22d3ee;
        padding-bottom:4px;
        text-shadow:0 0 6px rgba(34,211,238,.6);
    }

    /* MAIN TEXT */
    .main * {
        color:white !important;
    }

    h1,h2,h3 {
        color:white !important;
        font-weight:800;
    }

    .trip-tagline {
        color:#c7d2fe;
        font-size:18px;
    }

    /* BUTTON */
    .stButton > button {
        background:linear-gradient(135deg,#06b6d4,#6366f1);
        border-radius:14px;
        padding:.6rem 1.9rem;
        font-size:17px;
        border:none;
        box-shadow:0 0 18px rgba(99,102,241,.7);
    }

    .stButton > button:hover {
        background:linear-gradient(135deg,#22d3ee,#818cf8);
        transform:translateY(-2px);
    }

    /* DIVIDER */
    hr {
        border:none;
        height:2px;
        background:linear-gradient(90deg,#22d3ee,#6366f1,#22d3ee);
        margin:24px 0;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ==================================================
# IMAGES
# ==================================================
HERO_IMAGES = [
    "https://images.pexels.com/photos/338515/pexels-photo-338515.jpeg",
    "https://images.pexels.com/photos/460672/pexels-photo-460672.jpeg",
    "https://images.pexels.com/photos/210186/pexels-photo-210186.jpeg",
    "https://images.pexels.com/photos/753626/pexels-photo-753626.jpeg",
]


# ==================================================
# MAIN
# ==================================================
def main():

    # ---------------- IMAGE SLIDER ----------------
    slider_placeholder = st.empty()

    SLIDER_HEIGHT = 320
    SIDE_MARGIN = 22
    MAX_WIDTH = 1400

    for _ in range(2):
        for img in HERO_IMAGES:

            slider_placeholder.markdown(
                f"""
                <div style="
                    width:100%;
                    display:flex;
                    justify-content:center;
                    margin:{SIDE_MARGIN}px 0;">
                    <div style="
                        width:100%;
                        max-width:{MAX_WIDTH}px;
                        height:{SLIDER_HEIGHT}px;
                        margin:{SIDE_MARGIN}px;
                        overflow:hidden;
                        border-radius:20px;
                        box-shadow:0 0 40px rgba(34,211,238,.45);">
                        <img src="{img}" style="width:100%;height:100%;object-fit:cover;">
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            time.sleep(1.2)

    # ---------------- TITLE ----------------
    st.markdown(
        """
        <h1>TripSathi AI ✈️</h1>
        <div class="trip-tagline">
            <strong>Your Smart Travel Companion for Every Journey</strong><br>
        From relaxing vacations to important business trips, TripSathi AI designs personalized plans with expert insights, smart itineraries, and clear budgeting — so you travel with confidence.

        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    # ---------------- SIDEBAR ----------------
    with st.sidebar:

        st.markdown('<div class="sidebar-section-title">Journey Information</div>', unsafe_allow_html=True)

        departure_city = st.text_input("Departure Location")
        destination_city = st.text_input("Destination")

        start_date = st.date_input(
            "Arrival Date",
            min_value=date.today(),
            value=date.today(),
        )

        end_date = st.date_input(
            "Return Date",
            min_value=start_date,
            value=start_date,
        )

        duration = (end_date - start_date).days or 1
        st.caption(f"🗓️ Trip Duration: **{duration} days**")

        st.markdown('<div class="sidebar-section-title">Travel Preferences</div>', unsafe_allow_html=True)

        travel_type = st.selectbox(
            "Purpose of Travel",
            ["Leisure","Business","Adventure","Cultural","Exploration"],
        )

        interests = st.multiselect(
            "Key Interests",
            [
                "History & Culture",
                "Food & Cuisine",
                "Nature & Landscapes",
                "Art & Museums",
                "Shopping",
                "City Sightseeing",
                "Beaches",
                "Mountains",
            ],
        )

        pace = st.selectbox(
            "Travel Pace",
            ["Relaxed","Moderate","Fast-Paced"],
        )

        st.markdown('<div class="sidebar-section-title">Logistics</div>', unsafe_allow_html=True)

        budget = st.selectbox(
            "Budget Level",
            ["Economy","Mid-range","Premium","Luxury"],
        )

        travelers = st.selectbox(
            "Number of Travelers",
            ["Solo","Couple","Family","Group"],
        )

        accommodation = st.selectbox(
            "Accommodation Type",
            [
                "Budget Hotel",
                "Mid-range Hotel",
                "Luxury Hotel",
                "Serviced Apartment",
                "Resort",
            ],
        )

        food_pref = st.multiselect(
            "Food Preferences",
            [
                "Vegetarian",
                "Vegan",
                "Local Cuisine",
                "Street Food",
                "Fine Dining",
                "No Restrictions",
            ],
        )

        special_notes = st.text_area("Special Requests / Notes")

    # ---------------- GENERATE ----------------
    generate_clicked = st.button("Generate My Trip Plan", key="generate_btn")

    if generate_clicked:

        inputs = {
            "departure_city": departure_city,
            "destination_city": destination_city,
            "departure_date": str(start_date),
            "return_date": str(end_date),
            "duration": duration,
            "travel_type": travel_type,
            "interests": interests,
            "pace": pace,
            "budget": budget,
            "travelers": travelers,
            "accommodation": accommodation,
            "food_pref": food_pref,
            "notes": special_notes,
        }

        with st.spinner("TripSathi AI is preparing your personalized journey..."):
            crew_output = TripCrew(inputs).run()

        st.subheader("Your Personalized Travel Plan")

        tab1, tab2, tab3, tab4 = st.tabs(
            [
                "Recommended Destinations",
                "Destination Insights",
                "Daily Itinerary",
                "Budget Overview",
            ]
        )

        with tab1:
            st.markdown(crew_output.get("city_selection","No data available."))

        with tab2:
            st.markdown(crew_output.get("city_research","No data available."))

        with tab3:
            st.markdown(crew_output.get("itinerary","No data available."))

        with tab4:
            st.markdown(crew_output.get("budget","No data available."))


if __name__ == "__main__":
    main()
