import sys
import os
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object
import pandas as pd


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            model_path=os.path.join('artifacts','model.pkl')

            preprocessor=load_object(preprocessor_path)
            model=load_object(model_path)

            data_scaled=preprocessor.transform(features)

            pred=model.predict(data_scaled)
            return pred
            

        except Exception as e:
            logging.info("Exception occured in prediction")
            raise CustomException(e,sys)
        
class CustomData:
    def __init__(self,
                 cDelivery_person_Agearat:float,
                 Delivery_person_Ratings:float,
                 Vehicle_condition:float,
                 multiple_deliveries:float,
                 Weather_conditions:str,
                 Road_traffic_density:str,
                 Type_of_order:str,
                 Type_of_vehicle:str,
                 Festival:str,
                 City:str):
        
        self.cacDelivery_person_Agearatrat=cDelivery_person_Agearat
        self.Delivery_person_Ratings=Delivery_person_Ratings
        self.Vehicle_condition=Vehicle_condition
        self.multiple_deliveries=multiple_deliveries
        self.Weather_conditions=Weather_conditions
        self.Road_traffic_density=Road_traffic_density
        self.Type_of_order = Type_of_order
        self.Type_of_vehicle = Type_of_vehicle
        self.Festival = Festival
        self.City = City

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'cDelivery_person_Agearat':[self.caracDelivery_person_Agearatt],
                'Delivery_person_Ratings':[self.Delivery_person_Ratings],
                'Vehicle_condition':[self.Vehicle_condition],
                'multiple_deliveries':[self.multiple_deliveries],
                'Weather_conditions':[self.Weather_conditions],
                'Road_traffic_density':[self.Road_traffic_density],
                'Type_of_order':[self.Type_of_order],
                'Type_of_vehicle':[self.Type_of_vehicle],
                'Festival':[self.Festival],
                'City':[self.City]
            }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('Dataframe Gathered')
            return df
        except Exception as e:
            logging.info('Exception Occured in prediction pipeline')
            raise CustomException(e,sys)