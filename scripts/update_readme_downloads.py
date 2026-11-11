#!/usr/bin/env python3
"""
Automatically update download badges and links in README.md from version.json
or from a GitHub Actions release event payload.
"""
import os
import sys
import json
import re

def main():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    readme_path = os.path.join(root_dir, "README.md")
    version_json_path = os.path.join(root_dir, "version.json")

    # If run in a GitHub Actions release workflow, inspect github.event
    event_path = os.environ.get("GITHUB_EVENT_PATH")
    if event_path and os.path.exists(event_path):
        try:
            with open(event_path, "r", encoding="utf-8") as f:
                event = json.load(f)
            release = event.get("release", {})
            tag = release.get("tag_name", "").lstrip("v")
            assets = release.get("assets", [])

            if os.path.exists(version_json_path):
                with open(version_json_path, "r", encoding="utf-8") as f:
                    vdata = json.load(f)
            else:
                vdata = {}

            # Detect platform based on asset filenames
            for asset in assets:
                name = asset.get("name", "")
                download_url = asset.get("browser_download_url", "")
                if name.endswith(".apk") and "android" in vdata:
                    vdata["android"]["version"] = tag
                    vdata["android"]["download_url"] = download_url
                elif (name.endswith(".zip") or name.endswith(".exe")) and "windows" in vdata:
                    vdata["windows"]["version"] = tag
                    vdata["windows"]["download_url"] = download_url
                elif name.endswith(".dmg") and "macos" in vdata:
                    vdata["macos"]["version"] = tag
                    vdata["macos"]["download_url"] = download_url
                elif name.endswith(".ipa") and "ios" in vdata:
                    vdata["ios"]["version"] = tag
                    vdata["ios"]["download_url"] = download_url

            with open(version_json_path, "w", encoding="utf-8") as f:
                json.dump(vdata, f, indent=2, ensure_ascii=False)
                f.write("\n")
        except Exception as e:
            print(f"Warning: could not process event payload: {e}")

    if not os.path.exists(version_json_path) or not os.path.exists(readme_path):
        print("Error: version.json or README.md not found.")
        sys.exit(1)

    with open(version_json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    android_ver = data.get("android", {}).get("version", "1.9.47")
    android_url = data.get("android", {}).get("download_url", f"https://github.com/livekadeh/livekadeh-tunnel-releases/releases/download/v{android_ver}/LivekadehTunnel.apk")

    windows_ver = data.get("windows", {}).get("version", "1.9.41")
    windows_url = data.get("windows", {}).get("download_url", f"https://github.com/livekadeh/livekadeh-tunnel-releases/releases/download/v{windows_ver}/livekadeh_tunnel.exe")
    windows_zip_url = f"https://github.com/livekadeh/livekadeh-tunnel-releases/releases/download/v{windows_ver}/livekadeh_tunnel-windows-x86_64.zip"

    macos_ver = data.get("macos", {}).get("version", "1.9.21")
    macos_url = data.get("macos", {}).get("download_url", f"https://github.com/livekadeh/livekadeh-tunnel-releases/releases/download/v{macos_ver}/LivekadehTunnel-macOS.dmg")

    ios_ver = data.get("ios", {}).get("version", "1.9.10")
    ios_url = data.get("ios", {}).get("download_url", f"https://github.com/livekadeh/livekadeh-tunnel-releases/releases/download/v{ios_ver}/LivekadehTunnel.ipa")

    table_content = f"""<!-- DOWNLOAD_TABLE_START -->
| Platform | Engine & Architecture | Package Details | Direct Download |
| :---: | :--- | :--- | :--- |
| ![Android](https://img.shields.io/badge/Android-3DDC84?style=for-the-badge&logo=android&logoColor=white) | `arm64-v8a`, `armeabi-v7a`, `x86_64`<br>Android 7.0+ (API 24+) | **v{android_ver}** (Dual Engine)<br>VpnService + WireGuard + Hotspot | [⬇️ **Download APK**]({android_url}) |
| ![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white) | `x86_64` (64-bit)<br>Windows 10 / 11 / Server | **v{windows_ver}** (Dual Engine & Hotspot)<br>Livekadeh Multipath + WireGuard + Per-App | [⬇️ **Download Portable ZIP**]({windows_zip_url})<br>[⬇️ **Standalone EXE**]({windows_url}) |
| ![macOS](https://img.shields.io/badge/macOS-000000?style=for-the-badge&logo=apple&logoColor=white) | Universal (`arm64` & `x86_64`)<br>macOS 11.0+ (Big Sur+) | **v{macos_ver}** (Apple `utun`)<br>One-line terminal or DMG package | [⬇️ **Download DMG**]({macos_url}) |
| ![iOS](https://img.shields.io/badge/iOS-000000?style=for-the-badge&logo=apple&logoColor=white) | `arm64` (iPhone & iPad)<br>iOS 15.0+ | **v{ios_ver}** (WebKit Client)<br>Anardoni, Sideloadly, TrollStore | [⬇️ **Download IPA**]({ios_url}) |
| ![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black) | `x86_64` & `aarch64`<br>Ubuntu, Debian, CentOS, Alpine | **v1.9.10** (Kernel TUN)<br>Server & CLI Client in single binary | [⬇️ **Download Tarball**](https://github.com/livekadeh/livekadeh-tunnel-releases/releases/download/v1.9.10/livekadeh_tunnel-linux-x86_64.tar.gz) |
| ![MikroTik](https://img.shields.io/badge/MikroTik_CHR-222222?style=for-the-badge&logo=mikrotik&logoColor=white) | RouterOS v7 Container<br>`x86_64` Architecture | **v1.9.47** (Container Image)<br>Ready for `/container/add` import | [⬇️ **Download TAR Image**](https://github.com/livekadeh/livekadeh-tunnel-releases/releases/download/v1.9.47/livekadeh_tunnel-mikrotik-chr.tar) |
<!-- DOWNLOAD_TABLE_END -->"""

    with open(readme_path, "r", encoding="utf-8") as f:
        readme_text = f.read()

    pattern = re.compile(r"<!-- DOWNLOAD_TABLE_START -->.*?<!-- DOWNLOAD_TABLE_END -->", re.DOTALL)
    if pattern.search(readme_text):
        new_readme = pattern.sub(table_content, readme_text)
    else:
        print("Warning: marker not found, could not replace table.")
        return

    # Update latest android link in instructions if present
    new_readme = re.sub(
        r"LivekadehTunnel\.apk \(v[0-9\.]+\)",
        f"LivekadehTunnel.apk (v{android_ver})",
        new_readme
    )
    new_readme = re.sub(
        r"releases/download/v[0-9\.]+/LivekadehTunnel\.apk",
        f"releases/download/v{android_ver}/LivekadehTunnel.apk",
        new_readme
    )
    new_readme = re.sub(
        r"releases/download/v[0-9\.]+/livekadeh_tunnel-windows-x86_64\.zip",
        f"releases/download/v{windows_ver}/livekadeh_tunnel-windows-x86_64.zip",
        new_readme
    )

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(new_readme)

    print("README.md successfully updated with latest download links.")

if __name__ == "__main__":
    main()
