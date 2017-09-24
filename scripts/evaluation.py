# module for evaluation

# Division by Zero, No data, attribute not passed

from sklearn import metrics
from sklearn import feature_selection


# calculate ROC Curve

def rocc(y, y_score):
    fpr = dict()
    tpr = dict()
    fpr, tpr, thresholds = metrics.roc_curve(y, y_score[:, 1])
    auc_score = metrics.roc_auc_score(y, y_score[:,1])
    return fpr, tpr, auc_score

# calculate Precision Recall Curve

def prc(y, y_score):
    precision, recall, thresholds = metrics.precision_recall_curve(y, y_score[:,1])
    return precision, recall


# calcuate confusion matrix


def conf_mat(y, ypred):
    cmatrix = metrics.confusion_matrix(y, ypred)
    TP = cmatrix[0, 0]
    TN = cmatrix[1, 1]
    FP = cmatrix[0, 1]
    FN = cmatrix[1, 0]

    # other Metrics

    Specificity = ((TN * 1.0) / (TN + FP))
    Sensitivity = ((TP * 1.0) / (TP + FN))
    Accuracy = ((TP + TN) * 1.0) / (TN + TP + FP + FN)
    Error_Rate = ((FP + FN) * 1.0) / (TN + TP + FP + FN)
    Precision = ((TP * 1.0) / (TP + FP))
    FPR = ((FP * 1.0) / (TN + FP))
    f1score = (2 * Precision * Sensitivity) / (Precision + Sensitivity)
    #skf1score = metrics.f1_score(y, ypred, average='weighted')
    neglogloss = metrics.log_loss(y, ypred, eps=1e-15, normalize=True)
    mcc = metrics.matthews_corrcoef(y, ypred)

    return cmatrix, TP, TN, FP, FN, Specificity, Sensitivity, Accuracy, Error_Rate, Precision, FPR, f1score, neglogloss, mcc
