@echo off

python3 "train.py" "--dataroot" "datasets\shrec_16" "--name" "shrec16" "--ncf" "64" "128" "256" "256" "--pool_res" "4000" "2000" "1500" "1000" "--norm" "group" "--resblocks" "1" "--flip_edges" "0.2" "--slide_verts" "0.2" "--num_aug" "20" "--niter_decay" "100" ""