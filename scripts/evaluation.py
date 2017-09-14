# module for evaluation

from sklearn import metrics



# calculate ROC Curve

def rocc(y, ypred):
    fpr = dict()
    tpr = dict()
    fpr, tpr, thresholds = metrics.roc_curve(y, ypred)
    #print y, ypred, fpr, tpr, thresholds
    return fpr, tpr

def conf_mat(y, ypred):
    cmatrix = metrics.confusion_matrix(y, ypred)
    return cmatrix

