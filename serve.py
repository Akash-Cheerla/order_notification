import json
import uvicorn
from main import app
from loguru import logger

if __name__ == "__main__":
    with open("config.json", "r", encoding="utf-8") as f:
        config = json.load(f)

    logger.add(config["logs"]["filepath"],
               level=config["logs"]["level"],
               rotation=config["logs"]["rotation"]
               )
            
    logger.info("Running the service at {}/{}".format(config["host"], config["port"]))
    uvicorn.run(app, host=config["host"], port=config["port"])
