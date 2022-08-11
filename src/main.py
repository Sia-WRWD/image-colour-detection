import value
import colour_detection
import os

while True:
    print("Select a picture you would like to extract colours from: \n"
          "-------------------------------------------------------- \n"
          "1) HSV Colour Range \n"
          "2) Beach Ball \n"
          "3) Power Rangers \n"
          "4) Among Us \n"
          "5) ? \n"
          "6) Exit"
          )
    picture_choice = input("Your Input:")
    print("\n")

    if int(picture_choice) == 6:
        print("Program has Ended.")
        os._exit(1)
    else:
        src_values = value.get_src_values(int(picture_choice))

        while True:
            print("Select a Colour to Extract: \n"
                  "--------------------------- \n"
                  "1) Green \t"
                  "2) Blue \t"
                  "3) Red \n"
                  "4) Yellow \t"
                  "5) Cyan \t"
                  "6) Magenta \n"
                  "7) Orange \t"
                  "8) Purple \t"
                  "9) Back")
            colour_choice = input("Your Input:")
            print("\n")

            if int(colour_choice) == 9:
                break
            else:
                settings_values = value.get_settings_values(int(colour_choice))  # Get HSV arrays of values for the colour.

                colour_detection.colour_extraction(settings_values, src_values, colour_choice)
