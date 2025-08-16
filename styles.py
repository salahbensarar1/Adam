def get_css_styles():
    """Returns optimized CSS styling for the application"""
    return """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    /* Global Styles */
    .main .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        font-family: 'Poppins', sans-serif;
    }
    
    /* Hide Streamlit elements */
    .stDeployButton {
        visibility: hidden;
    }
    
    header[data-testid="stHeader"] {
        background: rgba(0,0,0,0);
        height: 0rem;
    }
    
    /* Hero Section */
    .hero-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        padding: 3rem 2rem;
        border-radius: 25px;
        color: white !important;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 20px 40px rgba(102, 126, 234, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    .hero-section h1 {
        color: white !important;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .hero-section p {
        color: white !important;
        opacity: 0.95;
    }
    
    /* Countdown Container */
    .countdown-container {
        background: linear-gradient(135deg, #ff6b6b 0%, #feca57 50%, #48dbfb 100%);
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        margin: 2rem 0;
        box-shadow: 0 15px 35px rgba(255, 107, 107, 0.3);
        color: white !important;
    }
    
    .countdown-container h2 {
        color: white !important;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .countdown-container p {
        color: white !important;
        opacity: 0.95;
    }
    
    .countdown-timer {
        display: flex;
        justify-content: center;
        gap: 1.5rem;
        margin: 2rem 0;
        flex-wrap: wrap;
    }
    
    .time-unit {
        background: rgba(255, 255, 255, 0.2);
        padding: 1.5rem 1rem;
        border-radius: 15px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.3);
        min-width: 75px;
        text-align: center;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .time-unit:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 25px rgba(255, 255, 255, 0.2);
    }
    
    .time-number {
        display: block;
        font-size: 2.2rem;
        font-weight: 700;
        color: white !important;
        animation: countdownPulse 2s ease-in-out infinite;
    }
    
    .time-label {
        display: block;
        font-size: 0.9rem;
        color: white !important;
        opacity: 0.9;
        margin-top: 0.5rem;
        font-weight: 500;
    }
    
    @keyframes countdownPulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }
    
    /* Special animation for seconds */
    .time-unit:last-child .time-number {
        animation: secondsTick 1s ease-in-out infinite;
        color: #feca57 !important;
    }
    
    @keyframes secondsTick {
        0% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.1); opacity: 0.8; }
        100% { transform: scale(1); opacity: 1; }
    }
    
    /* Progress Container */
    .progress-container {
        background: linear-gradient(135deg, rgba(255,255,255,0.95) 0%, rgba(247,248,249,0.95) 100%);
        padding: 2rem;
        border-radius: 20px;
        margin: 2rem 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        border: 1px solid rgba(0,0,0,0.05);
    }
    
    .progress-bar {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        height: 100%;
        border-radius: 10px;
        transition: width 0.5s ease;
        animation: progressGlow 2s ease-in-out infinite alternate;
    }
    
    @keyframes progressGlow {
        0% { box-shadow: 0 0 5px rgba(102, 126, 234, 0.5); }
        100% { box-shadow: 0 0 20px rgba(102, 126, 234, 0.8); }
    }
    
    /* Step Cards */
    .step-card {
        background: linear-gradient(135deg, rgba(255,255,255,0.95) 0%, rgba(247,248,249,0.95) 100%);
        padding: 2rem;
        border-radius: 20px;
        margin: 1rem 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        border: 1px solid rgba(102, 126, 234, 0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .step-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.15);
    }
    
    .step-card h2 {
        color: #2d3436 !important;
        margin-bottom: 1rem;
    }
    
    .step-card h3 {
        color: #667eea !important;
        margin: 1.5rem 0 1rem 0;
    }
    
    .step-card p {
        color: #636e72 !important;
        line-height: 1.6;
        margin-bottom: 1rem;
    }
    
    /* Fun Facts Container */
    .fun-fact {
        background: linear-gradient(135deg, #ff6b6b 0%, #feca57 100%);
        color: white !important;
        padding: 2rem;
        border-radius: 20px;
        margin: 1rem 0;
        box-shadow: 0 15px 35px rgba(255, 107, 107, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    .fun-fact h4 {
        color: white !important;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .fun-fact p {
        color: white !important;
        opacity: 0.95;
        line-height: 1.6;
    }
    
    /* Achievement Badges */
    .achievement-badge {
        display: inline-block;
        background: rgba(255, 255, 255, 0.2);
        padding: 0.5rem 1rem;
        border-radius: 25px;
        margin: 0.25rem;
        font-size: 0.9rem;
        font-weight: 600;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.3);
        backdrop-filter: blur(10px);
    }
    
    /* Code Container */
    .code-container {
        background: #2d3436;
        color: #ddd !important;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        font-family: 'Monaco', 'Consolas', monospace;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        border: 1px solid #636e72;
    }
    
    .code-container pre {
        margin: 0;
        color: #ddd !important;
        white-space: pre-wrap;
        word-wrap: break-word;
    }
    
    /* Mission Cards */
    .mission-card {
        background: linear-gradient(135deg, rgba(255,255,255,0.95) 0%, rgba(247,248,249,0.95) 100%);
        padding: 2rem;
        border-radius: 20px;
        margin: 1rem 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        border-left: 5px solid #667eea;
        transition: transform 0.3s ease;
    }
    
    .mission-card:hover {
        transform: translateX(10px);
    }
    
    .mission-card h3 {
        color: #667eea !important;
        margin-bottom: 1rem;
    }
    
    .mission-card p {
        color: #636e72 !important;
        line-height: 1.6;
    }
    
    /* Feature Grid */
    .feature-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 1.5rem;
        margin: 2rem 0;
    }
    
    .feature-item {
        background: linear-gradient(135deg, rgba(255,255,255,0.95) 0%, rgba(247,248,249,0.95) 100%);
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        border: 1px solid rgba(102, 126, 234, 0.1);
        transition: transform 0.3s ease;
    }
    
    .feature-item:hover {
        transform: translateY(-8px);
    }
    
    .feature-item h4 {
        color: #2d3436 !important;
        margin-bottom: 1rem;
    }
    
    .feature-item p {
        color: #636e72 !important;
        line-height: 1.5;
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .countdown-timer {
            gap: 0.8rem;
            justify-content: space-around;
        }
        
        .time-unit {
            min-width: 65px;
            padding: 1rem 0.5rem;
            flex: 1;
            max-width: 85px;
        }
        
        .time-number {
            font-size: 1.8rem;
        }
        
        .time-label {
            font-size: 0.8rem;
        }
        
        .hero-section {
            padding: 2rem 1rem;
        }
        
        .hero-section h1 {
            font-size: 2rem;
        }
        
        .feature-grid {
            grid-template-columns: 1fr;
        }
    }
    
    /* Animation Effects */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .step-card {
        animation: fadeInUp 0.6s ease-out;
    }
    
    /* Sidebar Styling */
    .css-1d391kg {
        background: linear-gradient(180deg, #2d3436 0%, #636e72 100%);
    }
    
    /* Button Styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.5rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
    }
</style>
"""
