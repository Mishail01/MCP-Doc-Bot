import sys
import os

from bot.scanner import RepositoryScanner
from bot.generator import DocumentationGenerator

def main():
    if len(sys.argv) < 2:
        print("Usage: python run.py <path_to_repository>")
        return

    repo_path = sys.argv[1]

    if not os.path.isdir(repo_path):
        print(f"Error: '{repo_path}' is not a valid directory.")
        return

    print("\n🔍 Scanning repository...")
    scanner = RepositoryScanner(repo_path)
    scan_results = scanner.scan_repository()

    print("✔️ Scan complete.")

    print("\n📝 Generating documentation...")
    generator = DocumentationGenerator()

    readme_path = generator.generate_readme(scan_results)
    api_doc_path = generator.generate_api_docs(scan_results)

    print("\n📄 Documentation generated successfully!")
    print(f"- README: {readme_path}")
    print(f"- API Docs: {api_doc_path}")

if __name__ == "__main__":
    main()
