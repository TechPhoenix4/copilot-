import streamlit as st
from dotenv import load_dotenv
import os

# Set the page layout to wide
st.set_page_config(layout="wide")

load_dotenv()

# Load Font Awesome via a <link> tag
st.markdown(
        r"""<head>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
        </head>
        """,
        unsafe_allow_html=True
    )

def main():
    # Navigation button to return home
    if st.button('🏠 Home', key='nav_home', help='Return Home'):
        st.switch_page("home.py")

    # Displaying the logo and heading side by side
    st.markdown(
        r"""
        <div class="header-container">
            <img src="https://upload.wikimedia.org/wikipedia/commons/e/e7/Hitachi_logo_LIGHT_HIRES.jpg" class="logo-img"/>
            <h1 class='heading-text'>CoPilot Of India</h1>
        </div>
        """, unsafe_allow_html=True
    )
    
    # Display the subheading
    st.markdown(r"<h2 class='subheading'>Conventional CoPilot For India</h2>", unsafe_allow_html=True)

    # Custom CSS for aligning the title, logo, and subheading
    st.markdown(
        r"""<style>
        /* Set background color for the entire page */
        .stApp {
            background-color: white;  /* Changed background color to white */
        }
        .header-container {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 100%;
            padding: 0px 0;
            background-color: #white;  
            margin-bottom: 0px;
        }
        .logo-img {
            width: 80px;  /* Adjust the size of the logo here */
            margin-right: 10px;  /* Reduce spacing between the logo and heading */
        }
        .heading-text {
            text-align: center;
            margin: 0;  /* Remove margins around the heading */
            padding: 0;  /* Remove padding around the heading */
            font-size: 50px;  /* Adjust the size of the heading text */
            color: black;  /* Set text color to black */
        }
        .subheading {
            text-align: center;
            margin-top: 0px;  /* Adjust spacing between title and subheading */
            font-size: 20px;
            color: black;  /* Optional: You can change the color to make it distinct */
        }
        .english-button {
            display: block;
            margin: 10px auto;  /* Center the button */
            padding: 5px 20px;  /* Padding for the button */
            font-size: 16px;  /* Font size of the button text */
            background-color: #007BFF;  /* Button color */
            color: white;  /* Text color */
            border: none;  /* No border */
            border-radius: 5px;  /* Rounded corners */
            cursor: pointer;  /* Cursor change on hover */
        }
        .english-button:hover {
            background-color: #0056b3;  /* Darker shade on hover */
        }

        .mic-button {
            display: block;
            margin: 20px auto;  /* Center the button and add some space from the English button */
            width: 60px;  /* Diameter of the circular button */
            height: 60px;  /* Diameter of the circular button */
            background-color: #007BFF;  /* Blue background color like the English button */
            color: white;  /* Icon color */
            border: none;  /* No border */
            border-radius: 50%;  /* Makes the button round */
            font-size: 24px;  /* Size of the microphone icon */
            cursor: pointer;  /* Cursor change on hover */
        }
        .mic-button:hover {
            background-color: #0056b3;  /* Darker shade of blue on hover */
        }

        /* Container for small buttons next to each other */
        .button-container {
            display: flex;
            justify-content: center;
            gap: 10px;  /* Add space between the buttons */
            margin-top: 20px;  /* Add some space from the mic button */
        }

        .small-button {
            padding: 5px 15px;  /* Small padding */
            font-size: 14px;  /* Smaller font size */
            background-color: #007BFF;  /* Blue background color like the English button */
            color: white;  /* Text color */
            border: none;  /* No border */
            border-radius: 5px;  /* Rounded corners */
            cursor: pointer;  /* Cursor change on hover */
        }
        .small-button:hover {
            background-color: #0056b3;  /* Darker blue on hover */
        }

        .examples-container {
            text-align: center;
            margin-top: 10px;  /* Adds space above the text */
        }
        .examples-text {
            font-size: 18px;  /* Font size of the text */
            color: #333333;  /* Dark gray color for the text */
            font-weight: bold;  /* Makes the text bold */
        }

        /* Style for rectangular buttons arranged in two rows, each row having two buttons */
        .example-buttons-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 10px;  /* Vertical space between the rows */
        }

        .button-row {
            display: flex;
            justify-content: center;
            gap: 20px;  /* Horizontal space between the buttons */
        }

        .example-button {
            padding: 10px 20px;  /* Padding for rectangular buttons */
            font-size: 14px;  /* Adjust font size */
            background-color: #e0f0e3;  /* Pastel green */
            color: black;  /* Black text color */
            border: 2px solid #007BFF;  /* Border color */
            border-radius: 5px;  /* Slightly rounded corners */
            cursor: pointer;
            width: 300px;  /* Set a fixed width for all buttons */
            height: 50px;  /* Fixed height to ensure text is centered */
            display: flex;
            justify-content: center;
            align-items: center;  /* Center text vertically and horizontally */
            text-align: center;
            white-space: nowrap;  /* Prevent text from wrapping */
        }

        .example-button:hover {
            background-color: #f0f0f0;  /* Light gray hover effect */
        }
        
        /* More Examples button styling */
        .more-examples-button {
            background: none;
            border: none;
            color: #007BFF;
            cursor: pointer;
            font-size: 16px;
            margin: 20px auto;
            display: block;
            text-decoration: underline;
        }
        
        .more-examples-button:hover {
            color: #0056b3;
        }
        
        /* Additional examples container */
        .additional-examples {
            display: none;
            margin-top: 20px;
        }
        
        /* Hide sidebar */
        [data-testid="stSidebar"][aria-expanded="true"] {
            display: none;
        }
        [data-testid="stSidebar"][aria-expanded="false"] {
            display: none;
        }
        /* Hide sidebar */
        [data-testid="stSidebar"][aria-expanded="true"] {
            display: none;
        }
        [data-testid="stSidebar"][aria-expanded="false"] {
            display: none;
        }        .input-container {
            position: relative;
            max-width: 650px;
            margin: 20px auto;
            padding: 0 20px;
            right: 40px
        }
        .chat-input {
            width: 100%;
            padding: 10px 50px 10px 15px;
            border: 1px solid #ccc;
            border-radius: 10px;
            font-size: 16px;
            outline: none;
        }
        .chat-input:focus {
            border-color: #007BFF;
        }
        .send-button {
            position: absolute;
            right: 25px;
            top: 50%;
            transform: translateY(-50%);
            background-color: white;
            color: #99a3b0;
            border: none;
            border-radius: 50%;
            width: 35px;
            height: 35px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 0;
        }
        .send-button:hover {
            background-color: #0056b3;
        }
        .reset-button {
            position: absolute;
            right: -85px;
            font-size: 16px;
            top: 50%;
            transform: translateY(-50%);
            background-color: #6c757d;
            color: white;
            border: none;
            border-radius: 0%;
            width: 90px;
            height: 35px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: ;
        }
        .reset-button:hover {
            background-color: #5a6268;
        }
        </style>
        """, unsafe_allow_html=True)
    
    # Initialize a session state to store messages
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    # Chat interface
    st.markdown("""
        <div class="chat-container">
            <div class="message-container user-message-container">
                <div class="icon">
                    <i class="fas fa-user"></i>
                </div>
                <div class="message user-message">
                   How to improve soil condition?
                </div>
            </div>
            <div class="message-container">
                <div class="icon">
                    <i class="fas fa-robot"></i>
                </div>
                <div class="message bot-message">
                    There are several ways to improve soil condition in India:

Adding organic matter: Adding organic matter such as compost, manure, or green manure can improve soil structure, increase water-holding capacity, and provide nutrients to plants.

Crop rotation: Crop rotation can help to break disease cycles, improve soil fertility, and reduce soil erosion.

Mulching: Mulching with organic materials such as straw, leaves, or grass clippings can help to retain moisture in the soil, suppress weeds, and improve soil structure.

Avoiding over-tillage: Over-tillage can lead to soil compaction, erosion, and loss of organic matter. It is important to avoid excessive tillage and use conservation tillage practices.

Using cover crops: Cover crops such as legumes, grasses, or clovers can help to improve soil fertility, reduce soil erosion, and suppress weeds.

Balancing soil pH: Soil pH can affect nutrient availability and plant growth. It is important to test soil pH and adjust it if necessary.

Using appropriate fertilizers: Using appropriate fertilizers based on soil test results can help to improve soil fertility and reduce nutrient runoff.
                </div>
            </div>
            <div class="input-container">
                <input type="text" class="chat-input" placeholder="Type your question..." />
                <button class="send-button">
                    <i class="fas fa-paper-plane"></i>
                </button>
                <button class="reset-button">
                    Reset Chat
                </button>
            </div>
        </div>
        <script>
            function sendMessage() {
                const inputField = document.getElementById('user-input');
                const message = inputField.value;
                if (message) {
                    // Send the message to the server
                    window.parent.postMessage({ type: 'new_message', message: message }, '*');
                    inputField.value = ''; // Clear the input field
                }
            }
            document.getElementById('user-input').addEventListener('keypress', function (e) {
                if (e.key === 'Enter') {
                    sendMessage();
                }
            });
        </script>
        <style>
            .chat-container {
                max-width: 800px;
                margin: 20px auto;
                padding: 20px;
                background-color: #f5f5f5;
                border-radius: 10px;
            }
            .message-container {
                display: flex;
                align-items: flex-start;
                margin: 10px 0;
                gap: 10px;
            }
            .message {
                padding: 10px 20px;
                border-radius: 20px;
                max-width: 70%;
            }
            .user-message-container {
                flex-direction: row-reverse;
            }
            .user-message {
                background-color: #007BFF;
                color: white;
            }
            .icon {
                width: 35px;
                height: 35px;
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                background-color: #e0e0e0;
                color: #606060;
                font-size: 20px;
            }
            .bot-message {
                background-color: #e0e0e0;
                color: black;
            }
            .hidden {
                display: none !important;
            }
        </style>
    """, unsafe_allow_html=True)



if __name__ == '__main__':
    main()