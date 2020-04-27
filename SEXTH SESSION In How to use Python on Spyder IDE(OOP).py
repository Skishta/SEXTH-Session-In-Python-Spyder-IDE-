'''بسم الله الرحمن الرحيم'''               
#اولا البايثون هي أحدث اللغات المستخدمة للبرمجة
#In this training program
#you will learn how to collect
#analyze and visualize any size of data
#Learn ٍsome-NOT ALL- Python basics.
#Learn simplest way in OOP (Object-Oriented Programming) and data structures in python
#Be able to implement some algorithms or program using python
#Learn the most needed data science algorithms

                    #SEXTH SESSION In How to use Python on Spyder IDE(OOP)
#اولا الObject_Orianted_Programmin هى بكل بساطة عبارة عن انك ازاى تعمل function وبعدين تستخدمها فى Block_Of_Codes
#function that prints to user
print("S.K")
#function that ask user
input("plz enter")
#function that rearrange list
sorted(list)
#function that change variable to a number
int(var)
#كل دول functions
#دلوقتى لو عايز اعمل create ل function هنعملها ازاى؟
ahmed(7,9)
#اى variable وجمبيها الاقواس () دى انا عملت الfunction
#طيب ازاى استدعيها او استخدمها؟
#هنا فى الfunction دى انا طلبت منة انة يشوفها function بال def وبعدين قولتلة خش جوة الاقواس وشوف الرقمين اللى عاملهم ل ahmed
def ahmed(num1,num2):
#دلوقتى هطلب منة يدخل يجمع الرقمين ويحطهم فى متغير اسمة الsums
    sums=num1+num2
#دلوقتى هنرجع الحاجة اللى عايزها تظهر لليوزر..بمعنى انى عايز يظهر لليوزر قيمة المتغير اللى جمعت على الرقمين
    return sums
#دلوقتى انا هطلب من اليوزر ي\خل رقمين وهخزنهم فى ال x&y وبعدين هطلبهم للfunction بتاعة ahmed
x=int(input("plz enter 1st number: "))
y=int(input("plz enter end number: "))
ahmed=(x,y)  
#طيب دلوقتى انا ممكن استعمل الfunction دى فى if condition ولو اليوزر عدى السن المسموح بة هيطبع ارقام معينة ولو مش قد السن المحدد هيطبع ارقام تانية
def ahmed(num1,num2):
    sums=num1+num2
    multp=num1*num2
    return sums
userage=int(input("plz enter your age: "))
#دلوقتى هعمل الشرط بتاعى لو اليوزر قد السن القانونى هيطبع 5و2
if 21<userage:
    n1=5
    n2=2
#ولو مش قد السن القانونى هيطبع 7و8
else:
    n1=7
    n2=8
#طيب فين الfunction ؟
#هنستدعى ahmed function دلوقتى وهدخل فيها ال 2variables بتوعى الجديد
ahmed(n1,n2)
#إذن فماهو الان الOOP ؟
#الoop هو اولا بتعرف variable على انة function بس قبلها بتشتغل باوامر الoop مثل الclass او الobject وخلافة..بردك ماهو الoop ؟
#الoop بالظبط كانك هتعرف vriable معين وهتحط فية مجموعة من الlists بحيث تعرف ت import جواها مجموعة من الخصائص الخاصة بالvariable دة
#على سبيل المثال:..
#هكتب الامر class وهديلة variable معين عشان يفهم انى هدخل تحت الvariables دى مجموعة من الخصائص
class stud:
#بعد كدة هعمل create للvariable بال def عشان اعملها function
#وبعدين هندة علية بامر init عشان كانى بالظبط هفتح الstud وحط جواها الخصائص اللى عايز ادخلها فيه
#وبعدين هكتب خصائص الstud داخل الاقواس
    def __init__(self,study,smart,age):
##دلوقتى انا بيكون عندى كلمة ثابتة by default لازم اكتبها بين الاقواس عشان اعرف اتحكم فى الclass stud وهى self.
#كانى بالظبط قولت لية اعمل init عشان تفتح ليها قايمة لل stud عشان هحط جواها حاجات
#وبعدين هكتب self.smart مثلا عشان اقولة حطلى بقى الكلمات دى ك قوايم تحت الstud
        self.study=study
        self.smart=smart
        self.age=age
#دلوقتى هندة على الclass واقولة فية شخص اسمة أحمد وبعدين اعملى import للارقام اللى هديهالك فى القوايم اللى جواك..بمعنى: 
ahmed=stud(80,10,90)        
#دلوقتى تم تخزين كل مرقم من دول على الlists اللى كانوا بين الاقواس "بالتوالى"
#لو عايوز مثلا نسبة الsmart عند احمد
ahmed.smart
#وهكذا شسمى اكثر من variable وبتندة على الclass وبعدين بتسجل ارقامك فى الاقواس فبيتعملهم import على الobjects داخل الclass
mohamed=stud(10,20,30)
mohamed.smart
radwan=stud(1.1,1.2,1.3)
radwan.smart