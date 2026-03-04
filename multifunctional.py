class multifunction():
        def Subfields():
            print("Sub-fields in AI are:")
            print("Machine Learning")
            print("Neural Networks")
            print("Vision")
            print("Robotics")
            print("Speech Processing")
            print("Natural Language Processing")
        def OddEven():
            number=int(input("Enter a number:"))
            if(number%2==0):
                print(number,"is a Even number")
                message="Even"
            else:
                print(number,"is a odd number")
                message="odd"
            return message
        def Eligible():
            gender=input("Please enter your gender")
            age=int(input("Please enter your age"))
            if(gender=="female" and age<18):
                print("Not eligible")
                result="Not eligible"
            elif(gender=="male" and age<21):
                print("Not eligible")
                result="Not eligible"
            else:
                print("Eligible")
                result="eligible"
                return result
        def percentage():
            subject1=int(input("Please enter your mark subject 1"))
            subject2=int(input("Please enter your mark subject 2"))
            subject3=int(input("Please enter your mark subject 3"))
            subject4=int(input("Please enter your mark subject 4"))
            subject5=int(input("Please enter your mark subject 5"))
            total=subject1+subject2+subject3+subject4+subject5
            percentage=total/5
            print(total)
            print(percentage)
        def areatriangle():
            print("Calculating Area of Triangle")
            Base=int(input("Please enter base"))
            Height=int(input("please enter height"))
            Area=(Base*Height)/2
            print("Base is", Base)
            print("Height is", Height)
            print("Area of a triangle ",Area)
            result="Area"
            return result
        def perimetertriangle():
            print("Calculating perimeter of Triangle")
            Height1=int(input("Please enter height 1"))
            Height2=int(input("please enter height 2"))
            Breath=int(input("Please enter base"))
            perimeter=Height1+Height2+Breath
            print("Height1 is", Height1)
            print("Height is", Height2)
            print("Perimeter of a triangle ",perimeter)
            result="perimeter"
            return result

