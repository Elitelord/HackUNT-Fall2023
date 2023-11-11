import pandas as pd
from PIL import Image
import streamlit as st
import altair as alt
from streamlit_calendar import calendar
from canvasapi import Canvas
import requests

API_URL = "https://unt.instructure.com/api/v1/"
API_KEY = "9082~1MuaTSggWfo8LFKsjyVFYGdbBV8KvK4RbfTGoiBtU8oEdVpNoPD2ipX2Fp3i4fKf"

#apiTest = Canvas(API_URL, API_KEY)

#course = apiTest.get_course(90487)
#st.write(course.name)

st.set_page_config(
    page_title="OnTime",
    layout="wide",
    initial_sidebar_state="expanded",
)

def home_page():
    st.title('Welcome to OnTime!')
    calendar_options = {
        "headerToolbar": {
            "left": "today prev,next",
            "center": "title",
            "right": "resourceTimelineDay,resourceTimelineWeek,resourceTimelineMonth",
        },
        "slotMinTime": "06:00:00",
        "slotMaxTime": "18:00:00",
        "initialView": "timeGrid",
        "resourceGroupField": "building",
        "resources": [
            {"id": "a", "building": "Building A", "title": "Building A"},
            {"id": "b", "building": "Building A", "title": "Building B"},
            {"id": "c", "building": "Building B", "title": "Building C"},
            {"id": "d", "building": "Building B", "title": "Building D"},
            {"id": "e", "building": "Building C", "title": "Building E"},
            {"id": "f", "building": "Building C", "title": "Building F"},
        ],
    }
    calendar_events = [
        {
            "title": "Event 1",
            "start": "2023-11-11T08:30:00",
            "end": "2023-11-11T10:30:00",
            "resourceId": "a",
        },
        {
            "title": "Event 2",
            "start": "2023-07-31T07:30:00",
            "end": "2023-07-31T10:30:00",
            "resourceId": "b",
        },
        {
            "title": "Event 3",
            "start": "2023-07-31T10:40:00",
            "end": "2023-07-31T12:30:00",
            "resourceId": "a",
        }
    ]
    custom_css="""
        .fc-event-past {
            opacity: 0.8;
        }
        .fc-event-time {
            font-style: italic;
        }
        .fc-event-title {
            font-weight: 700;
        }
        .fc-toolbar-title {
            font-size: 2rem;
        }
    """

    #test = calendar(events=calendar_events, options=calendar_options, custom_css=custom_css)
    #st.write(API_URL+"courses?access_token="+API_KEY)
    st.write(requests.get(API_URL+"courses?access_token="+API_KEY).json()[0]["name"])

if __name__ == '__main__':

    selected_page = st.sidebar.selectbox(
        'Select Page',
        ('Home', 'Calendar', 'Settings')
    )

    if selected_page == 'Home':
        home_page()
