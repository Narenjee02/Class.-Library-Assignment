class groupoffunction():
    def subfields():
            print("Sub-fields in AI are:")
            Lists=['Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Natural Language Processing']
            for temp in Lists:
                print(temp)
                sub="temp"
            return sub
    def oddEven():
            num=int(input("Enter a number:"))
            if(num%2)==0:
                print(num,"is Even number")
                message="Even Number"  
            else:
                print(num,"is Odd number")
                message="Odd Number"
            return message
    def percentage():
            Subject1=int(input("Subject1="))
            Subject2=int(input("Subject2="))
            Subject3=int(input("Subject3="))
            Subject4=int(input("Subject4="))
            Subject5=int(input("Subject5="))
            Add=Subject1+Subject2+Subject3+Subject4+Subject5
            print("Total :",Add)
            Percentage=Add/5
            print("Percentage :",Percentage)
            X="SSLC"
            return X
    def triangle():
             Height=int(input("Height:"))
             Breadth=int(input("Breadth:"))
             print("Area formula: (Height*Breadth)/2")
             print("Area of Triangle:",(Height*Breadth)/2)
             Weight="Triangle"
             Height1=int(input("Height1:"))
             Height2=int(input("Height2:"))
             Breadth=int(input("Breadth:"))
             print("Perimeter formula: Height1+Height2+Breadth")
             print("Perimeter of Triangle:",Height1+Height2+Breadth)
             weight="HHB"
             return Weight
    def Elegible():
                gender=input("Your Gender:")
                age=int(input("Your Age:"))
                if(age<21):
                    print("Not Eligible")
                    age="Not Eligible"
                else:
                    print("Eligible")
                    age="Eligible"
                gender=input("Your Gender:")
                age=int(input("Your Age:"))
                if(age<18):
                    print("Not Eligible")
                    age="Not Eligible"
                else:
                    print("Eligible")
                    age="Eligible"
                return age