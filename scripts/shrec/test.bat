@echo off

python3 "test.py" "--dataroot" "datasets\shrec_16" "--name" "shrec16" "--ncf" "64" "128" "256" "256" "--pool_res" "4000" "2000" "1500" "1000" "--norm" "group" "--resblocks" "1" "--export_folder" "meshes" ""