import sys
class colours:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
while True:
  repeatdone = False
  print(colours.BOLD + colours.HEADER + '''   BMI CALCULATOR (version 1.0.2) 
   by Thitut Uhthalye'''+ colours.ENDC, '''

  " Select Unit Calculator"

[1] Metric
[2] Imperial
  ''')
  while True:
          try:
                  unit = int(input())

          except ValueError:
                  print(colours.WARNING + '''Please enter 1 or 2
                  ''' + colours.ENDC)
                  continue
          if unit <= 0:
                  print(colours.WARNING + '''Please enter 1 or 2
                  ''' + colours.ENDC)
                  continue
          elif unit >=3:
                  print(colours.WARNING + '''Please enter 1 or 2
                  ''' + colours.ENDC)
                  continue
          else:
                  break
  if unit == 1:
    while True:
          try:
            x = float(input('''Weight (kg) : '''))
            y = float(input('''Height (cm) : '''))
          except ValueError:
            print(colours.WARNING + 'Please enter valid number' + colours.ENDC)
            continue
          if x <= 0 or y <= 0:
            print(colours.WARNING + 'Please enter valid number' + colours.ENDC)
            continue
          else:
            break
    BMI = x / ((y / 100) **2)
  elif unit == 2:
    while True:
          try:
            a = float(input('''Weight (lbs) : '''))
            b = float(input('''Height (in) : '''))
          except ValueError:
            print(colours.WARNING + 'Please enter valid number' + colours.ENDC)
            continue
          if a <= 0 or b <= 0:
            print(colours.WARNING + 'Please enter valid number' + colours.ENDC)
            continue
          else:
            break
    BMI = a * 703 / (b **2)
  else:
          print (colours.WARNING + '''You shouldn't get this result so congrats
for breaking the code. Anyways, ENTER ONLY 1 OR 2!
          - Thitut Uhthalye - A desperated hobbyist''' + colours.ENDC)
  if BMI < 15:
          Class = 'very serverely underweight'
          rcmd = '''If you are receiving treatment for an eating disorder then this tool is NOT to be used.

There may be an underlying medical cause for your weight, or your diet may not be providing you with enough calories. We suggest you discuss this with your GP.'''
  elif 15 <= BMI < 16:    
          Class = 'serverely underweight'
          rcmd = '''If you are receiving treatment for an eating disorder then this tool is NOT to be used.

There may be an underlying medical cause for your weight, or your diet may not be providing you with enough calories. We suggest you discuss this with your GP.'''
  elif 16 <= BMI < 18.5:    
          Class = 'underweight'
          rcmd = '''If you are receiving treatment for an eating disorder then this tool is NOT to be used.

There may be an underlying medical cause for your weight, or your diet may not be providing you with enough calories. We suggest you discuss this with your GP.'''
  elif 18.5 <= BMI < 25:    
          Class = 'normal (Healthy weight)'
          rcmd = 'We suggest you maintain your weight. Try to stay active and maintain current diet'
  elif 25 <= BMI < 30:    
          Class = 'overweight'
          rcmd = '''Your health would really benefit from gradually losing just 5% of your current weight. The best way to lose weight is through a combination of diet and exercise.

We've got lots of resources to help you lose weight safely. If you're concerned about your weight speak to your GP.'''
  elif 30 <= BMI < 35:    
          Class = 'Obese Class I (Moderately obese)'
          rcmd = '''Losing and keeping off 5% of your weight can have health benefits, such as lowering your blood pressure and reducing your risk of developing type 2 diabetes.

You should work towards achieving a healthier weight over time. We suggest you visit your GP to discuss.'''             
  elif 35 <= BMI < 40:    
          Class = 'Obese Class II (Severely obese)'
          rcmd = '''Losing and keeping off 5% of your weight can have health benefits, such as lowering your blood pressure and reducing your risk of developing type 2 diabetes.

You should work towards achieving a healthier weight over time. We suggest you visit your GP to discuss.'''             
  else:
          Class = 'Obese Class III (Very severely obese)'
          rcmd = '''Losing and keeping off 5% of your weight can have health benefits, such as lowering your blood pressure and reducing your risk of developing type 2 diabetes.

You should work towards achieving a healthier weight over time. We suggest you visit your GP to discuss.'''             
  print ("BMI = %.2f "%BMI)
  print ('Your result suggests you are', colours.BOLD + colours.ITALIC + Class + colours.ENDC, '''
_____________________

Recommendation:
''', rcmd)

  while True:
    try:
      repeat = str(input('''
_____________________
      
Do you want to repeat the programme?
      
[Y] Yes
[N] No
'''))
    except ValueError:
            print(colours.WARNING + 'Please enter Y or N' + colours.ENDC)
            continue
    if repeat.casefold() in {'y','yes','1'}:
            break
    elif repeat.casefold() in {'n','no','2'}:
            print(colours.FAIL + "The programme is terminated." + colours.ENDC)
            repeatdone = True
            break
    else:
            print(colours.WARNING + 'Please enter Y or N' + colours.ENDC)
            continue
    if repeatdone : break
  if repeatdone : break