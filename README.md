<img src='docs/imgs/alien.gif' align="right" width=325>
<br><br><br>

# Ordered MeshCNN


In this project we tried to improve the MeshCNN architecture adding information to the dataset and enforcing it with transformer neural networks to avoi isometry invariance problem

# Getting Started

### Installation
- Clone this repo:
```bash
git clone https://github.com/Niro-jpg/EAI.git
cd MeshCNN
```
- Install dependencies
- Import Dataset
- Use to convert the dataset the following command 
```bash
./scripts/shrec/order.bat
```
### 3D Shape Classification on SHREC

Run training (if using conda env first activate env e.g. ```source activate meshcnn```)
```bash
./scripts/shrec/train.bat
```



Run test and export the intermediate pooled meshes:
```bash
./scripts/shrec/test.bat
```


Note, you can also get pre-trained weights using bash ```./scripts/shrec/get_pretrained.bat```. 



