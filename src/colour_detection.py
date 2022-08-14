import cv2
import numpy as np


def colour_extraction(settings_values, img_src, colour_choice):
    img = cv2.imread(img_src)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    if int(colour_choice) == 3:  # If it is red.
        lower_bound = np.array(settings_values[1])
        upper_bound = np.array(settings_values[2])
        mask0 = cv2.inRange(hsv, lower_bound, upper_bound)

        lower_bound = np.array(settings_values[3])
        upper_bound = np.array(settings_values[4])
        mask1 = cv2.inRange(hsv, lower_bound, upper_bound)

        mask = mask0 + mask1

        kernel = np.ones((7, 7), np.uint8)

        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

        segmented_img = cv2.bitwise_and(img, img, mask=mask)

        contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        output = cv2.drawContours(img, contours, -1, (0, 0, 255), 2)

        num = 0
        for c in contours:
            num = num + 1
            cv2.putText(output, settings_values[0], (c[0, 0, 0], c[0, 0, 1]), 1, 1, (255, 0, 0), 1)

        if num <= 0:
            print(settings_values[0], " not detected!\n")
            cv2.destroyAllWindows()
        else:
            # Showing the output
            cv2.imshow("Orig-Img", output)
            cv2.imshow("Mask", mask)
            cv2.imshow("Segmented Img", segmented_img)
            print("Press on the image and press \"0\" to go back to the menu. \n")

    else:  # If it is not red.
        lower_bound = np.array(settings_values[1])
        upper_bound = np.array(settings_values[2])

        mask = cv2.inRange(hsv, lower_bound, upper_bound)

        kernel = np.ones((7, 7), np.uint8)

        if img_src != "../selected_pics/daft-punk.png":
            mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
            mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

        segmented_img = cv2.bitwise_and(img, img, mask=mask)

        contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        output = cv2.drawContours(img, contours, -1, (0, 0, 255), 2)

        num = 0
        for c in contours:
            num = num + 1
            cv2.putText(output, settings_values[0], (c[0, 0, 0], c[0, 0, 1]), 1, 1, (255, 0, 0), 1)

        if num <= 0:
            print(settings_values[0], "not detected!\n")
        else:
            # Showing the Output
            cv2.imshow("Orig-Img", output)
            cv2.imshow("Mask", mask)
            cv2.imshow("Segmented Img", segmented_img)
            print("Press on the image and press \"0\" to go back to the menu. \n")

    esc = cv2.waitKey(0)
    if esc:
        cv2.destroyAllWindows()
