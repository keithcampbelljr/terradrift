import re

def detect_state_drift(plan: list) -> bool:
    drift_detection_pattern = re.compile(r'("type":\s*"planned_change")')
    
    return any(re.search(drift_detection_pattern, line) for line in plan)
