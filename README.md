# TokenizeJW300
JW300の日本語コーパスをSpacyでTokenizeして固有語抽出とかする

必要なの
+ neologdn
+ spacy
+ ja_ginza
+  python -m spacy download en_core_web_sm          

JW300はこんな感じなのが入っている
> その ​ 後 ， 国 ​ が ​ 立て ​ た ​ 捕食 ​ 動物 ​ 抑制 ​ 計画 ​ に ​ より ， 1955 ​ 年 ​ から ​ 1964 ​ 年 ​ の ​ 間 ​ に ​ さらに ​ 2 万 7,646 ​ 匹 ​ の ​ コヨテ ​ が ​ 殺さ ​ れ ​ まし ​ た。

> Thereafter a federal predator - control program brought death to an additional 27,646 red wolves between 1955 and 1964.
