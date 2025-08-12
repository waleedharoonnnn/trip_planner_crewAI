from crewai import Task
from textwrap import dedent

"""
Creating Tasks Cheat Sheet:
- Begin with the end in mind. Identify the specific outcome your tasks are aiming to achieve.
- Break down the outcome into actionable tasks, assigning each task to the appropriate agent.
- Ensure tasks are descriptive, providing clear instructions and expected deliverables.

Goal:
- Develop a detailed itinerary, including city selection, attractions, and practical travel advice.

Key Steps for Task Creation:
1. Identify the Desired Outcome: Define what success looks like for your project.
    - A detailed 7 day travel itenerary.

2. Task Breakdown: Divide the goal into smaller, manageable tasks that agents can execute.
    - Itenerary Planning: develop a detailed plan for each day of the trip.
    - City Selection: Analayze and pick the best cities to visit.
    - Local Tour Guide: Find a local expert to provide insights and recommendations.

3. Assign Tasks to Agents: Match tasks with agents based on their roles and expertise.

4. Task Description Template:
  - Use this template as a guide to define each task in your CrewAI application. 
  - This template helps ensure that each task is clearly defined, actionable, and aligned with the specific goals of your project.

  Template:
  ---------
  def [task_name](self, agent, [parameters]):
      return Task(description=dedent(f'''
      **Task**: [Provide a concise name or summary of the task.]
      **Description**: [Detailed description of what the agent is expected to do, including actionable steps and expected outcomes. This should be clear and direct, outlining the specific actions required to complete the task.]

      **Parameters**: 
      - [Parameter 1]: [Description]
      - [Parameter 2]: [Description]
      ... [Add more parameters as needed.]

      **Note**: [Optional section for incentives or encouragement for high-quality work. This can include tips, additional context, or motivations to encourage agents to deliver their best work.]

      '''), agent=agent)

"""




"""
Travel Task Definitions
-----------------------
This module defines all the tasks required for building a complete
7-day travel itinerary, including city selection, local insights,
and detailed day-by-day planning.

Guiding Principles:
1. Begin with the end in mind — every task should clearly contribute
   to the overall travel planning goal.
2. Keep instructions actionable — agents should know exactly
   what to produce.
3. Provide motivation — encourage agents to go above and beyond.
"""

class TravelTasks:
    def __tip_section(self):
        """Friendly motivational bonus to encourage high-quality work."""
        return "Deliver your BEST work and earn a $10,000 commission!"

    def plan_itinerary(self, agent, city, travel_dates, interests):
        """Create a complete 7-day travel plan for the chosen city."""
        return Task(
            description=dedent(f"""
                **Task**: Develop a 7-Day Travel Itinerary

                **Description**:
                Using the provided city and traveler details, create a complete
                7-day travel itinerary. The plan should include:
                - Day-by-day schedule with morning, afternoon, and evening activities
                - Recommended attractions, restaurants, and local experiences
                - Weather forecasts for each day
                - Packing suggestions tailored to the trip and weather
                - Budget breakdown (accommodation, food, activities, transport)
                - Actual hotel, restaurant, and attraction names (no placeholders)

                **Parameters**:
                - City: {city}
                - Trip Dates: {travel_dates}
                - Traveler Interests: {interests}

                **Note**:
                {self.__tip_section()}
            """),
            agent=agent,
        )

    def identify_city(self, agent, origin, cities, interests, travel_dates):
        """Select the best city for the trip based on data and preferences."""
        return Task(
            description=dedent(f"""
                **Task**: Identify the Optimal Travel Destination

                **Description**:
                Analyze the provided list of candidate cities and select
                the best one based on:
                - Weather conditions during the travel period
                - Seasonal and cultural events
                - Flight costs from origin
                - Overall trip affordability
                - Alignment with traveler interests

                Deliver a detailed recommendation including:
                - Chosen city with justification
                - Current weather forecast
                - Upcoming events during the travel period
                - Example flight costs
                - Key attractions that match traveler interests

                **Parameters**:
                - Origin: {origin}
                - Candidate Cities: {cities}
                - Interests: {interests}
                - Trip Dates: {travel_dates}

                **Note**:
                {self.__tip_section()}
            """),
            agent=agent,
        )

    def gather_city_info(self, agent, city, travel_dates, interests):
        """Collect in-depth local insights for the chosen city."""
        return Task(
            description=dedent(f"""
                **Task**: Compile an In-depth City Guide

                **Description**:
                Research and produce a detailed city guide including:
                - Must-visit attractions and landmarks
                - Hidden gems and local favorites
                - Cultural customs and etiquette tips
                - Special events happening during travel dates
                - Local transportation options
                - Estimated daily costs
                - Weather forecast for trip duration

                Focus on actionable insights that can directly inform
                the itinerary planning process.

                **Parameters**:
                - City: {city}
                - Interests: {interests}
                - Trip Dates: {travel_dates}

                **Note**:
                {self.__tip_section()}
            """),
            agent=agent,
        )
