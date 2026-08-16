edad = 14

if edad >= 18: 
    print("Puedes pasar. ")
    if edad >= 21: 
        print("Y no solo eso, eres mayor en estados unidos")
    else: 
        print("Lamentablemente eres menor en Estados Unidos")
        
elif 13 < edad < 18:
    print("Eres legal en Suecia, pero no puedes pasar") 
    
elif edad <= 13:
    print("Ponte a estudiar mejor")
