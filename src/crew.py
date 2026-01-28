from crewai import Crew

from .agents import TripAgents
from .tasks import TripTasks


class TripCrew:
    def __init__(self, inputs):
        self.inputs = inputs

    def run(self):

        print("\n[TripSathi] Starting Trip Planning Pipeline...\n")

        # ---------------------------------
        # INITIALIZE AGENTS
        # ---------------------------------

        agents = TripAgents()
        tasks = TripTasks()

        city_selector = agents.city_selector_agent()
        print("[TripSathi] ✓ City Selection Agent ready")

        local_expert = agents.local_expert_agent()
        print("[TripSathi] ✓ Local Destination Expert ready")

        travel_planner = agents.travel_planner_agent()
        print("[TripSathi] ✓ Travel Planner Agent ready")

        budget_manager = agents.budget_manager_agent()
        print("[TripSathi] ✓ Budget Specialist Agent ready")

        # ---------------------------------
        # TASK CREATION
        # ---------------------------------

        print("\n[TripSathi] Creating mission tasks...\n")

        select_cities = tasks.city_selection_task(
            city_selector,
            self.inputs,
        )

        # ⚠️ TEMP — can later parse from city_selection output
        selected_city = (
            self.inputs.get("destination_city")
            if self.inputs.get("destination_city")
            else "Paris"
        )

        research_city = tasks.city_research_task(
            local_expert,
            selected_city,
        )

        create_itinerary = tasks.itinerary_creation_task(
            travel_planner,
            self.inputs,
            selected_city,
        )

        plan_budget = tasks.budget_planning_task(
            budget_manager,
            self.inputs,
            create_itinerary,
        )

        # ---------------------------------
        # EXECUTION
        # ---------------------------------

        print("[TripSathi] 🚀 Executing agent crew...\n")

        crew = Crew(
            agents=[
                city_selector,
                local_expert,
                travel_planner,
                budget_manager,
            ],
            tasks=[
                select_cities,
                research_city,
                create_itinerary,
                plan_budget,
            ],
            verbose=True,
        )

        result = crew.kickoff()

        print("\n[TripSathi] ✅ Crew execution completed\n")

        # ---------------------------------
        # RESULT PARSING (SAFE)
        # ---------------------------------

        final_result = {
            "city_selection": "No city selection found.",
            "city_research": "No city research found.",
            "itinerary": "No itinerary generated.",
            "budget": "No budget breakdown available.",
        }

        if hasattr(result, "tasks_output"):

            tasks_list = result.tasks_output

            if len(tasks_list) > 0:
                final_result["city_selection"] = tasks_list[0].raw

            if len(tasks_list) > 1:
                final_result["city_research"] = tasks_list[1].raw

            if len(tasks_list) > 2:
                final_result["itinerary"] = tasks_list[2].raw

            if len(tasks_list) > 3:
                final_result["budget"] = tasks_list[3].raw

        return final_result
