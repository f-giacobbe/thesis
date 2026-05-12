#!/usr/bin/env python
from pathlib import Path

from pydantic import BaseModel

from crewai.flow import Flow, listen, start

from sample_flow.crews.hr_crew.hr_crew import HrCrew

from pypdf import PdfReader


def get_cv_text(filepath):    
    reader = PdfReader(filepath)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text


class HrState(BaseModel):
    cv_file: str = f"{Path('input')}/cv.pdf"
    cv: str = ""
    debate: str = ""


class HrFlow(Flow[HrState]):

    @start()
    def pull_cv(self, crewai_trigger_payload: dict = None):
        print("Getting cv")
        print(self.state.cv_file)

        self.state.cv = get_cv_text(self.state.cv_file) 


    @listen(pull_cv)
    def cv_review(self):
        result = (
            HrCrew()
            .crew()
            .kickoff(inputs={"cv": self.state.cv})
        )

        # Combine all tasks from this specific crew execution
        full_text = ""
        for task_out in result.tasks_output:
            full_text += f"### Task: {task_out.name}\n{task_out.raw}\n\n"
                                    #{task_out.description}\n
        
        self.state.debate = full_text


    @listen(cv_review)
    def save_content(self):
        print("Saving content")
        output_dir = Path("output")
        output_dir.mkdir(exist_ok=True)
        with open(output_dir / "debate.md", "w") as f:
            f.write(self.state.debate)
        print("Debate saved to output/debate.md")


def kickoff():
    hr_flow = HrFlow()
    hr_flow.kickoff()


def plot():
    hr_flow = HrFlow()
    hr_flow.plot()


def run_with_trigger():
    """
    Run the flow with trigger payload.
    """
    import json
    import sys

    # Get trigger payload from command line argument
    if len(sys.argv) < 2:
        raise Exception("No trigger payload provided. Please provide JSON payload as argument.")

    try:
        trigger_payload = json.loads(sys.argv[1])
    except json.JSONDecodeError:
        raise Exception("Invalid JSON payload provided as argument")

    # Create flow and kickoff with trigger payload
    # The @start() methods will automatically receive crewai_trigger_payload parameter
    hr_flow = HrFlow()

    try:
        result = hr_flow.kickoff({"crewai_trigger_payload": trigger_payload})
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the flow with trigger: {e}")


if __name__ == "__main__":
    kickoff()
