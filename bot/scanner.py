import os
from .parser import CodeParser

class RepositoryScanner:
    """
    Scans an entire repository:
    - Finds all Python files
    - Parses each file using CodeParser
    """

    def __init__(self, base_path):
        self.base_path = base_path
        self.parser = CodeParser()

    def scan_repository(self):
        python_files = self._get_python_files()
        scan_results = {}

        for file in python_files:
            scan_results[file] = self.parser.parse_file(file)

        return scan_results

    def _get_python_files(self):
        """Walk through directory and collect .py files."""
        python_files = []

        for root, dirs, files in os.walk(self.base_path):
            for file in files:
                if file.endswith(".py"):
                    full_path = os.path.join(root, file)
                    python_files.append(full_path)

        return python_files
