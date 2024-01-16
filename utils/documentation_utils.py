```python
import libcst as cst

def add_docstrings_to_functions(code: str) -> str:
    """
    Add docstrings to functions in the given code if they are missing.

    Args:
        code (str): The source code to be documented.

    Returns:
        str: The source code with added docstrings.
    """
    class DocstringAdder(cst.CSTTransformer):
        def leave_FunctionDef(
            self, original_node: cst.FunctionDef, updated_node: cst.FunctionDef
        ) -> cst.FunctionDef:
            # Check if the function already has a docstring
            if not updated_node.body.body or not isinstance(updated_node.body.body[0], cst.SimpleStatementLine):
                return updated_node

            first_statement = updated_node.body.body[0]
            if isinstance(first_statement, cst.SimpleStatementLine) and isinstance(first_statement.body[0], cst.Expr):
                if isinstance(first_statement.body[0].value, cst.SimpleString):
                    # Docstring already exists
                    return updated_node

            # Add a placeholder docstring
            docstring = cst.SimpleStatementLine(
                body=[
                    cst.Expr(
                        value=cst.SimpleString(
                            value='"""TODO: Add a docstring here."""'
                        )
                    )
                ]
            )
            new_body = cst.IndentedBlock(body=[docstring] + list(updated_node.body.body))
            return updated_node.with_changes(body=new_body)

    wrapper = cst.MetadataWrapper(cst.parse_module(code))
    modified_tree = wrapper.visit(DocstringAdder())
    return modified_tree.code
```