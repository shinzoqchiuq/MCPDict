#!/usr/bin/env python3

from tables._表 import 表 as _表
import re

class 表(_表):

	def 析(自, 列):
		名 = 自.簡稱
		字 = ""
		音 = ""
		音標 = ""
		註 = ""
		if 名 in ("汝城", "瑞安東山", "新界客家話", "長壽", "宜章巖泉","郴州","樂昌皈塘","尤溪","晉江", "龍門路溪", "詔安", "道縣官話", "重慶", "樂昌三溪", "南安"):
			字, 音, 註 = 列[:3]
		elif 名 in ("通州金沙",):
			音, 字, 註 = 列[:3]
		elif 名 in ("江陰", "江陰新橋", "江陰申港"):
			_, 字, 註, 音 = 列[:4]
		elif 名 in ("東方八所",):
			_, 字, 聲韻, 調, 註 = 列[:5]
			音 = 聲韻 + 調
		elif 名 in ("龍游", "上猶社溪"):
			_, 字, 聲, 韻, 調值, _, 註 = 列[:7]
			音標 = 聲 + 韻 + 調值
		elif 名 in ("1900梅惠",):
			字,_,_,音 = 列[:4]
		elif 名 in ("劍川金華",):
			字, 聲韻, 調, 註 = 列[:4]
			音 = 聲韻 + 調
		elif 名 in ("樂昌黃圃",):
			字, 調, 聲韻, 註 = 列[:4]
			音 = 聲韻 + 調
			註 = 註.strip("{}")
		elif 名 in ("1926綜合",):
			字,音,_,_,_,註 = 列[:6]
		elif 名 in ("蒼南錢庫",):
			聲,韻,調,字,註 = 列[:5]
			if 調 == "轻声": 調 = "0"
			音 = 聲 + 韻 + 調
		elif 名 in ("1890會城",):
			字,_,_,聲,韻,註 = 列[:6]
			音 = 聲 + 韻
		elif 名 in ("貴陽",):
			字, _, _, 音標, 註 = 列[:6]
		elif 名 in ("樂淸"):
			_, 聲, 韻, 調, 字, 註 = 列[:6]
			音 = 聲 + 韻 + 調
		elif 名 in ("淸末溫州",):
			_,字,聲韻,_,_,調,註 = 列[:7]
			音 = 聲韻 + 調
		elif 名 in ("眞如南",):
			_, _, 字, 註, 聲, 韻, 調 = 列[:7]
			音 = 聲 + 韻 + 調
		#音標
		elif 名 in ("五峯", "恩平恩城","台山台城"):
			字, 音標 = 列[:2]
		elif 名 in ("華安髙安","五華"):
			音標, 字, 註 = 列[:3]
		elif 名 in ("惠來隆江",):
			字, 音標, 註 = 列[:3]
		elif 名 in ("壽寧平溪"):
			字, 音, 註 = 列[:3]
			字 = 字.replace("", "□")
		elif 名 in ("新會會城",):
			字, _, _, 音標 = 列[:4]
		elif 名 in ("1893福安"):
			字, _, 音, 註 = 列[:4]
		elif 名 in ("廈門","漳州","饒平", "遵義", "犍爲玉津", "綦江古南", "桐梓婁山關", "宣平"):
			字, _, 音標, 註 = 列[:4]
		elif 名 in ("遂昌","五華橫陂","蔡家話"):
			字, 聲韻, 調, 註 = 列[:4]
			音標 = 聲韻 + 調
		elif 名 in ("雙牌打鼓坪"):
			聲韻, 調, _, 註 = 列[:4]
			音 = 聲韻 + 調
			字 = 註[0]
			註 = 註[1:].strip("()（）")
		elif 名 in ("開化",):
			字, 註, 聲, 韻, 調 = 列[:5]
			音 = 聲 + 韻 + 調.strip("[]")
			if re.match(r"（.*?）", 註): 註 = 註[1:-1]
		elif 名 in ("富陽東梓關","新登城陽"):
			_, 字, 註, 音標 = 列[:4]
		elif 名 in ("新登下港",):
			字, 音標, 註 = 列[1], 列[6], 列[2]
		elif 名 in ("嘉善", "上海"):
			字, 聲, 韻, 調, 註 = 列[:5]
			音 = 聲 + 韻 + 調
			if 字.endswith("-"):
				字 = 字[:-1]
				音 = 音 + "-"
		elif 名 in ("臨海", "泰順羅陽", "雲和", "仙居"):
			字, _, 聲韻, 調值, 註 = 列[:5]
			音標 = 聲韻 + 調值
		elif 名 in ("松陽",):
			字, _, 聲韻, 調值 = 列[:4]
			音標 = 聲韻 + 調值
		elif 名 in ("珠海唐家",):
			字, 聲, 韻, 調值, 註 = 列[7], 列[12], 列[13], 列[14], 列[18]
			音標 = 聲 + 韻 + 調值
		elif 名 in ("江門",):
			字, 聲, 韻, 調值, jso, 註 = 列[7], 列[25], 列[26], 列[27], 列[11], 列[12]
			音標 = 聲 + 韻 + 調值
			if jso: 註 = jso + "。" + 註
			註 = 註.strip("。")
		elif 名 in ("江門墟頂","江門白沙","江門水南","江門沙仔尾","江門紫萊"):
			字, 聲, 韻, 調, 註 = 列[0], 列[6], 列[7], 列[4], 列[9]
			音 = 聲 + 韻 + 調
		elif 名 in ("江門禮樂","江門潮連"):
			字, 聲, 韻, 調值, 註 = 列[:5]
			音標 = 聲 + 韻 + 調值
		elif 名 in ("瑞安湖嶺",):
			_, 字, 音標, _, 註 = 列[:5]
		elif 名 in ("湖州",):
			字, _, 音標, _, 註 = 列[:5]
		elif 名 in ("武義",):
			_, 字, _, 音標, 註 = 列[:5]
		elif 名 in ("鳳凰-新豐",):
			字, py, _, 音標, 註 = 列[:5]
		elif 名 in ("潮州","汕頭"):
			字, _, _, 音標, 註 = 列[:5]
		elif 名 in ("汕頭市郊"):
			字, _, _, 音標, 註 = 列[:5]
		elif 名 in ("雷州",):
			字, _, _, _, _, 音標 = 列[:6]
			音標 = 音標.replace("˨˨˩", "˨˩")
		elif 名 in ("長泰",):
			_, 聲, 韻, 調值, 字, 註 = 列[:6]
			音標 = 聲 + 韻 + 調值
		elif 名 in ("普寧",):
			字,_,註,聲,韻,調值 = 列[:6]
			音標 = 聲 + 韻 + 調值
		elif 名 in ("中山三鄕",):
			字,聲,韻,調值, _, 註 = 列[:6]
			音標 = 聲 + 韻 + 調值
		elif 名 in ("深圳南頭",):
			字, _, _, _, 音標, 註 = 列[:6]
		elif 名 in ("通東餘東",):
			字, _, _, 聲韻, _, 調值, 註 = 列[:7]
			音標 = 聲韻 + 調值
		elif 名 in ("南寧", "南寧亭子"):
			_, 字, _, 音標, _, 註, c = 列[:7]
			音標 = 音標.replace(" ", "-")
			註 = c + 註
		elif 名 in ("蒼南蒲門",):
			字, 聲韻, 調值, _, _, _, 註 = 列[:7]
			音標 = 聲韻 + 調值
		elif 名 in ("鶴山雅瑤",):
			字, 聲, 韻, 調值, _, _, _, 註 = 列[:8]
			音標 = 聲 + 韻 + 調值
		elif 名 in ("開平護龍",):
			字, 聲, 韻, 調值, 註 = 列[:5]
			音標 = 聲 + 韻 + 調值
		elif 名 in ("揭陽",):
			字, _, _, _, _, 音標, 異讀, 註 = 列[:8]
			音 = 自.轉調類(音標)
			異讀 = 異讀.strip("(读)")
			if 異讀 == "文": 音+="="
			elif 異讀 == "白": 音+="-"
		elif 名 in ("台山斗山墟",):
			if (len(列) < 13): return
			字, 音標, 註 = 列[0], 列[12], 列[13]
		elif 名 in ("新會天湖",):
			字, 聲, 韻, 調值, 註 = 列[0], 列[11], 列[12], 列[13], 列[14]
			音標 = 聲 + 韻 + 調值
		elif 名 in ("鶴山沙坪",):
			字, 聲, jy, 韻, 調值, 註 = 列[0], 列[8], 列[9], 列[10], 列[11], 列[14]
			l = list()
			for i in 韻.split("，"):
				音標 = 聲 + jy + i + 調值
				音 = 自.轉調類(音標)
				l.append((字, 音, 註))
			return l
		elif 名 in ("縉雲",):
			字, _, _, _, _, 註, _, 音標 = 列[:8]
		elif 名 in ("深圳西鄕","深圳沙井"):
			字, _, _, _, _, _, _, 音標, 註 = 列[:9]
		elif 名 in ("新晃凳寨",):
			字,音標,註 = 列[0], 列[9], 列[10]
		elif 名 in ("如東豐利",):
			字,_,聲韻,_,_,_,調,_,_,註 = 列[:10]
			音 = 聲韻 + 調
		elif 名 in ("如東大豫",):
			字,_,_,_,調,註,聲,韻,_ = 列[:9]
			音 = 聲 + 韻 + 調
		elif 名 in ("詔安白葉","詔安霞葛"):
			字, 音, 註 = 列[:3]
			if " " in 音:
				l = list()
				for y,j in zip(音.split(" "), 註.split(" ")):
					l.append((字, y, j))
				return l
		elif 名 in ("1925鹽城"):
			字組, 音, 註 = 列[:3]
			l = list()
			for 字 in 字組.split(" "):
				if len(字) == 2:
					註 = f"（{字}）{註}".strip()
					字 = 字[0]
				elif len(字) > 2:
					註 = f"{字[1:]}{註}".strip()
					字 = 字[0]
				l.append((字, 音, 註))
			return l
		elif 名 in ("陽春河口",):
			字, 聲, 韻, 調, 註 = 列[9], 列[6], 列[7], 列[4].split("\\")[0], 列[10]
			音 = 聲 + 韻 + 調
		elif 名 in ("中山石岐",):
			字, 聲, 韻, 調值, 註 = 列[7], 列[12], 列[13], 列[14], 列[18]
			音標 = 聲 + 韻 + 調值
		elif 名 in ("上饒沙溪",):
			字, 音, _, 註 = 列[:4]
		elif 名 in ("1818漳州",):
			字, 音 = 列[0], 列[4]
		elif 名 in ("榮縣",):
			字,_,_,註,聲,韻,調 = 列[:7]
			if 聲 in "ø": 聲 = ""
			l = list()
			聲韻 = 聲 + 韻
			for 調 in 調.split("或"):
				音 = 自.轉調類(聲韻 + 調)
				l.append((字, 音, 註))
			return l
		elif 名 in ("鄭張",):
			自.爲音 = False
			字 = 列[0]
			註 = 列[16]
			音 = ("%s%s (%s%s切 %s聲 %s%s)"%(列[12], f"/{列[13]}" if 列[13] else "", 列[7],列[8],列[9],列[10],列[11]))
		elif 名 in ("白-沙",):
			自.爲音 = False
			字, 音 = 列[0], 列[4]
		elif 名 in ("中唐",):
			自.爲音 = False
			字, 音, 註 = 列[:3]
		elif 名 in ("中世朝鮮"):
			自.爲音 = False
			字 = 列[0]
			音 = "".join(列[1:4])
		elif 名 in ("溫州",):
			toneValues = {'阳入':8,'阴上':3,'阳平':2,'阴入':7,'阳去':6,'阴平':1,'阴去':5,'阳上':4}
			_,字,_,聲韻,_,_,調,註 = 列[:8]
			音 = 聲韻 + str(toneValues[調])
		elif 名 in ("瑞安陶山",):
			字, 聲, 韻, 調, 註, 備註 = 列[:6]
			調 = 調.strip("[]")
			音 = 聲 + 韻 + 調
			註 = (註 + " " +備註).strip()
		elif 名 in ("宜章梅田",):
			字,聲,韻,調,註 = 列[:5]
			音 = 聲 + 韻 + 調
		elif 名 in ("蒼南宜山",):
			聲,韻,調,字,註 = 列[:5]
			調 = 調.strip("[]")
			音 = 聲 + 韻 + 調
			註 = 註.strip("{}")
		elif 名 in ("南通", ):
			字 = 列[1]
			音 = 列[-6] + 列[-4]
			註 = 列[-7].strip()
			if len(字) > 1 and len(註) == 0:
				註 = 字[1:].strip()
				字 = 字[0]
		elif 名 in ("寧德",):
			字,_,聲韻,調值,註 = 列
			音標 = 聲韻 + 調值.split("|")[0]
		elif 名 in ("江門荷塘(上)","江門荷塘(下)"):
			字, 音標, 註 = 列[:3]
		elif 名 in ("汝城延壽",):
			字, 音, 註 = 列[:3]
		elif 名 in ("建陽連墩",):
			字, 音, 註 = 列[:3]
		elif 名 in ("塔玆語", "海倫","宜興南",):
			字, 聲韻, 調值, 註 = 列[:4]
			音標 = 聲韻 + 調值
		elif 名 in ("虎林", "吳江菀坪","景寧鄭坑","慈谿觀海衛","當塗霍里", "南陵", "南陵湖南街"):
			字, 聲, 韻, 調值, 註 = 列[:5]
			音標 = 聲 + 韻 + 調值
		elif 名 in ("滁州",):
			_, 字, 聲, 韻, 調值, 註 = 列[:6]
			音標 = 聲 + 韻 + 調值
		elif 名 in ("淮南","懷遠","鳳陽","陽新新街","上猶", "南陵仙坊", "武昌", "連州", "連州保安", "連州星子", "連州西岸", "連州豐陽"):
			_, 字, 聲, 韻, 調值, _, 註 = 列[:7]
			音標 = 聲 + 韻 + 調值
			音標 = 音標.lstrip("0")
		elif 自.文件名.startswith("榕江侗"):
			#缝 paŋ[1] {缝补}
			列[0] = 列[0].strip().replace(" /", "/").replace(" [", "[")
			if not 列[0]: return
			果 = 列[0].split(" ", 2)
			if len(果) < 2: return
			if len(果) == 2:
				字, 音 = 果
				註 = ""
			else:
				字, 音, 註 = 果
				註 = 註.strip("{}")
			if "/" in 音:
				l = list()
				for 項 in 音.split("/"):
					l.append((字, 項, 註))
				return l
		elif 自.文件名.startswith("粤西闽语方言字表"):
			if len(列) < 6: return
			字 = 列[0]
			音集 = 列[自.音列]
			if not 音集 or 音集.startswith("—"): return
			_js = 字[1:] if len(字)>1 else ""
			_js = _js.strip("（）")
			字 = 字[0]
			l = list()
			for 音標 in 音集.split("/"):
				音標 = 音標.strip()
				c = ""
				if "（" in 音標:
					n = 音標.index("（")
					c = 音標[n:]
					音標 = 音標[:n]
				音 = 自.轉調類(音標)
				註 = c + _js
				if 註.startswith("（") and 註.endswith("）"):
					註 = 註[1:-1]
				l.append((字, 音, 註))
			return l
		elif 自.文件名.startswith("鄉話"):
			index = 自.音列
			字, 註 = 列[:2]
			音 = "".join(列[index:index+3])
		elif 自.文件名.startswith("东莞20"):
			字 = 列[0]
			音標 = 列[自.音列]
			訓 = 音標.startswith("(")
			音標 = 音標.strip("()")
			l = list()
			for 音 in 音標.split("|"):
				音 = 自.轉調類(音)
				if 訓: 音 += "@"
				l.append((字, 音))
			return l
		elif 自.文件名.startswith("丹陽（雲陽訪仙河陽埤城）"):
			字 = 列[0][0]
			if 字.startswith("["): return
			註 = 列[0][1:].strip("()（）")
			音標 = 列[自.音列]
			if "、" in 音標:
				音標組 = 音標.split("、")
				l = list()
				for 音標 in 音標組:
					音標, 音註 = re.findall(r"^(.*\d+)([^\d]*?)$", 音標)[0]
					音 = 自.轉調類(音標)
					l.append((字, 音, 音註 if 音註 else 註))
				return l
		elif 自.文件名.startswith("广西富川富阳方言21点"):
			if not 列[0]: return
			字 = 列[0][0]
			註 = 列[0][1:].strip("()（）")
			音標 = 列[自.音列]
			if "/" in 音標:
				音標組 = 音標.split("/")
				l = list()
				l.append((字, 自.轉調類(音標組[0]), 註))
				if len(音標組) > 1:
					if "(" in 音標組[1]:
						音標, 註 = re.findall(r"([^()]*)\((.*)\)", 音標組[1])[0]
					else:
						音標 = 音標組[1]
					l.append((字, 自.轉調類(音標), 註))
				return l
		elif len(列) >= 4:
			字, _, 音標, 註 = 列[:4]
		elif len(列) == 2:
			字, 音 = 列[:2]
		else:
			字, 音, 註 = 列[:3]
		if 字:
			if 音標 and not 音:
				音 = 自.轉調類(音標)
			if len(字) != 1 or not 音: return
			音 = 自.正音(音)
			if 字 in "?�": 字 = "□"
			return 字, 音, 註
		return
