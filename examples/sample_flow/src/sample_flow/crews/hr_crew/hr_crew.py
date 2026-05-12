from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
import os
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class HrCrew():
    """HrCrew crew"""

    agents: list[BaseAgent]
    tasks: list[Task]
    llm: LLM = LLM(model=os.environ["MODEL"], 
                   temperature=0.3,
                   base_url=os.environ["OPENAI_API_BASE"],
                   api_key=os.environ["OPENAI_API_KEY"])

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def hr_specialist1(self) -> Agent:
        return Agent(
            config=self.agents_config['hr_specialist1'], # type: ignore[index]
            llm=self.llm,
            verbose=True
        )

    @agent
    def hr_specialist2(self) -> Agent:
        return Agent(
            config=self.agents_config['hr_specialist2'], # type: ignore[index]
            llm=self.llm,
            verbose=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def cv_review_task(self) -> Task:
        return Task(
            config=self.tasks_config['cv_review_task'], # type: ignore[index]
        )

    @task
    def debate_task(self) -> Task:
        return Task(
            config=self.tasks_config['debate_task'], # type: ignore[index]
            # output_file='output/debate.md'
        )
    
    @task
    def final_reconciliation_task(self) -> Task:
        return Task(
            config=self.tasks_config['final_reconciliation_task']
        )

    @crew
    def crew(self) -> Crew:
        """Creates the HrCrew crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
