import json
from typing import Any


def lambda_handler(event, context) -> dict[str, Any]:
    """Lambda function handler."""

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
        },
        "body": json.dumps({"message": "Hello from Lambda!"}),
    }
