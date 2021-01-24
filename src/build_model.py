from ludwig.experiment import experiment_cli
from ludwig.api import LudwigModel
import pandas as pd

def train_model():
    train_df = pd.read_csv("../hand_dataset_training.csv") 
    # print(train_df.shape)
    # print(train_df.head())
    test_df = pd.read_csv("../hand_dataset_testing.csv") 
    experiment_cli(
        config="../model.yaml",
        training_set=train_df, 
        test_set= test_df,
        output_directory="results",
        experiment_name= "exp",
        random_seed=100
    )



if __name__=="__main__":
    train_model()