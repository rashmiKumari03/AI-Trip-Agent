from crewai import Agent
from config.llm_config import get_llm


class TripAgents:
    def __init__(self):

        self.llm = get_llm()

        # Connectivity check
        try:
            resp = self.llm.invoke(
                [{"role": "user", "content": "Reply only with: LLM is working."}]
            )

            if getattr(resp, "content", None):
                print("[TripSathi] LLM connection OK")
            else:
                print("[TripSathi] LLM responded but empty content")

        except Exception as e:
            print("[TripSathi] LLM initialization failed:", e)
            raise

    # --------------------------------------------------
    # CITY STRATEGIST
    # --------------------------------------------------

    def city_selector_agent(self):
        return Agent(
            role="Global Destination Strategist",
            goal=(
                "Recommend the most suitable global destinations using departure city, "
                "travel dates, interests, pace, group type, and budget tier."
            ),
            backstory=(
                "A senior travel strategist who designs international journeys for "
                "business leaders, families, explorers, and luxury travelers. "
                "Expert in seasonality, visas, flight routing, and cultural fit."
            ),
            llm=self.llm,
            verbose=True,
        )

    # --------------------------------------------------
    # LOCAL INTELLIGENCE
    # --------------------------------------------------

    def local_expert_agent(self):
        return Agent(
            role="Local Destination Intelligence Specialist",
            goal=(
                "Provide deep, practical insights about destinations including attractions, "
                "neighborhoods, safety, transit, cuisine, and etiquette."
            ),
            backstory=(
                "A former tour director and cultural researcher who has lived in multiple "
                "countries and advises travelers on how to experience destinations "
                "authentically and safely."
            ),
            llm=self.llm,
            verbose=True,
        )

    # --------------------------------------------------
    # ITINERARY ARCHITECT
    # --------------------------------------------------

    def travel_planner_agent(self):
        return Agent(
            role="Itinerary Architect",
            goal=(
                "Create realistic, time-optimized day-by-day plans aligned with "
                "travel pace, dates, group type, and interests."
            ),
            backstory=(
                "An elite operations planner who builds seamless global itineraries "
                "covering transport, attractions, rest periods, and dining strategy."
            ),
            llm=self.llm,
            verbose=True,
        )

    # --------------------------------------------------
    # FINANCIAL STRATEGIST
    # --------------------------------------------------

    def budget_manager_agent(self):
        return Agent(
            role="Travel Financial Strategist",
            goal=(
                "Construct accurate budget frameworks across flights, hotels, meals, "
                "local transport, activities, and contingency reserves."
            ),
            backstory=(
                "A former airline pricing analyst and hospitality finance consultant "
                "who helps travelers maximize comfort within financial limits."
            ),
            llm=self.llm,
            verbose=True,
        )
