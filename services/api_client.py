import requests

BASE_URL = "https://rct-backend-908a.onrender.com/rct"  # replace with Render/Prod URL

# ---- Documents ----
def upload_document(file):
    url = f"{BASE_URL}/documents/upload"
    files = {"file": (file.name, file, file.type)}
    try:
        r = requests.post(url, files=files)
        if r.status_code == 200:
            return {"success": True, **r.json()}
        return {"success": False, "error": r.text}
    except Exception as e:
        return {"success": False, "error": str(e)}

def get_documents():
    try:
        r = requests.get(f"{BASE_URL}/documents")
        if r.status_code == 200:
            return r.json().get("files", [])
        return []
    except:
        return []

# ---- Requirements ----
def extract_requirements(doc_id: int):
    try:
        r = requests.post(f"{BASE_URL}/requirements/extract/{doc_id}")
        if r.status_code == 200:
            return {"success": True, **r.json()}
        return {"success": False, "error": r.text}
    except Exception as e:
        return {"success": False, "error": str(e)}

def get_requirements(doc_id: int):
    try:
        r = requests.get(f"{BASE_URL}/requirements/{doc_id}")
        if r.status_code == 200:
            return r.json().get("requirements", [])
        return []
    except:
        return []

# ---- User Stories ----
def generate_userstories(doc_id: int):
    try:
        r = requests.post(f"{BASE_URL}/requirements/{doc_id}/generate_userstories")
        if r.status_code == 200:
            return {"success": True, **r.json()}
        return {"success": False, "error": r.text}
    except Exception as e:
        return {"success": False, "error": str(e)}

def get_userstories(doc_id: int):
    try:
        r = requests.get(f"{BASE_URL}/userstories/{doc_id}")
        if r.status_code == 200:
            return r.json().get("userstories", [])
        return []
    except:
        return []

# ---- Reports ----
def generate_report(doc_id: int):
    try:
        r = requests.post(f"{BASE_URL}/reports/generate/{doc_id}")
        if r.status_code == 200:
            return {"success": True, **r.json()}
        return {"success": False, "error": r.text}
    except Exception as e:
        return {"success": False, "error": str(e)}

def download_report(report_id: str, fmt: str):
    try:
        r = requests.get(f"{BASE_URL}/reports/{report_id}/download?format={fmt}")
        if r.status_code == 200:
            return r.content
        return None
    except:
        return None

# ---- Audit Logs ----
def get_audit_logs():
    try:
        r = requests.get(f"{BASE_URL}/audit/logs")
        if r.status_code == 200:
            return r.json().get("logs", [])
        return []
    except:
        return []
