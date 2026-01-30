import asyncio
import httpx
import os
from dotenv import load_dotenv

load_dotenv()

TDX_APP_ID = os.getenv("TDX_APP_ID")
TDX_APP_KEY = os.getenv("TDX_APP_KEY")
TDX_API_BASE = os.getenv("TDX_API_BASE", "https://tdx.transportdata.tw/api/basic")
TDX_TOKEN_URL = os.getenv("TDX_TOKEN_URL", "https://tdx.transportdata.tw/auth/realms/TDXConnect/protocol/openid-connect/token")

async def get_token():
    """獲取TDX access token"""
    async with httpx.AsyncClient() as client:
        response = await client.post(
            TDX_TOKEN_URL,
            data={
                "grant_type": "client_credentials",
                "client_id": TDX_APP_ID,
                "client_key": TDX_APP_KEY,
            }
        )
        return response.json()["access_token"]

async def test_stop_of_route():
    """測試StopOfRoute API的響應結構"""
    token = await get_token()

    headers = {"Authorization": f"Bearer {token}"}

    async with httpx.AsyncClient() as client:
        # 測試307路線在Taipei
        url = f"{TDX_API_BASE}/v2/Bus/StopOfRoute/City/Taipei/307"
        print(f"請求URL: {url}")

        response = await client.get(url, headers=headers)
        data = response.json()

        print("API響應結構:")
        print(f"總共有 {len(data)} 個方向")

        if data:
            direction = data[0]  # 第一個方向
            print(f"\n第一個方向的結構:")
            print(f"RouteName: {direction.get('RouteName')}")
            print(f"Direction: {direction.get('Direction')}")

            stops = direction.get('Stops', [])
            if stops:
                print(f"\n第一個站牌的結構 (總共 {len(stops)} 個站牌):")
                stop = stops[0]
                print(f"StopUID: {stop.get('StopUID')}")
                print(f"StopID: {stop.get('StopID')}")
                print(f"StopName: {stop.get('StopName')}")
                print(f"StopSequence: {stop.get('StopSequence')}")

                # 檢查是否有位置信息
                if 'StopPosition' in stop:
                    print(f"StopPosition: {stop.get('StopPosition')}")
                else:
                    print("沒有找到StopPosition字段")

                # 打印完整的鍵
                print(f"\n完整的字段列表: {list(stop.keys())}")

if __name__ == "__main__":
    asyncio.run(test_stop_of_route())