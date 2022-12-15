import numpy as np
np.random.seed(25)

# Creating the matrixes to use for the problem
features = np.random.randint(0, 100, 10000).reshape(1000,10)
weights = np.array([ 0.24540611,  0.31467517, -0.07656614, -0.16161533, -0.09064962,
                    -0.00315615,  0.09609595,  0.2517064 ,  0.01100181, -0.38629211])


# Q9-1 Grading Tag:
def get_shape(ar):
    return ar.shape

# Q9-2 Grading Tag:
def check_min_max(ar):
    return (np.max(ar),np.min(ar))

# Q9-3 Grading Tag:
def count_nan(ar):
    return np.count_nonzero(ar==np.nan)

# Q9-4 Grading Tag:
def get_median(ar):
    return np.median(ar)

# Q9-5 Grading Tag:
def feat_minimum(ar):
    return np.where(ar == np.min(ar))[0]

# Q9-6 Grading Tag:
def feat_maximum(ar, feat_num):
    return np.where(ar[:,feat_num] == np.max(ar))


# Q9-7 Grading Tag:
def outlier_high(ar):
    return np.count_nonzero(ar >= 90)

# Q9-8 Grading Tag:
def outlier_low(ar):
    return np.count_nonzero(ar <= 10)

# Q9-9 Grading Tag:
def calc_features(np_feat, np_weight):
    return np_feat * np_weight

# Q9-10 Grading Tag:
def matrix_score(np_calc):
    result = np_calc.sum(axis=1)
    return result

c = calc_features(features,weights)
score = matrix_score(c)

# Q9-11 Grading Tag:
def score_mean(np_score):
    return np.mean(np_score)

# Q9-12 Grading Tag:
def classify(np_score):
    return (np_score >= score_mean(np_score)).astype('int') # .tolist()

prediction = classify(score)

# Q9-13 Grading Tag:
def perc_ones(np_pred):
    return np.count_nonzero(np_pred==1) / np_pred.shape[0] * 100.0

np.random.seed(1234)
truth = np.random.randint(0, 2, 1000)

# Q9-14 Grading Tag:
def num_correct(np_truth, np_pred):
    return (np.count_nonzero(np.logical_and(np_truth == np_pred,np_truth==0)),np.count_nonzero(np.logical_and(np_truth == np_pred,np_truth==1)))

print(num_correct(truth,prediction))