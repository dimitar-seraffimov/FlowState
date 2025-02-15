from playwright.sync_api import sync_playwright
import time
import json
from urllib.parse import urlparse

def get_tabs_info():
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
                    
                    # Get tab information
                    tab_info = {
                        # Basic info
                        "title": page.title(),
                        "url": url,
                        "domain": parsed_url.netloc,
                        "path": parsed_url.path,
                        "timestamp": time.time(),
                        
                        # Page state
                        "is_loading": page.evaluate("document.readyState !== 'complete'"),
                        
                        # Meta information
                        "meta_description": page.evaluate("document.querySelector('meta[name=\"description\"]')?.content || ''"),
                        "meta_keywords": page.evaluate("document.querySelector('meta[name=\"keywords\"]')?.content || ''"),
                        
                        # Content analysis
                        "word_count": page.evaluate("""
                            document.body.innerText
                            .split(/\s+/)
                            .filter(word => word.length > 0)
                            .length
                        """),
                        
                        # Link analysis
                        "num_links": page.evaluate("document.links.length"),
                        
                        # Time data
                        "time_opened": time.time(),
                        
                        # Tab behavior
                        "has_form": page.evaluate("document.forms.length > 0"),
                        "has_video": page.evaluate("""
                            document.getElementsByTagName('video').length > 0 || 
                            document.getElementsByTagName('iframe').length > 0
                        """),
                        
                        # Page category hints
                        "is_social_media": any(social in url.lower() 
                                             for social in ['facebook', 'twitter', 'linkedin', 'instagram']),
                        "is_email": any(email in url.lower() 
                                      for email in ['mail.google', 'outlook', 'yahoo.com/mail']),
                        "is_docs": any(docs in url.lower() 
                                     for docs in ['docs.google', 'notion.', 'confluence']),
                        
                        # Interaction potential
                        "is_interactive": page.evaluate("""
                            document.querySelectorAll('button, input, textarea, select').length > 0
                        """)
                    }
                    
                    # Get h1 content for better context
                    tab_info["main_heading"] = page.evaluate("""
                        document.querySelector('h1')?.innerText || 
                        document.querySelector('h2')?.innerText || 
                        ''
                    """)
                    
                    tabs_info.append(tab_info)
                    print(f"Successfully collected info for: {tab_info['title']}")
                    
                except Exception as e:
                    print(f"Error collecting tab info: {e}")
            
            return tabs_info 
            
        except Exception as e:
            print(f"Connection error: {e}")
            return []

def analyze_tab_patterns(tabs):
    """Analyze patterns in the collected tab data"""
    patterns = {
        "total_tabs": len(tabs),
        "categories": {
            "social_media": len([tab for tab in tabs if tab["is_social_media"]]),
            "email": len([tab for tab in tabs if tab["is_email"]]),
            "docs": len([tab for tab in tabs if tab["is_docs"]]),
        },
        "interaction_heavy": len([tab for tab in tabs if tab["is_interactive"]]),
        "content_heavy": len([tab for tab in tabs if tab["word_count"] > 500]),
        "video_content": len([tab for tab in tabs if tab["has_video"]]),
        "domains": list(set(tab["domain"] for tab in tabs))
    }
    return patterns

if __name__ == "__main__":
    # while True:
        print("\n--- Checking tabs ---")
        tabs = get_tabs_info()
        if tabs:
            # Analyze patterns
            patterns = analyze_tab_patterns(tabs)
            
            print("\nTab Patterns:")
            print(json.dumps(patterns, indent=2))
            
            print("\nDetailed Tab Info:")
            print(json.dumps(tabs, indent=2))
            
        # time.sleep(5)  # Wait 5 seconds before next check
