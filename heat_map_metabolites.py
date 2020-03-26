# -*- coding: utf-8 -*-

# Import the packages we need to run code
from pylab import *
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib import gridspec
from matplotlib import patches

# pull in the metadata csv
metadata = pd.read_csv('./Data/hmp2_metadata.csv', sep=',')
# Set the index to be the external ID, aka sample number
metadatamod = pd.DataFrame.set_index(metadata, metadata['External ID'])
# pull in the metabolomics csv
metabs = pd.read_csv('./Data/HMP2_metabolomics.csv', sep=',')

# Find the set of samples that have Crohn's Dz
CD_ind = list(np.where(metadata.diagnosis == 'CD'))
set_CD = {e for l in CD_ind for e in l}
# Find the places that the samples were for metabolomics
metabs_ind = list(np.where(metadata.data_type == \
                                                    'metabolomics'))
set_metabs = {e for l in metabs_ind for e in l}
# Find indices where both CD and metabolomics
CD_metabs_ind = pd.DataFrame({'Values': data} for data in (set_CD & set_metabs))
# Pull hbi and sample IDs (external IDs) for each sample
sample_IDs = []
hbis = []
for i in range(len(CD_metabs_ind)):
    index = CD_metabs_ind.Values[i]
    sample_IDs.append(metadata.iloc[index]['External ID'])
    hbis.append(metadata.iloc[index]['hbi'])
set_IDs = set(sample_IDs)
# The IDs to look at that are also in the metabolomics dataset
IDs_to_collate = pd.DataFrame({'Values': data} for data \
                              in(set_IDs & set(metabs.columns)))

# Create a dataframe that contains a collation of hbi in first row for those samples 
# whose hbi exists, followed by the metabolmic data for that sample in subsequent rows
Collated_metabs = pd.DataFrame()
for j in range(len(IDs_to_collate)):
    hbi_by_samp = pd.DataFrame([np.mean(metadatamod.loc[IDs_to_collate.loc[j]]['hbi'])], \
                                columns = [(metadatamod.loc[IDs_to_collate.loc[j]]\
                                            ['External ID']).iloc[0]])
    if not(hbi_by_samp.isnull().values.any()):
        pulled_metabs = metabs[IDs_to_collate.loc[j]]
        pulled_metabs.index += 1
        Collated_metabs = pd.concat([Collated_metabs, \
                                     pd.concat([hbi_by_samp, pulled_metabs])], axis=1)

# Find row-wise mean and std.
Collated_metabs_mean = Collated_metabs.mean(axis=1)
Collated_metabs_std = Collated_metabs.std(axis=1)

# sort the samples from low to high HBI
sort_Collated_metabs = Collated_metabs.sort_values(by = 0, axis=1)
sort_Collated_metabs.to_csv('./OutputFiles/03202020_sort_collate_metabolomics.csv')
# calculate z scores to normalize the data by row 
zscore_metabs = (sort_Collated_metabs.sub(Collated_metabs_mean, \
                                          axis = 'index')).div(Collated_metabs_std, \
                                            axis = 'index')
zscore_metabs.to_csv('./OutputFiles/03202020_sort_collate_metabolomics_zscore.csv') 

# plot the heatmap
fig_heatmap = figure(num=None, figsize=(12, 12), dpi=300)
plt.rcParams['font.size'] = 14
gs = gridspec.GridSpec(2, 1, height_ratios=[30, 1]) 
ax = fig_heatmap.add_subplot(gs[0])
sns.heatmap(data = zscore_metabs.loc[zscore_metabs.index != 0, :], cbar=True)
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
ax.get_xaxis().set_ticks([])
ax.get_yaxis().set_ticks([])
ax1 = fig_heatmap.add_subplot(gs[1])
ax1.get_xaxis().set_visible(False)
ax1.get_yaxis().set_visible(False)
ax1.get_xaxis().set_ticks([])
ax1.get_yaxis().set_ticks([])
sns.heatmap(data = sort_Collated_metabs.loc[sort_Collated_metabs.index == 0, :],\
            cbar=True, cmap ='Blues') 
text(15, 0.6, '0', fontsize=13)
text(47, 0.6, '1', fontsize=13)
text(74.5, 0.6, '2', fontsize=13)
text(93, 0.6, '3', fontsize=13)
text(107.5, 0.6, '4', fontsize=13)
text(117, 0.6, '5', fontsize=13)
text(122.5, 0.6, '6', fontsize=13)
text(128, 0.6, '7', fontsize=13)
text(133, 0.6, '8', fontsize=13)
text(135.5, 0.6, '9', fontsize=13)
text(138, 0.6, '18', fontsize=13)
fig_heatmap.text(0.03, 0.03, 'HBI', color='black', fontsize=16)
ax.set_title("Metabolomic Z Scores for Crohn's Disease Patients", fontsize=25)
fig_heatmap.tight_layout()
fig_heatmap.text(0.45, 0.008, 'Patients', ha='center', va='center', fontsize=20)
fig_heatmap.text(0.05, 0.5, 'Metabolites', ha='center', va='bottom', \
                 rotation='vertical', fontsize=20)
left, bottom, width, height = [0.845, 0.02, 0.05, 0.05]
ax3 = fig_heatmap.add_axes([left, bottom, width, height], frame_on = False, alpha = 1.0, fc = 'white')
ax3.set_axis_off()
rect = patches.Rectangle((0, 0), 1.0, 1.0, facecolor='white')
ax3.add_patch(rect)
plt.show(fig_heatmap)
fig_heatmap.savefig('./OutputFiles/metabs_by_hbi_heatmap.png', bbox='tight')