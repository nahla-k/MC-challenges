import requests
import logging

logging.basicConfig(level=logging.INFO)

def check_website(url):
    try: 
        head_response = requests.head(url)
        if head_response.status_code == 200:
            logging.info("website is accesible")
        else:
            logging.error("website is not accesible")

        tech_response = requests.get(url)
        server = tech_response.headers.get('Server')
        logging.info(f"server tech: {server}")

        options_response = requests.options(url)
        allow = options_response.headers.get('Allow')
        logging.info(f"allowed methods : {allow}")
    except requests.exceptions.RequestException as e:
        logging.error(f"error: {e}")

url = input("enter the url: ")        
check_website(url)