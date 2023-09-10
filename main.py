from python_terraform import Terraform
from drift_detection import detect_state_drift, format_terraform_plan

terraform = Terraform()

terraform.init()
terraform_plan = terraform.plan(json=True)

sanitized_terraform_plan = format_terraform_plan(plan=terraform_plan)
detect_state_drift(plan=sanitized_terraform_plan)

