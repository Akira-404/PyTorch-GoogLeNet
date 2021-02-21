# PyTorch-GoogLeNet  
使用pytorch实现GoogLeNet  



## 目录文件：

1. model.py
2. split_data.py
3. train.py
4. test.py



## 文件介绍：

model.py：GoogLeNet模型  

split_data.py：用于分割数据集  

train.py：用于训练网络模型  

test.py：用于测试网络  



## 注意：

数据集文件夹应该满足如下格式：

1. split_data.py中如果不填入任何目录，需要把split_data.py放入数据集文件夹，运行后以1：9自动分割验证集和训练集。  
2. split_data.py中如果填入目录，应该填入完整路径:（xxx/xxx/obj/）

    obj  
    ├── car/  
    ├── dog/  
    ├── cat/  
    ├── people/  
    └── tree/  
train.py中的训练集地址应该更改到对于的数据集地址：xxx/xxx/ojb

