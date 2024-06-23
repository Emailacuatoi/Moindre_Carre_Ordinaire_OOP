import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class  OrdinaryLeastSquares():
    def __init__(self, dataframe, var, intercept):
        self.dataframe = dataframe
        self.var       = var
        self.intercept = intercept
        self.b1 = None
        self.b0 = None
    def fit(self):
        X = np.array(self.dataframe)
        y = self.var
        self.b1= (np.linalg.inv(X.T@X)) @X.T @y
        if self.intercept == True:
            self.b0 = np.mean(self.var)- self.b1 @ np.array(np.mean(self.dataframe, axis=0)) 
        else:
            self.b0 = 0
    def predict(self, X_new):
        return X_new @ self.b1 + self.b0
    def get_coeffs(self):
        return self.b1, self.b0
    def determination_coefficient(self):
        X = np.array(self.dataframe)
        y_true = self.var
        y_pred =  X @ self.b1.T + self.b0
        y_mean = np.mean(self.var)
        n = len(X)
        p = len(X.loc[1,:])
        return 1 - (np.sum((y_true - y_pred)**2) / np.sum((y_true - y_mean)**2)) * ((n-1)/(n-p-1))
    def residu_visual(self):
        X = np.array(self.dataframe)
        y_true = self.var
        y_pred = X@self.b1 + self.b0
        plt.plot(y_true-y_pred)
    def graphe_prediction(self,X_new):
        plt.plot(X_new @ self.b1.T + self.b0)
        plt.title("Taux de Co2 prévision avec le modèle linéaire")
    def diagnostique_residuelle(self):
        X = np.array(self.dataframe)
        y_true = self.var
        y_pred= X@ self.b1 + self.b0
        """gausiannité"""
        epsilon=y_true -y_pred
        sigma2 = np.linalg.norm((epsilon-np.mean(epsilon)))**2/len(epsilon)
        student = np.mean(epsilon)/(np.sqrt(sigma2/len(epsilon)))
        quantile = 1.645
        student
        if student >= quantile:
            return "l'erreur ne suit pas la loi gaussienne"
        else:
            return "l'erreur suit la loi gaussienne "
    def test_nulltié_residu(self):
        X = np.array(self.dataframe)
        y_true = self.var
        y_pred = X@self.b1 + self.b0
        res = y_true-y_pred
        res_moy = np.mean(res)
        var_res = np.linalg.norm((res-res_moy))/(len(res)-1)
        Z = np.sqrt(len(res))*(res_moy)/np.sqrt(var_res)
        if np.abs(Z) > 1.645:
            return "residu n'est pas centré "
        else:
            return "residu est centré "






