# Crohn’s Disease Severity as a Function of the Microbiome

This repo contains the code to analyze Crohn’s Disease specific data in "Inflammatory Bowel Disease Multi-omics Database”. This database is the largest, most comprehensive datatset on the microbiome of IBD patients, to our knowledge. We only focused on a small set of patients who were diagnosed with Crohn’s disease. 

The repo contains two subfolders: Data and Output Files. The end result is a heat map of the metabolomics data from Crohn’s Disease patients.

The raw data that we need for our analysis is included in the repo in the Data folder. Additional data related to this project and more information on the database is provided at https://ibdmdb.org. This dataset is well-curated and has undergone initial processing. It can be downloaded directly from the website as a .tsv file. We opened these files using numbers and converted them to .csv files which are included in the Data folder. You can open the data sets in Excel, but they are very large and will likely take a long time to open.

The subfolder Output Files is currently empty, and will get
populated with the results from the Python file.

# Downloading Git Hub File

The repo includes a Python file which you can run to create the designated heat map. All large files are stored using git-lfs which should be used when working with data sets that are larger than 500 Mb. 

The data cannot be downloaded as a zip file because of the git-lfs structure.

## Installing

To perform the analysis, you'll first need to install the required
modules.

You should probably do this in a Python 3.7 virtual environment. I relied on Spyder within the anaconda environment to run the code. 
Note that all of these scripts were written in and for Python 3.7. 

I used pipreqs to look at the requirements of the code. As written, the code requires pandas 1.0.1, seaborn 0.10.0, numpy 1.18.1, and matplotlib 3.1.3.

To run the code, I downloaded the folder from GitHub and then ran the heat_map_metabolites.py file. Make sure to change your working directory to the appropriate directory so that your Output Files are saved in the correct location. The code is written so that the files will be saved in the folder “Output Files”. The installation instructions for pandas, seaborn, numpy and matplotlib are included in the beginning of the code, so you should not have to install these modules before running the code. 

The output files will contain two .csv files of processed data and a heat map comparing the patient’s hbi scores with the metabolite level. 

# Directory structure

#### Data

All data-related files are (or will be) in `Data/`:

* hmp2_metadata.csv is a large file that contains  all the data from the HMP2 study. Only a small subset corresponds to Crohn’s Disease patients. In our code, we will parse through the data to identify patients with Crohn’s Disease. We were especially interested in pulling the HBI values for each patient. The HBI index is an empirical measurement that is used to track clinical disease severity over time. 
* HMP2_metabolomics.csv contains all the metabolomics data corresponding to each patient. Not every patient has metabolomics data associated with their samples. We need to sort and collate this information to parse out which metabolomics data corresponds to which patient and which patients have HBI scores associated with them. 

#### Code

All of the code is in the main directory (not in a subfolder) as heat_map_metabolites.py

* heat_map_metabolites.py can be downloaded and run as a singular file to create the appropriate figure. 

#### Output Files

The Supplementary Files, Figures, and Tables are in the `OutputFiles/` folder.

* metabs_by_hbi_heatmap.png is our final figure. This figure shows the metabolites according to the HBI of the appropriate patient. We calculated the z score for the relative abundance of each metabolite for each patient and then ordered the patients by HBI. The heat map is z-scored by column.  
* sort_collate_metabolomics_zscore.csv is a processed version of the data that only includes patient’s with Crohn’s disease and the z score associated with specific metabolites. We calculated the z score for the relative abundance of each metabolite for each patient. 
* sort_collate_metabolomics.csv is a processed version of the metabolomics data set that only includes patients with Crohn’s disease who have an associated HBI score in their metadata. With this subset of patients, we pulled the patient metabolomic relative abundance data for further processing.

# References

* Lloyd Price J, et al. Multi-omics of the gut microbial ecosystem in inflammatory bowel diseases. Nature 2019; 569: 655-52. https://www.nature.com/articles/s41586-019-1237-9
* “The Inflammatory Bowel Disease Multi-omics Database” NIH Human Microbiome Project. https://www.ibdmdb.org
