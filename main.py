from python_terraform import Terraform
from drift_detection import detect_state_drift
from helper import format_terraform_plan_output

terraform = Terraform()

try:

    terraform.init()
    terraform_plan = terraform.plan(json=True)

    formatted_terraform_plan_output = format_terraform_plan_output(plan=terraform_plan)
    state_drift_detected = detect_state_drift(plan=formatted_terraform_plan_output)
    
    if state_drift_detected:
        print("state drift detected..")
    else:
        print("no state drift..")

except Exception as e:
    print(f"An error occurred: {str(e)}")

