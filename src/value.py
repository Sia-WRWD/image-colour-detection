def get_src_values(pic_id):
    match pic_id:
        case 1:
            pic_1_src = "../selected_pics/hsv-colour-range.jpg"
            src_values = pic_1_src
        case 2:
            pic_2_src = "../selected_pics/color_ball.jfif"
            src_values = pic_2_src
        case 3:
            pic_3_src = "../selected_pics/among-us.jpg"
            src_values = pic_3_src
        case 4:
            pic_4_src = "../selected_pics/daft-punk.png"
            src_values = pic_4_src
        case 5:
            pic_5_src = "../selected_pics/power-rangers.jpg"
            src_values = pic_5_src
        case 6:
            pic_6_src = "../selected_pics/fruit-basket.jpg"
            src_values = pic_6_src
        case 7:
            pic_7_src = "../selected_pics/tokyo.jpg"
            src_values = pic_7_src

    return src_values


def get_settings_values(color_id):
    match color_id:
        case 1:
            green_settings = ["Green", [30, 25, 25], [80, 255, 255]]
            setting_values = green_settings
        case 2:
            blue_settings = ["Blue", [96, 16, 16], [126, 255, 255]]
            setting_values = blue_settings
        case 3:
            red_settings = ["Red", [0, 25, 25], [6, 255, 255], [170, 24, 24], [180, 255, 255]]
            setting_values = red_settings
        case 4:
            yellow_settings = ["Yellow", [20, 25, 25], [30, 255, 255]]
            setting_values = yellow_settings
        case 5:
            cyan_settings = ["Cyan", [84, 16, 36], [92, 255, 255]]
            setting_values = cyan_settings
        case 6:
            magenta_settings = ["Magenta", [151, 24, 24], [169, 255, 255]]
            setting_values = magenta_settings
        case 7:
            orange_settings = ["Orange", [8, 50, 50], [21, 255, 255]]
            setting_values = orange_settings
        case 8:
            purple_settings = ["Purple", [130, 12, 12], [147, 255, 255]]
            setting_values = purple_settings
        case 9:
            black_settings = ["Black", [0, 0, 0], [180, 50, 100]]
            setting_values = black_settings
        case 10:
            white_settings = ["White", [0, 0, 0], [180, 20, 255]]
            setting_values = white_settings

    return setting_values
