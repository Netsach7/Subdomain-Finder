from flask import Flask, render_template, request
import dns.resolver

app = Flask(__name__)

def find_subdomains(domain):
    subdomains = []
    
    # Common subdomains to check
    common_subdomains = [
        "www", "mail", "ftp", "blog", "shop", "admin", "test", "dev", "api"
    ]
    
    # Brute force approach
    for subdomain in common_subdomains:
        full_domain = f"{subdomain}.{domain}"
        try:
            answers = dns.resolver.resolve(full_domain, 'A')
            subdomains.append(full_domain)
        except dns.resolver.NXDOMAIN:
            pass
    
    return subdomains

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        domain = request.form["domain"]
        subdomains = find_subdomains(domain)
        return render_template("result.html", domain=domain, subdomains=subdomains)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
