import streamlit as st
from twilio.rest import Client

# 🚑 Twilio API Credentials (Replace with yours)
TWILIO_SID = "AC8faeceda2fe455e679c8069f91093835"  # Replace with your actual Account SID
TWILIO_TOKEN = "424f10f31f44693fa607f5209de9cef3"  # Replace with your actual Auth Token
TWILIO_PHONE = "+15155795069"  # Replace with your Twilio phone number

# 📩 Emergency Contacts (Family, Friends)
EMERGENCY_CONTACTS = ["+91 8978038847", "+91 9440455161"]  # Replace with actual phone numbers

# 🌍 Sample Location (Instead of Google API)
def get_sample_location():
    lat, lon = 12.9716, 77.5946  # Example: Bangalore, India
    return lat, lon

# 🏥 Sample Hospital Data (Instead of Google API)
def get_nearest_hospitals():
    hospitals = [
        "Apollo Hospital, City Center",
        "Fortis Hospital, Downtown",
        "AIIMS, Main Road"
    ]
    return hospitals

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
        st.success("SOS alerts sent to emergency contacts!")
    except Exception as e:
        st.error(f"Failed to send SMS: {e}")

# 🚀 Accident Detection & SOS Alert
def detect_accident():
    # Fetch Sample Location
    lat, lon = get_sample_location()
    location_link = f"https://www.google.com/maps?q={lat},{lon}"

    # Find Nearest Hospitals
    hospitals = get_nearest_hospitals()
    hospital_info = "\n".join(hospitals[:3]) if hospitals else "No hospitals found nearby."

    # 📩 Send SOS Alert
    sos_message = f"🚨 Emergency! An accident occurred.\n📍 Location: {location_link}\n🏥 Nearest Hospitals:\n{hospital_info}"
    send_sms(sos_message)

# 🌐 Streamlit UI
def create_ui():
    st.title("Accident Detection & Emergency Response System")
    st.write("Click the button below to simulate an accident and send SOS alerts.")

    if st.button("🚨 Simulate Accident & Send SOS"):
        detect_accident()

# 🚀 Run System
if __name__ == "__main__":
    create_ui()
