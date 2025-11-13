You're absolutely right. I apologize for the incorrect instructions. Let me read the actual script carefully and create an accurate README.

# Salty - CSS Text Salting Framework

## Overview

Salty is an interactive framework for hiding JavaScript payloads within seemingly innocent text using CSS obfuscation techniques. The tool creates HTML documents where malicious JavaScript is concealed using various CSS hiding methods, making detection difficult for security scanners.

## Features

- 6 CSS evasion techniques for hiding text
- Interactive menu-driven interface
- Multiple JavaScript payload types
- Automatic payload recovery and execution
- Save and load payload configurations
- Generate email-ready HTML content

## Installation

```bash
git clone https://github.com/ekomsSavior/salty.git
cd salty
python3 salty.py
```

## Usage

Run the tool and follow the interactive menu:

```bash
python3 salty.py
```

### Menu Options

1. **Create JavaScript Payload** - Build a new payload with the following types:
   - JS Redirect: Redirects to a specified URL after a delay
   - Data Exfiltration: Steals cookies, user agent, forms, and links
   - C2 Beacon: Establishes periodic callbacks to a C2 server
   - Info Stealer: Collects comprehensive system information
   - DOM Scraper: Extracts page content and form data

2. **Generate Salted Email/Document** - Create HTML content with hidden payload:
   - Select from created payloads
   - Choose CSS hiding technique
   - Set email subject and visible body text
   - Outputs to timestamped HTML file

3. **Preview Detection Evasion** - View how CSS evasion techniques work

4. **Save Payload** - Export payload configurations to JSON

5. **Load Payload** - Import previously saved payloads

6. **Show Created Payloads** - List all currently loaded payloads

7. **Test Delivery Methods** - Review delivery options

## CSS Evasion Techniques

- **display_none**: Uses `display: none !important`
- **visibility_hidden**: Uses `visibility: hidden !important` 
- **text_indent**: Uses `text-indent: -9999px; overflow: hidden`
- **opacity_zero**: Uses `opacity: 0 !important`
- **font_size_zero**: Uses `font-size: 0px !important`
- **zero_width**: Uses zero-width spaces and absolute positioning

## How It Works

1. JavaScript payloads are Base64 encoded
2. Encoded payload is split into chunks
3. Each chunk is hidden using CSS techniques
4. Hidden chunks are surrounded by random visible text
5. Recovery JavaScript automatically finds and executes the reassembled payload

## Output

The tool generates HTML files containing:
- Legitimate-looking visible content
- CSS-hidden payload chunks distributed throughout the document
- Automatic recovery script that executes on page load

## Legal Notice

FOR AUTHORIZED SECURITY TESTING ONLY

This tool is intended for:
- Red team exercises and penetration testing
- Security research and education
- Testing defensive controls and detection capabilities

Use only on systems you own or have explicit permission to test. Comply with all applicable laws and regulations.

![Screenshot 2025-10-14 111008](https://github.com/user-attachments/assets/96fea3f5-289c-4ff2-b2c5-575e564f9be9)
