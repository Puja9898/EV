import joblib
import pandas as pd
from twilio.rest import Client

# 🚨 Load AI Model for Accident Detection (Optional)
# model = joblib.load("accident_model.pkl")

# 🚑 Twilio API Credentials (Replace with yours)
TWILIO_SID = "USae6cf7513717d9014783fc3e6bf8f184"
TWILIO_AUTH_TOKEN = "0459793b91c805d7cfdd82141019a87d"
TWILIO_PHONE = "+14155238886"  # Replace with your Twilio phone number

# 📩 Emergency Contacts (Family, Friends)
EMERGENCY_CONTACTS = [ "+91 9440455161"]  # Replace with actual phone numbers

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
def send_sms(message):
    try:
        client = Client(TWILIO_SID, TWILIO_TOKEN)
        
        for contact in EMERGENCY_CONTACTS:
            client.messages.create(
                body=message,
                from_=TWILIO_PHONE,
                to=contact
            )
            print(f"📩 SOS Sent to {contact}")
    except Exception as e:
        print(f"Failed to send SMS: {e}")

# 🚀 Accident Detection & SOS Alert
def detect_accident():
    print("🚦 Monitoring for accidents...")
    
    # Simulate Accident Detection (Replace with actual logic)
    accident_detected = True  # Set to True to simulate an accident

    if accident_detected:
        print("🚨 Accident Detected!")
        
        # Fetch Sample Location
        lat, lon = get_sample_location()
        location_link = f"https://www.google.com/maps?q={lat},{lon}"
        print("📍 Accident Location:", location_link)

        # Find Nearest Hospitals
        hospitals = get_nearest_hospitals()
        hospital_info = "\n".join(hospitals[:3]) if hospitals else "No hospitals found nearby."

        # 📩 Send SOS Alert
        sos_message = f"🚨 Emergency! An accident occurred.\n📍 Location: {location_link}\n🏥 Nearest Hospitals:\n{hospital_info}"
        send_sms(sos_message)
    else:
        print("✅ No Accident Detected.")

# 🚀 Run System
if __name__ == "__main__":
    detect_accident()
