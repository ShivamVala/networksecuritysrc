from networksecuritysrc.components.data_ingestion import DataIngestion
from networksecuritysrc.components.data_validation import DataValidation

from networksecuritysrc.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig, DataValidationConfig
from networksecuritysrc.exception.exception import NetworkSecurityException
from networksecuritysrc.logging.logger import logging
import sys, os


if __name__=='__main__':
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data Ingestion Completed")
        print(dataingestionartifact)
        data_validation_config=DataValidationConfig(trainingpipelineconfig)
        data_validation=DataValidation(dataingestionartifact,data_validation_config)
        logging.info("Initiate the data Validation")
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info("data Validation Completed")
        print(data_validation_artifact)
    except Exception as e:
           raise NetworkSecurityException(e,sys)
