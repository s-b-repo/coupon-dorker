import os
from googlesearch import search
import time

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/91.0.864.54",
    "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36",
]

def banner():
    print("""
  ██████╗  ██████╗ ██████╗ ██╗  ██╗███╗   ██╗███████╗
  ██╔══██╗██╔═══██╗██╔══██╗██║ ██╔╝████╗  ██║██╔════╝
  ██████╔╝██║   ██║██████╔╝█████╔╝ ██╔██╗ ██║███████╗
  ██╔═══╝ ██║   ██║██╔═══╝ ██╔═██╗ ██║╚██╗██║╚════██║
  ██║     ╚██████╔╝██║     ██║  ██╗██║ ╚████║███████║
  ╚═╝      ╚═════╝ ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝
     Coupon Dorking Tool - Use Responsibly!
    """)

def generate_dorks(filename="dorks.txt"):
    dorks = [

    # General coupon dorks
    "site:example.com inurl:coupon",
    "site:retailmenot.com inurl:discount",
    "site:groupon.com filetype:pdf",
    "intitle:\"coupon codes\" site:*.edu",
    "intitle:\"promo codes\" site:*.gov",
    "site:twitter.com inurl:\"coupon\"",
    "site:pastebin.com \"coupon code\"",
    "\"valid coupon code\" filetype:txt",
    "\"discount codes\" filetype:csv",
    "site:facebook.com inurl:\"coupon\"",
    "site:reddit.com \"coupon code\"",
    "\"active promo codes\" filetype:docx",
    "site:instagram.com \"promo code\"",
    "site:medium.com \"discount coupon\"",
    "\"recently added coupons\" site:*.com",

    # File type-specific searches
    "\"coupon code\" filetype:xls",
    "\"promo code\" filetype:doc",
    "\"discount codes\" filetype:json",
    "\"valid coupons\" filetype:yaml",
    "\"discounts list\" filetype:xml",
    "site:dropbox.com inurl:\"coupon\" filetype:txt",
    "site:drive.google.com \"coupon codes\" filetype:pdf",
    "site:docs.google.com \"active discounts\" filetype:docx",

    # Social media platforms
    "site:linkedin.com \"discount promo\"",
    "site:pinterest.com \"coupon offers\"",
    "site:youtube.com \"promo code\" intext:\"description\"",
    "site:tumblr.com inurl:\"coupon\"",
    "site:quora.com \"active promo code\"",
    "site:vk.com \"coupon code\"",
    "site:telegram.me \"promo code\"",
    "site:discord.com \"discount\"",
    "site:github.com \"coupon list\"",
    "site:gitlab.com \"promo codes\"",

    # E-commerce and marketplaces
    "site:ebay.com \"promo code\"",
    "site:amazon.com \"coupon\"",
    "site:walmart.com \"discount\"",
    "site:bestbuy.com \"promo code\"",
    "site:target.com \"coupon\"",
    "site:alibaba.com \"discount codes\"",
    "site:etsy.com \"coupon offers\"",
    "site:rakuten.com \"promo code\"",
    "site:shopify.com \"discount coupons\"",

    # Educational and institutional
    "site:*.edu \"student discount\"",
    "site:*.edu intext:\"coupon\"",
    "site:*.gov \"discount programs\"",
    "site:*.gov intext:\"active promo codes\"",

    # Generic keyword searches
    "\"discount codes for online shopping\"",
    "\"promo code for checkout\"",
    "\"coupon codes 2024\"",
    "\"valid promo codes 2024\"",
    "\"discount offers on electronics\"",
    "\"active discounts\" site:*.org",
    "\"exclusive promo codes\"",
    "\"best discount coupons\"",
    "\"recently verified promo codes\"",
    "\"deal of the day promo codes\"",
    "\"weekly discount offers\"",

    # File hosting and sharing sites
    "site:mediafire.com inurl:\"coupon\"",
    "site:4shared.com \"promo code\"",
    "site:mega.nz \"discount codes\"",
    "site:onedrive.live.com intext:\"coupon list\"",
    "site:we.tl \"promo codes\"",

    # Coupon-specific sites
    "site:slickdeals.net inurl:\"coupon\"",
    "site:couponfollow.com \"promo code\"",
    "site:coupons.com inurl:\"discount\"",
    "site:savings.com \"active promo code\"",
    "site:couponcabin.com inurl:\"coupons\"",
    "site:offers.com \"promo code\"",
    "site:dealsea.com intext:\"discount\"",
    "site:dealnews.com \"coupon offers\"",
    "site:promocodes.com \"active coupons\"",
    "site:groupon.com \"daily deals\"",

    # Expanding keywords and platforms
    "\"promo code generator\"",
    "\"exclusive discounts\"",
    "\"limited time offers\"",
    "\"online shopping deals\"",
    "\"flash sale coupon codes\"",
    "\"clearance sale promo codes\"",
    "\"early bird discounts\"",
    "\"top-rated discounts\"",
    "\"most popular promo codes\"",
    "\"new user promo codes\"",
    "\"first order discounts\"",
    "\"subscription coupon codes\"",

    # Miscellaneous sites
    "site:tripadvisor.com \"discount offers\"",
    "site:booking.com \"promo code\"",
    "site:airbnb.com \"coupon\"",
    "site:expedia.com \"discounts\"",
    "site:hotels.com \"promo codes\"",
    "site:ubereats.com \"coupon offers\"",
    "site:doordash.com \"discounts\"",
    "site:grubhub.com \"promo codes\"",
    "site:netflix.com \"coupon\"",
    "site:spotify.com \"discount\"",
    "site:hulu.com \"promo code\"",
    ]
    with open(filename, "w") as file:
        file.write("\n".join(dorks))
    print(f"[+] Dorks generated and saved to {filename}")

def load_dorks(filename="dorks.txt"):
    if not os.path.exists(filename):
        print(f"[-] Dorks file {filename} not found. Generating default dorks...")
        generate_dorks(filename)
    with open(filename, "r") as file:
        dorks = [line.strip() for line in file if line.strip()]
    print(f"[+] Loaded {len(dorks)} dorks from {filename}")
    return dorks



def perform_dorking(dorks, stop_results):
    results = {}
    for dork in dorks:
        print(f"\n[+] Searching for: {dork}")
        dork_results = []
        try:
            user_agent = random.choice(USER_AGENTS)
            for result in search(dork, stop=stop_results, lang="en", user_agent=user_agent):
                print(f" - {result}")
                dork_results.append(result)
                time.sleep(2)  # Add a delay of 2 seconds between queries
        except Exception as e:
            print(f"Error searching with dork: {dork}. Error: {e}")
        results[dork] = dork_results
    return results


def save_results(results, filename="coupon_dorks_results.txt"):
    with open(filename, "w") as file:
        for dork, urls in results.items():
            file.write(f"Dork: {dork}\n")
            for url in urls:
                file.write(f"{url}\n")
            file.write("\n")
    print(f"\n[+] Results saved to {filename}")

def main():
    banner()
    dorks_file = input("Enter the dorks filename (default: dorks.txt): ").strip() or "dorks.txt"
    dorks = load_dorks(dorks_file)
    stop_results = int(input("Enter the number of results to retrieve per dork: "))
    results = perform_dorking(dorks, stop_results)
    save_results(results)

if __name__ == "__main__":
    main()
