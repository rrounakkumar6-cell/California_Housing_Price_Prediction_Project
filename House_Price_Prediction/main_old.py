import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import root_mean_squared_error
from sklearn.model_selection import cross_val_score
# from sklearn.preprocessing import OrdinalEncoder  # Uncomment if you prefer ordinal

# 1. Load the data
housing = pd.read_csv("housing.csv")

# 2. Create a stratified test set based on income category
housing["income_cat"] = pd.cut(
    housing["median_income"],
    bins=[0., 1.5, 3.0, 4.5, 6., np.inf],
    labels=[1, 2, 3, 4, 5]
)

split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index, test_index in split.split(housing, housing["income_cat"]):
    strat_train_set = housing.loc[train_index].drop("income_cat", axis=1)
    strat_test_set = housing.loc[test_index].drop("income_cat", axis=1)

# Work on a copy of training data
housing = strat_train_set.copy()

# 3. Separate predictors and labels
housing_labels = housing["median_house_value"].copy()
housing = housing.drop("median_house_value", axis=1)

# 4. Separate numerical and categorical columns
num_attribs = housing.drop("ocean_proximity", axis=1).columns.tolist()
cat_attribs = ["ocean_proximity"]

# 5. Pipelines
# Numerical pipeline
num_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler()),
])

# Categorical pipeline
cat_pipeline = Pipeline([
    # ("ordinal", OrdinalEncoder())  # Use this if you prefer ordinal encoding
    ("onehot", OneHotEncoder(handle_unknown="ignore"))
])

# Full pipeline
full_pipeline = ColumnTransformer([
    ("num", num_pipeline, num_attribs),
    ("cat", cat_pipeline, cat_attribs),
])

# 6. Transform the data
housing_prepared = full_pipeline.fit_transform(housing)

# housing_prepared is now a NumPy array ready for training
print(housing_prepared.shape)

linear_regression = LinearRegression()
linear_regression.fit(housing_prepared , housing_labels)
linear_reg_pre = linear_regression.predict(housing_prepared)
"""linear_rmse = root_mean_squared_error(housing_labels , linear_reg_pre)
print(f"the rmse of linear reg is {linear_rmse}")"""
linear_rmse = -cross_val_score(linear_regression , housing_prepared , housing_labels, scoring = "neg_root_mean_squared_error"  , cv = 10 )
print(pd.Series(linear_rmse).describe())

dec_tree = DecisionTreeRegressor()
dec_tree.fit(housing_prepared , housing_labels)
dec_tree_pre = dec_tree.predict(housing_prepared)
"""dec_tree_rmse = root_mean_squared_error(housing_labels , dec_tree_pre)
print(f"the rmse of dec tree is {dec_tree_rmse}")"""
dec_tree_rmse = -cross_val_score(dec_tree , housing_prepared , housing_labels , scoring = "neg_root_mean_squared_error" , cv = 10)
print(pd.Series(dec_tree_rmse).describe())

ran_forest = RandomForestRegressor()
ran_forest.fit(housing_prepared , housing_labels)
ran_forest_pre = ran_forest.predict(housing_prepared)
"""forest_rmse = root_mean_squared_error(housing_labels , ran_forest_pre)
print(f"the rmse of random forest is {forest_rmse}")"""
forest_rmse  = -cross_val_score(ran_forest , housing_prepared , housing_labels , scoring = "neg_root_mean_squared_error" , cv = 10)
print(pd.Series(forest_rmse).describe())
