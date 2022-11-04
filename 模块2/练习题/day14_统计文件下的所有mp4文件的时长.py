"""统计文件下的所有mp4文件的时长"""
import os
import cv2


def get_duration_from_cv2(filename):
    cap = cv2.VideoCapture(filename)
    if cap.isOpened():
        rate = cap.get(5)
        frame_num = cap.get(7)
        duration = frame_num / rate
        return duration
    return -1


def get_video_hour(walk_path):
    dir_path_generator = os.walk(walk_path)
    total_time = 0
    for dir_path, dir_list, file_name_list in dir_path_generator:
        for file_name in file_name_list:
            file_path = os.path.join(dir_path, file_name)
            # print(file_path)
            file_suffix = file_path.rsplit('.')[-1]
            if file_suffix == 'mp4':
                video_time = get_duration_from_cv2(file_path)
                total_time += video_time
    return round(total_time / 60 / 60, 2)


def main():
    walk_path = r'C:\Users\Administrator\Desktop\影视课'
    video_hour = get_video_hour(walk_path)
    print('总时长：{} hour'.format(video_hour))


if __name__ == '__main__':
    main()
    ...