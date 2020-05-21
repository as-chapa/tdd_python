[ ] 12章：インスタンス化した場合に、別のメモリ空間に振られるので、assertEqualsが動作しないことが多かった
[x] 13章：Pythonは型がないので、キャスト系が軒並み不要
[x] 13章：Cast的な意図で `sum: Sum = result: Sum` のように書くと構文エラーとなる
[ ] 13章：P.92、SumにExpressionを実装しなくても動いた
[x] 13章：コンストラクタを定義しないと、的なのはdataclassで解決されるなぁ
[ ] 13章：P.93、sourceをキャストしなくても動く、typeでsourceを見たらsum型だった。Pythonにおける
Expressionのimplementsの意味
[ ] 13章：P.93「どんなExpressionであれ動作すべき」とあるが、Expressionをimplementsするクラスにはreduceを要求するように実装する？Pythonでそこまで強く継承関係作れるんだっけ？
[ ] 13章：P.96、メソッドの可視性云々のくだりはPythonだと関係なさそう
[ ] 14章：P.107、pair.pyの定義をdataclassにしたら__eq__と_、__hash__が意図通りに動いたが、そうじゃないと辞書をメモリ番地で聞きにいき、KeyErrorとなった
[x] 15章：P.117、型の強制度がないから、Expressionにplusメソッドがなくてもエラーにならない
[ ] 15章：P.118、Sumにplusが実装されてなくてもエラーになっていない
[ ] 16章：P.127、test_plus_same_currency_returns_moneyは通らない、そりゃSum返しているから当然だ