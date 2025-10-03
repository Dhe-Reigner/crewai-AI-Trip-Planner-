from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class Mycrew():
    """Mycrew crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def flight_Agent(self) -> Agent:
        return Agent(
            config=self.agents_config['flight_Agent'], # type: ignore[index]
            verbose=True
        )

    @agent
    def accommodation_Agent(self) -> Agent:
        return Agent(
            config=self.agents_config['accommodation_Agent'], # type: ignore[index]
            verbose=True
        )
    
    @agent
    def itinerary_Agent(self) -> Agent:
        return Agent(
            config=self.agents_config['itinerary_Agent'], # type: ignore[index]
            verbose=True
        )
    
    @agent
    def local_info_Agent(self) -> Agent:
        return Agent(
            config=self.agents_config['local_info_Agent'], # type: ignore[index]
            verbose=True
        )
    
    @agent
    def budget_Agent(self) -> Agent:
        return Agent(
            config=self.agents_config['budget_Agent'], # type: ignore[index]
            verbose=True
        )
    
    @agent
    def planner_Agent(self) -> Agent:
        return Agent(
            config=self.agents_config['planner_Agent'], # type: ignore[index]
            verbose=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def flight_task(self) -> Task:
        return Task(
            config=self.tasks_config['flight_task'], # type: ignore[index]
            output_file='flight.md'
        )

    @task
    def accommodation_task(self) -> Task:
        return Task(
            config=self.tasks_config['accommodation_task'], # type: ignore[index]
            output_file='accomodation.md'
        )
    
    @task
    def itinerary_task(self) -> Task:
        return Task(
            config=self.tasks_config['itinerary_task'], # type: ignore[index]
            output_file='itinery.md'
        )
    
    @task
    def local_info_task(self) -> Task:
        return Task(
            config=self.tasks_config['local_info_task'], # type: ignore[index]
            output_file='local_info.md'
        )
    
    @task
    def budget_task(self) -> Task:
        return Task(
            config=self.tasks_config['budget_task'], # type: ignore[index]
            output_file='budget.md'
        )
    
    @task
    def planner_task(self) -> Task:
        return Task(
            config=self.tasks_config['planner_task'], # type: ignore[index]
            output_file='planner.md'
        )
    @crew
    def crew(self) -> Crew:
        """Creates the Mycrew crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge


        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )


  
