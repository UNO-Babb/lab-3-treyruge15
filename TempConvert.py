#TempConvert.py
#Name:
#Date:
#Assignment:


def main():
  #Prompt the user for a Fahrenheit temperature
  #Convert that temperature to celsius, rounding to 1 decimal percision
  #Output converted temperature.
  tempF = input("Enter a temperature in degrees Farenheit: ")
  num1 = float(tempF)
  num2 = (num1-32) / (9/5)
  tempC = round(num2,1)
  
  print(tempF, "is ", tempC, "degrees celsius.")
if __name__ == '__main__':
  main()
