import os
import resend
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
load_dotenv()

# Set the Resend API key from environment variable
resend.api_key = os.getenv("RESEND_API_KEY")

def register_tools(mcp: FastMCP):
    """Register email sending tool with the MCP server."""

    @mcp.tool()
    async def send_email(
        to: str,
        subject: str,
        html: str,
        sender: str = "noreply@mcp.sg-cna.com"
    ) -> str:
        """
        Send an email using the Resend API.

        Args:
            to: Recipient email address (required).
            subject: Email subject (required).
            html: Email body in HTML format (required).
            sender: Sender email in "Name <email>" format (optional, defaults to noreply@mcp.com).

        Returns:
            Status message indicating result of the email send.
        """
        try:
            params = {
                "from": sender,
                "to": [to],
                "subject": subject,
                "html": html,
            }

            email = resend.Emails.send(params)
            return f"Email sent to {to} | ID: {email['id']}"
        
        except Exception as e:
            return f"Failed to send email: {str(e)}"
