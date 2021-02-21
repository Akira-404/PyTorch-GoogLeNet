import os
import random
from shutil import copy, rmtree

'''
0、数据集目录结构应该满足：
    obj
    ├── car/
    ├── dog/
    ├── cat/
    ├── people/
    └── tree/
1、将当前脚本放置到数据集目录或者填入数据集地址
2、执行脚本自动分割1：9的验证集和训练集
'''


def main(data_path=None):
    random.seed(0)

    # 验证集比例
    split_rate = 0.1

    if data_path != None:
        if os.path.exists(data_path) == False:
            print("路径不存在")
            return
        # 改变路径
        os.chdir(data_path)

    root_path = os.getcwd()
    print("当前目录：", root_path)

    listdirs = os.listdir(root_path)
    dirs = []

    # 判断目录下是否那些文件是文件夹
    for dir in listdirs:
        if os.path.isdir(dir):
            dirs.append(dir)
    print("dirs:", dirs)

    mk_dirs = ["train", "val"]
    new_path = {}

    # 如果存在train和val文件夹则先删除
    for mk_dir in mk_dirs:
        file_path = os.path.join(root_path, mk_dir)
        if os.path.exists(file_path):
            print("文件已存在->删除:", file_path)
            dirs.remove(mk_dir)
            rmtree(file_path)

    # 创建train和validation文件夹
    for mk_dir in mk_dirs:
        file_path = os.path.join(root_path, mk_dir)
        os.mkdir(file_path)
        new_path[mk_dir] = file_path
        # 创建原始数据集中的文件夹
        print()
        for d in dirs:
            print("make dir:", os.path.join(file_path, d))
            os.mkdir(os.path.join(file_path, d))
    print(new_path)

    # 分配图片数据
    for cls in dirs:
        cls_path = os.path.join(root_path, cls)
        imgs = os.listdir(cls_path)
        num = len(imgs)
        print("img_path:{}\nnum:{}".format(cls_path, num))

        # 随机截取一定长度的内容,属于验证集
        val_index = random.sample(imgs, k=int(num * split_rate))

        flag = "val"
        for i, img in enumerate(imgs):
            # 如果图片属于验证集则copy到验证集,反之copy到训练集
            if img in val_index:
                flag = "val"
                src = os.path.join(cls_path, img)
                dst = os.path.join(new_path["val"], cls)
                copy(src, dst)

            else:
                flag = "train"
                src = os.path.join(cls_path, img)
                dst = os.path.join(new_path["train"], cls)
                copy(src, dst)
            print("\r[{}][{}] copy [{}/{}]".format(flag, cls, i + 1, num), end="")
            print()
    print("分割完成")


if __name__ == '__main__':
    main("/home/lee/pyCode/dl_data/flower_photos/")
