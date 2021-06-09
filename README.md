# PChome 24h 自動化搶購

## 功能

* 自動化快速搶購 PChome 24h 指定網頁之商品

## 使用工具

* Python
* Selenium
    ```bash
    $ pip install selenium
    ```

## 使用方法

1. 將 repo 複製到自己的資料夾
    ```bash
    $ git clone https://github.com/jumpingchu/PChome-AutoBuy.git
    ```

2. 下載 `chromedriver.exe` 並放在同個資料夾內 ([前往下載](https://chromedriver.chromium.org/downloads))
   
3. 在 `settings.py` 填入資料（請保管好個資）
   
4. 執行程式
    ```bash
    $ python pchome_autobuy.py
    ```

## 注意事項
1. 可以先拿其他的商品連結做測試，以防搶購時的突發狀況或錯誤（但請記得馬上取消訂單！）
   
2. `settings.py` 內的 CHROME_PATH 可讓 chrome 記住登入資訊，可提升搶購速度，建議使用
   
3. 本程式碼 **尚未適用** 於數量多於１或必須選擇顏色或樣式的商品

4. 本程式碼單純是提供搶購足夠數量的商品為主，**禁止用於大量收購並哄抬價格的黃牛行為！**

## 程式執行流程

1. 將商品加入購物車
2. 前往購物車
3. 登入帳戶
4. 點選一次付清
5. 填入各項資料
6. 勾選同意
7. 點擊送出訂單

(2020/5/1 後記：這是一個為了搶 Nintendo Switch 而誕生的 Project...)
