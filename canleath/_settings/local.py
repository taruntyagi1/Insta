DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'IE',
        'USER': 'postgres',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'ATOMIC_REQUEST': True,
    }
}
ALLOWED_HOSTS = ['*']
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# RAZORPAY_KEY = 'rzp_test_p0zz3ixQX7REip'
# RAZORPAY_SECRET = 'rOon0Tk2i7EjiZeju0mLWYSf'
# flourish credential
RAZORPAY_KEY = 'rzp_test_21Pl7kJuUANUdk'
RAZORPAY_SECRET = 'yZJgV3jaleEVPzrrMoXU450k'
INSTAEATS_URL = 'http://localhost:8000/'

prod_url='http://localhost:8000'
HOST_URL = 'http://localhost:8000'