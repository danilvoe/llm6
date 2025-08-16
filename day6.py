

import asyncio

from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

async def main():
    #markitdown-mcp --http --host 127.0.0.1 --port 3001
    async with streamablehttp_client("http://127.0.0.1:3001/mcp") as (
        read_stream,
        write_stream,
        _,
    ):
        print("Конвертация веб страницы в markdown формат.")
        url = input("Введите url для конвертации страницы в markdown формат: ").strip()
        async with ClientSession(read_stream, write_stream) as session:
            # Initialize the connection
            await session.initialize()
            # List available tools
            tools = await session.list_tools()
            print(f"Available tools: {[tool.name for tool in tools.tools]}")
            tools = await session.call_tool('convert_to_markdown', {'uri': url})
            file = open('result.md', 'w')
            file.write(tools.content[0].text)
            file.close()

if __name__ == "__main__":
    asyncio.run(main())