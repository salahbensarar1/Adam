"""
Section Content for the Programming Adventure App
Completely rewritten with optimized HTML structure and better content organization.
"""

import streamlit as st
import time
import datetime


def show_welcome_section():
    """Display the Welcome section with improved structure"""
    
    st.markdown("""
    <div class="step-card">
        <h2>🎉 Welcome to Programming, Future Developer!</h2>
        <p>
            Hey there, amazing human! 👋 You're about to embark on one of the coolest journeys ever - 
            learning to speak the language of computers! Programming is like having magical powers 
            to create anything you can imagine.
        </p>
        <h3>🤔 Why C Programming?</h3>
        <p>
            Think of C as the <strong>superhero origin story</strong> of programming languages! 
            It's the foundation that almost everything else is built on. Once you master C, 
            other programming languages will feel like different flavors of ice cream - 
            same base, different toppings! 🍦
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col2:
        st.markdown("""
        <div class="fun-fact">
            <h4>🎮 Amazing Fact!</h4>
            <p>Your favorite games, the apps on your phone, and even parts of Instagram and TikTok use programming languages that are cousins of C!</p>
            <p>You're learning the same skills that created:</p>
            <div style="margin: 1rem 0;">
                <span class="achievement-badge">🎮 Video Games</span>
                <span class="achievement-badge">📱 Mobile Apps</span>
                <span class="achievement-badge">🌐 Websites</span>
                <span class="achievement-badge">🤖 AI Systems</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col1:
        st.markdown("""
        <div class="step-card">
            <h3>🚀 Your Programming Journey Has Just Begun!</h3>
            <p>You've taken the first and most important step. Here's what makes you special now:</p>
            <div class="feature-grid">
                <div class="feature-item">
                    <h4>🧠 You Think Logically</h4>
                    <p>Programming teaches you to break big problems into small, solvable pieces.</p>
                </div>
                <div class="feature-item">
                    <h4>🛠️ You Build Solutions</h4>
                    <p>Every line of code you write solves a real problem for real people.</p>
                </div>
                <div class="feature-item">
                    <h4>🎯 You're Creative</h4>
                    <p>Programming is art meets science - you create digital masterpieces!</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="step-card">
        <h3>🎯 Your Next Steps</h3>
        <div style="line-height: 1.8;">
            <p><strong>🔥 Master the fundamentals</strong> - Programming concepts that power everything</p>
            <p><strong>🚀 Build amazing projects</strong> - Each project makes you stronger</p>
            <p><strong>👥 Join communities</strong> - Connect with other awesome programmers</p>
            <p><strong>📚 Never stop learning</strong> - Technology evolves, and so will you!</p>
        </div>
    </div>
    """, unsafe_allow_html=True)


def show_mission_section():
    """Display the Mission section with clear objectives"""
    
    st.markdown("""
    <div class="step-card">
        <h2>🎯 Mission: Build the Ultimate Calculator</h2>
        <p>
            We're going to create a <strong>super-powered calculator</strong> that can solve math problems 
            faster than you can say "mathematics"! This isn't just any calculator - it's YOUR calculator, 
            built with your own hands and your own code.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown("""
        <div class="step-card">
            <h3>🛠️ Your Calculator's Superpowers</h3>
            <div class="feature-grid">
                <div class="feature-item">
                    <h4>➕ Addition Magic</h4>
                    <p>Add numbers faster than lightning!</p>
                </div>
                <div class="feature-item">
                    <h4>➖ Subtraction Skills</h4>
                    <p>Find differences with perfect precision!</p>
                </div>
                <div class="feature-item">
                    <h4>✖️ Multiplication Power</h4>
                    <p>Multiply like a mathematical superhero!</p>
                </div>
                <div class="feature-item">
                    <h4>➗ Division Mastery</h4>
                    <p>Split numbers with surgical accuracy!</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="fun-fact">
            <h4>🖥️ How Your Amazing Calculator Will Work:</h4>
            <div class="code-container">
                <pre>🎮 Welcome to the Ultimate Calculator! 🎮 <br>
<h5> Choose your mathematical adventure:</h5>
1️⃣ Addition (+)<br>
2️⃣ Subtraction (-)<br>
3️⃣ Multiplication (×)<br>
4️⃣ Division (÷)<br>
<br>
Enter your choice: 1 <br>
Enter first number: 25 <br>
Enter second number: 17 <br>
✨ Result: 25 + 17 = 42 ✨ <br>

🎉 Math mission accomplished! 🎉</pre>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="step-card">
        <h3>🏆 Why This Project Rocks</h3>
        <p>Building a calculator teaches you <strong>everything</strong> you need to know about programming:</p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1rem; margin: 1rem 0;">
            <div class="mission-card">
                <h4>💭 Logical Thinking</h4>
                <p>Learn to break problems into step-by-step solutions</p>
            </div>
            <div class="mission-card">
                <h4>🔢 Working with Data</h4>
                <p>Handle numbers, text, and user input like a pro</p>
            </div>
            <div class="mission-card">
                <h4>🎮 User Interaction</h4>
                <p>Create programs that respond to what users want</p>
            </div>
            <div class="mission-card">
                <h4>🐛 Problem Solving</h4>
                <p>Debug issues and make your code bulletproof</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def show_learn_section():
    """Display the Learn section with C programming fundamentals"""
    
    st.markdown("""
    <div class="step-card">
        <h2>🧠 Learn: C Programming Building Blocks</h2>
        <p>
            Think of programming like building with LEGO blocks! Each concept is a different shaped block that 
            you'll use to build your calculator. Each concept is a different shaped block that 
            fits together perfectly to create something amazing.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Concept 1: Hello World
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown("""
        <div class="step-card">
            <h3>🌍 Concept 1: Hello World - Your First Program</h3>
            <p>Every programmer's journey starts here. It's like teaching your computer to say "Hi!"</p>
            <div class="code-container">
                <pre>#include &lt;stdio.h&gt;  // Import tools (like getting a toolbox)
                
int main() {
    // This is where the magic happens!
    printf("Hello, World! 🌍\\n");
    return 0;  // Tell the computer "job done!"
}</pre>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="fun-fact">
            <h4>🔍 Code Breakdown:</h4>
            <p>🧰 <code>#include &lt;stdio.h&gt;</code> = Getting your toolbox ready</p>
            <p>🏠 <code>int main()</code> = Your program's home base</p>
            <p>💬 <code>printf()</code> = Making the computer talk</p>
            <p>✅ <code>return 0</code> = Mission accomplished!</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Concept 2: Variables
    st.markdown("""
    <div class="step-card">
        <h3>📦 Concept 2: Variables - Your Data Containers</h3>
        <p>Variables are like labeled boxes where you store information. Need to remember a number? Put it in a variable!</p>    
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(400px, 1fr)); gap: 2rem;">
            <div class="code-container">
                <pre>// Creating your storage boxes <br>
int age = 13;           // Whole numbers <br>
float height = 5.2;     // Decimal numbers   <br>
char grade = 'A';       // Single characters <br>   
char name[50] = "Alex"; // Text (strings)<br>

// Using your variables <br>
printf("Name: %s\\n", name); <br>
printf("Age: %d years\\n", age); <br>
printf("Height: %.1f feet\\n", height); <br>
printf("Grade: %c\\n", grade);</pre> <br>
            </div>
            <div class="fun-fact">
                <h4>🏷️ Variable Types:</h4>
                <p><strong>int</strong> = Whole numbers (1, 42, -10)</p>
                <p><strong>float</strong> = Decimal numbers (3.14, 5.7)</p>
                <p><strong>char</strong> = Single letters ('A', 'x', '!')</p>
                <p><strong>char[]</strong> = Words and sentences</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Concept 3: Input/Output
    st.markdown("""
    <div class="step-card">
        <h3>🗣️ Concept 3: Talking to Users</h3>
        <p>Programs are conversations! You ask questions, users give answers, and magic happens.</p>
        <div class="code-container">
            <pre>// Getting user input for our calculator <br>
char name[50];<br>
int num1, num2, result;<br>
<br>
printf("What's your name? "); <br>
scanf("%s", name);<br>
printf("Hello, %s! 👋\\n", name);<br>
<br>
// Calculator example<br>
printf("Enter first number: ");<br>
scanf("%d", &amp;num1);<br>
printf("Enter second number: ");<br>
scanf("%d", &amp;num2);<br>
<br>
result = num1 + num2;<br>
printf("%s, the answer is: %d! 🎉\\n", name, result);</pre>
        </div>
         <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; margin-top: 1rem;">
            <div class="fun-fact">
                <p>📤 <code>printf()</code> = Computer talks to you</p>
                <p>📥 <code>scanf()</code> = You talk to computer</p>
            </div>
            <div class="fun-fact">
                <p>💡 <strong>Pro Tip:</strong> Always be friendly with your users!</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Concept 4: Math Operations
    st.markdown("""
    <div class="step-card">
        <h3>🧮 Concept 4: Mathematical Superpowers</h3>
        <p>Time to give your calculator its powers! Here's how computers do math:</p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem;">
            <div class="code-container">
                <pre>int a = 10, b = 3; <br>
float x = 10.0, y = 3.0;<br>

<br>// Basic operations <br>
printf("Addition: %d + %d = %d\\n", a, b, a + b);<br>
printf("Subtraction: %d - %d = %d\\n", a, b, a - b);<br>
printf("Multiplication: %d × %d = %d\\n", a, b, a * b);<br>
printf("Division: %.1f ÷ %.1f = %.2f\\n", x, y, x / y);<br>

<br>// Special operations <br>
printf("Remainder: %d %% %d = %d\\n", a, b, a % b);</pre>
            </div>
            <div class="feature-grid">
                <div class="feature-item">
                    <h4>➕ Addition</h4>
                    <p><code>a + b</code></p>
                </div>
                <div class="feature-item">
                    <h4>➖ Subtraction</h4>
                    <p><code>a - b</code></p>
                </div>
                <div class="feature-item">
                    <h4>✖️ Multiplication</h4>
                    <p><code>a * b</code></p>
                </div>
                <div class="feature-item">
                    <h4>➗ Division</h4>
                    <p><code>a / b</code></p>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def show_build_section():
    """Display the Build section with step-by-step calculator construction"""
    
    st.markdown("""
    <div class="step-card">
        <h2>🛠️ Build: Create Your Calculator Step by Step</h2>
        <p>Now for the exciting part - let's build your calculator! We'll start simple and add more features as we go.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Step 1: Basic Structure
    st.markdown("""
    <div class="step-card">
        <h3>🏗️ Step 1: Build the Foundation</h3>
        <p>Every great building needs a strong foundation. Here's the basic structure of your calculator:</p>
        <div class="code-container">
            <pre>#include &lt;stdio.h&gt; 

int main() { <br>
    // Welcome message<br>
    printf("🎮 Welcome to Your Amazing Calculator! 🎮\\n");<br>
    printf("================================\\n");<br>
    <br>
    // Variables to store numbers and choice<br>
    float num1, num2, result;<br>
    int choice;<br>
<br>
    // Show menu<br>
    printf("Choose your mathematical adventure:\\n");<br>
    printf("1. Addition (+)\\n");<br>
    printf("2. Subtraction (-)\\n");<br>
    printf("3. Multiplication (×)\\n");<br>
    printf("4. Division (÷)\\n");<br>
    printf("Enter your choice (1-4): ");<br>
<br>
    return 0;<br>
}</pre>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Step 2: Add User Input
    st.markdown("""
    <div class="step-card">
        <h3>🎯 Step 2: Get User Input</h3>
        <p>Now let's make your calculator interactive! We'll ask users what they want to calculate:</p>
        <div class="code-container">
            <pre>// Get user's choice <br>
scanf("%d", &amp;choice);<br>
<br>
// Get the numbers to calculate<br>
printf("\\nEnter first number: ");<br>
scanf("%f", &amp;num1);<br>
printf("Enter second number: ");<br>
scanf("%f", &amp;num2);<br>
<br>
printf("\\n🔢 You entered: %.2f and %.2f\\n", num1, num2);</pre>
        </div>
        <div class="fun-fact">
            <h4>💡 What's Happening Here?</h4>
            <p><strong>scanf("%d", &choice)</strong> - Gets the menu choice</p>
            <p><strong>scanf("%f", &num1)</strong> - Gets the first number</p>
            <p><strong>%.2f</strong> - Shows 2 decimal places</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Step 3: Add the Math Logic
    st.markdown("""
    <div class="step-card">
        <h3>🧮 Step 3: Add the Mathematical Magic</h3>
        <p>Time to give your calculator its superpowers! We'll use if-else statements to perform different operations:</p>
        <div class="code-container">
            <pre>// Perform calculation based on choice<br>
if (choice == 1) {<br>
    result = num1 + num2;<br>
    printf("\\n✨ %.2f + %.2f = %.2f ✨\\n", num1, num2, result);<br>
} <br>
else if (choice == 2) {<br>
    result = num1 - num2;<br>
    printf("\\n✨ %.2f - %.2f = %.2f ✨\\n", num1, num2, result);<br>
}<br>
else if (choice == 3) {<br>
    result = num1 * num2;<br>
    printf("\\n✨ %.2f × %.2f = %.2f ✨\\n", num1, num2, result);<br>
}<br>
else if (choice == 4) {<br>
    if (num2 != 0) {<br>
        result = num1 / num2;<br>
        printf("\\n✨ %.2f ÷ %.2f = %.2f ✨\\n", num1, num2, result);<br>
    } else {<br>
        printf("\\n❌ Error: Cannot divide by zero!\\n");<br>
    }<br>
}<br>
else {<br>
    printf("\\n❌ Invalid choice! Please choose 1-4.\\n");<br>
}</pre>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Step 4: Complete Program
    st.markdown("""
    <div class="step-card">
        <h3>🎉 Step 4: Your Complete Calculator!</h3>
        <p>Congratulations! Here's your finished calculator program. Copy this code and try running it:</p>
        <div class="code-container">
            <pre>#include &lt;stdio.h&gt;<br>

int main() {<br>
    // Welcome the user<br>
    printf("🎮 Welcome to Your Amazing Calculator! 🎮\\n");<br>
    printf("================================\\n");<br>
    <br>
    // Declare variables<br>
    float num1, num2, result;<br>
    int choice;<br>
    <br>
    // Show menu<br>
    printf("Choose your mathematical adventure:\\n");<br>
    printf("1. Addition (+)\\n");<br>
    printf("2. Subtraction (-)\\n");<br>
    printf("3. Multiplication (×)\\n");<br>
    printf("4. Division (÷)\\n");<br>
    printf("Enter your choice (1-4): ");<br>
    <br>
    // Get user input<br>
    scanf("%d", &amp;choice);<br>
    printf("\\nEnter first number: ");<br>
    scanf("%f", &amp;num1);<br>
    printf("Enter second number: ");<br>
    scanf("%f", &amp;num2);<br>
    <br>
    // Perform calculation<br>
    switch(choice) {<br>
        case 1:<br>
            result = num1 + num2;<br>
            printf("\\n✨ %.2f + %.2f = %.2f ✨\\n", num1, num2, result);<br>
            break;<br>
        case 2:<br>
            result = num1 - num2;<br>
            printf("\\n✨ %.2f - %.2f = %.2f ✨\\n", num1, num2, result);<br>
            break;<br>
        case 3:<br>
            result = num1 * num2;<br>
            printf("\\n✨ %.2f × %.2f = %.2f ✨\\n", num1, num2, result);<br>
            break;<br>
        case 4:<br>
            if (num2 != 0) {<br>
                result = num1 / num2;<br>
                printf("\\n✨ %.2f ÷ %.2f = %.2f ✨\\n", num1, num2, result);<br>
            } else {<br>
                printf("\\n❌ Error: Cannot divide by zero!\\n");<br>
            }<br>
            break;<br>
        default:<br>
            printf("\\n❌ Invalid choice! Please choose 1-4.\\n");<br>
    }<br>
<br>
    printf("\\n🎉 Thanks for using your calculator! 🎉\\n");<br>
    return 0;<br>
}</pre>
        </div>    
        <div class="fun-fact">
            <h4>🏆 Congratulations, You're Now a Programmer!</h4>
            <p>You just built a complete, working calculator! This program demonstrates all the core concepts of programming:</p>
            <div style="line-height: 2;">
                <p>✅ Variables and data types</p>
                <p>✅ User input and output</p>
                <p>✅ Conditional logic (if/else)</p>
                <p>✅ Mathematical operations</p>
                <p>✅ Error handling</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def show_levelup_section():
    """Display bonus challenges and advanced features"""
    
    st.markdown("""
    <div class="step-card">
        <h2>🏆 Level Up: Bonus Challenges</h2>
        <p>Ready to make your calculator even more awesome? Here are some exciting challenges to level up your programming skills!</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="fun-fact">
            <h3>🎮 Challenge 1: Advanced Operations</h3>
            <p>Add these cool features to your calculator:</p>
            <div class="achievement-badge">🔢 Square root</div>
            <div class="achievement-badge">⚡ Power (x^y)</div>
            <div class="achievement-badge">📐 Sin, Cos, Tan</div>
            <div class="achievement-badge">🔄 Percentage</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="step-card">
            <h4>🔢 Sample Code: Square Root</h4>
            <div class="code-container">
                <pre>#include &lt;math.h&gt;  // For sqrt()<br>
<br>
case 5:<br>
    if (num1 >= 0) {<br>
        result = sqrt(num1);<br>
        printf("√%.2f = %.2f\\n", num1, result);<br>
    } else {<br>
        printf("❌ Cannot find square root of negative number!\\n");<br>
    }<br>
    break;</pre>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="step-card">
            <h3>🔄 Challenge 2: Looping Calculator</h3>
            <p>Make your calculator run continuously until the user wants to quit!</p>  
            <div class="code-container">
                <pre>int continue_calc = 1;
char choice;<br>
<br>
while (continue_calc) {<br>
    // Your calculator code here<br>
<br>
    printf("\\nDo another calculation? (y/n): ");<br>
    scanf(" %c", &amp;choice);<br>
<br>
    if (choice == 'n' || choice == 'N') {  <br>
        continue_calc = 0;<br>
        printf("Thanks for calculating! 👋\\n");<br>
    }<br>
}</pre>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="fun-fact">
            <h3>💾 Challenge 3: Memory Feature</h3>
            <p>Add memory functions like real calculators:</p>
            <div class="achievement-badge">💾 Store result</div>
            <div class="achievement-badge">📋 Recall stored value</div>
            <div class="achievement-badge">🗑️ Clear memory</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="step-card">
        <h3>🌟 Challenge 4: Scientific Calculator</h3>
        <p>Transform your basic calculator into a scientific powerhouse!</p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1rem;">
            <div class="mission-card">
                <h4>📐 Trigonometry</h4>
                <p>Add sin, cos, tan functions using the math.h library</p>
            </div>
            <div class="mission-card">
                <h4>📊 Statistics</h4>
                <p>Calculate mean, median, mode of a series of numbers</p>
            </div>
            <div class="mission-card">
                <h4>🔢 Number Systems</h4>
                <p>Convert between binary, decimal, and hexadecimal</p>
            </div>
            <div class="mission-card">
                <h4>📈 Graphing</h4>
                <p>Plot simple mathematical functions (advanced!)</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="fun-fact">
        <h3>🏆 Achievement Unlocked!</h3>
        <p>By completing these challenges, you'll have skills that many professional programmers use every day!</p>
        <div style="text-align: center; margin: 2rem 0;">
            <div class="achievement-badge">🎯 Problem Solver</div>
            <div class="achievement-badge">🧠 Logical Thinker</div>
            <div class="achievement-badge">🛠️ Code Builder</div>
            <div class="achievement-badge">🚀 Future Engineer</div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def show_resources_section():
    """Display learning resources and next steps"""
    
    st.markdown("""
    <div class="step-card">
        <h2>📚 Resources: Your Learning Arsenal</h2>
        <p>Here are amazing resources to continue your programming adventure!</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="step-card">
            <h3>🌐 Online Learning Platforms</h3>
            <div class="mission-card">
                <h4>🎯 Codecademy</h4>
                <p>Interactive C programming courses with hands-on practice</p>
            </div>
            <div class="mission-card">
                <h4>🎮 HackerRank</h4>
                <p>Programming challenges and contests to test your skills</p>
            </div>
            <div class="mission-card">
                <h4>📺 YouTube - Programming with Mosh</h4>
                <p>Clear, beginner-friendly programming tutorials</p>
            </div>
            <div class="mission-card">
                <h4>📖 Learn-C.org</h4>
                <p>Free interactive C programming tutorial</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="fun-fact">
            <h3>📱 Programming Apps</h3>
            <p>Learn programming on your phone!</p>
            <div class="achievement-badge">📱 SoloLearn</div>
            <div class="achievement-badge">🧠 Programming Hero</div>
            <div class="achievement-badge">🎮 Grasshopper</div>
            <div class="achievement-badge">💻 Encode</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="step-card">
            <h3>🛠️ Development Tools</h3>
            <div class="code-container">
                <pre>🖥️ Code Editors:<br>
• Visual Studio Code (FREE!)<br>
• Dev-C++<br>
• Code::Blocks<br>
<br>
🌐 Online Compilers:<br>
• OnlineGDB.com<br>
• Repl.it<br>
• CodeChef IDE</pre>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="step-card">
        <h3>🎯 Your Programming Roadmap</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem;">
            <div class="feature-item">
                <h4>🏗️ Beginner (You are here!)</h4>
                <p>Master C basics, build simple programs, understand logic</p>
            </div>
            <div class="feature-item">
                <h4>🚀 Intermediate</h4>
                <p>Learn data structures, algorithms, object-oriented programming</p>
            </div>
            <div class="feature-item">
                <h4>🏆 Advanced</h4>
                <p>Build real applications, contribute to open source, specialize</p>
            </div>
            <div class="feature-item">
                <h4>💼 Professional</h4>
                <p>Land your dream job, build amazing products, change the world!</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def show_celebrate_section():
    """Display celebration and achievements"""
    
    st.markdown("""
    <div class="hero-section">
        <h1>🎉 Congratulations, Amazing Programmer! 🎉</h1>
        <p>You've just completed an incredible journey and built your very own calculator!</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="step-card">
        <h2>🏆 What You've Accomplished</h2>
        <p>Look at all the amazing skills you've gained:</p>
        <div class="feature-grid">
            <div class="feature-item">
                <h4>💭 Logical Thinking</h4>
                <p>You can break complex problems into simple steps</p>
            </div>
            <div class="feature-item">
                <h4>🔧 Problem Solving</h4>
                <p>You know how to debug and fix issues in your code</p>
            </div>
            <div class="feature-item">
                <h4>🎯 Programming Fundamentals</h4>
                <p>Variables, functions, loops, and conditions are your tools now</p>
            </div>
            <div class="feature-item">
                <h4>🚀 Project Building</h4>
                <p>You can create real, working programs from scratch</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="fun-fact">
            <h3>🌟 Your Programming Superpowers</h3>
            <div style="line-height: 2;">
                <div class="achievement-badge">🧠 Computational Thinking</div>
                <div class="achievement-badge">🔍 Attention to Detail</div>
                <div class="achievement-badge">🎯 Goal-Oriented</div>
                <div class="achievement-badge">💪 Persistence</div>
                <div class="achievement-badge">🚀 Innovation</div>
                <div class="achievement-badge">🔧 Problem Solver</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="step-card">
            <h3>🎯 What's Next?</h3>
            <p>Your programming journey has just begun! Here's what you can do next:</p>
            <div style="line-height: 1.8;">
                <p>🎮 <strong>Build more projects</strong> - Create games, apps, websites</p>
                <p>📚 <strong>Learn new languages</strong> - Python, JavaScript, Java</p>
                <p>👥 <strong>Join coding communities</strong> - Share your projects</p>
                <p>🏆 <strong>Participate in contests</strong> - Test your skills</p>
                <p>🎓 <strong>Consider CS courses</strong> - Formal computer science education</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="countdown-container">
        <h2>🚀 You're Now Part of the Programming Universe! 🚀</h2>
        <p>Welcome to a community of millions of developers worldwide who are building the future!</p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 2rem; margin: 2rem 0;">
            <div style="text-align: center;">
                <h3 style="color: white; margin-bottom: 0.5rem;">🌍 25+ Million</h3>
                <p style="color: white; opacity: 0.9;">Developers Worldwide</p>
            </div>
            <div style="text-align: center;">
                <h3 style="color: white; margin-bottom: 0.5rem;">💼 $100K+</h3>
                <p style="color: white; opacity: 0.9;">Average Programmer Salary</p>
            </div>
            <div style="text-align: center;">
                <h3 style="color: white; margin-bottom: 0.5rem;">🚀 Unlimited</h3>
                <p style="color: white; opacity: 0.9;">Creative Possibilities</p>
            </div>
        </div>
        <p style="font-size: 1.2rem; margin-top: 2rem;">
            Remember: Every expert was once a beginner. Every master was once a disaster. 
            Keep coding, keep learning, and keep building amazing things! 🌟
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Add some fun interactive elements
    if st.button("🎉 Click to Celebrate Your Achievement! 🎉"):
        st.balloons()
        st.success("🏆 Congratulations! You're officially a programmer now! 🎮")
        
        # Show completion certificate
        st.markdown("""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    color: white; padding: 3rem; border-radius: 20px; 
                    text-align: center; margin: 2rem 0; 
                    border: 5px solid gold;">
            <h2>🏆 CERTIFICATE OF COMPLETION 🏆</h2>
            <h3>This certifies that</h3>
            <h1 style="color: gold; margin: 1rem 0; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);">
                FUTURE PROGRAMMING LEGEND
            </h1>
            <h3>has successfully completed</h3>
            <h2 style="color: #feca57;">C Programming Calculator Project</h2>
            <p style="margin: 2rem 0; font-size: 1.1rem;">
                With outstanding dedication, creativity, and programming skills!
            </p>
            <div style="margin-top: 2rem;">
                <span style="color: gold; font-size: 1.5rem;">⭐⭐⭐⭐⭐</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
