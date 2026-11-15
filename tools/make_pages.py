#!/usr/bin/env python3
"""作業用の index.html（本文の断片）から、単体で開ける public/index.html を作る。
使い方: python3 tools/make_pages.py <元の index.html>"""
import sys, pathlib
src = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8")
a = src.index("<style>"); b = src.index("</style>") + len("</style>"); c = src.index("<script>")
doc = f"""<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Winny 伝搬シミュレータ</title>
<meta name="description" content="合成データで、P2P ネットワークへの参加・検索・キャッシュ転送・Port0 の仲介の流れを見せる模擬。実ネットワークには接続しない。">
{src[a:b]}
</head>
<body>
{src[b:c].strip()}
{src[c:].strip()}
</body>
</html>
"""
out = pathlib.Path(__file__).resolve().parent.parent / "public" / "index.html"
out.write_text(doc, encoding="utf-8")
print("wrote", out, len(doc.encode("utf-8")), "bytes")
