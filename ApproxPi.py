#ApproxPi.py
#Name:
#Date:
#Assignment:
import math
import time


#PLEASE NOTE - This is an optional, extra credit portion of the lab.

def main():
  realPi = math.pi

  #ask user for decimal percision (up to 10)
  num1 = input("Enter how many decimal places you would like to round Pi to (Limit of 10): ")
  num2 = int(num1)
  start = time.time()
  #calculate pi using the approximation technique
  approxPi = 4
  sign = -1
  denominator = 3
  while round(approxPi,num2) != round(realPi,num2):
    print(approxPi)
    approxPi = approxPi + (sign * 4 / denominator)

    sign = sign * -1
    denominator = denominator + 2
  #Loop until the level of percision is reached

  end = time.time()

  elapsedTime = end - start
  print(elapsedTime)

if __name__ == '__main__':
  main()
