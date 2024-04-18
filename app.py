from src.logger import logging
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion
from src.components.data_ingestion import DataIngestionConfig
import sys

if __name__ == "__main__":
    logging.info("Execution has started")

    try:
        # data_ingestion_config = DataIngestionConfig()
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()
    # Get the configuration for data ingestion
    except Exception as e:
        logging.info("custom exception raised in app.py")
        raise CustomException(e, sys)