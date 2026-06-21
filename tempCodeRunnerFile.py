weight = float(input("請輸入體重(kg): "))
height = float(input("請輸入身高(cm): "))

BMI = weight / (height/100) **2
print(f"你的BMI是 {BMI:.1f}.") #:.1f表示保留小數點後一位
if BMI < 18.5:
    print("體重過輕")   
elif BMI < 24:
    print("體重正常")
elif BMI < 27:
    print("體重過重")
else:
    print("肥胖")