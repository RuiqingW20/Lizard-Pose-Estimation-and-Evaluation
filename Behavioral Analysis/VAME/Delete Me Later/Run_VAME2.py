# Imports
import vame
from pathlib import Path

# Set Up Variables
working_directory = "C:/Users/kaiwi/OneDrive/Documents/VAME/data/"
working_directory_path = Path("C:/Users/kaiwi/OneDrive/Documents/VAME/data/")
project = "lizard project"
videos = []
poses_estimations = []

# Initialize Project
config = 'C:/Users/kaiwi/OneDrive/Documents/VAME/data/lizard project-Nov27-2024/config.yaml'

# Create Motif Videos
vame.motif_videos(config, videoType='.mp4', parametrization='hmm')

# Run Community Detection -- Failed Here
vame.community(config, parametrization='hmm', cut_tree=3, cohort=False)

# UMAP Visualization
fig = vame.visualization(config, label='community')

# Generative Reconstruction Decoder
vame.generative_model(config, mode="centers")

# Output Video
vame.gif(config, pose_ref_index=[0,5], subtract_background=True, start=None,
         length=360, max_lag=30, label='community', file_format='.mp4', crop_size=(300,300))

# Source: VAME Documentation at https://ethoml.github.io/VAME/docs/getting_started/running
# Source: ChatGPT