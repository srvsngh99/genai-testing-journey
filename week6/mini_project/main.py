"""Main script to demonstrate our resilient API caller."""
from core.api_client import ResilientAPIClient
from core.exceptions import APIError, APIResponseError
from core.logger_config import setup_logger

logger = setup_logger("Main")

def main():
    logger.info("--- Starting Robust API Caller ---")
    client = ResilientAPIClient(base_url="https://httpbin.org", timeout=5)
    
    # Scenario 1: Successful Call (receives JSON response)
    try:
        logger.info("Testing a successful endpoint...")
        data = client.get("/get")
        logger.info(f"Success! Received URL from JSON: {data.get('url')}")
    except Exception as e:
        logger.error(f"Unexpected failure: {e}")
        
    print("\n" + "="*40 + "\n")
    
    # Scenario 2: Failing Call with Retries (500 Server Error)
    try:
        logger.info("Testing a 500 Server Error endpoint (Should Retry)...")
        client.get("/status/500", retries=2)
    except APIResponseError as e:
        logger.error(f"Caught custom exception properly (500): {e.args[0]} (Status: {e.status_code})")
        
    print("\n" + "="*40 + "\n")
    
    # Scenario 3: Failing Call without Retries (400 Bad Request)
    try:
        logger.info("Testing a 400 Bad Request endpoint (Should Fail Fast)...")
        client.get("/status/400", retries=2)
    except APIResponseError as e:
        logger.error(f"Caught custom exception properly (400): {e.args[0]} (Status: {e.status_code})")

    logger.info("--- Demonstration Complete ---")

if __name__ == "__main__":
    main()
