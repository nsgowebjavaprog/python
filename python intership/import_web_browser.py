import webbrowser

choice=int(input("\n 1:Google\n 2:YOUTUBE\n 3:WHATSAPP\n Hello,User Enter the choice :"))



if choice == 1:
    webbrowser.open("https://www.programiz.com/python-programming")
    
if choice == 2:    

    webbrowser.open("https://www.youtube.com/watch?v=aFg6Zy5I0Mk")

if choice == 3:
    webbrowser.open("https://web.whatsapp.com/#")
else:
    print("wrong input")