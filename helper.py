from python_terraform import Terraform

def format_terraform_plan_output(plan: tuple) -> list:
    # pull json from tuple
    terraform_plan_json = plan[1]
    # format json and remove \n
    formatted_plan = terraform_plan_json.split('\n')

    return formatted_plan