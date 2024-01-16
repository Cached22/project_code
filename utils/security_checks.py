```python
import subprocess
import json
from utils.error_handling import handle_errors

@handle_errors
def check_security_vulnerabilities(file_path):
    """
    Checks for security vulnerabilities in the given file using Bandit.
    
    :param file_path: Path to the file to be checked.
    :return: A dictionary with the results of the security checks.
    """
    # Run Bandit security check as a subprocess
    result = subprocess.run(['bandit', '-f', 'json', file_path], capture_output=True, text=True)
    
    # Parse the JSON output from Bandit
    try:
        output = json.loads(result.stdout)
        vulnerabilities = output['results']
        metrics = output['metrics']
    except json.JSONDecodeError:
        raise ValueError("Failed to parse security check output.")
    
    # Extract relevant information
    issues = []
    for issue in vulnerabilities:
        issues.append({
            'filename': issue['filename'],
            'issue_text': issue['issue_text'],
            'severity': issue['issue_severity'],
            'line_number': issue['line_number'],
            'test_id': issue['test_id']
        })
    
    return {
        'total_issues': len(issues),
        'issues': issues,
        'metrics': metrics
    }
```