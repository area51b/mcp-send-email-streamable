# mcp-send-email-streamable

This project implements a Model Context Protocol (MCP) server with tools to send emails using the Resend API.

## Features
- **Model Context Protocol (MCP) Server**: Provides a template for building MCP-compliant services.
- **Email Sending Tool**: Integrates with the [Resend API](https://resend.com/) to send emails programmatically.

## Project Structure
- `main.py`: Entry point for the MCP server.
- `src/config/settings.py`: Configuration settings for the project.
- `src/tools/mcp_tools.py`: Contains the MCP tool for sending emails via Resend.
- `k8s/`: Kubernetes deployment, service, and route manifests.

## Requirements
- Python 3.10+
- Dependencies listed in `requirements.txt`

## Setup
1. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
2. **Configure Resend API Key:**
   Set your Resend API key in the environment
3. **Run the server:**
   ```sh
   python main.py
   ```

## Usage
Use the provided MCP tool to send emails by making requests to the server. See `src/tools/mcp_tools.py` for tool details and usage examples.

## Deployment
Kubernetes manifests are provided in the `k8s/` directory for containerized deployment.

## License
MIT
