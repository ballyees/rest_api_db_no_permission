#!/bin/bash

source C:/Users/MSI-PS42-OEM/Anaconda3/etc/profile.d/conda.sh
conda activate sanicAPI
echo "Start restful-api Store, PID: $BASHPID"
python D:/Subject/Database/dbproject/rest_api_db_no_permission/main.py