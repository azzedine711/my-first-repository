the_request = str(input('are you hungry (anwser with yes or no): '))
the_food =['t3am','shekshouka','tshe5shou5a','grantita','batatkousha','3des','loubya','bercouces','tajin','sourba vermicel','shourba friq','tajin lma3dnousiya','la7rira','oush y5iyer azzedin']

from random import choice

the_result = choice (the_food)

if the_request == "yes":
    print("make " + the_result)
elif the_request == "no":
    print("why are you here")
else:
    print("make sure you wrote the anwser correctly")