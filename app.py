from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Ortak cevap fonksiyonları
def api_response(data=None, status=200):
    return jsonify({
        "developer": "@ffnyxff",
        "data": data
    }), status

def api_error():
    return jsonify({
        "developer": "@ffnyxff",
        "error": "API hatası"
    }), 500

# 1️⃣ Ad Soyad
@app.route("/api/adsoyad", methods=["GET"])
def api_adsoyad():
    ad = request.args.get("ad", "")
    soyad = request.args.get("soyad", "")
    il = request.args.get("il", "")
    ilce = request.args.get("ilçe", "")

    params = {"ad": ad, "soyad": soyad, "il": il, "ilçe": ilce}
    url = "https://croos.rf.gd/Api/adsoyad.php"

    try:
        res = requests.get(url, params=params, timeout=10)
        res.raise_for_status()
        return api_response(res.json())
    except Exception:
        return api_error()

# 2️⃣ TC
@app.route("/api/tc", methods=["GET"])
def api_tc():
    tc = request.args.get("tc", "")
    if not tc:
        return api_response({"message": "tc parametresi gereklidir"}, 400)
    url = "https://croos.rf.gd/Api/tc.php"
    try:
        res = requests.get(url, params={"tc": tc}, timeout=10)
        res.raise_for_status()
        return api_response(res.json())
    except Exception:
        return api_error()

# 3️⃣ Aile
@app.route("/api/aile", methods=["GET"])
def api_aile():
    tc = request.args.get("tc", "")
    if not tc:
        return api_response({"message": "tc parametresi gereklidir"}, 400)
    url = "https://croos.rf.gd/Apiaile.php"
    try:
        res = requests.get(url, params={"tc": tc}, timeout=10)
        res.raise_for_status()
        return api_response(res.json())
    except Exception:
        return api_error()

# 4️⃣ TC GSM
@app.route("/api/tcgsm", methods=["GET"])
def api_tcgsm():
    tc = request.args.get("tc", "")
    if not tc:
        return api_response({"message": "tc parametresi gereklidir"}, 400)
    url = "https://croos.rf.gd/Api/tcgsm.php"
    try:
        res = requests.get(url, params={"tc": tc}, timeout=10)
        res.raise_for_status()
        return api_response(res.json())
    except Exception:
        return api_error()

# 5️⃣ GSM TC
@app.route("/api/gsmtc", methods=["GET"])
def api_gsmtc():
    gsm = request.args.get("gsm", "")
    if not gsm:
        return api_response({"message": "gsm parametresi gereklidir"}, 400)
    url = "https://croos.rf.gd/Api/gsmtc.php"
    try:
        res = requests.get(url, params={"gsm": gsm}, timeout=10)
        res.raise_for_status()
        return api_response(res.json())
    except Exception:
        return api_error()

# 6️⃣ Adres
@app.route("/api/adres", methods=["GET"])
def api_adres():
    tc = request.args.get("tc", "")
    if not tc:
        return api_response({"message": "tc parametresi gereklidir"}, 400)
    url = "https://croos.rf.gd/Api/adres.php"
    try:
        res = requests.get(url, params={"tc": tc}, timeout=10)
        res.raise_for_status()
        return api_response(res.json())
    except Exception:
        return api_error()

# 7️⃣ Adres No
@app.route("/api/adresno", methods=["GET"])
def api_adresno():
    adres_no = request.args.get("adresNo", "")
    if not adres_no:
        return api_response({"message": "adresNo parametresi gereklidir"}, 400)
    url = "https://croos.rf.gd/Api/adresno.php"
    try:
        res = requests.get(url, params={"adresNo": adres_no}, timeout=10)
        res.raise_for_status()
        return api_response(res.json())
    except Exception:
        return api_error()

# 8️⃣ Anasayfa testi
@app.route("/", methods=["GET"])
def home():
    return api_response({"message": "API Servisi Çalışıyor"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
