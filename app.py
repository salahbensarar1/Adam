import streamlit as st
from styles import get_css_styles

# Page config MUST be first Streamlit command
st.set_page_config(
    page_title="🚀 Programming Adventure",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Now import other modules
import time
import datetime
from styles import get_css_styles
from sections import *

# Load CSS styles FIRST - this is critical for proper rendering
st.markdown(get_css_styles(), unsafe_allow_html=True)
st.write("CSS Loaded!" if get_css_styles() else "CSS Failed!")



# Initialize session state
if 'deadline' not in st.session_state:
    st.session_state.deadline = datetime.datetime.now() + datetime.timedelta(days=30)

if 'completed_steps' not in st.session_state:
    st.session_state.completed_steps = set()

if 'user_name' not in st.session_state:
    st.session_state.user_name = "Future Programmer"

# Calculate countdown
now = datetime.datetime.now()
time_left = st.session_state.deadline - now
days_left = max(0, time_left.days)
hours_left = max(0, time_left.seconds // 3600)
minutes_left = max(0, (time_left.seconds % 3600) // 60)
seconds_left = max(0, time_left.seconds % 60)

# Progress calculation
total_steps = 7
progress = len(st.session_state.completed_steps) / total_steps * 100

# Sidebar navigation with better styling
st.sidebar.markdown("""
<div style="text-align: center; padding: 1.5rem; 
            background: linear-gradient(135deg, rgba(255,255,255,0.15) 0%, rgba(255,255,255,0.05) 100%); 
            border-radius: 15px; margin-bottom: 1.5rem; 
            border: 1px solid rgba(255,255,255,0.1);">
    <h3 style="color: white; margin: 0; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">
        🗺️ Your Programming Journey
    </h3>
</div>
""", unsafe_allow_html=True)

sections = [
    ("🏠", "Welcome", "Start your adventure"),
    ("🎯", "Mission", "What we're building"),
    ("🧠", "Learn", "C programming basics"),
    ("🛠️", "Build", "Step-by-step coding"),
    ("🏆", "Level Up", "Bonus challenges"),
    ("📚", "Resources", "Learning materials"),
    ("🎉", "Celebrate", "You did it!")
]

# Create navigation with better formatting
navigation_options = []
for emoji, title, desc in sections:
    navigation_options.append(f"{emoji} {title}")

selected_section = st.sidebar.radio(
    "Choose your path:",
    navigation_options,
    help="Navigate through your programming adventure!"
)

# Extract the section name for logic
section_name = selected_section.split(" ", 1)[1]

# Show section descriptions in sidebar
for emoji, title, desc in sections:
    if title == section_name:
        st.sidebar.markdown(f"""
        <div style="background: rgba(255,255,255,0.1); padding: 1rem; border-radius: 10px; margin: 1rem 0;">
            <p style="color: white; margin: 0; opacity: 0.9; font-size: 0.9rem;">
                <strong>{emoji} {title}</strong><br>
                {desc}
            </p>
        </div>
        """, unsafe_allow_html=True)
        break

# Hero section with improved design
st.markdown(f"""
<div class="hero-section">
    <h1>🚀 Programming Adventure! 🎮</h1>
    <p>Build Your Amazing Calculator with C Programming</p>
</div>
""", unsafe_allow_html=True)

# Countdown Timer with better error handling
if days_left >= 0:
    st.markdown(f"""
    <div class="countdown-container">
        <h2>⏰ Mission Countdown Timer ⏰</h2>
        <p>You have this much time to complete your awesome calculator!</p>
        <div class="countdown-timer">
            <div class="time-unit">
                <span class="time-number">{days_left}</span>
                <span class="time-label">Days</span>
            </div>
            <div class="time-unit">
                <span class="time-number">{hours_left}</span>
                <span class="time-label">Hours</span>
            </div>
            <div class="time-unit">
                <span class="time-number">{minutes_left}</span>
                <span class="time-label">Minutes</span>
            </div>
            <div class="time-unit">
                <span class="time-number">{seconds_left}</span>
                <span class="time-label">Seconds</span>
            </div>
        </div>
        <p>
            {"🔥 Let's do this! You've got plenty of time!" if days_left > 20 else 
             "⚡ Getting exciting! Time to focus!" if days_left > 7 else 
             "🚨 Final sprint! You can do it!"}
        </p>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <div class="countdown-container">
        <h2>🎉 Mission Complete Time! 🎉</h2>
        <p>The deadline has arrived! How did you do with your calculator project?</p>
    </div>
    """, unsafe_allow_html=True)

# Progress tracking with beautiful animation
st.markdown(f"""
<div class="progress-container">
    <h3>🌟 Your Progress Journey: {progress:.0f}%</h3>
    <div style="background: #e9ecef; height: 20px; border-radius: 10px; overflow: hidden;">
        <div class="progress-bar" style="width: {progress}%;"></div>
    </div>
    <div style="display: flex; justify-content: space-between; margin-top: 0.5rem; font-size: 0.9rem; color: #636e72;">
        <span>🎯 Started</span>
        <span>🚀 Building</span>
        <span>🏆 Complete!</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Main content sections with improved error handling
try:
    if section_name == "Welcome":
        show_welcome_section()
        if 'welcome' not in st.session_state.completed_steps:
            st.session_state.completed_steps.add('welcome')
    
    elif section_name == "Mission":
        show_mission_section()
        if 'mission' not in st.session_state.completed_steps:
            st.session_state.completed_steps.add('mission')
    
    elif section_name == "Learn":
        show_learn_section()
        if 'learn' not in st.session_state.completed_steps:
            st.session_state.completed_steps.add('learn')
    
    elif section_name == "Build":
        show_build_section()
        if 'build' not in st.session_state.completed_steps:
            st.session_state.completed_steps.add('build')
    
    elif section_name == "Level Up":
        show_levelup_section()
        if 'levelup' not in st.session_state.completed_steps:
            st.session_state.completed_steps.add('levelup')
    
    elif section_name == "Resources":
        show_resources_section()
        if 'resources' not in st.session_state.completed_steps:
            st.session_state.completed_steps.add('resources')
    
    elif section_name == "Celebrate":
        show_celebrate_section()
        if 'celebrate' not in st.session_state.completed_steps:
            st.session_state.completed_steps.add('celebrate')

except Exception as e:
    st.error(f"Error loading section: {e}")
    st.markdown("""
    <div class="step-card">
        <h3>⚠️ Section Loading Error</h3>
        <p>There was an issue loading this section. Please try refreshing the page or selecting a different section.</p>
    </div>
    """, unsafe_allow_html=True)

# Footer with encouragement
st.markdown(f"""
<div style="background: linear-gradient(135deg, #2d3436 0%, #636e72 100%); 
            color: white; padding: 2rem; border-radius: 15px; 
            text-align: center; margin-top: 3rem;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);">
    <p style="margin: 0; font-size: 1.1rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">
        🌟 Remember: Every line of code you write makes you a better programmer! 🌟
    </p>
    <p style="margin: 0.5rem 0 0 0; opacity: 0.8;">
        Created with ❤️ for future programming legends | Time remaining: {days_left} days, {hours_left} hours, {minutes_left} minutes, {seconds_left} seconds
    </p>
</div>
""", unsafe_allow_html=True)

# Auto-refresh for real-time countdown updates
if days_left >= 0:
    time.sleep(1)
    st.rerun()
