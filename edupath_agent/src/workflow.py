from typing import Dict, Any
from google.adk.agents import SequentialAgent, ParallelAgent, LoopAgent
from src.agents.definitions import scout_agent, tutor_agent, planner_agent, critic_agent, liaison_agent

def create_edupath_workflow():
    """
    Composes the individual agents into a Graph.
    Pattern: Parallel -> Loop -> Sequential
    """

    # 1. Parallel Phase: Scout & Tutor work simultaneously
    parallel_phase = ParallelAgent(
        name="Research_and_Grading_Phase",
        sub_agents=[scout_agent, tutor_agent]
    )

    # 2. Loop Phase: Planning & Critiquing
    # The loop will continue until:
    # - max_iterations (3) is reached, OR
    # - One of the agents calls a tool that sets escalate=True
    planning_loop = LoopAgent(
        name="Planning_Loop",
        sub_agents=[planner_agent, critic_agent],
        max_iterations=3
    )

    # 3. Root Workflow: Connects all phases
    root_workflow = SequentialAgent(
        name="EduPath_Root",
        sub_agents=[parallel_phase, planning_loop, liaison_agent]
    )

    return root_workflow