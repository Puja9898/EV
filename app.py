import joblib
import numpy as np
import pandas as pd
import requests
import serial
from twilio.rest import Client
import joblib
import numpy as np
import pandas as pd
import requests
import serial
from twilio.rest import Client

# 🚨 Load AI Model for Accident Detection
model = joblib.load("accident_model.pkl")

# 🚑 Twilio API Credentials (Replace with yours)
 

# 📩 Emergency Contacts (Family, Friends)
#EMERGENCY_CONTACTS = ["+91 8978038847", "+91 9440455161"]

# 🏥 Sample Hospital Data (Instead of Google API)
def get_nearest_hospitals():
    hospitals = [
        "Apollo Hospital, City Center",
        "Fortis Hospital, Downtown",
        "AIIMS, Main Road"
    ]
    return hospitals

# 🌍 Sample Location (Instead of Google API)
def get_sample_location():
    lat, lon = 12.9716, 77.5946  # Example: Bangalore, India
    return lat, lon

# 📩 Send SMS via Twilio
#
# 🚀 Accident Detection & SOS Alert
def detect_accident():
    print("🚦 Monitoring for accidents...")
    
    # Test Data: Simulating sensor values
    accident_detected = model.predict([[16.2, 7.5, 0, 1]])[0]

    if accident_detected == 1:
        print("🚨 Accident Detected!")
        
        # Fetch Sample Location
        lat, lon = get_sample_location()
        location_link = f"https://www.google.com/maps?q={lat},{lon}"
        print("📍 Accident Location:", location_link)

        # Find Nearest Hospitals
        hospitals = get_nearest_hospitals()
        hospital_info = "\n".join(hospitals[:3]) if hospitals else "No hospitals found nearby."

        # 📩 Send SOS Alert
        #sos_message = f"🚨 Emergency! An accident occurred.\n📍 Location: {location_link}\n🏥 Nearest Hospitals:\n{hospital_info}"
        #send_sms(sos_message)
    else:
        print("✅ No Accident Detected.")

# 🚀 Run System
detect_accident() 
