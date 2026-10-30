#!/usr/bin/env python3
"""Mark Six exclusive number generator based on HKJC history and birthday."""

from __future__ import annotations

import csv
import random
import sys
from datetime import date, datetime
from pathlib import Path

CSV_NAME = "hkjc_marksix_results.csv"
BALL_COLUMNS = ("ball_1", "ball_2", "ball_3", "ball_4", "ball_5", "ball_6")
POOL = tuple(range(1, 50))
COMBO_SIZE = 6
OUTPUT_SETS = 3
MAX_ATTEMPTS = 50_000

LIFE_TRAITS = {
    1: "開創與主導",
    2: "協調與直覺",
    3: "表達與靈感",
    4: "務實與穩定",
    5: "變通與機遇",
    6: "責任與和諧",
    7: "分析與洞察",
    8: "事業與豐盛",
    9: "完成與廣結",
}

LUCKY_HOURS = (
    ("子時 23:00–00:59", "夜深靜心，適合整理靈感"),
    ("丑時 01:00–02:59", "潛意識活躍，宜早睡養運"),
    ("寅時 03:00–04:59", "陽氣初生，適合規劃目標"),
    ("卯時 05:00–06:59", "晨光開運，宜散步啟動"),
    ("辰時 07:00–08:59", "進食補氣，適合處理要務"),
    ("巳時 09:00–10:59", "思緒清晰，利於判斷選擇"),
    ("午時 11:00–12:59", "火氣正旺，宜把握當下"),
    ("未時 13:00–14:59", "節奏放緩，適合細心核對"),
    ("申時 15:00–16:59", "行動力高，利於推進計劃"),
    ("酉時 17:00–18:59", "收斂成果，適合總結檢視"),
    ("戌時 19:00–20:59", "人際運旺，宜與親友交流"),
    ("亥時 21:00–22:59", "氣場柔和，適合靜心許願"),
)

DIRECTIONS = (
    "正北方",
    "東北方",
    "正東方",
    "東南方",
    "正南方",
    "西南方",
    "正西方",
    "西北方",
)

# Famous HKJC off-course betting branches, mapped to Hong Kong compass sectors.
BETTING_STATIONS = (
    {
        "name": "上水廣場投注站",
        "area": "北區上水",
        "address": "新界上水龍琛路39號上水廣場",
        "direction": "正北方",
    },
    {
        "name": "大埔超級城投注站",
        "area": "大埔",
        "address": "新界大埔安邦路8號大埔超級城",
        "direction": "東北方",
    },
    {
        "name": "太古城中心投注站",
        "area": "港島東",
        "address": "香港鰂魚涌太古城道18號太古城中心",
        "direction": "正東方",
    },
    {
        "name": "中環士丹利街投注站",
        "area": "中環",
        "address": "香港中環士丹利街",
        "direction": "東南方",
    },
    {
        "name": "香港仔中心投注站",
        "area": "南區香港仔",
        "address": "香港香港仔南寧街38號香港仔中心",
        "direction": "正南方",
    },
    {
        "name": "堅尼地城吉席街投注站",
        "area": "西環",
        "address": "香港堅尼地城吉席街",
        "direction": "西南方",
    },
    {
        "name": "荃灣沙咀道投注站",
        "area": "荃灣",
        "address": "新界荃灣沙咀道",
        "direction": "正西方",
    },
    {
        "name": "屯門市廣場投注站",
        "area": "屯門",
        "address": "新界屯門屯門鄉事會路2號屯門市廣場",
        "direction": "西北方",
    },
    {
        "name": "旺角洗衣街投注站",
        "area": "旺角",
        "address": "九龍旺角洗衣街",
        "direction": "正北方",
    },
    {
        "name": "銅鑼灣糖街投注站",
        "area": "銅鑼灣",
        "address": "香港銅鑼灣糖街",
        "direction": "東南方",
    },
    {
        "name": "沙田新城市廣場投注站",
        "area": "沙田",
        "address": "新界沙田沙田正街18號新城市廣場",
        "direction": "東北方",
    },
)


def script_dir() -> Path:
    return Path(__file__).resolve().parent


def load_historical_combos(csv_path: Path) -> set[frozenset[int]]:
    if not csv_path.is_file():
        raise FileNotFoundError(f"找不到資料檔：{csv_path}")

    history: set[frozenset[int]] = set()
    with csv_path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        missing = [col for col in BALL_COLUMNS if col not in (reader.fieldnames or [])]
        if missing:
            raise ValueError(f"CSV 缺少欄位：{', '.join(missing)}")

        for row in reader:
            balls: list[int] = []
            for col in BALL_COLUMNS:
                raw = (row.get(col) or "").strip()
                if not raw:
                    balls = []
                    break
                balls.append(int(raw))
            if len(balls) != COMBO_SIZE:
                continue
            combo = frozenset(balls)
            if len(combo) != COMBO_SIZE:
                continue
            history.add(combo)
    return history


def parse_birthday(text: str) -> date:
    cleaned = text.strip()
    try:
        return datetime.strptime(cleaned, "%Y-%m-%d").date()
    except ValueError as exc:
        raise ValueError("生日格式須為 YYYY-MM-DD，例如 1977-10-02") from exc


def digital_root(n: int) -> int:
    if n <= 0:
        raise ValueError("無法計算生命密碼")
    while n > 9:
        n = sum(int(d) for d in str(n))
    return n


def life_number(birthday: date) -> int:
    total = birthday.year + birthday.month + birthday.day
    return digital_root(total)


def ask_birthday() -> date:
    if len(sys.argv) > 1:
        return parse_birthday(sys.argv[1])

    while True:
        raw = input("請輸入生日（YYYY-MM-DD，例如 1977-10-02）：").strip()
        try:
            return parse_birthday(raw)
        except ValueError as exc:
            print(f"輸入有誤：{exc}", flush=True)


def generate_exclusive_combos(
    history: set[frozenset[int]],
    rng: random.Random,
    count: int,
    life: int,
) -> list[list[int]]:
    """Draw unused Mark Six sets. Life number is always included as a personal anchor."""
    results: list[list[int]] = []
    used: set[frozenset[int]] = set()
    attempts = 0

    while len(results) < count:
        attempts += 1
        if attempts > MAX_ATTEMPTS:
            raise RuntimeError("無法在合理次數內產生未開過的專屬組合")

        remaining = [n for n in POOL if n != life]
        picks = [life] + rng.sample(remaining, COMBO_SIZE - 1)
        combo = frozenset(picks)
        if combo in history or combo in used:
            continue
        used.add(combo)
        results.append(sorted(picks))

    return results


def daily_fortune(today: date, life: int, rng: random.Random) -> tuple[str, str]:
    slot_index = (today.toordinal() + life) % len(LUCKY_HOURS)
    hour, hint = LUCKY_HOURS[slot_index]
    extra = rng.choice(
        (
            "宜保持平常心，不追不急。",
            "宜專注一件事，避免分心。",
            "宜先核對資料，再作決定。",
            "宜把好運分享，氣場更順。",
        )
    )
    return hour, f"{hint}；{extra}"


def format_combo(balls: list[int]) -> str:
    return "  ".join(f"{n:02d}" for n in balls)


def earthly_branch_index(now: datetime) -> int:
    """Map clock hour to 十二時辰 index: 子=0 ... 亥=11."""
    return ((now.hour + 1) % 24) // 2


def personal_lucky_direction(now: datetime, life: int) -> str:
    """Derive today's personal lucky compass point from date, current hour, and life number."""
    branch = earthly_branch_index(now)
    index = (now.year + now.month + now.day + branch + life) % len(DIRECTIONS)
    return DIRECTIONS[index]


def recommend_betting_station(
    direction: str,
    now: datetime,
    life: int,
) -> dict[str, str]:
    """Pick the luckiest listed HK betting branch facing today's lucky direction."""
    candidates = [s for s in BETTING_STATIONS if s["direction"] == direction]
    if not candidates:
        candidates = list(BETTING_STATIONS)
    pick_index = (now.toordinal() + now.hour + now.minute + life) % len(candidates)
    return candidates[pick_index]


def configure_console() -> None:
    if sys.platform != "win32":
        return
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if callable(reconfigure):
            reconfigure(encoding="utf-8")


def main() -> int:
    configure_console()
    csv_path = script_dir() / CSV_NAME
    try:
        history = load_historical_combos(csv_path)
    except (OSError, ValueError) as exc:
        print(f"讀取歷史開獎失敗：{exc}", file=sys.stderr)
        return 1

    try:
        birthday = ask_birthday()
    except ValueError as exc:
        print(f"輸入有誤：{exc}", file=sys.stderr)
        return 1
    life = life_number(birthday)
    now = datetime.now()
    today = now.date()
    rng = random.SystemRandom()

    try:
        combos = generate_exclusive_combos(history, rng, OUTPUT_SETS, life)
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    hour, fortune = daily_fortune(today, life, rng)
    lucky_dir = personal_lucky_direction(now, life)
    station = recommend_betting_station(lucky_dir, now, life)
    current_branch = LUCKY_HOURS[earthly_branch_index(now)][0]

    print()
    print("=" * 46)
    print("  六合彩專屬號碼產生器")
    print("=" * 46)
    print(f"生日         ：{birthday.isoformat()}")
    print(f"生命密碼     ：{life}（{LIFE_TRAITS[life]}）")
    print(f"歷史已開組合 ：{len(history)} 組（已嚴格剔除）")
    print(f"產生日期     ：{today.isoformat()}")
    print(f"當前時間     ：{now.strftime('%H:%M')}（{current_branch}）")
    print("-" * 46)
    print("今日 3 組專屬號碼（含生命密碼錨點，且從未開出）：")
    for i, combo in enumerate(combos, start=1):
        print(f"  第 {i} 組  {format_combo(combo)}")
    print("-" * 46)
    print(f"今日吉時     ：{hour}")
    print(f"運勢提示     ：{fortune}")
    print("-" * 46)
    print(f"個人吉方位   ：{lucky_dir}")
    print("（依今日日期、當前時辰與生命密碼推算）")
    print(f"今日吉投注站 ：{station['name']}")
    print(f"地區         ：{station['area']}　方位：{station['direction']}")
    print(f"地址         ：{station['address']}")
    print(f"前往提示     ：宜朝{lucky_dir}出發，氣場較順。")
    print("=" * 46)
    print("僅供娛樂參考，並不保證中獎。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
