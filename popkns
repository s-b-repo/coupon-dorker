import os
from googlesearch import search

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
        "\"recently added coupons\" site:*.com"
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

def perform_dorking(dorks, num_results):
    results = {}
    for dork in dorks:
        print(f"\n[+] Searching for: {dork}")
        dork_results = []
        try:
            for result in search(dork, num_results=num_results, stop=num_results, lang="en"):
                print(f" - {result}")
                dork_results.append(result)
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
    num_results = int(input("Enter the number of results to retrieve per dork: "))
    results = perform_dorking(dorks, num_results)
    save_results(results)

if __name__ == "__main__":
    main()
