import streamlit as st
import re
from urllib.parse import quote
import qrcode
from io import BytesIO
import base64

def validate_phone_number(phone):
    """Validate and format phone number"""
    # Remove all non-digit characters
    phone = re.sub(r'\D', '', phone)
    
    # Check if phone number is valid (should be at least 10 digits)
    if len(phone) < 10:
        return None
    
    # Add country code if not present (assuming India +91 as default)
    if len(phone) == 10:
        phone = "91" + phone
    elif not phone.startswith("91") and len(phone) == 12:
        pass  # Already has country code
    elif phone.startswith("91"):
        pass  # Already has country code
    else:
        # For other country codes, keep as is
        pass
    
    return phone

def generate_whatsapp_link(phone_number, message):
    """Generate WhatsApp Web link with pre-filled message"""
    encoded_message = quote(message)
    return f"https://web.whatsapp.com/send?phone={phone_number}&text={encoded_message}"

def generate_qr_code(url):
    """Generate QR code for the WhatsApp link"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Convert to base64 for display
    buffer = BytesIO()
    img.save(buffer, format='PNG')
    img_str = base64.b64encode(buffer.getvalue()).decode()
    
    return img_str

def create_html_auto_opener(whatsapp_url, phone_number, message):
    """Create HTML with JavaScript to auto-open WhatsApp link"""
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>WhatsApp Message Sender</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {{
                font-family: Arial, sans-serif;
                max-width: 600px;
                margin: 50px auto;
                padding: 20px;
                text-align: center;
                background: linear-gradient(135deg, #25D366, #128C7E);
                color: white;
                min-height: 100vh;
            }}
            .container {{
                background: rgba(255, 255, 255, 0.1);
                padding: 30px;
                border-radius: 15px;
                backdrop-filter: blur(10px);
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
            }}
            .whatsapp-icon {{
                font-size: 60px;
                margin-bottom: 20px;
            }}
            .btn {{
                background: #25D366;
                color: white;
                padding: 15px 30px;
                border: none;
                border-radius: 30px;
                font-size: 18px;
                font-weight: bold;
                cursor: pointer;
                text-decoration: none;
                display: inline-block;
                margin: 10px;
                transition: all 0.3s ease;
                box-shadow: 0 4px 15px rgba(37, 211, 102, 0.4);
            }}
            .btn:hover {{
                background: #128C7E;
                transform: translateY(-2px);
                box-shadow: 0 6px 20px rgba(37, 211, 102, 0.6);
            }}
            .message-preview {{
                background: rgba(255, 255, 255, 0.2);
                padding: 15px;
                border-radius: 10px;
                margin: 20px 0;
                text-align: left;
            }}
            .phone-number {{
                font-weight: bold;
                color: #FFE135;
            }}
            #countdown {{
                font-size: 24px;
                font-weight: bold;
                color: #FFE135;
                margin: 20px 0;
            }}
            .instructions {{
                margin-top: 30px;
                font-size: 14px;
                opacity: 0.9;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="whatsapp-icon">📱</div>
            <h1>WhatsApp Message Ready!</h1>
            
            <div id="countdown">Opening in <span id="timer">5</span> seconds...</div>
            
            <div class="message-preview">
                <p><strong>📞 To:</strong> <span class="phone-number">+{phone_number}</span></p>
                <p><strong>💬 Message:</strong> {message}</p>
            </div>
            
            <a href="{whatsapp_url}" class="btn" id="whatsapp-btn" target="_blank">
                🚀 Open WhatsApp Now
            </a>
            
            <button class="btn" onclick="copyLink()" style="background: #128C7E;">
                📋 Copy Link
            </button>
            
            <div class="instructions">
                <p><strong>Instructions:</strong></p>
                <p>1. WhatsApp Web will open automatically in 5 seconds</p>
                <p>2. If not logged in, scan the QR code with your phone</p>
                <p>3. Your message will be pre-filled and ready to send</p>
                <p>4. Click the send button in WhatsApp to deliver the message</p>
            </div>
        </div>

        <script>
            let countdown = 5;
            const timerElement = document.getElementById('timer');
            const whatsappBtn = document.getElementById('whatsapp-btn');
            
            const countdownInterval = setInterval(() => {{
                countdown--;
                timerElement.textContent = countdown;
                
                if (countdown <= 0) {{
                    clearInterval(countdownInterval);
                    document.getElementById('countdown').innerHTML = '🚀 Opening WhatsApp...';
                    window.open('{whatsapp_url}', '_blank');
                    setTimeout(() => {{
                        document.getElementById('countdown').innerHTML = '✅ WhatsApp Opened! Check your browser tabs.';
                    }}, 2000);
                }}
            }}, 1000);
            
            function copyLink() {{
                navigator.clipboard.writeText('{whatsapp_url}').then(() => {{
                    alert('✅ WhatsApp link copied to clipboard!');
                }}).catch(() => {{
                    // Fallback for older browsers
                    const textArea = document.createElement('textarea');
                    textArea.value = '{whatsapp_url}';
                    document.body.appendChild(textArea);
                    textArea.select();
                    document.execCommand('copy');
                    document.body.removeChild(textArea);
                    alert('✅ WhatsApp link copied to clipboard!');
                }});
            }}
            
            // Also open on button click
            whatsappBtn.addEventListener('click', (e) => {{
                e.preventDefault();
                window.open('{whatsapp_url}', '_blank');
            }});
        </script>
    </body>
    </html>
    """
    return html_content

def main():
    st.set_page_config(
        page_title="WhatsApp Message Sender",
        page_icon="📱",
        layout="wide"
    )
    
    st.title("📱 WhatsApp Message Sender")
    st.write("Generate WhatsApp links and QR codes - **Streamlit Cloud Compatible!**")
    
    # Success message about compatibility
    st.success("✅ This version works perfectly on Streamlit Cloud without browser automation!")
    
    # Create two columns
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Create form
        with st.form("whatsapp_form"):
            st.subheader("📋 Message Details")
            
            # Phone number input
            phone_input = st.text_input(
                "📞 Phone Number",
                placeholder="Enter phone number (e.g., +919876543210 or 9876543210)",
                help="Enter the phone number with or without country code. For India, +91 will be added automatically."
            )
            
            # Message input
            message_input = st.text_area(
                "💬 Message",
                placeholder="Type your message here...",
                height=120,
                help="Enter the message you want to send"
            )
            
            # Options
            st.subheader("📤 Delivery Options")
            
            col_opt1, col_opt2 = st.columns(2)
            with col_opt1:
                auto_open = st.checkbox("🚀 Auto-open WhatsApp", value=True, help="Automatically open WhatsApp Web")
            with col_opt2:
                show_qr = st.checkbox("📱 Generate QR Code", value=True, help="Create QR code for mobile access")
            
            # Submit button
            submit_button = st.form_submit_button("✨ Generate WhatsApp Link", type="primary", use_container_width=True)
            
            if submit_button:
                if not phone_input.strip():
                    st.error("❌ Please enter a phone number")
                elif not message_input.strip():
                    st.error("❌ Please enter a message")
                else:
                    # Validate and format phone number
                    formatted_phone = validate_phone_number(phone_input)
                    
                    if formatted_phone:
                        # Generate WhatsApp link
                        whatsapp_url = generate_whatsapp_link(formatted_phone, message_input.strip())
                        
                        st.success("✅ WhatsApp link generated successfully!")
                        
                        # Display formatted info
                        st.info(f"📞 **Formatted Phone:** +{formatted_phone}")
                        st.info(f"💬 **Message Preview:** {message_input.strip()[:100]}{'...' if len(message_input.strip()) > 100 else ''}")
                        
                        # Store in session state
                        st.session_state.whatsapp_url = whatsapp_url
                        st.session_state.phone_number = formatted_phone
                        st.session_state.message = message_input.strip()
                        st.session_state.auto_open = auto_open
                        st.session_state.show_qr = show_qr
                        
                    else:
                        st.error("❌ Invalid phone number format")
    
    with col2:
        st.subheader("🎯 Quick Actions")
        
        # Show results if available
        if hasattr(st.session_state, 'whatsapp_url'):
            # Direct WhatsApp link
            st.markdown("### 🔗 Direct Link")
            st.link_button("📱 Open WhatsApp Web", st.session_state.whatsapp_url, use_container_width=True)
            
            # Copy link button
            st.markdown("### 📋 Copy Link")
            if st.button("📄 Copy to Clipboard", use_container_width=True):
                st.code(st.session_state.whatsapp_url, language=None)
                st.success("👆 Link displayed above - select and copy!")
            
            # Auto-opener
            if st.session_state.auto_open:
                st.markdown("### 🚀 Auto-Opener")
                if st.button("🌐 Generate Auto-Open Page", use_container_width=True):
                    html_content = create_html_auto_opener(st.session_state.whatsapp_url, st.session_state.phone_number, st.session_state.message)
                    st.session_state.html_page = html_content
                    st.success("✅ Auto-open page generated! See below.")
            
            # QR Code
            if st.session_state.show_qr:
                st.markdown("### 📱 QR Code")
                try:
                    qr_img = generate_qr_code(st.session_state.whatsapp_url)
                    st.image(f"data:image/png;base64,{qr_img}", width=200)
                    st.caption("Scan with phone camera to open WhatsApp")
                except Exception as e:
                    st.error(f"QR generation failed: {e}")
    
    # Auto-open HTML page
    if hasattr(st.session_state, 'html_page'):
        st.markdown("---")
        st.subheader("🌐 Auto-Open WhatsApp Page")
        st.markdown("**Download this HTML file and open it in any browser:**")
        
        st.download_button(
            label="📥 Download Auto-Open Page",
            data=st.session_state.html_page,
            file_name=f"whatsapp_sender_{st.session_state.phone_number}.html",
            mime="text/html",
            use_container_width=True
        )
        
        st.info("💡 **How it works:** The HTML page will automatically open WhatsApp Web after 5 seconds with your message pre-filled!")
    
    # Instructions
    st.markdown("---")
    st.subheader("📋 How to Use")
    
    tab1, tab2, tab3 = st.tabs(["🚀 Quick Start", "📱 Mobile Users", "🔧 Advanced"])
    
    with tab1:
        st.markdown("""
        ### For Desktop Users:
        1. **Fill the form** with phone number and message
        2. **Click "Generate WhatsApp Link"**
        3. **Click "Open WhatsApp Web"** button
        4. **Login to WhatsApp Web** if needed (scan QR code)
        5. **Send the message** (it will be pre-filled)
        """)
    
    with tab2:
        st.markdown("""
        ### For Mobile Users:
        1. **Generate the QR code** using the checkbox option
        2. **Scan the QR code** with your phone's camera
        3. **WhatsApp will open** with the message ready to send
        4. **Tap send** to deliver the message
        """)
    
    with tab3:
        st.markdown("""
        ### Advanced Features:
        - **Auto-Open Page**: Downloads an HTML file that auto-opens WhatsApp
        - **Link Copying**: Get the raw WhatsApp URL for integration
        - **QR Code**: Perfect for mobile users or sharing
        - **Batch Processing**: Use the raw link format for multiple messages
        """)
    
    # Why this approach
    with st.expander("🤔 Why This Approach?"):
        st.markdown("""
        **This solution is designed for Streamlit Cloud compatibility:**
        
        ✅ **No browser automation** (Playwright/Selenium not needed)  
        ✅ **Pure Python + HTML/JavaScript** approach  
        ✅ **Works on all cloud platforms**  
        ✅ **No additional system dependencies**  
        ✅ **Mobile-friendly with QR codes**  
        
        **Previous browser automation issues on Streamlit Cloud:**
        - Browser binaries not installed
        - Security restrictions on cloud platforms  
        - Complex dependencies and system requirements
        - Unreliable headless browser behavior
        
        **This approach gives you:**
        - 100% reliable WhatsApp link generation
        - Multiple delivery methods (direct link, QR, auto-open page)
        - Works on any device/platform
        - Easy to deploy and maintain
        """)

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #888; padding: 20px;'>
        <p>🚀 <strong>Streamlit Cloud Compatible WhatsApp Sender</strong></p>
        <p>No browser automation • No complex dependencies • 100% reliable</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()