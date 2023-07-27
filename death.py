age = float(input('how old are you: '))
death = (input('you may die at the age of (press y for default aka 70 years): '))
if death == 'y':
    death = 70
    years = death - age
    months = 12 * death - age * 12
    weeks = 52.1429 * death - age * 52.1429
    days = 365.25 * death - age * 365.25
    hours = 8760 * death - age * 8760
    minutes = 525600 * death - age * 525600
    seconds = 31536000 * death - age * 31536000
    print(f'if you were lucky enough to live until you are 70 then you are left '
          f'with:\n1- {years} year\n2- {months} month\n3- {weeks} week\n4- {days} day\n5- {hours} hour'
          f'\n6- {minutes} minute\n7- {seconds} second\ngood luck xD')

else:
    death = float(death)
    years = death - age
    months = 12 * death - age * 12
    weeks = 52.1429 * death - age * 52.1429
    days = 365.25 * death - age * 365.25
    hours = 8760 * death - age * 8760
    minutes = 525600 * death - age * 525600
    seconds = 31536000 * death - age * 31536000
    print(f'if you were lucky enough to live until you are {death} then you are left '
          f'with:\n1- {years} year\n2- {months} month\n3- {weeks} week\n4- {days} day\n5- {hours} hour'
          f'\n6- {minutes} minute\n7- {seconds} second\ngood luck xD')