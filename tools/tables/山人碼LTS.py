#!/usr/bin/env python3

from tables._表 import 表 as _表

class 表(_表):
	_file = "ShanRenMaLTS.words.dict.yaml"
	簡稱 = "山人"
	說明 = "來源：https://github.com/siuze/ShanRenMaLTS"
	patches = {"□": "ak,akv"}

	def 析(自, 列):
		if len(列) < 2: return
		return 列[0], 列[1]
