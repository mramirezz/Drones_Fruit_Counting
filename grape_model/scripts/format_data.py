import os
import shutil

data_dir = 'data'
train_file = 'train.txt'
test_file = 'test.txt'

dataset_yolo_dir = 'dataset_yolo'

images_train_dir = os.path.join(dataset_yolo_dir, 'images/train')
images_val_dir = os.path.join(dataset_yolo_dir, 'images/val')
labels_train_dir = os.path.join(dataset_yolo_dir, 'labels/train')
labels_val_dir = os.path.join(dataset_yolo_dir, 'labels/val')

os.makedirs(images_train_dir, exist_ok=True)
os.makedirs(images_val_dir, exist_ok=True)
os.makedirs(labels_train_dir, exist_ok=True)
os.makedirs(labels_val_dir, exist_ok=True)

def copy_files(file_list, images_dest, labels_dest):
    with open(file_list, 'r') as f:
        codes = f.read().splitlines()
    
    for code in codes:
        img_file = f'{code}.jpg'
        txt_file = f'{code}.txt'
        
        src_img_path = os.path.join(data_dir, img_file)
        src_txt_path = os.path.join(data_dir, txt_file)
        
        dest_img_path = os.path.join(images_dest, img_file)
        dest_txt_path = os.path.join(labels_dest, txt_file)
        
        if os.path.exists(src_img_path) and os.path.exists(src_txt_path):
            shutil.copy(src_img_path, dest_img_path)
            shutil.copy(src_txt_path, dest_txt_path)
        else:
            print(f'Archivos no encontrados: {src_img_path}, {src_txt_path}')


copy_files(train_file, images_train_dir, labels_train_dir)

copy_files(test_file, images_val_dir, labels_val_dir)

print('Archivos copiados exitosamente.')
