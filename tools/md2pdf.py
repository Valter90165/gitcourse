#!/usr/bin/env python3
"""Converte una dispensa markdown in PDF impaginato (Chromium headless)."""
import sys, subprocess, pathlib, markdown, re

CSS = """
body{font-family:'Liberation Serif',Georgia,serif;font-size:10.5pt;line-height:1.45;color:#111;}
h1{font-size:19pt;border-bottom:2px solid #333;padding-bottom:4pt;margin-top:22pt;page-break-after:avoid;}
h2{font-size:14pt;margin-top:16pt;color:#1a1a1a;page-break-after:avoid;}
h3{font-size:12pt;margin-top:12pt;color:#333;page-break-after:avoid;}
table{border-collapse:collapse;width:100%;margin:9pt 0;font-size:9.5pt;page-break-inside:avoid;}
th,td{border:1px solid #999;padding:4pt 6pt;text-align:left;vertical-align:top;}
th{background:#ececec;font-weight:bold;}
blockquote{border-left:3px solid #777;margin-left:0;padding:5pt 0 5pt 12pt;background:#f7f7f7;}
blockquote p{margin:4pt 0;}
code{font-family:'Liberation Mono',monospace;font-size:9pt;background:#f0f0f0;padding:1pt 3pt;}
pre{background:#f4f4f4;padding:7pt;border-left:3px solid #888;font-size:9pt;}
li{margin-bottom:2.5pt;}
hr{border:none;border-top:1px solid #bbb;margin:16pt 0;}
@page{margin:18mm 16mm;}
"""

def build(md_path):
    md_path = pathlib.Path(md_path)
    src = md_path.read_text()
    title = re.search(r'^#\s+(.+)$', src, re.M)
    title = title.group(1).strip() if title else md_path.stem
    body = markdown.markdown(src, extensions=["tables","fenced_code","sane_lists"])
    html = f"<!DOCTYPE html><html lang='it'><head><meta charset='utf-8'><title>{title}</title><style>{CSS}</style></head><body>{body}</body></html>"
    tmp = pathlib.Path("/tmp/claude-0/-home-user-gitcourse/312953b9-762a-5be5-9108-1acce4effb62/scratchpad")
    tmp.mkdir(parents=True, exist_ok=True)
    hf = tmp / (md_path.stem + ".html")
    hf.write_text(html)
    pdf = md_path.with_suffix(".pdf")
    subprocess.run(["/opt/pw-browsers/chromium-1194/chrome-linux/chrome","--headless","--disable-gpu",
                    "--no-sandbox","--no-pdf-header-footer",f"--print-to-pdf={pdf}",f"file://{hf}"],
                   capture_output=True)
    n = pdf.read_bytes().count(b"/Type /Page") or pdf.read_bytes().count(b"/Type/Page")
    print(f"{pdf.name}: {pdf.stat().st_size//1024} KB, ~{n} pagine, {len(body)} car. HTML, {body.count('<table>')} tabelle")

for a in sys.argv[1:]: build(a)
