"""A resilient API client that retries on failure."""
import time
import requests

from .exceptions import APIError, APITimeoutError, APIResponseError
from .logger_config import setup_logger

logger = setup_logger("API_Client")

class ResilientAPIClient:
    def __init__(self, base_url, timeout=3):
        self.base_url = base_url
        self.timeout = timeout

    def get(self, endpoint, retries=3):
        url = self.base_url + endpoint
        
        for attempt in range(1, retries + 1):
            try:
                logger.info(f"Attempt {attempt}: Calling {url}")
                
                # Modern requests call
                response = requests.get(url, headers={'User-Agent': 'TestClient'}, timeout=self.timeout)
                
                # Raise an HTTPError if the HTTP request returned an unsuccessful status code
                response.raise_for_status()
                
                logger.info("Call successful!")
                return response.json()
                
            except requests.exceptions.HTTPError as e:
                status_code = e.response.status_code
                logger.error(f"HTTP Error {status_code}: {e}")
                
                # Do not retry on 4xx errors (client errors), raise immediately
                if 400 <= status_code < 500:
                    raise APIResponseError("Client Error - Bad Request", status_code)
                    
                # Retry on 5xx errors (server errors), but raise if max retries reached
                if attempt == retries:
                    raise APIResponseError("Max retries reached on Server Error.", status_code)
                    
            except (requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
                logger.error(f"Timeout/Network Error: {e}")
                if attempt == retries:
                    raise APITimeoutError("Request timed out or network failed.")
                    
            except requests.exceptions.RequestException as e:
                logger.error(f"Unexpected request error: {e}")
                raise APIError("Something went very wrong with the request.")
            
            # Exponential backoff sleep before trying again
            sleep_time = 2 ** attempt
            logger.warning(f"Waiting {sleep_time} seconds before trying again...")
            time.sleep(sleep_time)
