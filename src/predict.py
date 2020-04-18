import train

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing
import time
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')
# ML libraries
import lightgbm as lgb
import xgboost as xgb
from xgboost import plot_importance, plot_tree
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
le = preprocessing.LabelEncoder()


def main():

	# test = os.environ.get("TEST_DATA")
	# train_data = os.environ.get("TRAINING_DATA")

	TRAINING_DATA_DIR = os.environ.get("TRAINING_DATA")
	TEST_DATA = os.environ.get("TEST_DATA")

	train_data = pd.read_csv(TRAINING_DATA_DIR)
	test = pd.read_csv(TEST_DATA)

	

if __name__ == "__main__":

	main()
