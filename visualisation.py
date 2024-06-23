import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
def heatmap(data):
    """Tracer le corrélation entre les variables avec heatmap"""
    rte_new = data.iloc[np.arange(len(data))%2==0]
    rte_new = rte_new.reset_index(drop=True)
    rte_core = rte_new.iloc[:,2:len(rte_new)]
    return sns.heatmap(rte_core.corr())
def boxplot(data):
    """Visualiser avec boxplotla consomation et la prédiction des jours J et jours J-1"""
    return plt.boxplot(data.iloc[:,2:5])
def dif_prevision_conso(data):
    """Visualiser la différence entre la consomation et la prédiction des jours J et jours J-1"""
    difference1 = data.iloc[:, 2] - data.iloc[:, 3]
    difference0 = data.iloc[:, 2] - data.iloc[:, 4]
    longeur=np.arange(0,len(difference1))
    quantile75=np.ones(len(difference1))*difference1.quantile(0.75)
    quantile25=np.ones(len(difference1))*difference1.quantile(0.25)
    fig, axe = plt.subplots(2, 1, figsize=(12, 6))
    fig.suptitle('Différence entre la Prévision et La consommation')
    plt.xlabel("Time")
    plt.ylabel("Consommation d'energie en MW")
    axe[0].plot(np.array(difference1))
    axe[0].plot(longeur,quantile75, color='red', linestyle="dashed")
    axe[0].plot(longeur,quantile25, color='red', linestyle = "dashed")
    axe[0].set_title("Jour J-1")
    axe[1].plot(np.array(difference0))
    axe[1].plot(longeur,quantile75, color='red', linestyle = "dashed")
    axe[1].plot(longeur,quantile25, color='red', linestyle = "dashed")
    axe[1].set_title("Jour J")  
def conso_par_heure(data):
    """Visualiser la consomation en moyenne par heure"""
    group_by=data.groupby("Heures")
    consom=group_by.mean()['Consommation']
    consom[0::2]
    plt.figure(figsize=(15,6))
    plt.plot(consom[0::2])
    plt.xlabel("Heuures dans un jour")
    plt.ylabel("Comsommation d'énergie en MW")   
def pie(data):
    """Visualiser avec pie graphe la distribution des type d'énergie"""
    fioul=data['Fioul'].sum()
    charbon=data['Charbon'].sum()
    gaz=data['Gaz'].sum()
    nucleaire=data['Nucléaire'].sum()
    solaire=data['Solaire'].sum()
    hydraulique=data['Hydraulique'].sum()
    eolien=data['Eolien'].sum()
    bioenergies=data['Bioénergies'].sum()
    labels=np.array(['Fioul','Charbon','Gaz','Nucléaire','Solaire','Hydraulique','Eolien','Bioénergies'])
    plt.pie(np.array([fioul,charbon,gaz,nucleaire,solaire,hydraulique,eolien,bioenergies]), labels=labels)
    plt.title("Pourcentage des différentes filières de production d’électricité")  
def conso_total(data):
    """Visualiser la consomation totale"""
    plt.figure(figsize=(15,8))
    plt.plot(data["Consommation"])
    plt.title("Consommation d'energie totale")   
def conso_par_type(data):
    """Visualiser la consomation par chaque type d'énergie"""
    fig, axe = plt.subplots(3,3, figsize=(12,10))
    axe[0,0].plot(data['Taux de Co2'])
    axe[0,0].set_title('Taux_CO2')
    axe[0,1].plot(data['Charbon'])
    axe[0,1].set_title('Charbon')
    axe[0,2].plot(data['Gaz'])
    axe[0,2].set_title('Gaz')
    axe[1,0].plot(data['Nucléaire'])
    axe[1,0].set_title('Nucléaire')
    axe[1,1].plot(data['Solaire'])
    axe[1,1].set_title('Solaire')
    axe[1,2].plot(data['Hydraulique'])
    axe[1,2].set_title('Hydraulique')
    axe[2,0].plot(data['Eolien'])
    axe[2,0].set_title('Eolien')
    axe[2,1].plot(data['Bioénergies'])
    axe[2,1].set_title('Bioénergies')
    axe[2,2].plot( data['Fioul'])
    axe[2,2].set_title('Fioul')
    plt.show()



