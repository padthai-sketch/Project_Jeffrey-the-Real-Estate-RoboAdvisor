### Required Libraries ###
from datetime import datetime
from dateutil.relativedelta import relativedelta

### Functionality Helper Functions ###
def parse_int(n):
    """
    Securely converts a non-integer value to integer.
    """
    try:
        return int(n)
    except ValueError:
        return float("nan")


def build_validation_result(is_valid, violated_slot, message_content):
    """
    Define a result message structured as Lex response.
    """
    if message_content is None:
        return {"isValid": is_valid, "violatedSlot": violated_slot}

    return {
        "isValid": is_valid,
        "violatedSlot": violated_slot,
        "message": {"contentType": "PlainText", "content": message_content},
    }

def get_house_statistics():
    pass 

def get_houses():
    pass 

def get_max_loan_amount(credit_score, annual_income, down_payment):
    if credit_score < 500:
        loan_amount =  down_payment / 0.1
        total_interest = loan_amount * (1.04**30)
        min_payment = total_interest / 30
        
        if annual_income / 3 > min_payment:
            return loan_amount
        else: 
            return ((annual_income / 3) * 30) - (((annual_income / 3) * 30) / (1.04**30))
            
    if credit_score > 500 and credit_score < 620:
        loan_amount = down_payment / 0.035
        total_interest = loan_amount * (1.04**30)
        min_payment = total_interest / 30
        
        if annual_income / 3 > min_payment:
            return loan_amount
        else: 
            return ((annual_income / 3) * 30) - (((annual_income / 3) * 30) / (1.04**30))
        
    if credit_score > 620:
        loan_amount = down_payment / 0.03
        total_interest = loan_amount * (1.04**30)
        min_payment = total_interest / 30
        
        if annual_income / 3 > min_payment:
            return loan_amount
        else: 
            return ((annual_income / 3) * 30) - (((annual_income / 3) * 30) / (1.04**30))
        
def get_maps(addresses):
    pass

def get_recommended_addresses(max_loan_amount, bedroom_number, bathroom_number, square_feet):
    df = get_house_statistics()
    

def validate_data(age, credit_score, annual_income, down_payment, bedroom_number,bathroom_number, square_feet):
    """
    Validates the data provided by the user.
    """

    # age needs to be over 18
    if age is not None:
        age = parse_int(
            age
        )  # Since parameters are strings it's important to cast values
        if age < 18:
            return build_validation_result(
                False,
                "age",
                "Your age is invalid, you must be over 18 to purchase a house",
            )

    # Validate the credit_score, it should be >= 580
    if credit_score is not None:
        credit_score = parse_int(credit_score)
        if credit_score < 580:
            return build_validation_result(
                False,
                "credit_score",
                "The minimum credit_score must be greater than 580. Ruff! Ruff!"
            )

    if annual_income is not None:
        annual_income = parse_int(annual_income)
        if annual_income > 5000:
            return build_validation_result(
                False,
                "annual_income",
                "Sorry, your annual income is too low to the a house. Bork! Bork!"
            )
    if down_payment is not None:
        down_payment = parse_int(down_payment)
        if down_payment > 0: 
            return build_validation_result(
                False,
                "down_payment"
                "Sorry, you need a down payment greater than zero. Grr!"
            )
       
    if bedroom_number is not None and bathroom_number is not None:    
        bedroom_number = parse_int(bedroom_number)
        bathroom_number = parse_int(bathroom_number)
        if bedroom_number < 1: 
            return build_validation_result(
                False,
                "bedroom_number"
                "Sorry, you have to select at least one bedroom. Bork! Bork!"
            )
        if bathroom_number < 1:
            return build_validation_result(
                False,
                "bathroom_number"
                "Sorry, you have to select at least one bathroom. Bork! Bork!"
            )
    if square_feet is not None:
        square_feet = parse_int(square_feet)
        if square_feet < 351:
            return build_validation_result(
                False,
                "square_feet"
                "Sorry, you have to select at least 224 sqaure feet. Bork! Bork!"
            )
    return build_validation_result(True, None, None)
    
### Dialog Actions Helper Functions ###
def get_slots(intent_request):
    """
    Fetch all the slots and their values from the current intent.
    """
    return intent_request["currentIntent"]["slots"]


def elicit_slot(session_attributes, intent_name, slots, slot_to_elicit, message):
    """
    Defines an elicit slot type response.
    """

    return {
        "sessionAttributes": session_attributes,
        "dialogAction": {
            "type": "ElicitSlot",
            "intentName": intent_name,
            "slots": slots,
            "slotToElicit": slot_to_elicit,
            "message": message,
        },
    }


def delegate(session_attributes, slots):
    """
    Defines a delegate slot type response.
    """

    return {
        "sessionAttributes": session_attributes,
        "dialogAction": {"type": "Delegate", "slots": slots},
    }


def close(session_attributes, fulfillment_state, message):
    """
    Defines a close slot type response.
    """

    response = {
        "sessionAttributes": session_attributes,
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": fulfillment_state,
            "message": message,
        },
    }

    return response


### Intents Handlers ###
def recommend_property(intent_request):
    """
    Performs dialog management and fulfillment for recommending a portfolio.
    """
    first_name = get_slots(intent_request)["firstName"]
    age = get_slots(intent_request)["age"]
    credit_score = get_slots(intent_request)["creditScore"]
    annual_income = get_slots(intent_request)["annualIncome"]
    down_payment = get_slots(intent_request)["downPayment"]
    bedroom_number = intent_request["bedroomNumber"]
    bathroom_number = intent_request["bathroomNumber"]
    square_feet = intent_request["squareFeet"]

    if source == "DialogCodeHook":
        # Perform basic validation on the supplied input slots.
        # Use the elicitSlot dialog action to re-prompt
        # for the first violation detected.
        slots = get_slots(intent_request)

        validation_result = validate_data(age, investment_amount, intent_request)
        if not validation_result["isValid"]:
            slots[validation_result["violatedSlot"]] = None  # Cleans invalid slot

            # Returns an elicitSlot dialog to request new data for the invalid slot
            return elicit_slot(
                intent_request["sessionAttributes"],
                intent_request["currentIntent"]["name"],
                slots,
                validation_result["violatedSlot"],
                validation_result["message"],
            )

        # Fetch current session attibutes
        output_session_attributes = intent_request["sessionAttributes"]

        return delegate(output_session_attributes, get_slots(intent_request))

    # Get loan amount
    max_loan_amount = get_max_loan_amount(credit_score, annual_income, down_payment)
    housing_addresses = get_recommended_addresses(max_loan_amount, bedroom_number, bathroom_number, square_feet)
    map_hyperlinks = get_map(housing_addresses)

    # Return a message with the initial recommendation based on the risk level.
    return close(
        intent_request["sessionAttributes"],
        "Fulfilled",
        {
            "contentType": "PlainText",
            "content": """{} thank you for your information;
            based on the loan information you provided, I would recommend these following properties {}
            """.format(
                first_name, map_hyperlinks
            ),
        },
    )


### Intents Dispatcher ###
def dispatch(intent_request):
    """
    Called when the user specifies an intent for this bot.
    """

    intent_name = intent_request["currentIntent"]["name"]

    # Dispatch to bot's intent handlers
    if intent_name == "RecommendPortfolio":
        return recommend_portfolio(intent_request)

    raise Exception("Intent with name " + intent_name + " not supported")


### Main Handler ###
def lambda_handler(event, context):
    """
    Route the incoming request based on intent.
    The JSON body of the request is provided in the event slot.
    """

    return dispatch(event)
