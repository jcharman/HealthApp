def impBMI():

    #Get height and weight values
    height = float(input('Please enter your height in inches: '))
    weight = float(input('Please enter your weight in pounds: '))
    #Do the first steps of the formula
    heightSquared = (height * height)
    finalWeight = (weight * 703)
    
    #Fiqure out and print the BMI
    bmi = finalWeight / heightSquared

    if bmi < 18:
        text = 'Underweight'

    elif bmi <= 24: # we already know that bmi is >=18 
        text = 'Ideal'

    elif bmi <= 29:
        text = 'Overweight'

    elif bmi <= 39:
        text = 'Obese'

    else:
        text = 'Extremely Obese'
    print ('Your BMI is: ' + str(bmi))    
    print ('This is: ' + text)
    
def metricBMI():

    text = str('placeholder')

    #Get height and weight values 
    height = float(input('Please enter your height in meters: '))
    weight = float(input('Please enter your weight in kilograms: '))

    #Square the height value
    heightSquared = (height * height)

    #Calculate BMI
    bmi = weight / heightSquared

    #Print BMI value
    print ('Your BMI value is ' + str(bmi))

    if bmi < 18:
        text = 'Underweight'

    elif bmi <= 24: # we already know that bmi is >=18 
        text = 'Ideal'

    elif bmi <= 29:
        text = 'Overweight'

    elif bmi <= 39:
        text = 'Obese'

    else:
        text = 'Extremely Obese'

    print ('This is: ' + text)

def impBMR():
    gender = input('Are you male (M) or female (F) ')
    if gender == 'M' or 'm':
        
        #Get user's height, weight and age values.
        height = float(input('Please enter your height in inches'))
        weight = float(input('Please enter your weight in pounds'))
        age = int(input('Please enter your age in years'))
        
        #Figure out and print the BmR
        bmr = 66 + (6.2 * weight) + (12.7 * height) - (6.76 * age)
        return bmr
    
    elif gender == 'F' or 'f':
        #Get user's height, weight and age values.
        height = float(input('Please enter your height in inches'))
        weight = float(input('Please enter your weight in pounds'))
        age = int(input('Please enter your age in years'))
        
        #Figure out and print the BmR
        bmr = 655 + (4.35 * weight) + (4.7 * height) - (4.7 * age)
        return bmr

def metricBMR():
    #Get user's gender
    gender = input('Are you male (M) or female (F) ')
    if gender == 'M' or 'm':
        
        #Get user's height, weight and age values.
        height = float(input('Please enter your height in centimeters'))
        weight = float(input('Please enter your weight in kilograms'))
        age = int(input('Please enter your age in years'))
        
        #Figure out and print the BmR
        bmr = 66 + (13.7 * weight) + (5 * height) - (6.8 * age)
        return bmr
    
    elif gender == 'F' or 'f':
        #Get user's height, weight and age values.
        height = float(input('Please enter your height in centimeters'))
        weight = float(input('Please enter your weight in kilograms'))
        age = int(input('Please enter your age in years'))
        
        #Figure out and print the BmR
        bmr = 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
        return bmr

def metricHBE():

        #Get BMR
        bmr = metricBMR()
        
        #Get activity rating
        print('Are You:') 
        print('(1) sedentary (little or no exercise)?')
        print('(2) lightly active (light exercise/sports 1-3 days/week)?')
        print('(3) moderatetely active (moderate exercise/sports 3-5 days/week)?')              
        print('(4) extra active (very hard exercise/sports & physical job or 2x training)?')
        print('(5) very active (hard exercise/sports 6-7 days a week)?')
        active = int(input('Enter a number: '))
        
        #Calculate HBE
        if active == 1:
                hbe = bmr * 1.2
                print (hbe)
        
        elif active == 2:
                hbe = bmr * 1.375
                print (hbe)

        elif active == 3:
                hbe = bmr * 1.55
                print (hbe)

        elif active == 4:
                hbe = bmr * 1.725
                print (hbe)        
        
        elif active == 5:
                hbe = bmr * 1.9
                print (hbe)
    
def impHBE():

        #Get BMR
        bmr = impBMR()
        
        #Get activity rating
        print('Are You:') 
        print('(1) sedentary (little or no exercise)?')
        print('(2) lightly active (light exercise/sports 1-3 days/week)?')
        print('(3) moderatetely active (moderate exercise/sports 3-5 days/week)?')              
        print('(4) extra active (very hard exercise/sports & physical job or 2x training)?')
        print('(5) very active (hard exercise/sports 6-7 days a week)?')
        active = input('Enter a number: ')
        
        #Calculate HBE
        if active == 1:
                hbe = bmr * 1.2
                print (hbe)
        
        elif active == 2:
                hbe = bmr * 1.375
                print (hbe)

        
        elif active == 3:
                hbe = bmr * 1.55
                print (hbe)

        elif active == 4:
                hbe = bmr * 1.725
                print (hbe)        
        
        elif active == 5:
                hbe = bmr * 1.9
                print (hbe)
             
        
menu = True
while menu:

    #Ask weather to print BMI or BMR
    output = input('Calulate BMI, BMR or Harris Benedict Equation (HBE) or exit? ')

    #BMI
    if output == 'BMI' or 'bmi':
        measurements = input('Do you work in metric (M) or imperial (I)')
        if measurements == 'M' or 'm':
            metricBMI()
           
        elif measurements == 'I' or 'i':
            impBMI()
    
    #BMR
    elif output == 'BMR' or 'bmr':
        measurements = input('Do you work in metric (M) or imperial (I)')
        if measurements == 'M' or 'm':
            metricBMR()
        
        elif measurements == 'I' or 'i':
            impBMR()
 
    #HBE
    elif output == 'HBE' or 'hbe':
        measurements = input('Do you work in metric (M) or imperial (I)')
        if measurements == 'M' or 'm':
            metricHBE()
        
        elif measurements == 'I' or 'i':
            impHBE()
    
    #Exit
    elif output == 'exit' or 'Exit' or 'EXIT':
        menu = False