import re
import click

def parse_state_file(plan: list) -> bool:
    drift_detection_pattern = re.compile(r'("type":\s*"planned_change")')
    
    return any(re.search(drift_detection_pattern, line) for line in plan)

def format_terraform_plan_output(plan: tuple) -> list:
    # pull json from tuple
    terraform_plan_json = plan[1]
    # format json and remove \n
    formatted_plan = terraform_plan_json.split('\n')

    return formatted_plan

def state_drift_detection(plan: list) -> None:
        
        formatted_terraform_plan_output = format_terraform_plan_output(plan=plan)
        state_drift_detected = parse_state_file(plan=formatted_terraform_plan_output)

        # TODO: remidation/logging/alerting??
        if state_drift_detected:
            click.echo("State drift detected..")
        else:
            click.echo("No state drift..")