# Phishing URL Detector

A lightweight machine-learning inspired Phishing URL Detector built in Python + Flask. It scores a URL based on suspicious features and flags it as SAFE or PHISHING in real-time via a web interface.

Built entirely on Android using Termux.

## Demo

- `google.com` -> SAFE - Legit (Score: 0)
- `safaricom.co.ke` -> SAFE - Legit (Score: 0)
- `safaricom-free.xyz` -> PHISHING - DANGER (Score: 7+)
- `http://paypal-login-secure-verify.xyz/login` -> PHISHING - DANGER (Score: 10+)

## How It Works


The detector in `train.py` extracts features from a URL and gives a risk score:

| Feature | Points | Why It's Suspicious |
| :--- | :--- | :--- |
| URL Length > 75 chars | +2 | Phishers hide real domain |
| Many dots / subdomains | +2 | e.g. `paypal.com.secure.xyz` |
| Uses IP address | +4 | e.g. `http://192.168.1.1/login` |
| Many hyphens | +2 | e.g. `safaricom-free-bonus` |
| Suspicious words | +3 | `login`, `verify`, `secure`, `free`, `bonus`, `update` |
| Free / risky TLD | +3 | `.xyz`, `.top`, `.tk`, `.ml`, `.ga` |
| No HTTPS | +1 | Legit sites use HTTPS |
| `@` symbol in URL | +3 | Hides real destination |

**Decision Rule:**
- Score < 5 = SAFE - Legit
- Score >= 5 = PHISHING - DANGER

## Tech Stack

- Python 3
- Flask (Web App)
- HTML / CSS (Frontend)
- Termux (Android Development)

## Project Structure
phishing-url-detector/
├── train.py      # Scoring logic + feature extraction
├── app.py        # Flask web server
├── model.json    # Saved model / thresholds
└── README.md     # Documentation
## How to Run

pip install flask
python train.py
python app.py
# Open http://localhost:5000

## Future Improvements
- Train on real PhishTank dataset
- Add WHOIS / Domain Age check
- Add ML model (Random Forest)
- Deploy on Render / Railway
