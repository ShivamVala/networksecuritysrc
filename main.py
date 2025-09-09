from networksecuritysrc.components.data_ingestion import DataIngestion
from networksecuritysrc.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig
from networksecuritysrc.exception.exception import NetworkSecurityException
from networksecuritysrc.logging.logger import logging
import sys, os


if __name__=='__main__':
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
        
        
    except Exception as e:
           raise NetworkSecurityException(e,sys)
