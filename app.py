from src.logger import logging
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion, DataIngestionConfig
from src.components.data_transformation import DataTransformation, DataTransformationConfig

import sys

if __name__ == "__main__":
    logging.info("Execution has started")

    try:
        # data_ingestion_config = DataIngestionConfig()
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()

        data_transformation = DataTransformation()
        data_transformation.initiate_data_transformation(train_data_path, test_data_path)
    # Get the configuration for data ingestion
    except Exception as e:
        logging.info("custom exception raised in app.py")
        raise CustomException(e, sys)