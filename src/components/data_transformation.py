import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import os


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts',"preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformer_object(self):
        '''
        This function is responsible for data transformation
        '''
        try:
            numerical_columns = ['reading_score', 'writing_score']

            categorical_columns = ['gender', 'race_ethnicity', 'parental_level_of_education', 'lunch', 'test_preparation_course']
            num_pipeline = Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="median"))
                    ("scaler",StandardScaler())
                ]
            )
            cat_pipeline = Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="median")),
                    ("one_hot_encoder",OneHotEncoding()),
                    ("scaler",StandardScaler())

                ]

            )

            logging.info(f"Categorical columns:{categorical_columns}")
            logging.info(f"Numerical columns:{numerical_columns}")

            preprocessor=ColumnTransformer(
                [
                    ("num_pipeline",num_pipeline,numerical_cloumns),
                    ("cat_pipeline",cat_pipeline,categorical_columns)
                ]
            )

            return preprocessor

            
        except Exception as e:
            raise CustomExceeption(sys,e) 

    def initiate_data_transformaton(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("Read train and test data completed")

            logging.info("obtaining preprocessor object")
            preprocessor_obj=self.get_data_transformer_object()
            target_column_name="math_score"
            numerical_columns = ['reading_score', 'writing_score']
            input_feature_train_df=df.drop(columns=[target_column_name],axis=1)
            pass
        except:
            pass
            