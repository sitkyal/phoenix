# All Models

from sklearn.model_selection import cross_val_score


def decision_tree(X, y, k, eval_metric=None):
    from sklearn import tree

    cm = tree.DecisionTreeClassifier()
    score = round(
        (cross_val_score(cm, X, y, cv=k, scoring=eval_metric, n_jobs=-1).max()), 3)
    model_name = 'Decision Tree Classifier'
    print 'Decision Tree Classifier Score: {}'.format(score)
    return model_name, score


def knn(X, y, k, eval_metric=None):
    from sklearn.neighbors import KNeighborsClassifier

    cm = KNeighborsClassifier()
    score = round(
        (cross_val_score(cm, X, y, cv=k, scoring=eval_metric, n_jobs=-1).max()), 3)
    model_name = 'KNN'
    print 'KNN Score: {}'.format(score)
    return model_name, score


def Random_Forest_Classifier(X, y, k, eval_metric=None):
    from sklearn.ensemble import RandomForestClassifier

    cm = RandomForestClassifier()
    score = round(
        (cross_val_score(cm, X, y, cv=k, scoring=eval_metric, n_jobs=-1).max()), 3)
    model_name = 'Random Forest Classifier'
    print 'Random Forest Classifier: {}'.format(score)
    return model_name, score


def AdaBoost_Classifier(X, y, k, eval_metric=None):
    from sklearn.ensemble import AdaBoostClassifier

    cm = AdaBoostClassifier()
    score = round(
        (cross_val_score(cm, X, y, cv=k, scoring=eval_metric, n_jobs=-1).max()), 3)
    model_name = 'Ada Boost Classifier'
    print 'Ada Boost Classifier: {}'.format(score)
    return model_name, score


def GradientBoosting_Classifier(X, y, k, eval_metric=None):
    from sklearn.ensemble import GradientBoostingClassifier

    cm = GradientBoostingClassifier()
    score = round(
        (cross_val_score(cm, X, y, cv=k, scoring=eval_metric, n_jobs=-1).max()), 3)
    model_name = 'Gradient Boosting Classifier'
    print 'Gradient Boosting  Classifier: {}'.format(score)
    return model_name, score


def Logistic_Regression(X, y, k, eval_metric=None):
    from sklearn import linear_model

    cm = linear_model.LogisticRegression()
    score = round(
        (cross_val_score(cm, X, y, cv=k, scoring=eval_metric, n_jobs=-1).max()), 3)
    model_name = 'Logistic Regression'
    print 'Logistic Regression: {}'.format(score)
    return model_name, score


def svm(X, y, k, eval_metric=None):
    from sklearn.svm import SVC

    cm = SVC()
    score = round(
        (cross_val_score(cm, X, y, cv=k, scoring=eval_metric, n_jobs=-1).max()), 3)
    model_name = 'Support Vector Machine'
    print 'Support Vector Machine: {}'.format(score)
    return model_name, score

def XGBoost_Classifier(X, y, k, eval_metric=None):
    from xgboost import XGBClassifier

    cm = XGBClassifier()
    score = round(
        (cross_val_score(cm, X, y, cv=k, scoring=eval_metric, n_jobs=-1).max()), 3)
    model_name = 'XG Boost Classifier'
    print 'XG Boost Classifier: {}'.format(score)
    return model_name, score

