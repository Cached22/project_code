```python
import radon.metrics
import radon.raw
import radon.visitors
from radon.complexity import cc_visit, cc_rank
from radon.cli.harvest import CCHarvester

def analyze_code_metrics(file_path):
    """
    Analyze the code metrics of a given Python file.

    :param file_path: Path to the Python file to be analyzed.
    :return: A dictionary containing code metrics.
    """
    with open(file_path, 'r') as file:
        code = file.read()

    # Raw metrics
    raw_metrics = radon.raw.analyze(code)
    total_lines = raw_metrics.loc
    lines_of_code = raw_metrics.lloc
    comments = raw_metrics.comments
    blank_lines = raw_metrics.blank
    single_comments, multi_comments = raw_metrics.single_comments, raw_metrics.multi

    # Maintainability Index
    maintainability_index = radon.metrics.mi_visit(code, True)

    # Cyclomatic Complexity
    complexity_visitor = CCHarvester(file_path, code)
    functions_complexity = complexity_visitor.functions
    classes_complexity = complexity_visitor.classes

    # Count the number of functions and classes
    num_functions = len(functions_complexity)
    num_classes = len(classes_complexity)

    # Calculate average cyclomatic complexity
    cyclomatic_complexity = sum(cc_rank(f.complexity) for f in functions_complexity) / num_functions if num_functions else 0

    return {
        'total_lines': total_lines,
        'lines_of_code': lines_of_code,
        'comments': comments,
        'blank_lines': blank_lines,
        'single_line_comments': single_comments,
        'multi_line_comments': multi_comments,
        'number_of_functions': num_functions,
        'number_of_classes': num_classes,
        'average_cyclomatic_complexity': cyclomatic_complexity,
        'maintainability_index': maintainability_index,
    }
```