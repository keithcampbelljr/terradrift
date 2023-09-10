import re

def format_terraform_plan(plan: tuple) -> list:
    # pull json from tuple
    terraform_plan_json = plan[1]
    # format json and remove \n
    formatted_plan = terraform_plan_json.split('\n')

    return formatted_plan


def detect_state_drift(plan: list) -> None:
    
    drift_detection_pattern = re.compile(r'("type":\s*"planned_change")')

    for line in plan:
        if re.search(drift_detection_pattern, line):
            print("State drift detected..")
