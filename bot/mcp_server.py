import json

from .scanner import RepositoryScanner
from .generator import DocumentationGenerator

# Mock MCP classes for local testing
class MCPServer:
    def __init__(self, name):
        pass
    def register_tool(self, tool):
        pass
    def start(self):
        pass

class Tool:
    def __init__(self, name, func):
        self.name = name
        self.func = func


class DocumentationBotServer(MCPServer):
    """
    MCP Server for the Documentation Bot.
    Provides:
    - repo scanning
    - code explanation
    - documentation generation
    """

    def __init__(self):
        super().__init__("mcp-doc-bot")

        # Register tools
        self.register_tool(Tool("scan_repo", self.scan_repo))
        self.register_tool(Tool("explain", self.explain))
        self.register_tool(Tool("generate_docs", self.generate_docs))

        # Stores last scan result
        self.scan_cache = None

    async def scan_repo(self, repo_path: str):
        """
        Scan and parse an entire repository.
        """
        scanner = RepositoryScanner(repo_path)
        self.scan_cache = scanner.scan_repository()

        return {
            "status": "success",
            "files_scanned": len(self.scan_cache),
            "details": self.scan_cache
        }

    async def explain(self, query: str):
        """
        Explain any function/class detected in the last scan.
        Example queries:
        - "explain add"
        - "what does Calculator.divide do"
        """
        if not self.scan_cache:
            return {"error": "No repository scanned yet."}

        # Search for match in scanned data
        results = []

        for file, data in self.scan_cache.items():

            # Functions
            for func in data.get("functions", []):
                if query.lower() in func["name"].lower():
                    results.append({
                        "type": "function",
                        "file": file,
                        "name": func["name"],
                        "args": func["args"],
                        "docstring": func["docstring"]
                    })

            # Classes + methods
            for cls in data.get("classes", []):
                if query.lower() in cls["name"].lower():
                    results.append({
                        "type": "class",
                        "file": file,
                        "name": cls["name"],
                        "docstring": cls["docstring"]
                    })

                for method in cls["methods"]:
                    if query.lower() in method["name"].lower():
                        results.append({
                            "type": "method",
                            "file": file,
                            "class": cls["name"],
                            "name": method["name"],
                            "args": method["args"],
                            "docstring": method["docstring"]
                        })

        if not results:
            return {"message": "No matching function/class found."}

        return results

    async def generate_docs(self, repo_path: str):
        """
        Re-run documentation generation.
        """
        if not self.scan_cache:
            # Fresh scan
            scanner = RepositoryScanner(repo_path)
            self.scan_cache = scanner.scan_repository()

        generator = DocumentationGenerator()

        readme = generator.generate_readme(self.scan_cache)
        api_docs = generator.generate_api_docs(self.scan_cache)

        return {
            "status": "success",
            "readme_path": readme,
            "api_docs_path": api_docs
        }


# Entry point for MCP systems
def start_server():
    server = DocumentationBotServer()
    server.start()
