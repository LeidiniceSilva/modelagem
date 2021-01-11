# -*- coding: utf-8 -*-

__author__      = "Leidinice Silva"
__email__       = "leidinicesilva@gmail.com"
__date__        = "12/29/2020"
__description__ = "This script plot seasonal cycle graphics from Reg and Had models end obs database"

import os
import netCDF4
import statistics
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib as mpl

# mpl.use('agg')

from pylab import *
from netCDF4 import Dataset
from sklearn import metrics
from scipy.stats import norm
from matplotlib.font_manager import FontProperties


def import_rcm(var, area, exp, dt):
	
	path = '/home/nice/Documents/dataset/rcm/{0}'.format(exp)	
	arq  = '{0}/{1}_{2}_reg_had_{3}_mon_{4}_lonlat_seamask.nc'.format(path, var, area, exp, dt)	
	
	data = netCDF4.Dataset(arq)
	var  = data.variables[var][:]
	lat  = data.variables['lat'][:]
	lon  = data.variables['lon'][:]
	value = var[:][:,:,:]

	annual_rcm = np.nanmean(np.nanmean(value[0:240:12,:,:], axis=1), axis=1) 
	season_rcm = np.nanmean(np.nanmean(value[2:240:3,:,:], axis=1), axis=1)
	djf_rcm = np.nanmean(season_rcm[3:80:4])
	mam_rcm = np.nanmean(season_rcm[0:80:4])
	jja_rcm = np.nanmean(season_rcm[1:80:4])
	son_rcm = np.nanmean(season_rcm[2:80:4])

	return annual_rcm, djf_rcm, mam_rcm, jja_rcm, son_rcm


def import_gcm(var, area, exp, dt):
	
	path = '/home/nice/Documents/dataset/gcm/{0}'.format(exp)	
	arq  = '{0}/{1}_{2}_Amon_HadGEM2-ES_{3}_r1i1p1_mon_{4}_lonlat_seamask.nc'.format(path, var, area, exp, dt)	
	
	data = netCDF4.Dataset(arq)
	var  = data.variables[var][:]
	lat  = data.variables['lat'][:]
	lon  = data.variables['lon'][:]
	value = var[:][:,:,:]

	annual_gcm = np.nanmean(np.nanmean(value[:,:,:], axis=1), axis=1) 
	season_gcm = np.nanmean(np.nanmean(value[0:240:3,:,:], axis=1), axis=1)
	djf_gcm = np.nanmean(season_gcm[3:80:4])
	mam_gcm = np.nanmean(season_gcm[0:80:4])
	jja_gcm = np.nanmean(season_gcm[1:80:4])
	son_gcm = np.nanmean(season_gcm[2:80:4])

	return annual_gcm, djf_gcm, mam_gcm, jja_gcm, son_gcm

	
def import_obs(var, area, dataset, dt):
	
	path = '/home/nice/Documents/dataset/obs'
	arq  = '{0}/{1}_{2}_{3}_obs_mon_{4}_lonlat.nc'.format(path, var, area, dataset, dt)	
			
	data = netCDF4.Dataset(arq)
	var  = data.variables[var][:] 
	lat  = data.variables['lat'][:]
	lon  = data.variables['lon'][:]
	value = var[:][:,:,:]

	annual_obs = np.nanmean(np.nanmean(value[:,:,:], axis=1), axis=1) 
	season_obs = np.nanmean(np.nanmean(value[0:240:3,:,:], axis=1), axis=1)
	djf_obs = np.nanmean(season_obs[3:80:4])
	mam_obs = np.nanmean(season_obs[0:80:4])
	jja_obs = np.nanmean(season_obs[1:80:4])
	son_obs = np.nanmean(season_obs[2:80:4])

	return annual_obs, djf_obs, mam_obs, jja_obs, son_obs
	
               
# Import regcm exps model end obs database climatology
# Precipitation
annual_rcm_pre_samz, djf_rcm_pre_samz, mam_rcm_pre_samz, jja_rcm_pre_samz, son_rcm_pre_samz = import_rcm('pr', 'samz', 'hist', '1986-2005')
annual_gcm_pre_samz, djf_gcm_pre_samz, mam_gcm_pre_samz, jja_gcm_pre_samz, son_gcm_pre_samz = import_gcm('pr', 'samz', 'hist', '1986-2005')
annual_cru_pre_samz, djf_cru_pre_samz, mam_cru_pre_samz, jja_cru_pre_samz, son_cru_pre_samz = import_obs('pre', 'samz', 'cru_ts4.04', '1986-2005')
annual_udel_pre_samz, djf_udel_pre_samz, mam_udel_pre_samz, jja_udel_pre_samz, son_udel_pre_samz = import_obs('pre', 'samz', 'udel_v301', '1986-2005')
annual_chirps_pre_samz, djf_chirps_pre_samz, mam_chirps_pre_samz, jja_chirps_pre_samz, son_chirps_pre_samz = import_obs('precip', 'samz', 'chirps-v2.0', '1986-2005')
annual_era5_pre_samz, djf_era5_pre_samz, mam_era5_pre_samz, jja_era5_pre_samz, son_era5_pre_samz = import_obs('mtpr', 'samz', 'era5', '1986-2005')

annual_rcm_pre_eneb, djf_rcm_pre_eneb, mam_rcm_pre_eneb, jja_rcm_pre_eneb, son_rcm_pre_eneb = import_rcm('pr', 'eneb', 'hist', '1986-2005')
annual_gcm_pre_eneb, djf_gcm_pre_eneb, mam_gcm_pre_eneb, jja_gcm_pre_eneb, son_gcm_pre_eneb = import_gcm('pr', 'eneb', 'hist', '1986-2005')
annual_cru_pre_eneb, djf_cru_pre_eneb, mam_cru_pre_eneb, jja_cru_pre_eneb, son_cru_pre_eneb = import_obs('pre', 'eneb', 'cru_ts4.04', '1986-2005')
annual_udel_pre_eneb, djf_udel_pre_eneb, mam_udel_pre_eneb, jja_udel_pre_eneb, son_udel_pre_eneb = import_obs('pre', 'eneb', 'udel_v301', '1986-2005')
annual_chirps_pre_eneb, djf_chirps_pre_eneb, mam_chirps_pre_eneb, jja_chirps_pre_eneb, son_chirps_pre_eneb = import_obs('precip', 'eneb', 'chirps-v2.0', '1986-2005')
annual_era5_pre_eneb, djf_era5_pre_eneb, mam_era5_pre_eneb, jja_era5_pre_eneb, son_era5_pre_eneb = import_obs('mtpr', 'eneb', 'era5', '1986-2005')

annual_rcm_pre_matopiba, djf_rcm_pre_matopiba, mam_rcm_pre_matopiba, jja_rcm_pre_matopiba, son_rcm_pre_matopiba = import_rcm('pr', 'matopiba', 'hist', '1986-2005')
annual_gcm_pre_matopiba, djf_gcm_pre_matopiba, mam_gcm_pre_matopiba, jja_gcm_pre_matopiba, son_gcm_pre_matopiba = import_gcm('pr', 'matopiba', 'hist', '1986-2005')
annual_cru_pre_matopiba, djf_cru_pre_matopiba, mam_cru_pre_matopiba, jja_cru_pre_matopiba, son_cru_pre_matopiba = import_obs('pre', 'matopiba', 'cru_ts4.04', '1986-2005')
annual_udel_pre_matopiba, djf_udel_pre_matopiba, mam_udel_pre_matopiba, jja_udel_pre_matopiba, son_udel_pre_matopiba = import_obs('pre', 'matopiba', 'udel_v301', '1986-2005')
annual_chirps_pre_matopiba, djf_chirps_pre_matopiba, mam_chirps_pre_matopiba, jja_chirps_pre_matopiba, son_chirps_pre_matopiba = import_obs('precip', 'matopiba', 'chirps-v2.0', '1986-2005')
annual_era5_pre_matopiba, djf_era5_pre_matopiba, mam_era5_pre_matopiba, jja_era5_pre_matopiba, son_era5_pre_matopiba = import_obs('mtpr', 'matopiba', 'era5', '1986-2005')

# Temperature
annual_rcm_tas_samz, djf_rcm_tas_samz, mam_rcm_tas_samz, jja_rcm_tas_samz, son_rcm_tas_samz = import_rcm('tas', 'samz', 'hist', '1986-2005')
annual_gcm_tas_samz, djf_gcm_tas_samz, mam_gcm_tas_samz, jja_gcm_tas_samz, son_gcm_tas_samz = import_gcm('tas', 'samz', 'hist', '1986-2005')
annual_cru_tas_samz, djf_cru_tas_samz, mam_cru_tas_samz, jja_cru_tas_samz, son_cru_tas_samz = import_obs('tmp', 'samz', 'cru_ts4.04', '1986-2005')
annual_udel_tas_samz, djf_udel_tas_samz, mam_udel_tas_samz, jja_udel_tas_samz, son_udel_tas_samz = import_obs('temp', 'samz', 'udel_v301', '1986-2005')
annual_era5_tas_samz, djf_era5_tas_samz, mam_era5_tas_samz, jja_era5_tas_samz, son_era5_tas_samz = import_obs('t2m', 'samz', 'era5', '1986-2005')

annual_rcm_tas_eneb, djf_rcm_tas_eneb, mam_rcm_tas_eneb, jja_rcm_tas_eneb, son_rcm_tas_eneb = import_rcm('tas', 'eneb', 'hist', '1986-2005')
annual_gcm_tas_eneb, djf_gcm_tas_eneb, mam_gcm_tas_eneb, jja_gcm_tas_eneb, son_gcm_tas_eneb = import_gcm('tas', 'eneb', 'hist', '1986-2005')
annual_cru_tas_eneb, djf_cru_tas_eneb, mam_cru_tas_eneb, jja_cru_tas_eneb, son_cru_tas_eneb = import_obs('tmp', 'eneb', 'cru_ts4.04', '1986-2005')
annual_udel_tas_eneb, djf_udel_tas_eneb, mam_udel_tas_eneb, jja_udel_tas_eneb, son_udel_tas_eneb = import_obs('temp', 'eneb', 'udel_v301', '1986-2005')
annual_era5_tas_eneb, djf_era5_tas_eneb, mam_era5_tas_eneb, jja_era5_tas_eneb, son_era5_tas_eneb = import_obs('t2m', 'eneb', 'era5', '1986-2005')

annual_rcm_tas_matopiba, djf_rcm_tas_matopiba, mam_rcm_tas_matopiba, jja_rcm_tas_matopiba, son_rcm_tas_matopiba = import_rcm('tas', 'matopiba', 'hist', '1986-2005')
annual_gcm_tas_matopiba, djf_gcm_tas_matopiba, mam_gcm_tas_matopiba, jja_gcm_tas_matopiba, son_gcm_tas_matopiba = import_gcm('tas', 'matopiba', 'hist', '1986-2005')
annual_cru_tas_matopiba, djf_cru_tas_matopiba, mam_cru_tas_matopiba, jja_cru_tas_matopiba, son_cru_tas_matopiba = import_obs('tmp', 'matopiba', 'cru_ts4.04', '1986-2005')
annual_udel_tas_matopiba, djf_udel_tas_matopiba, mam_udel_tas_matopiba, jja_udel_tas_matopiba, son_udel_tas_matopiba = import_obs('temp', 'matopiba', 'udel_v301', '1986-2005')
annual_era5_tas_matopiba, djf_era5_tas_matopiba, mam_era5_tas_matopiba, jja_era5_tas_matopiba, son_era5_tas_matopiba = import_obs('t2m', 'matopiba', 'era5', '1986-2005')

# Plot model end obs data climatology
fig = plt.figure()
time = np.arange(1, 5 + 1)

ax1 = fig.add_subplot(3, 2, 1)
plt.plot(1, djf_rcm_pre_samz, 'ko')
plt.plot(1, djf_gcm_pre_samz, 'bo')
plt.plot(1, djf_cru_pre_samz, 'r^')
plt.plot(1, djf_udel_pre_samz, 'g+')
plt.plot(1, djf_chirps_pre_samz, 'y*')
plt.plot(1, djf_era5_pre_samz, 'mx')
plt.plot(2, mam_rcm_pre_samz, 'ko')
plt.plot(2, mam_gcm_pre_samz, 'bo')
plt.plot(2, mam_cru_pre_samz, 'r^')
plt.plot(2, mam_udel_pre_samz, 'g+')
plt.plot(2, mam_chirps_pre_samz, 'y*')
plt.plot(2, mam_era5_pre_samz, 'mx')
plt.plot(3, jja_rcm_pre_samz, 'ko')
plt.plot(3, jja_gcm_pre_samz, 'bo')
plt.plot(3, jja_cru_pre_samz, 'r^')
plt.plot(3, jja_udel_pre_samz, 'g+')
plt.plot(3, jja_chirps_pre_samz, 'y*')
plt.plot(3, jja_era5_pre_samz, 'mx')
plt.plot(4, son_rcm_pre_samz, 'ko')
plt.plot(4, son_gcm_pre_samz, 'bo')
plt.plot(4, son_cru_pre_samz, 'r^')
plt.plot(4, son_udel_pre_samz, 'g+')
plt.plot(4, son_chirps_pre_samz, 'y*')
plt.plot(4, son_era5_pre_samz, 'mx')
plt.plot(5, np.nanmean(annual_rcm_pre_samz, axis=0), 'ko')
plt.plot(5, np.nanmean(annual_gcm_pre_samz, axis=0), 'bo')
plt.plot(5, np.nanmean(annual_cru_pre_samz, axis=0), 'r^')
plt.plot(5, np.nanmean(annual_udel_pre_samz, axis=0), 'g+')
plt.plot(5, np.nanmean(annual_chirps_pre_samz, axis=0), 'y*')
plt.plot(5, np.nanmean(annual_era5_pre_samz, axis=0), 'mx')
plt.title(u'A) SAMZ', fontweight='bold')
plt.xticks(time, ('DJF', 'MAM', 'JJA', 'SON', 'Annual'))
plt.yticks(np.arange(0, 14, 2), fontsize=7)
plt.setp(ax1.get_xticklabels(), visible=False)
ax1.xaxis.grid(True, which='major', linestyle='--')
ax1.yaxis.grid(True, which='major', linestyle='--')

ax2 = fig.add_subplot(3, 2, 2)
plt.plot(1, djf_rcm_tas_samz, 'ko')
plt.plot(1, djf_gcm_tas_samz, 'bo')
plt.plot(1, djf_cru_tas_samz, 'r^')
plt.plot(1, djf_udel_tas_samz, 'g+')
plt.plot(1, djf_era5_tas_samz, 'mx')
plt.plot(2, mam_rcm_tas_samz, 'ko')
plt.plot(2, mam_gcm_tas_samz, 'bo')
plt.plot(2, mam_cru_tas_samz, 'r^')
plt.plot(2, mam_udel_tas_samz, 'g+')
plt.plot(2, mam_era5_tas_samz, 'mx')
plt.plot(3, jja_rcm_tas_samz, 'ko')
plt.plot(3, jja_gcm_tas_samz, 'bo')
plt.plot(3, jja_cru_tas_samz, 'r^')
plt.plot(3, jja_udel_tas_samz, 'g+')
plt.plot(3, jja_era5_tas_samz, 'mx')
plt.plot(4, son_rcm_tas_samz, 'ko')
plt.plot(4, son_gcm_tas_samz, 'bo')
plt.plot(4, son_cru_tas_samz, 'r^')
plt.plot(4, son_udel_tas_samz, 'g+')
plt.plot(4, son_era5_tas_samz, 'mx')
plt.plot(5, np.nanmean(np.nanmean(annual_rcm_tas_samz, axis=0), axis=0), 'ko')
plt.plot(5, np.nanmean(np.nanmean(annual_gcm_tas_samz, axis=0), axis=0), 'bo')
plt.plot(5, np.nanmean(np.nanmean(annual_cru_tas_samz, axis=0), axis=0), 'r^')
plt.plot(5, np.nanmean(np.nanmean(annual_udel_tas_samz, axis=0), axis=0), 'g+')
plt.plot(5, np.nanmean(np.nanmean(annual_era5_tas_samz, axis=0), axis=0), 'mx')
plt.title(u'D) SAMZ', fontweight='bold')
plt.xticks(time, ('DJF', 'MAM', 'JJA', 'SON', 'Annual'))
plt.yticks(np.arange(20, 32, 2), fontsize=7)
plt.setp(ax2.get_xticklabels(), visible=False)
ax2.xaxis.grid(True, which='major', linestyle='--')
ax2.yaxis.grid(True, which='major', linestyle='--')

ax3 = fig.add_subplot(3, 2, 3)
plt.plot(1, djf_rcm_pre_eneb, 'ko')
plt.plot(1, djf_gcm_pre_eneb, 'bo')
plt.plot(1, djf_cru_pre_eneb, 'r^')
plt.plot(1, djf_udel_pre_eneb, 'g+')
plt.plot(1, djf_chirps_pre_eneb, 'y*')
plt.plot(1, djf_era5_pre_eneb, 'mx')
plt.plot(2, mam_rcm_pre_eneb, 'ko')
plt.plot(2, mam_gcm_pre_eneb, 'bo')
plt.plot(2, mam_cru_pre_eneb, 'r^')
plt.plot(2, mam_udel_pre_eneb, 'g+')
plt.plot(2, mam_chirps_pre_eneb, 'y*')
plt.plot(2, mam_era5_pre_eneb, 'mx')
plt.plot(3, jja_rcm_pre_eneb, 'ko')
plt.plot(3, jja_gcm_pre_eneb, 'bo')
plt.plot(3, jja_cru_pre_eneb, 'r^')
plt.plot(3, jja_udel_pre_eneb, 'g+')
plt.plot(3, jja_chirps_pre_eneb, 'y*')
plt.plot(3, jja_era5_pre_eneb, 'mx')
plt.plot(4, son_rcm_pre_eneb, 'ko')
plt.plot(4, son_gcm_pre_eneb, 'bo')
plt.plot(4, son_cru_pre_eneb, 'r^')
plt.plot(4, son_udel_pre_eneb, 'g+')
plt.plot(4, son_chirps_pre_eneb, 'y*')
plt.plot(4, son_era5_pre_eneb, 'mx')
plt.plot(5, np.nanmean(annual_rcm_pre_eneb, axis=0), 'ko')
plt.plot(5, np.nanmean(annual_gcm_pre_eneb, axis=0), 'bo')
plt.plot(5, np.nanmean(annual_cru_pre_eneb, axis=0), 'r^')
plt.plot(5, np.nanmean(annual_udel_pre_eneb, axis=0), 'g+')
plt.plot(5, np.nanmean(annual_chirps_pre_eneb, axis=0), 'y*')
plt.plot(5, np.nanmean(annual_era5_pre_eneb, axis=0), 'mx')
plt.title(u'B) ENEB', fontweight='bold')
plt.ylabel(u'Precipitation (mm d⁻¹)', fontweight='bold')
plt.xticks(time, ('DJF', 'MAM', 'JJA', 'SON', 'Annual'))
plt.yticks(np.arange(0, 12, 2), fontsize=7)
plt.setp(ax3.get_xticklabels(), visible=False)
ax3.xaxis.grid(True, which='major', linestyle='--')
ax3.yaxis.grid(True, which='major', linestyle='--')

ax4 = fig.add_subplot(3, 2, 4)
plt.plot(1, djf_rcm_tas_eneb, 'ko')
plt.plot(1, djf_gcm_tas_eneb, 'bo')
plt.plot(1, djf_cru_tas_eneb, 'r^')
plt.plot(1, djf_udel_tas_eneb, 'g+')
plt.plot(1, djf_era5_tas_eneb, 'mx')
plt.plot(2, mam_rcm_tas_eneb, 'ko')
plt.plot(2, mam_gcm_tas_eneb, 'bo')
plt.plot(2, mam_cru_tas_eneb, 'r^')
plt.plot(2, mam_udel_tas_eneb, 'g+')
plt.plot(2, mam_era5_tas_eneb, 'mx')
plt.plot(3, jja_rcm_tas_eneb, 'ko')
plt.plot(3, jja_gcm_tas_eneb, 'bo')
plt.plot(3, jja_cru_tas_eneb, 'r^')
plt.plot(3, jja_udel_tas_eneb, 'g+')
plt.plot(3, jja_era5_tas_eneb, 'mx')
plt.plot(4, son_rcm_tas_eneb, 'ko')
plt.plot(4, son_gcm_tas_eneb, 'bo')
plt.plot(4, son_cru_tas_eneb, 'r^')
plt.plot(4, son_udel_tas_eneb, 'g+')
plt.plot(4, son_era5_tas_eneb, 'mx')
plt.plot(5, np.nanmean(np.nanmean(annual_rcm_tas_eneb, axis=0), axis=0), 'ko')
plt.plot(5, np.nanmean(np.nanmean(annual_gcm_tas_eneb, axis=0), axis=0), 'bo')
plt.plot(5, np.nanmean(np.nanmean(annual_cru_tas_eneb, axis=0), axis=0), 'r^')
plt.plot(5, np.nanmean(np.nanmean(annual_udel_tas_eneb, axis=0), axis=0), 'g+')
plt.plot(5, np.nanmean(np.nanmean(annual_era5_tas_eneb, axis=0), axis=0), 'mx')
plt.title(u'E) ENEB', fontweight='bold')
plt.ylabel(u'Temperature (°C)', fontweight='bold')
plt.xticks(time, ('DJF', 'MAM', 'JJA', 'SON', 'Annual'))
plt.yticks(np.arange(20, 32, 2), fontsize=7)
plt.setp(ax4.get_xticklabels(), visible=False)
ax4.xaxis.grid(True, which='major', linestyle='--')
ax4.yaxis.grid(True, which='major', linestyle='--')

ax5 = fig.add_subplot(3, 2, 5)
ax51=plt.plot(1, djf_rcm_pre_matopiba, 'ko', 1, djf_gcm_pre_matopiba, 'bo', 1, djf_cru_pre_matopiba, 'r^', 1, djf_udel_pre_matopiba, 'g+', 1, djf_chirps_pre_matopiba, 'y*', 1, djf_era5_pre_matopiba, 'mx')
plt.plot(2, mam_rcm_pre_matopiba, 'ko')
plt.plot(2, mam_gcm_pre_matopiba, 'bo')
plt.plot(2, mam_cru_pre_matopiba, 'r^')
plt.plot(2, mam_udel_pre_matopiba, 'g+')
plt.plot(2, mam_chirps_pre_matopiba, 'y*')
plt.plot(2, mam_era5_pre_matopiba, 'mx')
plt.plot(3, jja_rcm_pre_matopiba, 'ko')
plt.plot(3, jja_gcm_pre_matopiba, 'bo')
plt.plot(3, jja_cru_pre_matopiba, 'r^')
plt.plot(3, jja_udel_pre_matopiba, 'g+')
plt.plot(3, jja_chirps_pre_matopiba, 'y*')
plt.plot(3, jja_era5_pre_matopiba, 'mx')
plt.plot(4, son_rcm_pre_matopiba, 'ko')
plt.plot(4, son_gcm_pre_matopiba, 'bo')
plt.plot(4, son_cru_pre_matopiba, 'r^')
plt.plot(4, son_udel_pre_matopiba, 'g+')
plt.plot(4, son_chirps_pre_matopiba, 'y*')
plt.plot(4, son_era5_pre_matopiba, 'mx')
plt.plot(5, np.nanmean(annual_rcm_pre_matopiba, axis=0), 'ko')
plt.plot(5, np.nanmean(annual_gcm_pre_matopiba, axis=0), 'bo')
plt.plot(5, np.nanmean(annual_cru_pre_matopiba, axis=0), 'r^')
plt.plot(5, np.nanmean(annual_udel_pre_matopiba, axis=0), 'g+')
plt.plot(5, np.nanmean(annual_chirps_pre_matopiba, axis=0), 'y*')
plt.plot(5, np.nanmean(annual_era5_pre_matopiba, axis=0), 'mx')
plt.title(u'C) MATOPIBA', fontweight='bold')
plt.xlabel(u'Period', fontweight='bold')
plt.xticks(time, ('DJF', 'MAM', 'JJA', 'SON', 'Annual'), fontsize=7)
plt.yticks(np.arange(0, 12, 2), fontsize=7)
ax5.xaxis.grid(True, which='major', linestyle='--')
ax5.yaxis.grid(True, which='major', linestyle='--')

legend = ['Reg','Had','CRU','UDEL','CHIRPS','ERA5']
plt.legend(ax51, legend, loc='lower left', bbox_to_anchor=(-0.3, -0.8), shadow=True, ncol=6)

ax6 = fig.add_subplot(3, 2, 6)
plt.plot(1, djf_rcm_tas_matopiba, 'ko')
plt.plot(1, djf_gcm_tas_matopiba, 'bo')
plt.plot(1, djf_cru_tas_matopiba, 'r^')
plt.plot(1, djf_udel_tas_matopiba, 'g+')
plt.plot(1, djf_era5_tas_matopiba, 'mx')
plt.plot(2, mam_rcm_tas_matopiba, 'ko')
plt.plot(2, mam_gcm_tas_matopiba, 'bo')
plt.plot(2, mam_cru_tas_matopiba, 'r^')
plt.plot(2, mam_udel_tas_matopiba, 'g+')
plt.plot(2, mam_era5_tas_matopiba, 'mx')
plt.plot(3, jja_rcm_tas_matopiba, 'ko')
plt.plot(3, jja_gcm_tas_matopiba, 'bo')
plt.plot(3, jja_cru_tas_matopiba, 'r^')
plt.plot(3, jja_udel_tas_matopiba, 'g+')
plt.plot(3, jja_era5_tas_matopiba, 'mx')
plt.plot(4, son_rcm_tas_matopiba, 'ko')
plt.plot(4, son_gcm_tas_matopiba, 'bo')
plt.plot(4, son_cru_tas_matopiba, 'r^')
plt.plot(4, son_udel_tas_matopiba, 'g+')
plt.plot(4, son_era5_tas_matopiba, 'mx')
plt.plot(5, np.nanmean(np.nanmean(annual_rcm_tas_matopiba, axis=0), axis=0), 'ko')
plt.plot(5, np.nanmean(np.nanmean(annual_gcm_tas_matopiba, axis=0), axis=0), 'bo')
plt.plot(5, np.nanmean(np.nanmean(annual_cru_tas_matopiba, axis=0), axis=0), 'r^')
plt.plot(5, np.nanmean(np.nanmean(annual_udel_tas_matopiba, axis=0), axis=0), 'g+')
plt.plot(5, np.nanmean(np.nanmean(annual_era5_tas_matopiba, axis=0), axis=0), 'mx')
plt.title(u'F) MATOPIBA', fontweight='bold')
plt.xlabel(u'Period', fontweight='bold')
plt.xticks(time, ('DJF', 'MAM', 'JJA', 'SON', 'Annual'), fontsize=7)
plt.yticks(np.arange(20, 32, 2), fontsize=7)
ax6.xaxis.grid(True, which='major', linestyle='--')
ax6.yaxis.grid(True, which='major', linestyle='--')

fig.tight_layout()
plt.subplots_adjust(left=0.15, bottom=0.15, right=0.93, top=0.93, wspace=0.35, hspace=0.35)

# Path out to save figure
path_out = '/home/nice/Downloads'
name_out = 'pyplt_seasonal_cicle_reg_had_obs_1986-2005.png'
if not os.path.exists(path_out):
	create_path(path_out)
plt.savefig(os.path.join(path_out, name_out), dpi=200, bbox_inches='tight')

plt.show()
exit()








