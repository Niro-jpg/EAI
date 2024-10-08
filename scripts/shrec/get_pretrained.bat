@echo off

SET "CHECKPOINT=checkpoints\shrec16"
mkdir "-p" "%CHECKPOINT%"
wget "https://www.dropbox.com/s/wqq1qxj4fjbpfas/shrec16_wts.tar.gz"
tar "-xzvf" "shrec16_wts.tar.gz" && DEL  "shrec16_wts.tar.gz"
mv "latest_net.pth" "%CHECKPOINT%"
echo "downloaded pretrained weights to" "%CHECKPOINT%"