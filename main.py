import random
from js import setTimeout, document

# 定数宣言
GAME_TURNS=30
INTERVAL=1000  # モグラの出現間隔（ミリ秒）
WIDTH=50 # モグラの横幅

# infoの要素の取得
info=document.getElementById("info")
# canvasの要素の取得
canvas=document.getElementById("canvas")
context=canvas.getContext("2d")  #2D描画コンテキストの取得
# ゲーム全体の流れを辞書が多変数で管理
game={
    "turns":GAME_TURNS, # 残りのゲームターン数
    "score":0,  # スコア
    "mx":0,  #モグラのｘ座標
    "my":0,  #モグラのy座標
    "hide":True, # モグラが隠れているか
}

def next_turn():
    """次のターンの処理を行う関数"""
    # 残りのターン数を確認
    if game["turns"]<=0:
        game_over()
        return
    # ターン数を1減らす
    game["turns"]-=1
    # モグラの状態を変更して画面を描画
    update_mogura()
    update_screen()
    # 次回のタイマーセット
    setTimeout(next_turn, INTERVAL)

def update_mogura():
    """モグラの状態を変更する関数"""
    game["hide"]=not game["hide"]
    if not game["hide"]:
        # モグラの位置をランダムに決定
        game["mx"]=random.randint(0, canvas.width - WIDTH)
        # サンプル画像に合わせて上から1／4を外す
        game["my"]=random.randint(110, canvas.height - WIDTH)

def update_screen():
    """画面を描画する関数"""
    # 画面クリア
    context.clearRect(0, 0, canvas.width, canvas.height)
    # 背景画像の描画
    hatake_img=document.getElementById("hatake_img")
    context.drawImage(hatake_img, 0, 0, canvas.width, canvas.height)
    # モグラの描画
    if not game["hide"]:
        mogura_img=document.getElementById("mogura_img")
        context.drawImage(mogura_img, game["mx"], game["my"], WIDTH, WIDTH)
    # スコアの更新
    info.innerText=(f"スコア: {game['score']}点 /"
                    f"残り時間: {game['turns']}")

def game_over():
    """ゲームオーバー処理"""
    # 画面クリア
    context.clearRect(0, 0, canvas.width, canvas.height)
    # ゲームオーバー表示
    info.innerText=f"ゲームオーバー！ 最終スコア: {game['score']}点"
    # ゲーム開始ボタンの有効化
    document.getElementById("start_button").disabled=False
