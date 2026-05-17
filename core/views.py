from django.shortcuts import render
from urllib.parse import quote


def google_link(text):
    return f"https://www.google.com/search?q={quote(text)}"


def home(request):

    industries = [
        {"name": "Office & Commercial Buildings", "url": google_link("Office & Commercial Buildings")},
        {"name": "Facilities & Critical Infrastructure", "url": google_link("Facilities & Critical Infrastructure")},
        {"name": "Hospitals & Elderly Care", "url": google_link("Hospitals & Elderly Care")},
        {"name": "Manufacturing & Plants", "url": google_link("Manufacturing & Plants")},
        {"name": "Open Pit & Underground", "url": google_link("Open Pit & Underground")},
        {"name": "Stores & Shopping Centers", "url": google_link("Stores & Shopping Centers")},
        {"name": "Schools & Training Centers", "url": google_link("Schools & Training Centers")},
        {"name": "Hotels & Resorts", "url": google_link("Hotels & Resorts")},
        {"name": "Military & Government", "url": google_link("Military & Government")},
        {"name": "Emergency Services", "url": google_link("Emergency Services")},
        {"name": "Public Transport & Terminals", "url": google_link("Public Transport & Terminals")},
        {"name": "Residential", "url": google_link("Residential")},
        {"name": "IT Infrastructure", "url": google_link("IT Infrastructure")},
        {"name": "Sports & Ergonomics", "url": google_link("Sports & Ergonomics")},
        {"name": "VR/AR", "url": google_link("VR/AR")},
    ]

    engineering = [
        {"name": "Simulation", "url": google_link("simulation")},
        {"name": "Logistic Planning", "url": google_link("logistic planning")},
        {"name": "Digital Twin", "url": google_link("digital twin")},
        {"name": "XR", "url": google_link("XR")},
        {"name": "WiFi Sensing", "url": google_link("wifi sensing")},
        {"name": "IoT", "url": google_link("iot")},
    ]

    software = [
        {"name": "Rheina", "url": google_link("rheina")},
        {"name": "Kuisioner", "url": google_link("kuisioner")},
    ]


    company = [
        {"name": "About Us", "url": google_link("About Us")},
        {"name": "Event and Dates", "url": google_link("Event and Dates")},
        {"name": "Career", "url": google_link("Career")},
    ]


    context = {
        "industries": industries,
        "engineering": engineering,
        "software": software,
        "focus_topic_url": focus_topic_url,
        "company": company,
        "contact_url": contact_url,
    }

    return render(request, "core/home.html", context)
