"""praproses.py: Rangkaian praproses SIMUTEH (dipakai ulang mulai P5)."""
import json
import cv2
import numpy as np

PARAM_BAWAAN = {
    "lebar": 640,          # Sampling: lebar citra kerja (piksel)
    "gamma": 1.0,          # < 1 mencerahkan, > 1 menggelapkan
    "clahe_clip": 2.0,     # 0 berarti CLAHE tidak dipakai
    "clahe_tile": 8,       # Ukuran ubin CLAHE (8x8)
    "penapis": "median",   # "none", "rerata", "gaussian", "median"
    "kernel": 3,           # Ukuran kernel penapis derau
    "sigma": 1.0,          # Sigma penapis Gaussian
    "tajam_k": 0.0,        # 0 berarti tanpa penajaman
}

def praproses(img_bgr, p=None):
    """Urutan: ubah ukuran -> gamma -> CLAHE kanal V -> redam derau -> tajamkan."""
    p = {**PARAM_BAWAAN, **(p or {})}

    # TODO 1: Ubah ukuran agar lebar = p["lebar"], rasio aspek tetap
    h, w = img_bgr.shape[:2]
    lebar_baru = p["lebar"]
    tinggi_baru = int(h * (lebar_baru / w))
    img = cv2.resize(img_bgr, (lebar_baru, tinggi_baru), interpolation=cv2.INTER_AREA)

    # TODO 2: Bila p["gamma"] != 1, terapkan koreksi gamma dengan cv2.LUT
    if p["gamma"] != 1.0:
        lut = np.array([255 * ((i / 255.0) ** p["gamma"]) for i in range(256)]).clip(0, 255).astype(np.uint8)
        img = cv2.LUT(img, lut)

    # TODO 3: Bila p["clahe_clip"] > 0, ubah ke HSV, terapkan CLAHE pada kanal V saja, lalu kembalikan ke BGR
    if p["clahe_clip"] > 0:
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        clahe = cv2.createCLAHE(clipLimit=p["clahe_clip"], tileGridSize=(p["clahe_tile"], p["clahe_tile"]))
        hsv[:, :, 2] = clahe.apply(hsv[:, :, 2])
        img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    # TODO 4: Redam derau sesuai p["penapis"], p["kernel"], p["sigma"]
    penapis = p["penapis"]
    k = p["kernel"]
    if penapis == "rerata":
        img = cv2.blur(img, (k, k))
    elif penapis == "gaussian":
        img = cv2.GaussianBlur(img, (k, k), p["sigma"])
    elif penapis == "median":
        img = cv2.medianBlur(img, k)

    # TODO 5: Bila p["tajam_k"] > 0, lakukan unsharp masking
    if p["tajam_k"] > 0:
        blur = cv2.GaussianBlur(img, (5, 5), 1.0)
        img = cv2.addWeighted(img, 1.0 + p["tajam_k"], blur, -p["tajam_k"], 0)

    return img

def simpan_param(p, path="hasil/param_praproses.json"):
    with open(path, "w") as f:
        json.dump({**PARAM_BAWAAN, **p}, f, indent=2)
