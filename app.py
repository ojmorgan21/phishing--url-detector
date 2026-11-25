from flask import Flask, request, render_template_string
import train

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>PhishGuard - Phishing URL Detector</title>
<style>
*{box-sizing:border-box;font-family:Inter,system-ui,-apple-system,sans-serif}
body{margin:0;background:#070b14;color:#eef2ff;min-height:100vh}
.top{max-width:900px;margin:0 auto;padding:24px 18px 0;display:flex;justify-content:space-between;align-items:center}
.logo{font-weight:800;font-size:20px;letter-spacing:-.5px}
.logo span{color:#22c55e}
.badge{font-size:12px;background:#111c33;border:1px solid #26345c;padding:6px 10px;border-radius:999px;color:#a5b4fc}
.hero{max-width:900px;margin:0 auto;padding:28px 18px;text-align:center}
.hero h1{font-size:38px;line-height:1.05;margin:10px 0;letter-spacing:-1px}
.hero h1 i{color:#38bdf8;font-style:normal}
.hero p{color:#94a3b8;font-size:16px;line-height:1.6;max-width:600px;margin:0 auto}
.card{max-width:720px;margin:22px auto;background:#0f172a;border:1px solid #1e293b;border-radius:20px;padding:18px;box-shadow:0 20px 60px rgba(0,0,0,.4)}
.form{display:flex;gap:10px}
input{flex:1;background:#020617;border:1px solid #334155;color:white;padding:15px 16px;border-radius:12px;font-size:15px;outline:none}
input:focus{border-color:#38bdf8}
button{background:#22c55e;color:#04120a;border:0;padding:0 22px;border-radius:12px;font-weight:800;font-size:15px;cursor:pointer}
.examples{display:flex;gap:8px;flex-wrap:wrap;justify-content:center;margin-top:14px}
.examples button{background:#1e293b;color:#cbd5e1;font-weight:500;padding:7px 12px;font-size:13px}
.result{margin-top:16px;border-radius:14px;padding:18px;text-align:left}
.safe{background:#052e16;border:1px solid #16a34a}
.danger{background:#450a0a;border:1px solid #ef4444}
.result h2{margin:0;font-size:22px}
.result p{margin:8px 0 0;color:#e2e8f0;line-height:1.5}
.meter{height:8px;background:rgba(255,255,255,.2);border-radius:999px;margin-top:12px;overflow:hidden}
.fill{height:100%;background:white;border-radius:999px}
.grid{max-width:900px;margin:10px auto 30px;padding:0 18px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px}
.box{background:#0f172a;border:1px solid #1e293b;border-radius:16px;padding:16px}
.box b{display:block;margin-bottom:6px}
.box span{color:#94a3b8;font-size:13px;line-height:1.5;display:block}
.footer{text-align:center;color:#64748b;font-size:12px;padding-bottom:30px}
@media(max-width:650px){.hero h1{font
