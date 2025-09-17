import os


class SetConfig():
    dir_name = "./data"
    extension_name = ".jpg" 
    file_name_path_1 = os.path.join(dir_name, "1"+ extension_name)
    file_name_path_2 = os.path.join(dir_name, "2"+ extension_name)
    file_name_path_3 = os.path.join(dir_name, "2"+ extension_name)
    file_name_path_4 = os.path.join(dir_name, "2"+ extension_name)
    save_dir_name = "./save_data"
    save_file_name_1 = os.path.join(save_dir_name, "1_"+extension_name)
    save_file_name_gr_1 = os.path.join(save_dir_name, "1_grascale"+extension_name)
    save_file_name_no_1 = os.path.join(save_dir_name, "1_no"+extension_name)
