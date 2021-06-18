# -*- coding: utf-8 -*-

__author__      = "Leidinice Silva"
__email__       = "leidinicesilvae@gmail.com"
__date__        = "05/26/2018"
__description__ = "Statistical indices to see performance of the model"


from netCDF4 import Dataset

import numpy as np
import scipy.stats as st


def compute_corr(model, obs):

    """
    The input arrays must have the same dimentions
    :Param model: Numpy array with model data
    :Param obs: Numpy array with obs data
    :Return: Pearson Linear Correlation
    """
   
    check_dims(model, obs)
    corr = np.corrcoef(model, obs)[0][1]
    
    return corr

def compute_r2(model, obs):

	"""
	The input arrays must have the same dimensions
	:Param model: Numpy array with model data
	:Param obs: Numpy array with obs data
	:Return: R-squared
	"""

	corr = np.corrcoef(model, obs)[0][1]
	r2 = corr ** 2

	return r2

    
def compute_mae(model, obs):

    """
    The input arrays must have the same dimensions
    :Param model: Numpy array with model data
    :Param obs: Numpy array with obs data
    :Return: Mean Absoluty Error
    """

    mae = np.mean(np.abs(model - obs))
    
    return mae
    

def compute_rmse(model, obs):

    """
    The input arrays must have the same dimensions
    :Param model: Numpy array with model data
    :Param obs: Numpy array with obs data
    :Return: Root Mean Square Error
    """

    rmse = np.sqrt(((np.array(model) - np.array(obs)) ** 2).mean()) 
    
    return rmse
    
     
def compute_bias(model, obs):

    """
    The input arrays must have the same dimensions
    :Param model: Numpy array with model data
    :Param obs: Numpy array with obs data
    :Return: Mean Bias Error
    """

    bias = np.nanmean(np.array(model) - np.array(obs))
    
    return bias


def compute_pbias(model, obs):

    """
    The input arrays must have the same dimensions
    :Param model: Numpy array with model data
    :Param obs: Numpy array with obs data
    :Return: Percentage Bias
    """

    pbias = 100.0 * sum(np.array(model) - np.array(obs)) / sum(np.array(obs))
    
    return pbias
        
    
def compute_apb(model, obs):

    """
    The input arrays must have the same dimensions
    :Param model: Numpy array with model data
    :Param obs: Numpy array with obs data
    :Return: Absolute Percent Bias
    """

    apb = 100.0 * sum(np.abs(model, obs)) / sum(obs)
    
    return apb
    
    
def compute_anomaly(model, obs):

    """
    The input arrays must have the same dimensions
    :Param model: Numpy array with model data
    :Param obs: Numpy array with obs data
    :Return: Anomaly and Standard Anomaly
    """

    clim_mean = np.nanmean(obs, axis=0)
    clim_std = np.nanstd(obs, axis=0)
    anomaly = model - clim_mean
    standard_anomaly = (model - clim_mean)/clim_std
    
    return anomaly, standard_anomaly
   
    
def compute_fcst_correct(model, obs, fcst):

    """
    The input arrays must have the same dimensions
    :Param model: Numpy array with model data
    :Param obs: Numpy array with obs data
    :Return: Forecast Data Correction
    """

    sim = np.sort(model)
    alpha_mod, loc_mod, beta_mod = ss.gamma.fit(sim, loc=0)
    obs = np.sort(obs)
    alpha_obs, loc_obs, beta_obs = ss.gamma.fit(obs, loc=0)

    fcst_fcst_correc = []
    for i in fcst:
        prob = ss.gamma.cdf(i, alpha_mod, scale=beta_mod)
        fcst_correc.append(ss.gamma.ppf(prob, alpha_obs, scale=beta_obs))
        
    return fcst_correct


def compute_effic_coeffic(model, obs):

    """
    The input arrays must have the same dimensions
    :Param model: Numpy array with model data
    :Param obs: Numpy array with obs data
    :Return: Nash–Sutcliffe Efficient Coefficient
    """

    nash = 1 - sum((model - obs) ** 2) / sum((obs - np.mean(obs)) ** 2)
    
    return nash
    
    
def compute_index_agreement(model, obs):

    """
    The input arrays must have the same dimensions
    :Param model: Numpy array with model data
    :Param obs: Numpy array with obs data
    :Return: Index of Agreement
    """

    p1 = (model - obs)**2
    p2 = np.abs(model - np.mean(obs))
    p3 = np.abs(obs - np.mean(obs))
    icw = 1 - sum(p1) / sum((p2 + p3)**2)
    
    return icw
    

def compute_added_value(gcm, rcm, obs):

    """
    The input arrays must have the same dimensions
    :Param rcm: Numpy array with regional model data
    :Param gcm: Numpy array with global model data
    :Param obs: Numpy array with obs data
    :Return: Added Value Index
    """

    p1 = (gcm - obs)**2
    p2 = (rcm - obs)**2
    p3 = p1 - p2
    p4 = np.max([p1, p2], axis=0)  
    av = p3 / p4
   
    return av
    
    

	
	
