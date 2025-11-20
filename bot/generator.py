import os
from jinja2 import Template

class DocumentationGenerator:
    """
    Converts parsed codebase information into Markdown documentation.
    Uses templates located in templates/ directory.
    """

    def __init__(self, template_path="templates", output_path="sample_output"):
        self.template_path = template_path
        self.output_path = output_path

        os.makedirs(self.output_path, exist_ok=True)

    def _load_template(self, filename):
        """Load a template file from the templates folder."""
        path = os.path.join(self.template_path, filename)

        with open(path, "r", encoding="utf-8") as f:
            return Template(f.read())

    def generate_readme(self, scan_results):
        """Generate README.md based on repository information."""
        readme_template = self._load_template("readme_template.md")

        # Prepare data (like number of files, functions, classes)
        total_files = len(scan_results)

        total_functions = sum(len(info.get("functions", [])) 
                              for info in scan_results.values())

        total_classes = sum(len(info.get("classes", [])) 
                            for info in scan_results.values())

        rendered = readme_template.render(
            total_files=total_files,
            total_functions=total_functions,
            total_classes=total_classes,
            scan_results=scan_results
        )

        output_path = os.path.join(self.output_path, "README.md")

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(rendered)

        return output_path

    def generate_api_docs(self, scan_results):
        """Generate detailed API documentation markdown."""
        api_template = self._load_template("api_template.md")

        rendered = api_template.render(scan_results=scan_results)

        output_path = os.path.join(self.output_path, "api_docs.md")

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(rendered)

        return output_path
