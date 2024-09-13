import stripe

stripe.api_key = 'sk_test_51PvFXfDKCJU8J1SteoVk2Ft7PB9W5fmgYy0ooXuGqsOrscfzkRLvfE9OtGRI3NmGDqdyHRDSyy0fp2Lts0XWiF0k00d8osOPMc'
stripe.api_version = '2022-08-01'

try:
    # Create a test customer
    customer = stripe.Customer.create(email='test@example.com')
    print("Customer created:", customer)
except stripe.error.StripeError as e:
    print(f"Stripe error: {e}")
