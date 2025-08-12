from crewai import Agent
from textwrap import dedent
from langchain_openai import ChatOpenAI

from tools.search_tools import SearchTools
from tools.calculator_tools import CalculatorTools

"""
Creating Agents Cheat Sheet:
- Think like a boss: Work backwards from the goal and decide which 'employees'
  you need to hire to get the job done.
- Define the Captain (lead agent) who orients the crew toward the goal.
- Define which specialists the captain needs to communicate with and delegate tasks to.
- Build a top-down structure for efficiency.

Goal:
- Create a 7-day travel itinerary with detailed per-day plans,
  including budget, packing suggestions, and safety tips.

Captain/Manager/Boss:
- Expert Travel Agent

Employees/Experts:
- City Selection Expert
- Local Tour Guide

Notes:
- Agents should be results-driven and have a clear, actionable goal.
- Role: their job title (what they *do*).
- Goal: measurable, specific, and actionable.
- Backstory: like their résumé, highlighting skills and expertise.
"""

class TravelAgents:
    def __init__(self):
        # Default to GPT-3.5 for faster, more cost-effective performance
        self.OpenAIGPT35 = ChatOpenAI(
            model_name="gpt-3.5-turbo", 
            temperature=0.7
        )

    def expert_travel_agent(self):
        return Agent(
            role="Expert Travel Agent",
            backstory=dedent("""
                A seasoned professional in travel planning and logistics, 
                with over 20 years of experience designing tailored itineraries 
                for families, solo travelers, and corporate clients. 
                Skilled at balancing budget, safety, and unique travel experiences.
            """),
            goal=dedent("""
                Design a 7-day travel itinerary that includes:
                - Daily activity schedules
                - Budget breakdowns
                - Packing suggestions
                - Safety tips
                - Recommended restaurants and accommodations
            """),
            tools=[
                SearchTools.search_internet,
                CalculatorTools.calculate
            ],
            verbose=True,
            llm=self.OpenAIGPT35
        )

    def city_selection_expert(self):
        return Agent(
            role="City Selection Expert",
            backstory=dedent("""
                Data-driven travel researcher with expertise in evaluating destinations 
                based on climate, seasonal events, cost efficiency, and traveler preferences. 
                Experienced in filtering dozens of options down to the single best choice.
            """),
            goal=dedent("""
                Analyze multiple potential cities and select the best destination 
                based on weather, seasonality, travel cost, and traveler interests.
            """),
            tools=[SearchTools.search_internet],
            verbose=True,
            llm=self.OpenAIGPT35
        )

    def local_tour_guide(self):
        return Agent(
            role="Local Tour Guide",
            backstory=dedent("""
                A well-connected local expert with deep knowledge of the city's 
                history, culture, hidden gems, and insider-only recommendations. 
                Skilled at personalizing advice to traveler preferences.
            """),
            goal=dedent("""
                Provide detailed insights on attractions, cultural norms, 
                must-visit landmarks, local dining, and special events in the selected city.
            """),
            tools=[SearchTools.search_internet],
            verbose=True,
            llm=self.OpenAIGPT35
        )
