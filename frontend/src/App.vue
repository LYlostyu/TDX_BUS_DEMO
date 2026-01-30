<script setup>
import axios from "axios";
import { computed, reactive, onMounted, onUnmounted } from "vue";

const apiBase = import.meta.env.VITE_API_BASE || "http://localhost:8000";
const defaultCity = import.meta.env.VITE_DEFAULT_CITY || "Taipei";

// 台灣各縣市行政區對應表
const districtsByCity = {
  Taipei: ["中正區", "大同區", "中山區", "松山區", "大安區", "萬華區", "信義區", "士林區", "北投區", "內湖區", "南港區", "文山區"],
  NewTaipei: ["板橋區", "新莊區", "中和區", "永和區", "土城區", "樹林區", "鶯歌區", "三峽區", "淡水區", "汐止區", "瑞芳區", "五股區", "泰山區", "林口區", "深坑區", "石碇區", "坪林區", "三芝區", "石門區", "八里區", "平溪區", "雙溪區", "貢寮區", "金山區", "萬里區", "烏來區"],
  Keelung: ["中正區", "七堵區", "暖暖區", "仁愛區", "中山區", "安樂區", "信義區"],
  Taoyuan: ["桃園區", "中壢區", "大溪區", "楊梅區", "蘆竹區", "大園區", "龜山區", "八德區", "龍潭區", "平鎮區", "新屋區", "觀音區", "復興區"],
  Hsinchu: ["東區", "北區", "香山區"],
  HsinchuCounty: ["竹北市", "湖口鄉", "新豐鄉", "新埔鎮", "關西鎮", "芎林鄉", "寶山鄉", "竹東鎮", "五峰鄉", "橫山鄉", "尖石鄉", "北埔鄉", "峨眉鄉"],
  MiaoliCounty: ["苗栗市", "苑裡鎮", "通霄鎮", "竹南鎮", "頭份市", "後龍鎮", "卓蘭鎮", "大湖鄉", "公館鄉", "銅鑼鄉", "南庄鄉", "頭屋鄉", "三義鄉", "西湖鄉", "造橋鄉", "三灣鄉", "獅潭鄉", "泰安鄉"],
  Taichung: ["中區", "東區", "南區", "西區", "北區", "北屯區", "西屯區", "南屯區", "太平區", "大里區", "霧峰區", "烏日區", "豐原區", "后里區", "石岡區", "東勢區", "和平區", "新社區", "潭子區", "大雅區", "神岡區", "大肚區", "沙鹿區", "龍井區", "梧棲區", "清水區", "大甲區", "外埔區", "大安區"],
  ChanghuaCounty: ["彰化市", "芬園鄉", "花壇鄉", "秀水鄉", "鹿港鎮", "福興鄉", "線西鄉", "和美鎮", "伸港鄉", "員林市", "社頭鄉", "永靖鄉", "埔心鄉", "溪湖鎮", "大村鄉", "埔鹽鄉", "田中鎮", "北斗鎮", "田尾鄉", "埤頭鄉", "溪州鄉", "竹塘鄉", "二林鎮", "大城鄉", "芳苑鄉", "二水鄉"],
  NantouCounty: ["南投市", "中寮鄉", "草屯鎮", "國姓鄉", "埔里鎮", "仁愛鄉", "名間鄉", "集集鎮", "水里鄉", "魚池鄉", "信義鄉", "竹山鎮", "鹿谷鄉"],
  YunlinCounty: ["斗南鎮", "大埤鄉", "虎尾鎮", "土庫鎮", "褒忠鄉", "東勢鄉", "台西鄉", "崙背鄉", "麥寮鄉", "斗六市", "林內鄉", "古坑鄉", "莿桐鄉", "西螺鎮", "二崙鄉", "北港鎮", "水林鄉", "口湖鄉", "四湖鄉", "元長鄉"],
  Chiayi: ["東區", "西區"],
  ChiayiCounty: ["番路鄉", "梅山鄉", "竹崎鄉", "阿里山鄉", "中埔鄉", "大埔鄉", "水上鄉", "鹿草鄉", "太保市", "朴子市", "東石鄉", "六腳鄉", "新港鄉", "民雄鄉", "大林鎮", "溪口鄉", "義竹鄉", "布袋鎮"],
  Tainan: ["中西區", "東區", "南區", "北區", "安平區", "安南區", "永康區", "歸仁區", "新化區", "左鎮區", "玉井區", "楠西區", "南化區", "仁德區", "關廟區", "龍崎區", "官田區", "麻豆區", "佳里區", "西港區", "七股區", "將軍區", "學甲區", "北門區", "新營區", "後壁區", "白河區", "東山區", "六甲區", "下營區", "柳營區", "鹽水區", "善化區", "大內區", "山上區", "新市區", "安定區"],
  Kaohsiung: ["楠梓區", "左營區", "鼓山區", "三民區", "鹽埕區", "前金區", "新興區", "苓雅區", "前鎮區", "旗津區", "小港區", "鳳山區", "林園區", "大寮區", "大樹區", "大社區", "仁武區", "鳥松區", "岡山區", "橋頭區", "燕巢區", "田寮區", "阿蓮區", "路竹區", "湖內區", "茄萣區", "永安區", "彌陀區", "梓官區", "旗山區", "美濃區", "六龜區", "甲仙區", "杉林區", "內門區", "茂林區", "桃源區", "那瑪夏區"],
  PingtungCounty: ["屏東市", "三地門鄉", "霧台鄉", "瑪家鄉", "九如鄉", "里港鄉", "高樹鄉", "鹽埔鄉", "長治鄉", "麟洛鄉", "竹田鄉", "內埔鄉", "萬丹鄉", "潮州鎮", "泰武鄉", "來義鄉", "萬巒鄉", "崁頂鄉", "新埤鄉", "南州鄉", "林邊鄉", "東港鎮", "琉球鄉", "佳冬鄉", "新園鄉", "枋寮鄉", "枋山鄉", "春日鄉", "獅子鄉", "車城鄉", "牡丹鄉", "恆春鎮", "滿州鄉"],
  YilanCounty: ["宜蘭市", "頭城鎮", "礁溪鄉", "壯圍鄉", "員山鄉", "羅東鎮", "三星鄉", "大同鄉", "五結鄉", "冬山鄉", "蘇澳鎮", "南澳鄉", "釣魚台"],
  HualienCounty: ["花蓮市", "新城鄉", "秀林鄉", "吉安鄉", "壽豐鄉", "鳳林鎮", "光復鄉", "豐濱鄉", "瑞穗鄉", "萬榮鄉", "玉里鎮", "卓溪鄉", "富里鄉"],
  TaitungCounty: ["台東市", "綠島鄉", "蘭嶼鄉", "延平鄉", "卑南鄉", "鹿野鄉", "關山鎮", "海端鄉", "池上鄉", "東河鄉", "成功鎮", "長濱鄉", "太麻里鄉", "金峰鄉", "大武鄉", "達仁鄉"],
  PenghuCounty: ["馬公市", "西嶼鄉", "望安鄉", "七美鄉", "白沙鄉", "湖西鄉"],
  KinmenCounty: ["金沙鎮", "金湖鎮", "金寧鄉", "金城鎮", "烈嶼鄉", "烏坵鄉"],
  LienchiangCounty: ["南竿鄉", "北竿鄉", "莒光鄉", "東引鄉"]
};

const state = reactive({
  route: "",
  city: defaultCity,
  district: "",
  loading: false,
  error: "",
  directions: [],
  selectedDirection: 0,
  lastUpdated: "",
  currentTime: new Date().toLocaleString('zh-TW'),
});

let timeInterval;
let dataInterval;

onMounted(() => {
  timeInterval = setInterval(() => {
    state.currentTime = new Date().toLocaleString('zh-TW');
  }, 1000);
  
  // 每分鐘自動更新公車資料
  dataInterval = setInterval(() => {
    if (state.route && !state.loading) {
      fetchData();
    }
  }, 60000); // 60000毫秒 = 1分鐘
});

onUnmounted(() => {
  if (timeInterval) {
    clearInterval(timeInterval);
  }
  if (dataInterval) {
    clearInterval(dataInterval);
  }
});

const hasData = computed(() => state.directions.length > 0);
const selectedBucket = computed(() => {
  const bucket = state.directions.find((d) => d.direction === state.selectedDirection) || state.directions[0];
  if (!bucket || !state.district.trim()) return bucket;

  // 按鄉鎮市區過濾站牌 - 移除"區"字以增加匹配靈活性
  const districtKeyword = state.district.replace('區', '').replace('鄉', '').replace('鎮', '').replace('市', '');
  const filteredStops = bucket.stops.filter(stop =>
    stop.name?.zh?.includes(districtKeyword) ||
    stop.name?.en?.toLowerCase().includes(districtKeyword.toLowerCase())
  );

  return {
    ...bucket,
    stops: filteredStops
  };
});

const sortedDirections = computed(() =>
  [...state.directions].sort((a, b) => (a.direction || 0) - (b.direction || 0))
);

function etaLabel(stop) {
  const s = stop.stop_status;
  if (s === 1) return "尚未發車";
  if (s === 2) return "交管不停靠";
  if (s === 3) return "末班已過";
  if (s === 4) return "未營運";

  const secs = stop.estimate_seconds;
  if (secs === null || secs === undefined) return "—";
  if (secs <= 30) return "進站";
  if (secs < 90) return "1 分";
  const mins = Math.round(secs / 60);
  return `${mins} 分`;
}

function badgeTone(stop) {
  const status = stop.stop_status;
  if (status === 2 || status === 4) return "badge muted";
  if (status === 3) return "badge warning";
  const secs = stop.estimate_seconds;
  if (secs !== null && secs <= 90) return "badge active";
  return "badge";
}

function mapUrl(stop) {
  const lat = stop.position?.lat;
  const lon = stop.position?.lon;
  if (lat && lon) {
    return `https://www.google.com/maps?q=${lat},${lon}`;
  }
  return null;
}

const availableDistricts = computed(() => districtsByCity[state.city] || []);

const nextUpdateIn = computed(() => {
  if (!state.route || !state.lastUpdated) return null;
  // 簡單的倒計時顯示，實際上我們每分鐘更新一次
  return "每分鐘自動更新";
});

function directionLabel(d) {
  if (d === 0) return "去程"; //0
  if (d === 1) return "返程"; //1
  return `方向 ${d ?? "-"}`;
}

async function fetchData() {
  state.error = "";
  if (!state.route.trim()) {
    state.error = "請輸入路線號碼";
    return;
  }

  state.loading = true;
  try {
    const resp = await axios.get(
      `${apiBase}/api/routes/${encodeURIComponent(state.route.trim())}/stop-etas`,
      {
        params: { city: state.city },
      }
    );
    state.directions = resp.data?.directions || [];
    state.lastUpdated = resp.data?.updated_at || "";
    if (state.directions.length) {
      state.selectedDirection = state.directions[0].direction ?? 0;
    }
    if (!state.directions.length) {
      state.error = "查無資料，請確認路線與城市";
    }
  } catch (err) {
    state.error = err?.response?.data?.detail || "查詢失敗，請稍後再試";
  } finally {
    state.loading = false;
  }
}
</script>

<template>
  <div class="hero">
    <div>
      <p class="eyebrow">TDX • Bus ETA</p>
      <h1>查詢公車即時到站</h1>
      <p class="lead">
        選擇城市和行政區，輸入路線號碼（如 307、236區、綠1），即時查看去程 / 回程每站預估到站時間。資料來源：
        /v2/Bus/EstimatedTimeOfArrival 與 /v2/Bus/StopOfRoute。
      </p>
      <p class="current-time">現在時間：{{ state.currentTime }}</p>
      <div class="actions">
        <select v-model="state.city" class="input city-select">
          <option value="Taipei">Taipei (台北市)</option>
          <option value="NewTaipei">NewTaipei (新北市)</option>
          <option value="Keelung">Keelung (基隆市)</option>
          <option value="Taoyuan">Taoyuan (桃園市)</option>
          <option value="Hsinchu">Hsinchu (新竹市)</option>
          <option value="HsinchuCounty">HsinchuCounty (新竹縣)</option>
          <option value="MiaoliCounty">MiaoliCounty (苗栗縣)</option>
          <option value="Taichung">Taichung (台中市)</option>
          <option value="ChanghuaCounty">ChanghuaCounty (彰化縣)</option>
          <option value="NantouCounty">NantouCounty (南投縣)</option>
          <option value="YunlinCounty">YunlinCounty (雲林縣)</option>
          <option value="Chiayi">Chiayi (嘉義市)</option>
          <option value="ChiayiCounty">ChiayiCounty (嘉義縣)</option>
          <option value="Tainan">Tainan (台南市)</option>
          <option value="Kaohsiung">Kaohsiung (高雄市)</option>
          <option value="PingtungCounty">PingtungCounty (屏東縣)</option>
          <option value="YilanCounty">YilanCounty (宜蘭縣)</option>
          <option value="HualienCounty">HualienCounty (花蓮縣)</option>
          <option value="TaitungCounty">TaitungCounty (台東縣)</option>
          <option value="PenghuCounty">PenghuCounty (澎湖縣)</option>
          <option value="KinmenCounty">KinmenCounty (金門縣)</option>
          <option value="LienchiangCounty">LienchiangCounty (連江縣)</option>
        </select>
        <select v-model="state.district" class="input district-select">
          <option value="">全部行政區</option>
          <option v-for="district in availableDistricts" :key="district" :value="district">
            {{ district }}
          </option>
        </select>
        <input
          v-model="state.route"
          class="input route-input"
          placeholder="輸入路線號碼"
          inputmode="numeric"
          @keyup.enter="fetchData"
        />
        <button class="primary" :disabled="state.loading" @click="fetchData">
          {{ state.loading ? "查詢中..." : "查詢" }}
        </button>
      </div>
      <p class="hint">城市預設為 {{ defaultCity }}，可依 TDX City 代碼調整。選擇鄉鎮市區可過濾顯示該區域的站牌。</p>
    </div>
  </div>

  <div class="card content">
    <div class="content-head">
      <div>
        <p class="eyebrow">路線</p>
        <h2 class="route-title">
          {{ state.route || "" }}
          <span class="city">{{ state.city }}</span>
        </h2>
        <p class="timestamp" v-if="state.lastUpdated">更新：{{ state.lastUpdated }}</p>
        <p class="auto-update" v-if="nextUpdateIn">🔄 {{ nextUpdateIn }}</p>
      </div>
      <div class="direction-tabs" v-if="sortedDirections.length">
        <button
          v-for="dir in sortedDirections"
          :key="dir.direction ?? -1"
          :class="['tab', state.selectedDirection === dir.direction ? 'active' : '']"
          @click="state.selectedDirection = dir.direction"
        >
          {{ directionLabel(dir.direction) }}
        </button>
      </div>
    </div>

    <div v-if="state.error" class="alert">{{ state.error }}</div>
    <div v-else-if="state.loading" class="loading">讀取中…</div>
    <div v-else-if="hasData && selectedBucket">
      <div class="stop-list">
        <div v-for="stop in selectedBucket.stops" :key="stop.stop_uid" class="stop-row">
          <div :class="badgeTone(stop)">{{ etaLabel(stop) }}</div>
          <div class="timeline">
            <div class="dot"></div>
            <div class="line"></div>
          </div>
          <div class="stop-info">
            <div class="name-zh">
              <a v-if="mapUrl(stop)" :href="mapUrl(stop)" target="_blank" rel="noopener noreferrer" class="stop-link">
                {{ stop.name?.zh }}
              </a>
              <span v-else>{{ stop.name?.zh }}</span>
            </div>
            <div class="name-en">{{ stop.name?.en }}</div>
            <div class="meta">
              Seq {{ stop.stop_sequence || "-" }} · UID {{ stop.stop_uid || "-" }}
            </div>
          </div>
        </div>
      </div>
    </div>
    <div v-else class="empty">請輸入路線並點擊查詢。</div>
  </div>
</template>

<style scoped>
.hero {
  display: flex;
  gap: 28px;
  padding: 8px 12px 28px;
}

.eyebrow {
  letter-spacing: 0.08em;
  text-transform: uppercase;
  font-size: 12px;
  color: #5c6f91;
  margin: 0 0 4px;
}

h1 {
  margin: 0;
  font-size: 34px;
  color: #0d1a2d;
}

.lead {
  color: #42526b;
  line-height: 1.6;
  max-width: 720px;
}

.actions {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 14px;
}

.input {
  border: 1px solid #d8deeb;
  border-radius: 12px;
  padding: 12px 14px;
  font-size: 16px;
  min-width: 200px;
  background: #fff;
  transition: border 0.2s, box-shadow 0.2s;
}

.input:focus {
  outline: none;
  border-color: #3b82f6;
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.18);
}

.route-input {
  flex: 1;
}

.city-select {
  width: 200px;
}

.district-select {
  width: 180px;
}

.primary {
  background: linear-gradient(135deg, #2563eb, #38bdf8);
  border: none;
  color: #fff;
  border-radius: 12px;
  padding: 12px 18px;
  font-size: 16px;
  font-weight: 600;
  box-shadow: 0 12px 30px rgba(37, 99, 235, 0.25);
  transition: transform 0.15s ease, box-shadow 0.2s ease;
}

.primary:disabled {
  opacity: 0.6;
  cursor: not-allowed;
  box-shadow: none;
}

.primary:not(:disabled):hover {
  transform: translateY(-1px);
  box-shadow: 0 16px 36px rgba(37, 99, 235, 0.32);
}

.hint {
  color: #6b7a99;
  margin-top: 6px;
  font-size: 13px;
}

.current-time {
  color: #0d1a2d;
  margin-top: 8px;
  font-size: 14px;
  font-weight: 500;
}

.card.content {
  margin-top: 10px;
  padding: 20px 18px;
}

.content-head {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 10px;
  flex-wrap: wrap;
}

.route-title {
  margin: 6px 0 6px;
  font-size: 26px;
  display: flex;
  align-items: baseline;
  gap: 10px;
}

.city {
  font-size: 16px;
  color: #607089;
}

.timestamp {
  margin: 0;
  color: #607089;
}

.auto-update {
  margin: 2px 0 0;
  color: #059669;
  font-size: 12px;
  font-weight: 500;
}

.direction-tabs {
  display: flex;
  gap: 8px;
}

.tab {
  border: 1px solid #d8deeb;
  border-radius: 12px;
  padding: 10px 14px;
  background: #f6f8fc;
  color: #294057;
  font-weight: 600;
  min-width: 120px;
}

.tab.active {
  background: linear-gradient(135deg, #2563eb, #38bdf8);
  color: white;
  border-color: transparent;
  box-shadow: 0 12px 28px rgba(37, 99, 235, 0.24);
}

.alert {
  background: #fff6f2;
  color: #b54708;
  border: 1px solid #ffd4bd;
  padding: 12px 14px;
  border-radius: 12px;
}

.loading,
.empty {
  color: #5c6f91;
  padding: 12px 0;
}

.stop-list {
  margin-top: 12px;
  display: grid;
  gap: 12px;
}

.stop-row {
  display: grid;
  grid-template-columns: 110px 26px 1fr;
  align-items: center;
  gap: 14px;
  padding: 14px 12px;
  border: 1px solid #e6ecf5;
  border-radius: 14px;
  background: linear-gradient(135deg, #fff, #f9fbff);
}

.badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 999px;
  padding: 6px 12px;
  background: #e8edf7;
  color: #1c2c46;
  font-weight: 700;
  min-width: 72px;
}

.badge.active {
  background: #22c55e1a;
  color: #0f9d46;
}

.badge.warning {
  background: #fef2c0;
  color: #915103;
}

.badge.muted {
  background: #ececf1;
  color: #6f7285;
}

.timeline {
  display: flex;
  align-items: center;
  gap: 6px;
}

.dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: #2563eb;
}

.line {
  height: 1px;
  flex: 1;
  background: #cbd5e1;
}

.stop-info .name-zh {
  font-weight: 700;
  color: #0f172a;
}

.stop-link {
  color: inherit;
  text-decoration: none;
  cursor: pointer;
}

.stop-link:hover {
  color: #2563eb;
  text-decoration: underline;
}

.stop-info .name-en {
  color: #5c6f91;
  font-size: 13px;
}

.stop-info .meta {
  color: #7b879e;
  font-size: 12px;
  margin-top: 2px;
}

@media (max-width: 700px) {
  .stop-row {
    grid-template-columns: 1fr;
    align-items: start;
  }

  .timeline {
    display: none;
  }

  .route-title {
    font-size: 22px;
  }
}
</style>
