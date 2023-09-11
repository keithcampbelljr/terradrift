import click
from drift_detection import state_drift_detection
from python_terraform import Terraform

def run_drift_detect() -> None:
    try: 
        terraform = Terraform()
        terraform.init()
        terraform_plan = terraform.plan(json=True)

        state_drift_detection(plan=terraform_plan)

    except Exception as e:
        click.echo(f"An error occurred: {str(e)}")

@click.group()
def cli():
    pass

@cli.command()
def detect():
    run_drift_detect()

if __name__ == "__main__":
    cli()
