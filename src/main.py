import value
import colour_detection
import os

while True:
    print("Select a picture you would like to extract colours from: \n"
          "-------------------------------------------------------- \n"
          "1) HSV Colour Range \n"
          "2) Beach Ball \n"
          "3) Among Us \n"
          "4) Daft Punk Album \n"
          "5) Power Rangers \n"
          "6) Fruit Basket \n"
          "7) Tokyo City \n"
          "8) Exit"
          )
    picture_choice = input("Your Input:")
    print("\n")

    if int(picture_choice) == 8:
        print(
            "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n"
            "MMMMMMMMMMMMMMMWWWWNNNNWWWWMMMMMMMMMMMMMMMWWWWWMMMMMMMMMMMMMMMMMMMM\n"
            "MMMMMMMMMMWWWNXK00OOOOOO000KXNWWMMMMMMWWNXKKKKKXNNWWMMMMMMMMMMMMMMM\n"
            "MMMMMMMMMWWX0kxxxxkkkkkkkkkkOO0XNNNNNXK0OOOOOOOOOO0KNWMMMMMMMMMMMMM\n"
            "MMMMMMMMWXOdddxxxkkkkkkkkkkkkkkkOO00OOOOOOOOOOOOOOkk0XWWMMMMMMMMMMM\n"
            "MMMMMMMWKxddxxxxxkkkkkkOOOOOOOOOOOOOOOOOOOOOOOOOOOOkkOKNWMMMMMMMMMM\n"
            "MMMMMMW0xdxxxkkxkkkOOOOOO00000OOOO000OO00OOOOOOO0OO00OO0XWMMMMMMMMM\n"
            "MMMMMNOdddxxkxxdddxxkkOO000000000000000000000000000000OO0XWMWMMMMMM\n"
            "MMMWXkooodddolc::;;;:::cclddxxkO000KKKKK0KKK000000OOOOkkkkOKNWMWMMM\n"
            "MWXOxdoddoolc:;,,,''......'',:loxk000KKKKK0Okxdollcc::ccllllx0NWMMM\n"
            "WKxoddxxxdoollllllllllllcc:::clodxkOOO0000Okxdl:;,,,,,,;::clclkNMMM\n"
            "WKdodxxxxxdoollccccllllllllcccclodxkkOOOOOkxdoollllllooddddxxdx0WMM\n"
            "WKdoddxddolcc:;''''....':clcc::::coxkOO00Oxdoolllol:,,:clclodddONMM\n"
            "WKdooooollccc:;',;;.  ..;lolc:;;;:odxOO0Okdolccodl,...':l::clodONMM\n"
            "MKdoddoodooooollccc:,',:cllcc::::codxkO00Oxlccclol;..':lllllooxKWMM\n"
            "MKxdxxxxxxxkkkxxddddoooooolllclloodxxkO00OkdolllooolllodddxkOKNWMMM\n"
            "WKxdxxxxkkkkkkkkxxxxxxdoollooddddddddxkO000OkxxdxxxkkkkkkOKXWWMMMMM\n"
            "WKxdxxxxkkkkkkkkkkxxxxxddoddddddddddddkO000OOOkkkOOOOOOOOXWWWMMMMMM\n"
            "WKxdxdxxxxkkkkkkkkxxxxxxxxxdoollllooodkO000OOkkkkOOOOOOkOKWWMMMMMMM\n"
            "WKdddddxxxkkkkkkkkkkkxxxxkxdollodoooodk0000OkxxxkOOOOOOkkkKWMMMMMMM\n"
            "WKdodddxxxkkkkkkkkkkkkxxxxkxoooddooodxOKKK0OkkxxkO00O0OOkxkXWMMMMMM\n"
            "WKdodddddddddddxxxxxxxddxxxxdoollloodkO00OkkkkkkOOOOOOOOkkxkXWMMMMM\n"
            "MKdlooodooolccc::::::::::clllllloddxxxkkkkxdxxkkkkkkkkkkkkkxONMMMMM\n"
            "W0oloooddddoolc:;;,,''....''''',;::::ccccc::cccccclooddxxxdx0NMMMMM\n"
            "WKolooooooooooooolllccc:::::::;;;;;;;;,,,,,,,,,,,,,;;:cllokKNWMMMMM\n"
            "WKl:;,''''''',,;:cllooooollooooooooooooooooooooooooooodddkXWMMMMMMM\n"
            "Wk,.................';:lddxxxddddddddddddddddxxxxdxxkkO0KNWMMMMMMMM\n"
            "Wk'.',,;;;;;;;;,,''.....':ldxxxxxxxxxddolllllllooodOKXWWWWWWMMMMMMM\n"
            "WO:;:::::::::::::;;:;,'.....;ldddolcc;,..........'c0NWMWWWWWMMMMMMM\n"
            "WOc;::::::::::::::::::;;,'.  .,:;'.........''''''..,;lkXWMWWMMMMMMM\n"
            "WOc;::::::::::::::::::::;;,..    ...',;;;::ccllllc:,,..,xXWMMMMMMMM\n"
            "WOc;:::::::::::::::::::::::;'.   .,;::;::lodddxxxdol::;..:0WWMMMMMM\n"
            "WOc;::::::::::::::::::::::::;,.. .',;::::clcllodxxxdoc;;,.;0WMMMMMM\n"
            "WOc;:::;;;;::::::::::::::::::;;'...',;:::::;::codxxxdl:;;..oNMMMMMM\n"
            "WO:,,'......',;;;::::::::::::;:;,'',;;:::::::;:codxxdl::;,.:KWMMMMM\n"
            "Wk'...',;;,'....,;:::;:::::::::::;;;;,,,,,,,;;;:lodol:;:;,.;KWMMMMM\n"
            "Wx..:oxkOOkkd:. .';::::::::::::::;'...........',;cc:::;:;..cNWWMMMM\n"
            "W0dxOOOOOOOO0k:. .,;::::::::::::;.. .'cooolc,....,;::::;'..kWMMMMMM\n"
            "WX0OOOOOOOOxo;. ..,;::::::::::::,.  .:kOOkkkxc.  .';;:;,..oNMMMMMMM\n"
            "WX0OOOOOkd:'. ..',;;:;;;;;;;;;;;,.   ,dOOkkkkxl.  .';;,..oNMMMMMMMM\n"
            "WNXKXXXK0xlllodxxxxxxxxxxxxxxxxxxdolldOKKKKKKK0xolloxxdokNWWMMMMMMM\n"
            "MMMMWWWMMMMMMMMWWWWWWWWWWWWWWWWWWWWWWWMMMMMMMMMMMMWWWWWWWMWWMMMMMMM\n"
            "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWMMMMMMMMWMMMMMMMMMMMMMMMMMMM\n"
            "- xQcL"
        )
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
                  "9) Black \n"
                  "10) White \t"
                  "11) Back")
            colour_choice = input("Your Input:")
            print("\n")

            if int(colour_choice) == 11:
                break
            else:
                settings_values = value.get_settings_values(int(colour_choice))  # Get HSV arrays of values for the colour.

                colour_detection.colour_extraction(settings_values, src_values, colour_choice)
