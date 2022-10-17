# Quickbase Development Repository

This repository is designed to orchestrate the flow of data from the various sources into Quickbase 
via the Quickbase, Dropbox and OneDrive API. It is customizable based on what needs to be accomplished. 

## Components

This repository contains 

1. Two Jupyter Notebooks that contain user inputs and are designed to be run one time, at creation of the application. 

* `A_Tables` - contains user inputs in order to quickly create or delete tables via the Quickbase API
* `B_BuildInit` - Builds the initial Library and DateRange table. Stores data on Dropbox (will change to OneDrive)

2. There are two Python scripts designed to be run on schedule. 
* `C_Update_Library` - runs on an hourly schedule and updates the Library data in full. This uses the Dropbox API
* `D_Update_DateRange` - runs on a 1-minute schedule and appends records to the DateRange table via the Quickbase API

3. Python scripts that begin with an `f` are sub-functions. 

The `D_Update_DateRange` python script works by referencing the last time the script was run and checks for all records after that timestamp. 
It then uses the Quickbase API to add those individual records. 

Quickbase pipelines are built within the application and triggered based on files being updated.

## Environment Variables
To update environment variables (i.e. Dropbox API, Quickbase API) use the bash_profile and update the variable names. 
`nano ~/.bash_profile` 