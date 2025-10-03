
#Scenario: Successful login
#Given the user is on the login page
#When they enter a valid username and password
#Then they should see the message "Welcome" 

#The Python code with @given, @when, @then connects each line of the scenario to a function that implements it
from behave import given, when, then #@“import” the keywords @given, @when, @then from the Behave library.Decorators used to link text from the scenario
#A decorator is a special way to add extra functionality to a function without changing its code.
#They are applied with the @ symbol placed above a function



#context.page = "login" just stores the fact that the user is on the login page (like keeping the "state")

@given("the user is on the login page")
def step_impl(context): #The function step_impl runs when this step is executed.
    context.page = "login"  #This means we declare that the user is currently on the login page.

#The @when(...) matches the "When" step.
#When the user enters correct credentials, we set context.result = "success" (meaning login succeeded).
#Here we simulate that the user entered the correct username and password
@when("they enter a valid username and password")
def step_impl(context):
    context.result = "success"

#Here we do an assertion: assert context.result == "success".
#If the condition is true → the test passes.
#If not → the test fails.

@then('they should see the message "Welcome"')
def step_impl(context):
    assert context.result == "success"


#Overall Logic

#Start with the user being on the login page.

#Simulate entering valid credentials.

#Assert that the login was successful (which represents showing the "Welcome" message).


