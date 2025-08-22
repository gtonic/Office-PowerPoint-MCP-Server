#!/usr/bin/env python
"""
MCP Server for PowerPoint manipulation using python-pptx.
Entry point that uses the new modular architecture.
"""
import argparse
from src.office_ppt_mcp.protocol.mcp_server import main

if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="MCP Server for PowerPoint manipulation using python-pptx")

    parser.add_argument(
        "-t",
        "--transport",
        type=str,
        default="stdio",
        choices=["stdio", "http", "sse"],
        help="Transport method for the MCP server (default: stdio)"
    )

    parser.add_argument(
        "-p",
        "--port",
        type=int,
        default=8000,
        help="Port to run the MCP server on (default: 8000)"
    )
    args = parser.parse_args()
    main(args.transport, args.port)