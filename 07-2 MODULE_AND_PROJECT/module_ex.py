import fah_converter # 같은 폴더 안에 있으면 모듈을 불러옴

if __name__ == "__main__":
    print("Enter a celcius value: "),
    celcius = float(input())
    fahrenheit = fah_converter.convert_c_to_f(celcius)  # 모듈명.함수명() 형태로
    
    print ("Tha's {0} degrees Fahrenheit".format(fahrenheit))
# print ("Tha's", fahrenheit, " degrees Fahrenheit")
