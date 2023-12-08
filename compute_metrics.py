import time
import numpy as np
from scipy import stats, linalg
from scipy.stats.stats import pearsonr
import pandas as pd
from IDTxl.idtxl.data import Data
from IDTxl.idtxl.multivariate_te import MultivariateTE

# data = Data()

# data.generate_mute_data(100, 5)

# settings = {

#     'cmi_estimator':  'JidtKraskovCMI',

#     'n_perm_max_stat': 200,

#     'n_perm_min_stat': 200,

#     'n_perm_omnibus': 500,

#     'n_perm_max_seq': 500,

#     'max_lag_sources': 5,

#     'min_lag_sources': 2

#     }

# network_analysis = MultivariateTE()

# results = network_analysis.analyse_network(settings, data)



def partial_corr(C):
    """
    Returns the sample linear partial correlation coefficients between pairs of variables in C, controlling 
    for the remaining variables in C.
    Parameters
    ----------
    C : array-like, shape  (p,n)
        Array with the different variables. Each column of C is taken as a variable
    Returns
    -------
    P : array-like, shape (p, p)
        P[i, j] contains the partial correlation of C[:, i] and C[:, j] controlling
        for the remaining variables in C.
    """

    C = np.asarray(C)
    C = C.T
    p = C.shape[1]
    P_corr = np.zeros((p, p), dtype=float) # sample linear partial correlation coefficients
    corr = np.corrcoef(C,rowvar=False) # Pearson product-moment correlation coefficients. #same for np.cov()
    corr_inv = linalg.inv(corr) # the (multiplicative) inverse of a matrix.

    for i in range(p):
        P_corr[i, i] = 1
        for j in range(i+1, p):
            # if (corr_inv[i,i]*corr_inv[j,j])<0:
                # print(corr_inv[i,i], corr_inv[j,j]) #CANT DO THISSSSS
            pcorr_ij = -corr_inv[i,j]/(np.sqrt(corr_inv[i,i]*corr_inv[j,j]))  
            # https://en.wikipedia.org/wiki/Partial_correlation#Using_matrix_inversion  
            P_corr[i,j]=pcorr_ij
            P_corr[j,i]=pcorr_ij
    return P_corr

def partial_corr_using_linear_regression(C):
    """
    %% MATLAB partial_corr equivalent script.
    Returns the sample linear partial correlation coefficients between pairs of variables in C, controlling 
    for the remaining variables in C.
    Parameters
    ----------
    C : array-like, shape  (p,n)
        Array with the different variables. Each column of C is taken as a variable
    Returns
    -------
    P : array-like, shape (p, p)
        P[i, j] contains the partial correlation of C[:, i] and C[:, j] controlling
        for the remaining variables in C.
    """
    
    C = np.asarray(C)
    C = C.T
    p = C.shape[1]
    P_corr = np.zeros((p, p), dtype=float)
    for i in range(p):
        P_corr[i, i] = 1
        for j in range(i+1, p):
            idx = np.ones(p, dtype=bool)
            idx[i] = False
            idx[j] = False
            beta_i = linalg.lstsq(C[:, idx], C[:, j])[0]
            beta_j = linalg.lstsq(C[:, idx], C[:, i])[0]

            res_j = C[:, j] - C[:, idx].dot(beta_i)
            res_i = C[:, i] - C[:, idx].dot(beta_j)
            
            corr = stats.pearsonr(res_i, res_j)[0]
            P_corr[i, j] = corr
            P_corr[j, i] = corr
        
    return P_corr

def pearson_corr(C):
    # return np.corrcoef(C)
    return pearsonr(C)

def pearson_corr_with_pval(C):
    corr = np.zeros((len(C), len(C)))
    pval = np.zeros((len(C), len(C)))

    for i in range(len(C)):
        for j in range(len(C)):
            corr[i][j], pval[i][j] = pearsonr(C[i], C[j])
    return corr, pval

# # print(partial_corr(ts_array[:5, :]))
# # print(partial_corr_using_linear_regression(ts_array[:5, :]))
# t = time.time()
# out = partial_corr(ts_array)
# elapsed = time.time() - t
# print(elapsed)

# t = time.time()
# out = partial_corr_using_linear_regression(ts_array)
# elapsed = time.time() - t
# print(elapsed)



#########

# ts_array = np.load('../Glasser180ts_run1_npy/sub-01.npy')
# print(partial_corr(ts_array))
# print(partial_corr(ts_array).shape)


