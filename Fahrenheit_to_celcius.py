#a program to convert fahrenheit to celcius
name=input("Enter your name:")
print("Hello",name)
fahren=float(input("Please Enter The Temparature (Fahrenheit): "))
celcius=(fahren-32)*5/9
celcius=round(celcius,2)
print("The temparature in Celcius is ",celcius,"Thank you",name)