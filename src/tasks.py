from crewai import Task


class TripTasks:

    # --------------------------------------------------
    # DESTINATION STRATEGY
    # --------------------------------------------------

    def city_selection_task(self, agent, inputs):
        return Task(
            name="city_selection",
            description=(
                "You are a senior travel strategist.\n\n"
                "Analyze the following traveler profile and recommend the most suitable "
                "international destinations.\n\n"

                f"Departure Location: {inputs.get('departure_city')}\n"
                f"Destination Preference (if any): {inputs.get('destination_city')}\n"
                f"Travel Dates: {inputs.get('departure_date')} to {inputs.get('return_date')}\n"
                f"Trip Duration: {inputs.get('duration')} days\n"
                f"Purpose of Travel: {inputs.get('travel_type')}\n"
                f"Interests: {inputs.get('interests')}\n"
                f"Travel Pace: {inputs.get('pace')}\n"
                f"Budget Tier: {inputs.get('budget')}\n"
                f"Travelers: {inputs.get('travelers')}\n"
                f"Accommodation Preference: {inputs.get('accommodation')}\n"
                f"Food Preferences: {inputs.get('food_pref')}\n"
                f"Special Notes: {inputs.get('notes')}\n\n"

                "OUTPUT FORMAT:\n"
                "- Recommend exactly 3 destinations.\n"
                "- For each destination include:\n"
                "  • Why it fits these preferences\n"
                "  • Ideal travel season\n"
                "  • Estimated flight duration from departure city\n"
                "  • Type of traveler it suits\n"
            ),
            agent=agent,
            expected_output=(
                "Three numbered destination recommendations with short analytical paragraphs."
            ),
        )

    # --------------------------------------------------
    # LOCAL INTELLIGENCE
    # --------------------------------------------------

    def city_research_task(self, agent, city):
        return Task(
            name="city_research",
            description=(
                f"You are now researching the destination: {city}.\n\n"
                "Provide a professional briefing covering:\n"
                "- Top attractions & landmarks\n"
                "- Neighborhoods to stay in\n"
                "- Local cuisine highlights\n"
                "- Cultural etiquette & safety notes\n"
                "- Transport systems\n"
                "- Weather expectations\n"
            ),
            agent=agent,
            expected_output="Well-structured travel guide with headings and bullet points.",
        )

    # --------------------------------------------------
    # ITINERARY DESIGN
    # --------------------------------------------------

    def itinerary_creation_task(self, agent, inputs, city):
        return Task(
            name="itinerary",
            description=(
                f"Design a detailed {inputs['duration']}-day itinerary for {city}.\n\n"

                f"Traveler Profile:\n"
                f"- Travelers: {inputs.get('travelers')}\n"
                f"- Travel Pace: {inputs.get('pace')}\n"
                f"- Interests: {inputs.get('interests')}\n"
                f"- Food Preferences: {inputs.get('food_pref')}\n"
                f"- Accommodation Type: {inputs.get('accommodation')}\n\n"

                "INSTRUCTIONS:\n"
                "- Create day-by-day schedules\n"
                "- Morning / Afternoon / Evening blocks\n"
                "- Include transit notes\n"
                "- Balance sightseeing with rest\n"
                "- Add dining suggestions\n"
            ),
            agent=agent,
            expected_output="Daily itinerary grouped by day with time blocks.",
        )

    # --------------------------------------------------
    # FINANCIAL PLANNING
    # --------------------------------------------------

    def budget_planning_task(self, agent, inputs, itinerary):
        return Task(
            name="budget",
            description=(
                "Prepare a professional travel budget estimate.\n\n"

                f"Budget Tier: {inputs['budget']}\n"
                f"Travelers: {inputs.get('travelers')}\n"
                f"Trip Duration: {inputs['duration']} days\n"
                f"Accommodation Type: {inputs.get('accommodation')}\n\n"

                "Include cost ranges for:\n"
                "- Flights\n"
                "- Accommodation\n"
                "- Daily transport\n"
                "- Activities & attractions\n"
                "- Meals\n"
                "- Insurance & contingency\n\n"

                "Summarize with an estimated total per person."
            ),
            agent=agent,
            context=[itinerary],
            expected_output="Itemized cost table with final estimated totals.",
        )
