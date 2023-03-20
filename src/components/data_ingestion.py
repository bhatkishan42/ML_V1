import pandas as pd
import numpy as np
import sys
import os
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.exception import CustomException
from src.logger import logging


# Define a configuration object to store data paths
@dataclass
class IngestionConfig:
    train_data: str = os.path.join("artifacts", "train.csv")
    test_data: str = os.path.join("artifacts", "test.csv")
    raw_data: str = os.path.join("artifacts", "raw.csv")


class DataIngestion:
    def __init__(self):
        self.ingest_config = IngestionConfig()

    def ingestion(self):
        try:
            # Read data from raw file and split into test, train, and raw data
            db = pd.read_csv("DB/Data/stud.csv")
            logging.info("Completed reading data and moving to test train split")
            # print(db.shape)

            # Make directory if not already present
            os.makedirs(os.path.dirname(self.ingest_config.train_data), exist_ok=True)

            # Save raw data
            db.to_csv(self.ingest_config.raw_data)

            # Split data into test and train data
            train_data, test_data = train_test_split(db, test_size=0.2, random_state=1508)

            # Save train and test data
            train_data.to_csv(self.ingest_config.train_data, index=False, header=True)
            test_data.to_csv(self.ingest_config.test_data, index=False, header=True)

            logging.info("Split test and train data")
            return self.ingest_config.train_data, self.ingest_config.test_data
            
        except Exception as e:
            CustomException(e, sys)


if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data = obj.ingestion()

