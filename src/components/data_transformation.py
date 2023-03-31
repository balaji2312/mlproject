import pandas as pd
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from src.exception import CustomException
import sys
import os
from dataclasses import dataclass
import numpy as np
from src.logger import logging

from src.utils import save_object

@dataclass
class DataTransformationConfig :
    Preprocessor_obj_file_path=os.path.join("artifacts","preprocessor.pkl")


class DataTransformation:
    def __init__(self):
        self.data_Transformation_config= DataTransformationConfig()

    def get_data_transformer_object(self):
        '''
        This funcation is responsible to perform Data Transformation
        '''
        try:
            numerical_columns=['reading_score','writing_score']
            categorical_columns=['gender','race_ethnicity'
                                 ,'parental_level_of_education','lunch'
                                 ,'test_preparation_course']
            
            num_pipeline= Pipeline(
                steps=[
                ('Handling missing values',SimpleImputer(strategy='median')),
                ('scaler',StandardScaler())
                ]
            )
            categorical_pipeline=Pipeline(
                steps=[
                ('Handling missing values',SimpleImputer(strategy='most_frequent')),
                ('one_hot_encoder',OneHotEncoder()),
                ('scaler',StandardScaler(with_mean=False))
                ]
            )
            logging.info("Numerical columns{} - standard scaling completed".format(numerical_columns))

            logging.info("Categorical columns{} - encoding completed".format(categorical_columns))

            preprocessor=ColumnTransformer(
                [
                ('numerical_pipeline',num_pipeline,numerical_columns),
                ('categorical_pipeline',categorical_pipeline,categorical_columns)
                ]
            )
            return preprocessor
        
        except Exception as e:

            raise CustomException(e,sys)
        

    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("Read train and test data completed")

            logging.info("obtaining preprocessing object")

            preprocessing_object=self.get_data_transformer_object()

            target_column=["math_score"]
            numerical_columns=['reading_score','writing_score']
            categorical_columns=['gender','race_ethnicity'
                                 ,'parental_level_of_education','lunch'
                                 ,'test_preparation_course']
            
            input_feature_tain_df=train_df.drop(columns=target_column,axis=1)
            target_feature_train_df=train_df[target_column]

            input_feature_test_df=test_df.drop(columns=target_column,axis=1)
            target_feature_test_df=test_df[target_column]

            logging.info("Applying Preprocessing object on training and testing dataframe")
            

            input_feature_train_arr=preprocessing_object.fit_transform(input_feature_tain_df)
            input_feature_test_arr=preprocessing_object.transform(input_feature_test_df)

            train_arr=np.c_[
                input_feature_train_arr,target_feature_train_df
                  ]
            test_arr=np.c_[
                input_feature_test_arr,target_feature_test_df
                  ]
            logging.info("Preprocessing has been completed")

            save_object(

                file_path=self.data_Transformation_config.Preprocessor_obj_file_path,
                obj=preprocessing_object
            )
            logging.info("Dumped the preprocessing object into pickel file")

            return (
                train_arr,
                test_arr,
                self.data_Transformation_config.Preprocessor_obj_file_path
                )
            


        except Exception as e:
            raise CustomException(e,sys)
            
            
        


