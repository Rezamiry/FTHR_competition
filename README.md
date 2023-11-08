# FTHR_competition
Our submission for French Trot Horse Racing: Forecasting Competition. https://canssiontario.utoronto.ca/workshops-conferences/french-trot-horse-racing/

Part of the processing is been carried out using Compute Canada(CC) servers. More specifically, the part where we extracted the historical statistics of each horse, jockey, and trainer took around 16 hours.
For testing, our model requires the historical statistics of horse/jockey/trainer.

Consider the following steps for reproducing the results:
1. copy the dataset parquet file in the same folder as the scripts/notebooks
2. run the extract_historical_features.py. (Consider using the provided script for submitting a job to the CC server. `sbatch trot_sbatch.sh extract_historical_features`)
3. run the feature_engineering.ipynb notebook.
4. run the modeling.ipynb notebook. (for parameter tuning we used CC)
5. go through testing.ipynb notebook to see the final results

Make sure you have the following libraries installed in the environment:
- numpy
- pandas
- tensorflow


### Historical Feature Extraction:
One of the major predictors of success in new races probably is the historical performance of the contestant. We considered the horse, jockey, and, trainer as the contestants as all of them play major roles in the outcome of the competition.
For each row in the dataset (after sorting based on RaceStartTime), we considered the previous races that the horse/jockey/trainer participated in. We calculated the performance metrics of those races and added them to the dataset.\
There is one bug in this part that caused the horse/jockey/trainer average finish position feature to be faulty so we deleted this feature. Also because it took a long time doing the feature extraction we did not have the time to redo this part.

### Feature Engineering:
Most of the features in the dataset are features that are categorical either because of their nature (Gender, RaceCondition, etc.) or we did not know the exact meaning of hence we one-hot encoded them.
The rest of them were numerical such as horseAge and we did not change them.
We scaled all features using MinMaxScaler so all of them are in the same range.
We created a target variable based on four performance metrics: finishPosition, PRPrice, PIRPosition, and BeatenMargin. We included all of these performance metrics to have better discrimination between participants.
For example, the beatenMargin can determine how close were the first and second positions.

### Training data:
It only make sense to use all of one match data to predict the probability of wining. Hence, each instance in the training/validation/test is the information of one match. Each row of this two dimensional matrix is the features of one contestant.
Because each match have different number of contestants, we padded all matches to have 20 rows (add zero rows to the end of each instance).
At the end each training instance was in the shape: (20,210)
Training set: anything before (2020,11,1) \
Validation set: anything between (2020,11,1) and (2021,11,1) \
Test set size: anything after (2021,11,1)

### The model architecture:
We used a Convolutional Neural Network with a self-attention mechanism for predicting the target variable.
The first layers of the network only focus on the feature extraction of each participant regardless of other contestants. We achieved this by using vertical kernels. These layers will extract important patterns from each contestant (row).
The next layers will have horizontal kernels hence fusing the participant features for predicting the target.
The final layers are fully connected layers and softmax for predicting the target variable (win probability).




