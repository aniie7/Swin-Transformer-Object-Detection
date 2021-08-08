import os


def check_data(imgs_path, labels_path):
    imgs_list = os.listdir(imgs_path)
    labels_list = os.listdir(labels_path)
    no_labels = [img_name for img_name in imgs_list if img_name[:-3]+'xml' not in labels_list]
    no_images = [label_name for label_name in labels_list if labels_path[:-3] + 'png' not in imgs_list]
    print(no_labels)
    print(no_images)
    print(len(no_images))
    print(len(no_labels))


if __name__ == '__main__':
    imgs_path = 'VOC2012/JPEGImages'
    labels_path = 'VOC2012/Annotations'
    check_data(imgs_path, labels_path)