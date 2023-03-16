import pandas as pd
import numpy as np
import os
import sys


from data_ingestion import DataIngestion as di
from dataclasses import dataclass
from src.exception import CustomException
from src.logger import logging
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler


@dataclass
class DataTransformConfig:
    preprocessor_obj_file_path = os.path.join('artifacts','preprocessor.csv')

class DataTransformer ():
    def __init__(self):
        self.data_transformation_congig=DataTransformConfig()
        pass

    def get_data_transformer_object(self):
        
        try:
            cat_feat = ['reading_score', 'writing_score']

            nunm_feat = ['gender', 'race_ethnicity', 'parental_level_of_education', 'lunch',
                         'test_preparation_course']
            
            """
            Creating pipeline for the Categorical and Numerical aspects
        
            """
            num_pipeline= Pipeline(
                steps=[
                ("imputer",SimpleImputer(strategy="median")),
                ("scaler",StandardScaler())

                ]
            )
            cat_pipeline=Pipeline(

                steps=[
                ("imputer",SimpleImputer(strategy="most_frequent")),
                ("one_hot_encoder",OneHotEncoder()),
                ("scaler",StandardScaler(with_mean=False))
                ]

            )


        except:
            pass

        