import ast

class CodeParser:
    """
    Parse Python files using AST.
    Extracts:
    - Functions (name, args, docstring)
    - Classes (name, docstring, methods)
    """

    def parse_file(self, file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                source = f.read()

            tree = ast.parse(source)
            return self._extract_info(tree)

        except Exception as e:
            return {"error": str(e), "file": file_path}

    def _extract_info(self, tree):
        result = {
            "functions": [],
            "classes": []
        }

        for node in ast.walk(tree):

            # --- FUNCTIONS ---
            if isinstance(node, ast.FunctionDef):
                result["functions"].append({
                    "name": node.name,
                    "args": [arg.arg for arg in node.args.args],
                    "docstring": ast.get_docstring(node)
                })

            # --- CLASSES ---
            elif isinstance(node, ast.ClassDef):
                class_info = {
                    "name": node.name,
                    "docstring": ast.get_docstring(node),
                    "methods": []
                }

                for body_item in node.body:
                    if isinstance(body_item, ast.FunctionDef):
                        class_info["methods"].append({
                            "name": body_item.name,
                            "args": [arg.arg for arg in body_item.args.args],
                            "docstring": ast.get_docstring(body_item)
                        })

                result["classes"].append(class_info)

        return result
