
from playwright.sync_api import sync_playwright
import time
import json
from urllib.parse import urlparse


def get_basic_tab_info():
    """Collect basic information about open tabs"""
    with sync_playwright() as p:
        try:
            print("Connecting to Chrome...")
            browser = p.chromium.connect_over_cdp("http://localhost:9222")
            context = browser.contexts[0]
            pages = context.pages
            
            tabs_info = []
            for page in pages:
                try:
                    url = page.url
                    parsed_url = urlparse(url)
                    
                    # Only collect essential info
                    tab_info = {
                        "title": page.title(),
                        "url": url,
                        "domain": parsed_url.netloc,
                        "timestamp": time.time()
                    }
                    
                    tabs_info.append(tab_info)
                    print(f"Collected basic info for: {tab_info['title']}")
                    
                except Exception as e:
                    print(f"Error collecting basic tab info: {e}")
            
            return tabs_info
            
        except Exception as e:
            print(f"Connection error: {e}")
            return []

def analyze_tab_content(page):
    """Detailed content analysis of a single tab"""
    return {
        "meta_description": page.evaluate("document.querySelector('meta[name=\"description\"]')?.content || ''"),
        "meta_keywords": page.evaluate("document.querySelector('meta[name=\"keywords\"]')?.content || ''"),
        "word_count": page.evaluate("""
            document.body.innerText
            .split(/\s+/)
            .filter(word => word.length > 0)
            .length
        """),
        "num_links": page.evaluate("document.links.length"),
        "main_heading": page.evaluate("""
            document.querySelector('h1')?.innerText || 
            document.querySelector('h2')?.innerText || 
            ''
        """)
    }

def analyze_tab_behavior(page):
    """Analyze interactive elements and behavior indicators"""
    return {
        "has_form": page.evaluate("document.forms.length > 0"),
        "has_video": page.evaluate("""
            document.getElementsByTagName('video').length > 0 || 
            document.getElementsByTagName('iframe').length > 0
        """),
        "is_interactive": page.evaluate("""
            document.querySelectorAll('button, input, textarea, select').length > 0
        """)
    }

def categorize_tab(url):
    """Categorize tab based on URL patterns"""
    url_lower = url.lower()
    return {
        "is_social_media": any(social in url_lower 
                             for social in ['facebook', 'twitter', 'linkedin', 'instagram']),
        "is_email": any(email in url_lower 
                      for email in ['mail.google', 'outlook', 'yahoo.com/mail']),
        "is_docs": any(docs in url_lower 
                     for docs in ['docs.google', 'notion.', 'confluence']),
        "is_chat": any(chat in url_lower
                      for chat in ['slack.com', 'discord.com', 'teams.microsoft']),
        "is_dev": any(dev in url_lower
                     for dev in ['github.com', 'stackoverflow.com', 'gitlab.com'])
    }

def analyze_tab_patterns(tabs):
    """Analyze patterns across all tabs"""
    patterns = {
        "total_tabs": len(tabs),
        "domains": list(set(tab["domain"] for tab in tabs)),
        "domain_count": {},
        "timestamp_range": {
            "oldest": min(tab["timestamp"] for tab in tabs),
            "newest": max(tab["timestamp"] for tab in tabs)
        }
    }
    
    # Count domains
    for tab in tabs:
        domain = tab["domain"]
        patterns["domain_count"][domain] = patterns["domain_count"].get(domain, 0) + 1
    
    return patterns

if __name__ == "__main__":
    while True:
        print("\n--- Checking tabs ---")
        tabs = get_basic_tab_info()
        
        if tabs:
            # Basic pattern analysis
            patterns = analyze_tab_patterns(tabs)
            print("\nBasic Tab Patterns:")
            print(json.dumps(patterns, indent=2))
            
            ## Optional: Get categories for each tab
            #for tab in tabs:
            #    tab["categories"] = categorize_tab(tab["url"])
            
            print("\nTabs without categories:")
            print(json.dumps(tabs, indent=2))
            
        time.sleep(5)   