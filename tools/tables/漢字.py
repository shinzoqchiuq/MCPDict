#!/usr/bin/env python3

from tables._表 import 表 as _表
import re

def get_note():
	說明 = open("../README.md", encoding="U8").read()
	說明 = re.sub(r"^#.*$", "", 說明, flags=re.M).strip()
	說明 = re.sub(r"\[(.*?)\]\((.*?)\)", "<a href=\\2>\\1</a>", 說明)
	說明 = re.sub(r"^- (.+)$", "<li>\\1</li>", 說明, flags=re.M)
	說明 = 說明.replace("</li>\n", "</li>")
	說明 = re.sub(r"(<li>.+</li>)", "<ul>\\1</ul>", 說明)
	return 說明

class 表(_表):
	顏色 = "#9D261D"
	網站 = "漢字音典在線版"
	網址 = "https://mcpdict.sourceforge.io/cgi-bin/search.py?字=%s"
	說明 = get_note()

	def 讀(自):
		return dict()
