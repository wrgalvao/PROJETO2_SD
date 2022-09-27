from concurrent.futures import thread
import threading
from flask import Flask, render_template, request
from msilib.schema import Error
from xmlrpc.server import SimpleXMLRPCServer
import mysql.connector
from mysql.connector import Error
import serverHotel
from flask import jsonify
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client


app = Flask(__name__,
            static_url_path='', 
            static_folder='.',
            template_folder='templates')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hotel/<hotel>")
def hotel(hotel):
    ips = {1:"127.0.0.1", 2:"127.0.0.2", 3:"10.147.17.43"}
    ip = ips.get(int(hotel), 1)
    return render_template(f"hotel{hotel}.html", ip=ip)

@app.route("/buscarQuartoDisponivel", methods=["GET"])
def buscarQuarto():
    ip, porta = request.args.get('ip'), request.args.get('porta')
    return str(app.bot.busca(ip, int(porta)))
    #return str([ip,porta])
class ThreadedWeb(threading.Thread):
    """Thread for web"""
    def __init__(self, bot):
        self.bot = bot
        threading.Thread.__init__(self)

    def run(self):
        print("Starting web")
        app.bot=self.bot
        app.run()

class ThreadedBot(threading.Thread):
    """Thread for bot"""
    def __init__(self):
        threading.Thread.__init__(self)
    def busca(self, ip, porta):
        servidor = xmlrpc.client.ServerProxy("http://{0}:{1}/".format(ip, porta))
        quantidadeDisponivel = servidor.buscarQuartoDisponivel()
        return quantidadeDisponivel

    def run(self):
        print("Starting bot")
        serverHotel.iniciarRPC()

bot = ThreadedBot()
web = ThreadedWeb(bot)

bot.start()
web.start()



