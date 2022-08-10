import streamlit as st
import datetime
from datetime import time
import pywhatkit as py
import keyboard
import time
import numpy as np


d = st.slider('Enter the delay', 60, 120,80 )
delay  = datetime.timedelta(0,d)
phonelist = st.text_input("Please input numbers you want to send message to with seperated by a comma")
message = st.text_area("Enter your Message")
submit = st.button("Send Message")



if 'count' not in st.session_state:
    st.session_state.count = 1

if 'sent_phones' not in st.session_state:
    st.session_state.sent_phones = []

if 'SentTo' not in st.session_state:
    st.session_state.SentTo = 0

if 'progress' not in st.session_state:
    st.session_state.progress = 0

if 'list_len' not in st.session_state:
    st.session_state.list_len = 0

if 'list' not in st.session_state:
    st.session_state.list = []


if st.session_state.count > 1:
    # st.text(st.session_state.count)
    if submit:
        phone = list(dict.fromkeys(phonelist.split(',')))
        st.session_state.list = phone
        st.session_state.list_len = len(phone)
        st.session_state.progress = 0
        # st.progress(st.session_state.progress)
        
        c1 = st.empty()
        c2 = st.empty()
        with c1.container():
            st.progress(st.session_state.progress)
        for each in phone:
    
            now = datetime.datetime.now()
            with c2.container():
                # c1 = st.empty()
                # st.progress(st.session_state.progress)
                # c1.text("{0:.0%}".format(st.session_state.progress))

                st.text("Sending Message to " + each)


                py.sendwhatmsg(each, message, (now + delay).hour, (now + delay).minute)
                time.sleep(3)
                keyboard.press_and_release('ctrl+w')

                st.session_state.SentTo = phone.index(each) + 1
                st.session_state.sent_phones.append(each)
                
                st.session_state.progress = st.session_state.SentTo / len(phone)

                with c1.container():    
                    st.progress(st.session_state.progress)
                    st.text("{0:.0%}".format(st.session_state.progress))


                st.text(f"Sent to {st.session_state.SentTo} of {len(phone)}")
                st.success("Message Sent to {}".format(phone[0:st.session_state.SentTo]))

                

    # st.progress(st.session_state.progress)
    # st.text("{0:.0%}".format(st.session_state.progress))

    # st.text(f"Sent to {st.session_state.SentTo} of {st.session_state.list_len}")

    # st.success("Message Sent to {}".format(st.session_state.list[0:st.session_state.SentTo]))
            
st.session_state.count += 1