import os
import requests

# 下載CSV檔用函式
def download_csv(url, file_path):
    response = requests.get(url)
    response.raise_for_status()
    with open(file_path, 'wb') as file:
        file.write(response.content)
    print(f'CSV檔 {file_path} 下載完成！')

# 報表的下載號碼
table_number = {'確診報表':2, '分齡確診報表':4, '性別確診報表':5,
                '死亡報表':14, '分齡死亡報表':16, '性別死亡報表':17,
                '疫苗接種報表':38, '各國疫情報表':28}

# 【列表】共392
# 全區23、南投縣13、台中市29、台北市12、台南市37、台東縣16、嘉義市2、嘉義縣18
# 基隆市8、宜蘭縣12、屏東縣33、彰化縣26、新北市29、新竹市3、新竹縣13、桃園市13
# 澎湖縣6、花蓮縣13、苗栗縣18、連江縣4、金門縣6、雲林縣20、高雄市38

# 清單(疫苗接種以外)
lists = [
    '全國_全區', '新北市_全區', '台北市_全區', '桃園市_全區', '台中市_全區',
    '台南市_全區', '高雄市_全區', '宜蘭縣_全區', '新竹縣_全區', '苗栗縣_全區',
    '彰化縣_全區', '南投縣_全區', '雲林縣_全區', '嘉義縣_全區', '屏東縣_全區',
    '台東縣_全區', '花蓮縣_全區', '澎湖縣_全區', '基隆市_全區', '新竹市_全區',
    '嘉義市_全區', '金門縣_全區', '連江縣_全區',

    '南投縣_南投市', '南投縣_草屯鎮', '南投縣_埔里鎮', '南投縣_竹山鎮', '南投縣_名間鄉',
    '南投縣_信義鄉', '南投縣_仁愛鄉', '南投縣_水里鄉', '南投縣_國姓鄉', '南投縣_鹿港鄉',
    '南投縣_魚池鄉', '南投縣_中寮鄉', '南投縣_集集鎮',

    '台中市_北屯區', '台中市_西屯區', '台中市_大里區', '台中市_太平區', '台中市_南屯區',
    '台中市_北區', '台中市_豐原區', '台中市_南區', '台中市_沙鹿區', '台中市_西區',
    '台中市_潭子區', '台中市_大雅區', '台中市_清水區', '台中市_龍井區', '台中市_烏日區',
    '台中市_東區', '台中市_大甲區', '台中市_霧峰區', '台中市_梧棲區', '台中市_神岡區',
    '台中市_大肚區', '台中市_后里區', '台中市_東勢區', '台中市_外埔區', '台中市_新社區',
    '台中市_大安區', '台中市_中區', '台中市_石岡區', '台中市_和平區',

    '台北市_內湖區', '台北市_文山區', '台北市_士林區', '台北市_北投區', '台北市_大安區',
    '台北市_中山區', '台北市_信義區', '台北市_萬華區', '台北市_松山區', '台北市_南港區',
    '台北市_中正區', '台北市_大同區',

    '台南市_永康區', '台南市_安南區', '台南市_東區', '台南市_北區', '台南市_南區',
    '台南市_仁德區', '台南市_新營區', '台南市_歸仁區', '台南市_安平區', '台南市_中西區',
    '台南市_善化區', '台南市_佳里區', '台南市_新市區', '台南市_新化區', '台南市_麻豆區',
    '台南市_關廟區', '台南市_安定區', '台南市_西港區', '台南市_鹽水區', '台南市_六甲區',
    '台南市_柳營區', '台南市_官田區', '台南市_學甲區', '台南市_白河區', '台南市_下營區',
    '台南市_後壁區', '台南市_七股區', '台南市_東山區', '台南市_將軍區', '台南市_玉井區',
    '台南市_山上區', '台南市_大內區', '台南市_北門區', '台南市_楠西區', '台南市_南化區',
    '台南市_左鎮區', '台南市_龍崎區',

    '台東縣_台東市', '台東縣_卑南鄉', '台東縣_成功鎮', '台東縣_太麻里鄉', '台東縣_關山鎮',
    '台東縣_鹿野鄉', '台東縣_東河鄉', '台東縣_池上鄉', '台東縣_蘭嶼鄉', '台東縣_海端鄉',
    '台東縣_長濱鄉', '台東縣_金峰鄉', '台東縣_大武鄉', '台東縣_延平鄉', '台東縣_達仁鄉',
    '台東縣_綠島鄉',

    '嘉義市_西區', '嘉義市_東區',

    '嘉義縣_民雄鄉', '嘉義縣_水上鄉', '嘉義縣_中埔鄉', '嘉義縣_太保市', '嘉義縣_朴子市',
    '嘉義縣_大林鎮', '嘉義縣_竹崎鄉', '嘉義縣_新港鄉', '嘉義縣_六腳鄉', '嘉義縣_布袋鎮',
    '嘉義縣_梅山鄉', '嘉義縣_東石鄉', '嘉義縣_溪口鄉', '嘉義縣_鹿草鄉', '嘉義縣_義竹鄉',
    '嘉義縣_番路鄉', '嘉義縣_阿里山鄉', '嘉義縣_大埔鄉',

    '基隆市_安樂區', '基隆市_信義區', '基隆市_七堵區', '基隆市_中正區', '基隆市_中山區',
    '基隆市_暖暖區', '基隆市_仁愛區', '基隆市_其他',

    '宜蘭縣_宜蘭市', '宜蘭縣_羅東鎮', '宜蘭縣_冬山鄉', '宜蘭縣_五結鄉', '宜蘭縣_蘇澳鎮',
    '宜蘭縣_礁溪鄉', '宜蘭縣_員山鄉', '宜蘭縣_頭城鎮', '宜蘭縣_壯圍鄉', '宜蘭縣_三星鄉',
    '宜蘭縣_南澳鄉', '宜蘭縣_大同鄉',

    '屏東縣_屏東市', '屏東縣_內埔鄉', '屏東縣_潮州鎮', '屏東縣_萬丹鄉', '屏東縣_東港鎮',
    '屏東縣_長治鄉', '屏東縣_新園鄉', '屏東縣_恆春鎮', '屏東縣_鹽埔鄉', '屏東縣_里港鄉',
    '屏東縣_九如鄉', '屏東縣_枋寮鄉', '屏東縣_竹田鄉', '屏東縣_萬巒鄉', '屏東縣_高樹鄉',
    '屏東縣_佳冬鄉', '屏東縣_林邊鄉', '屏東縣_麟洛鄉', '屏東縣_崁頂鄉', '屏東縣_來義鄉',
    '屏東縣_瑪家鄉', '屏東縣_南州鄉', '屏東縣_三地門鄉', '屏東縣_新埤鄉', '屏東縣_琉球鄉',
    '屏東縣_泰武鄉', '屏東縣_車城鄉', '屏東縣_春日鄉', '屏東縣_牡丹鄉', '屏東縣_獅子鄉',
    '屏東縣_滿州鄉', '屏東縣_枋山鄉', '屏東縣_霧台鄉',

    '彰化縣_彰化市', '彰化縣_員林市', '彰化縣_和美鎮', '彰化縣_鹿港鎮', '彰化縣_花壇鄉',
    '彰化縣_溪湖鎮', '彰化縣_福興鄉', '彰化縣_二林鎮', '彰化縣_大村鄉', '彰化縣_秀水鄉',
    '彰化縣_伸港鄉', '彰化縣_社頭鄉', '彰化縣_田中鎮', '彰化縣_埔心鄉', '彰化縣_北斗鎮',
    '彰化縣_永靖鄉', '彰化縣_埔鹽鄉', '彰化縣_芳苑鄉', '彰化縣_埤頭鄉', '彰化縣_溪州鄉',
    '彰化縣_田尾鄉', '彰化縣_芳園鄉', '彰化縣_線西鄉', '彰化縣_二水鄉', '彰化縣_大城鄉',
    '彰化縣_竹塘鄉',

    '新北市_板橋區', '新北市_中和區', '新北市_新莊區', '新北市_三重區', '新北市_新店區',
    '新北市_汐止區', '新北市_土城區', '新北市_永和區', '新北市_蘆洲區', '新北市_淡水區',
    '新北市_樹林區', '新北市_林口區', '新北市_三峽區', '新北市_五股區', '新北市_鶯歌區',
    '新北市_泰山區', '新北市_八里區', '新北市_瑞芳區', '新北市_深坑區', '新北市_三芝區',
    '新北市_金山區', '新北市_萬里區', '新北市_貢寮區', '新北市_石碇區', '新北市_石門區',
    '新北市_烏來區', '新北市_雙溪區', '新北市_坪林區', '新北市_平溪區',

    '新竹市_東區', '新竹市_北區', '新竹市_香山區',

    '新竹縣_竹北市', '新竹縣_竹東鎮', '新竹縣_湖口鄉', '新竹縣_新豐鄉', '新竹縣_新埔鎮',
    '新竹縣_關西鎮', '新竹縣_芎林鄉', '新竹縣_寶山鄉', '新竹縣_橫山鄉', '新竹縣_尖石鄉',
    '新竹縣_北埔鄉', '新竹縣_峨嵋鄉', '新竹縣_五峰鄉',

    '桃園市_桃園區', '桃園市_中壢區', '桃園市_平鎮區', '桃園市_八德區', '桃園市_龜山區',
    '桃園市_蘆竹區', '桃園市_楊梅區', '桃園市_龍潭區', '桃園市_大溪區', '桃園市_大園區',
    '桃園市_觀音區', '桃園市_新屋區', '桃園市_復興區',

    '澎湖縣_馬公市', '澎湖縣_湖西鄉', '澎湖縣_白沙鄉', '澎湖縣_西嶼鄉', '澎湖縣_七美鄉',
    '澎湖縣_望安鄉',

    '花蓮縣_花蓮市', '花蓮縣_吉安鄉', '花蓮縣_新城鄉', '花蓮縣_玉里鎮', '花蓮縣_壽豐鄉',
    '花蓮縣_秀林鄉', '花蓮縣_光復鄉', '花蓮縣_鳳林鎮', '花蓮縣_瑞穗鄉', '花蓮縣_富里鄉',
    '花蓮縣_萬榮鄉', '花蓮縣_卓溪鄉', '花蓮縣_豐濱鄉',

    '苗栗縣_頭份市', '苗栗縣_竹南鎮', '苗栗縣_苗栗市', '苗栗縣_苑裡鎮', '苗栗縣_後龍鎮',
    '苗栗縣_公館鄉', '苗栗縣_通霄鎮', '苗栗縣_造橋鄉', '苗栗縣_三義鄉', '苗栗縣_銅鑼鄉',
    '苗栗縣_卓蘭鎮', '苗栗縣_頭屋鄉', '苗栗縣_大湖鄉', '苗栗縣_南庄鄉', '苗栗縣_三灣鄉',
    '苗栗縣_泰安鄉', '苗栗縣_西湖鄉', '苗栗縣_獅潭鄉',

    '連江縣_南竿鄉', '連江縣_東引鄉', '連江縣_北竿鄉', '連江縣_莒光鄉',

    '金門縣_金寧鄉', '金門縣_金城鎮', '金門縣_金湖鎮', '金門縣_金沙鎮', '金門縣_烈嶼鄉',
    '金門縣_烏坵鄉',

    '雲林縣_斗六市', '雲林縣_虎尾鎮', '雲林縣_斗南鎮', '雲林縣_西螺鎮', '雲林縣_北港鎮',
    '雲林縣_麥寮鄉', '雲林縣_莿桐鄉', '雲林縣_古坑鄉', '雲林縣_土庫鎮', '雲林縣_崙背鄉',
    '雲林縣_二崙鄉', '雲林縣_元長鄉', '雲林縣_大埤鄉', '雲林縣_林內鄉', '雲林縣_台西鄉',
    '雲林縣_口湖鄉', '雲林縣_水林鄉', '雲林縣_四湖鄉', '雲林縣_褒忠鄉', '雲林縣_東勢鄉',

    '高雄市_鳳山區', '高雄市_三民區', '高雄市_楠梓區', '高雄市_左營區', '高雄市_前鎮區',
    '高雄市_小港區', '高雄市_苓雅區', '高雄市_鼓山區', '高雄市_大寮區', '高雄市_仁武區',
    '高雄市_岡山區', '高雄市_林園區', '高雄市_路竹區', '高雄市_新興區', '高雄市_鳥松區',
    '高雄市_橋頭區', '高雄市_大社區', '高雄市_大樹區', '高雄市_燕巢區', '高雄市_梓官區',
    '高雄市_前金區', '高雄市_湖內區', '高雄市_旗山區', '高雄市_茄萣區', '高雄市_阿蓮區',
    '高雄市_美濃區', '高雄市_旗津區', '高雄市_鹽埕區', '高雄市_彌陀區', '高雄市_永安區',
    '高雄市_內門區', '高雄市_杉林區', '高雄市_六龜區', '高雄市_田寮區', '高雄市_桃源區',
    '高雄市_那瑪夏區', '高雄市_甲仙區', '高雄市_茂林區'
    ]

# 清單(疫苗接種)
lists_vaccination = [
    '總計', '新北市', '台北市', '桃園市', '台中市',
    '台南市', '高雄市', '宜蘭縣', '新竹縣', '苗栗縣',
    '彰化縣', '南投縣', '雲林縣', '嘉義縣', '屏東縣',
    '台東縣', '花蓮縣', '澎湖縣', '基隆市', '新竹市',
    '嘉義市', '金門縣', '連江縣'
    ]

# -----------確診報表----------------------------------------------------------------------------------

# 報表種類
report_name = '確診報表'

# 儲存資料夾
save_folder = 'C:/Users/User/OneDrive/TibaMe_AI/TibaMe_Tableau/HW/疫情數據/csv/' + report_name

# 創建保存檔案的資料夾(如果不存在)
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# 設定url、檔案名稱、檔案路徑 + 下載CSV檔
for i in range(len(lists)):
    url = 'https://covid-19.nchc.org.tw/2023_dt_csv.php?big5=yes&dt_name={}&ext={}'
    url = url.format(table_number[report_name], lists[i])
    file_name = '{}_{}.csv'.format(report_name, lists[i])
    file_path = os.path.join(save_folder, file_name)
    download_csv(url, file_path)

# -----------分齡確診報表----------------------------------------------------------------------------------

# 報表種類
report_name = '分齡確診報表'

# 儲存資料夾
save_folder = 'C:/Users/Tibame_EX14/OneDrive/TibaMe_AI/TibaMe_Tableau/HW/疫情數據/csv/' + report_name

# 創建保存檔案的資料夾(如果不存在)
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# 設定url、檔案名稱、檔案路徑 + 下載CSV檔
for i in range(len(lists)):
    url = 'https://covid-19.nchc.org.tw/2023_dt_csv.php?big5=yes&dt_name={}&ext={}'
    url = url.format(table_number[report_name], lists[i])
    file_name = '{}_{}.csv'.format(report_name, lists[i])
    file_path = os.path.join(save_folder, file_name)
    download_csv(url, file_path)

# -----------性別確診報表----------------------------------------------------------------------------------

# 報表種類
report_name = '性別確診報表'

# 儲存資料夾
save_folder = 'C:/Users/Tibame_EX14/OneDrive/TibaMe_AI/TibaMe_Tableau/HW/疫情數據/csv/' + report_name

# 設定url、檔案名稱、檔案路徑 + 下載CSV檔
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# 下載每市的CSV檔
for i in range(len(lists)):
    url = 'https://covid-19.nchc.org.tw/2023_dt_csv.php?big5=yes&dt_name={}&ext={}'
    url = url.format(table_number[report_name], lists[i])
    file_name = '{}_{}.csv'.format(report_name, lists[i])
    file_path = os.path.join(save_folder, file_name)
    download_csv(url, file_path)

# -----------死亡報表----------------------------------------------------------------------------------

# 報表種類
report_name = '死亡報表'

# 儲存資料夾
save_folder = 'C:/Users/Tibame_EX14/OneDrive/TibaMe_AI/TibaMe_Tableau/HW/疫情數據/csv/' + report_name

# 創建保存檔案的資料夾(如果不存在)
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# 設定url、檔案名稱、檔案路徑 + 下載CSV檔
for i in range(len(lists)):
    url = 'https://covid-19.nchc.org.tw/2023_dt_csv.php?big5=yes&dt_name={}&ext={}'
    url = url.format(table_number[report_name], lists[i])
    file_name = '{}_{}.csv'.format(report_name, lists[i])
    file_path = os.path.join(save_folder, file_name)
    download_csv(url, file_path)

# -----------分齡死亡報表----------------------------------------------------------------------------------

# 報表種類
report_name = '分齡死亡報表'

# 儲存資料夾
save_folder = 'C:/Users/Tibame_EX14/OneDrive/TibaMe_AI/TibaMe_Tableau/HW/疫情數據/csv/' + report_name

# 創建保存檔案的資料夾(如果不存在)
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# 設定url、檔案名稱、檔案路徑 + 下載CSV檔
for i in range(len(lists)):
    url = 'https://covid-19.nchc.org.tw/2023_dt_csv.php?big5=yes&dt_name={}&ext={}'
    url = url.format(table_number[report_name], lists[i])
    file_name = '{}_{}.csv'.format(report_name, lists[i])
    file_path = os.path.join(save_folder, file_name)
    download_csv(url, file_path)

# -----------性別死亡報表----------------------------------------------------------------------------------

# 報表種類
report_name = '性別死亡報表'

# 儲存資料夾
save_folder = 'C:/Users/Tibame_EX14/OneDrive/TibaMe_AI/TibaMe_Tableau/HW/疫情數據/csv/' + report_name

# 創建保存檔案的資料夾(如果不存在)
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# 設定url、檔案名稱、檔案路徑 + 下載CSV檔
for i in range(len(lists)):
    url = 'https://covid-19.nchc.org.tw/2023_dt_csv.php?big5=yes&dt_name={}&ext={}'
    url = url.format(table_number[report_name], lists[i])
    file_name = '{}_{}.csv'.format(report_name, lists[i])
    file_path = os.path.join(save_folder, file_name)
    download_csv(url, file_path)

# -----------疫苗接種報表----------------------------------------------------------------------------------

# 報表種類
report_name = '疫苗接種報表'

# 儲存資料夾
save_folder = 'C:/Users/Tibame_EX14/OneDrive/TibaMe_AI/TibaMe_Tableau/HW/疫情數據/csv/' + report_name

# 創建保存檔案的資料夾(如果不存在)
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# 設定url、檔案名稱、檔案路徑 + 下載CSV檔
for i in range(len(lists_vaccination)):
    url = 'https://covid-19.nchc.org.tw/2023_dt_csv.php?big5=yes&dt_name={}&ext={}'
    url = url.format(table_number[report_name], lists_vaccination[i])
    file_name = '{}_{}.csv'.format(report_name, lists_vaccination[i])
    file_path = os.path.join(save_folder, file_name)
    download_csv(url, file_path)

# -----------各國疫情報表----------------------------------------------------------------------------------

# 報表種類
report_name = '各國疫情報表'

# 儲存資料夾
save_folder = 'C:/Users/Tibame_EX14/OneDrive/TibaMe_AI/TibaMe_Tableau/HW/疫情數據/csv/' + report_name

#創建保存檔案的資料夾(如果不存在)
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# 設定url、檔案名稱、檔案路徑 + 下載CSV檔
url = 'https://covid-19.nchc.org.tw/2023_dt_csv.php?big5=yes&dt_name={}'
url = url.format(table_number[report_name])
file_name = '{}.csv'.format(report_name)
file_path = os.path.join(save_folder, file_name)
download_csv(url, file_path)