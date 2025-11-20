import asyncio
from bot.mcp_server import DocumentationBotServer

async def test_bot():
    bot = DocumentationBotServer()
    # Scan example repo
    await bot.scan_repo("tests/example_repo")
    # Ask some explanations
    result1 = await bot.explain("add")
    result2 = await bot.explain("Calculator")
    # Generate docs
    await bot.generate_docs("tests/example_repo")

    # Save conversation logs
    with open("tests/results/mcp_conversation_log.txt", "w") as f:
        f.write("Explain 'add':\n")
        f.write(str(result1))
        f.write("\n\nExplain 'Calculator':\n")
        f.write(str(result2))

asyncio.run(test_bot())

def print_bot(message):
    print(f"[MCP Bot] {message}")

print_bot("Scanning repository for MCP session...")
# After scan
print_bot("Generating explanations for sample queries...")
