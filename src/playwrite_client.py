from playwright.sync_api import sync_playwright
import time
import re
from urllib.parse import quote

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

def handle_initial_dialogs(page):
    """Handle any initial dialogs or popups that appear on WhatsApp Web"""
    try:
        print("🔍 Checking for initial dialogs...")
        
        # Wait a moment for page to load
        time.sleep(3)
        
        # Common selectors for dialogs and popups
        dialog_selectors = [
            '[data-testid="popup-panel-close"]',  # Close button for popups
            '[aria-label="Close"]',              # Generic close button
            'button[aria-label="Dismiss"]',      # Dismiss button
            'button[aria-label="OK"]',           # OK button
            'button[aria-label="Got it"]',       # Got it button
            '[data-testid="modal-close"]',       # Modal close
            'div[role="dialog"] button',         # Any button in dialog
            '.dialog-close',                     # Dialog close class
        ]
        
        # Try to close any dialogs
        for selector in dialog_selectors:
            try:
                dialog_element = page.query_selector(selector)
                if dialog_element and dialog_element.is_visible():
                    print(f"🔘 Found and closing dialog...")
                    dialog_element.click()
                    time.sleep(1)
                    break
            except:
                continue
        
        # Also try pressing Escape key to close any modal
        try:
            page.keyboard.press("Escape")
            time.sleep(1)
        except:
            pass

        print("✅ Dialog handling completed")

    except Exception as e:
        print(f"Dialog handling info: {str(e)}")

def send_whatsapp_message(phone_number, message):
    """Send a message to a specific phone number via WhatsApp Web"""
    try:
        with sync_playwright() as p:
            # Launch browser with larger window
            browser = p.chromium.launch(
                headless=False,
                args=['--start-maximized', '--disable-blink-features=AutomationControlled']
            )
            
            context = browser.new_context(
                viewport={'width': 1280, 'height': 720},
                user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            )
            
            page = context.new_page()

            print("🔄 Opening WhatsApp Web...")

            # First, go to WhatsApp Web main page
            page.goto("https://web.whatsapp.com/")
            
            # Handle initial dialogs
            handle_initial_dialogs(page)

            print("⏳ Waiting for WhatsApp Web to load...")

            # Check if we need to login (look for QR code)
            try:
                # Wait for either QR code or main interface
                page.wait_for_selector('canvas[aria-label="Scan me!"], [data-testid="chat-list"], div[data-testid="landing-main"]', timeout=15000)
                
                qr_code = page.query_selector('canvas[aria-label="Scan me!"]')
                if qr_code:
                    print("📱 QR Code detected! Please scan with your phone to log in.")
                    print("⏳ Waiting for login... (You have up to 3 minutes)")

                    # Wait for login with extended timeout
                    try:
                        page.wait_for_selector('canvas[aria-label="Scan me!"]', state='detached', timeout=180000)  # 3 minutes
                        print("✅ Login successful!")
                        time.sleep(3)  # Wait for interface to fully load
                    except:
                        print("⏰ Login timeout. Please try again and scan the QR code quickly.")
                        return
                else:
                    print("✅ Already logged in!")

            except Exception as e:
                print(f"Error during initial load: {str(e)}")
                return
            
            # Now navigate to the specific chat with pre-filled message
            print("📱 Opening chat with recipient...")

            # URL encode the message to handle special characters
            encoded_message = quote(message)
            whatsapp_url = f"https://web.whatsapp.com/send?phone={phone_number}&text={encoded_message}"
            
            page.goto(whatsapp_url)
            
            # Wait for chat to load
            time.sleep(5)
            
            # Handle any dialogs that might appear when opening chat
            handle_initial_dialogs(page)
            
            # Wait for message input box
            print("🔍 Looking for message input...")
            try:
                # Try multiple selectors for message input
                message_selectors = [
                    '[data-testid="conversation-compose-box-input"]',
                    'div[contenteditable="true"][data-tab="10"]',
                    'div[contenteditable="true"]',
                    '.input-container div[contenteditable="true"]'
                ]
                
                message_input = None
                for selector in message_selectors:
                    try:
                        page.wait_for_selector(selector, timeout=10000)
                        message_input = page.query_selector(selector)
                        if message_input:
                            break
                    except:
                        continue
                
                if message_input:
                    print("✅ Message input found!")

                    # Check if message is already there from URL
                    current_text = message_input.text_content() or ""
                    
                    if message not in current_text:
                        print("📝 Typing message...")
                        # Clear any existing text and type our message
                        message_input.click()
                        page.keyboard.press("Control+a")  # Select all
                        page.keyboard.type(message)
                        time.sleep(1)
                    else:
                        print("✅ Message already pre-filled!")

                    # Look for send button
                    send_selectors = [
                        '[data-testid="send"]',
                        'button[aria-label="Send"]',
                        'span[data-icon="send"]',
                        'button[aria-label="Send message"]'
                    ]
                    
                    send_button = None
                    for selector in send_selectors:
                        send_button = page.query_selector(selector)
                        if send_button and send_button.is_visible():
                            break
                    
                    if send_button:
                        print("📤 Sending message...")
                        send_button.click()
                        time.sleep(2)
                        print("✅ Message sent successfully!")
                    else:
                        print("⚠️ Send button not found. Please click send manually in the WhatsApp window.")
                        print("The message has been typed and is ready to send!")

                        # Keep browser open longer for manual sending
                        time.sleep(10)
                else:
                    print("❌ Could not find message input box. Please check if the phone number is valid and has WhatsApp.")

            except Exception as e:
                print(f"Error while sending message: {str(e)}")
                print("💡 The browser window is open. You can try sending the message manually.")
                time.sleep(10)
            
            # Keep browser open for a moment to see result
            time.sleep(3)
            browser.close()
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        print("Make sure you have Playwright installed and configured properly.")
