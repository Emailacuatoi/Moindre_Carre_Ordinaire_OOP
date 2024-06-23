import numpy as np
import pandas as pd

def read_csv_file(file_name):
    """open csv"""
    data = []
    with open(file_name, 'r') as file:
        for line in file:
            row = line.strip().split(';')
            data.append(row)
    return data
def data_cleaning(rte):
    """effectuer Data Processing"""
    rte_new=rte.iloc[np.arange(len(rte))%2==0]
    rte_new=rte_new.reset_index(drop=True)
    return rte_new
def moyen(data):
    """calculer la moyenne de chaque variable et les mettre dans un dataframe"""
    header=np.array(data.columns.tolist())[2:len(data.columns.tolist())]
    mean=np.array([])
    for i in range (2,len(data.columns.tolist())):
        mean=np.append(mean,np.mean(data.iloc[:,i]))       
    data_frame=pd.DataFrame([mean], columns=header)
    return data_frame
def med(data):
    """calculer la médiane de chaque variable et les mettre dans un dataframe"""
    header=np.array(data.columns.tolist())[2:len(data.columns.tolist())]
    median=np.array([])
    for i in range (2,len(data.columns.tolist())):
        median=np.append(median,np.median(data.iloc[:,i]))
    data_frame=pd.DataFrame([median], columns=header)
    return data_frame
def var(data):
    """calculer la variance de chaque variable et les mettre dans un dataframe"""
    header=np.array(data.columns.tolist())[2:len(data.columns.tolist())]
    variance=np.array([])
    for i in range (2,len(data.columns.tolist())):
        variance=np.append(variance,np.var(data.iloc[:,i]))
    data_frame=pd.DataFrame([variance], columns=header)
    return data_frame
def intervalle_interquantile(data):
    """calculer l'intervalle d'interquantile de chaque variable et les mettre dans un dataframe"""
    header=np.array(data.columns.tolist())[2:len(data.columns.tolist())]
    intervalle=np.array([])
    for i in range (2,len(data.columns.tolist())):
        intervalle=np.append(intervalle,f'({data.iloc[:,i].quantile(0.75)} , {data.iloc[:,i].quantile(0.25)})')
    data_frame=pd.DataFrame([intervalle], columns=header)
    return data_frame
def maxi(data):
    """calculer le maximum de chaque variable et les mettre dans un dataframe"""
    header=np.array(data.columns.tolist())[2:len(data.columns.tolist())]
    maximum=np.array([])
    for i in range (2,len(data.columns.tolist())):
        maximum=np.append(maximum,np.max(data.iloc[:,i]))     
    data_frame=pd.DataFrame([maximum], columns=header)
    return data_frame
def mini(data):
    """calculer le minimum de chaque variable et les mettre dans un dataframe"""
    header=np.array(data.columns.tolist())[2:len(data.columns.tolist())]
    minimum=np.array([])
    for i in range (2,len(data.columns.tolist())):
        minimum=np.append(minimum,np.min(data.iloc[:,i]))       
    data_frame=pd.DataFrame([minimum], columns=header)
    return data_frame
def summary(data):
    """mettre tous les statistique desciptive au-dessus dans un dataframe"""
    header=np.array(data.columns.tolist())[2:len(data.columns.tolist())]
    mean=np.array([])
    median=np.array([])
    variance=np.array([])
    intervalle=np.array([])
    maximum=np.array([])
    minimum=np.array([])
    for i in range (2,len(data.columns.tolist())):
        mean=np.append(mean,np.mean(data.iloc[:,i]))
        median=np.append(median,np.median(data.iloc[:,i]))
        variance=np.append(variance,np.var(data.iloc[:,i]))
        intervalle=np.append(intervalle,f'({data.iloc[:,i].quantile(0.75)} , {data.iloc[:,i].quantile(0.25)})')
        maximum=np.append(maximum,np.max(data.iloc[:,i]))
        minimum=np.append(minimum,np.min(data.iloc[:,i]))
    data_frame=pd.DataFrame([mean, median, variance, intervalle, maximum, minimum], columns=header)
    data_frame.insert(0, 'Parametre', ["Mean","Median", "Variance","Intervalle_interquantile",'Maximum', 'Minimum'])
    return data_frame
def corr(data):
    """calculer la corrélation du dataframe"""
    return data.corr(method='pearson')



