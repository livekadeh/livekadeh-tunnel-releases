<div align="center">

# 🚀 Livekadeh Tunnel (لایوکده تانل)

**High-Performance Dual-Engine VPN & Stream-Encrypted Tunnel**  
*Ultra-low Latency ChaCha20 L3 VPN + Native Userspace WireGuard Engine*

[![Latest Release](https://img.shields.io/github/v/release/livekadeh/livekadeh-tunnel-releases?color=00E5FF&label=Release&logo=github&style=for-the-badge)](https://github.com/livekadeh/livekadeh-tunnel-releases/releases/latest)
[![WireGuard Engine](https://img.shields.io/badge/WireGuard-Native%20GoBackend-88171A?style=for-the-badge&logo=wireguard&logoColor=white)](https://www.wireguard.com/)
[![License](https://img.shields.io/badge/License-Proprietary-FF5252?style=for-the-badge)](LICENSE)
[![Dual Stack](https://img.shields.io/badge/Dual--Stack-Multi--TCP%20%7C%20UDP-7C4DFF?style=for-the-badge)](README.md)
[![Platforms](https://img.shields.io/badge/Platforms-Android%20%7C%20Windows%20%7C%20macOS%20%7C%20iOS%20%7C%20Linux%20%7C%20MikroTik-00E676?style=for-the-badge)](README.md)

</div>

---

A lightweight, high-performance, full-duplex TCP/UDP stream-encrypted tunnel and WireGuard-style Virtual Network Adapter (Wintun L3 VPN, macOS `utun`, and Linux `tun`). Encrypts and tunnels arbitrary network traffic (All Ports, Browsing, SSH, Web, RDP, VoIP, Gaming, or specific Windows applications) between Linux / MikroTik CHR servers and Windows, Android, iOS, macOS, and Linux clients without SSL/TLS overhead, identifiable handshakes, or Deep Packet Inspection (DPI) fingerprints.

---

## ⚡ Key Highlights

- **Dual-Engine Architecture (Livekadeh + WireGuard Client):**
  - Use the client as a full WireGuard VPN application or a native Livekadeh tunnel.
  - Import standard WireGuard configuration files (`.conf`), paste raw keys, or scan QR codes.
  - Run the native userspace WireGuard engine (`libwg-go`) directly inside the app.
  - Combine standard WireGuard with Livekadeh Tunnel features:
    - **Server DNS Shield:** Enforce automatic family protection and anti-malware filters.
    - **Anti-Sanction DNS Presets:** Bypass regional service blocks with built-in Iranian DNS servers.
    - **Per-App Routing:** Split traffic to route specific applications or bypass domestic domains.
    - **Profile Management:** Store multiple WireGuard and Livekadeh configurations with separate active memory.
    - **Real-Time Monitoring:** View live handshake status, data transfer counters, and account expiration.
- **Hotspot & Local Network Proxy Sharing (Android & Windows):**
  - Share the encrypted tunnel across local devices, smart TVs, and gaming consoles.
  - Integrated HTTP, HTTPS, and SOCKS5 proxy server on ports 8080 and 1080 without requiring root access.
  - Transparent Root NAT policy routing and transparent TLS SNI proxy for zero-configuration tethering.
  - Real-time connected client monitor with ARP MAC discovery and request counters.
- **Per-Application Flow Routing (Windows):**
  - Route selected application executables through the encrypted tunnel via WinDivert.
  - Dual-stack bypass protection with automated IPv6 filtering.
  - Native UDP, QUIC (port 443), and DNS flow diversion with MSS clamping.
- **Custom Split Rules & Anti-Sanction DNS Presets:**
  - Route specific traffic with IP direct, CIDR bypass, and custom domain rules.
  - Preloaded Iranian anti-sanction DNS servers (Shecan, Electro, 403, Radar, Begzar).
- **1-Line Automated Server Installer:**
  - Fast curl installation for Ubuntu, Debian, CentOS, AlmaLinux, Rocky, Alpine, and Arch.
  - Automatically sets up systemd service, IP forwarding, and Web Management Panel.
- **Multi-User Web Management Panel & QR Code:**
  - Modern web dashboard running on port 8444.
  - Multi-user authentication, client bandwidth tracking, and instant QR Code generation (`livekadeh://<key>@<host>:<port>`).
- **QR Code Configuration Import Across All Clients:**
  - **Android:** Direct QR Code camera and gallery image scanner powered by ZXing.
  - **Windows:** Unified **"Import"** menu supports config files (`.conf`, `.json`, `.txt`), clipboard paste, and QR code images (`PNG`, `JPG`, `BMP`).
  - **macOS / Linux CLI:** Interactive prompt accepts raw `host:port` and `livekadeh://` URIs.
  - **Empty By Default:** No hardcoded server IPs or keys; all fields remain clean for user configuration.
- **In-App Auto-Updates Across All Platforms:**
  - **CLI / Linux / macOS:** Run `livekadeh_tunnel -u` to self-update automatically from GitHub.
  - **Windows:** "About Tunnel" and "Check Updates" buttons check and download the latest release.
  - **Android:** In-app update dialog checks GitHub releases and downloads APK updates directly.
- **Multi-Client Support with Dynamic IP Pool (10.10.10.2 - 10.10.10.254):**
  - Connect concurrent users simultaneously with independent sessions and traffic quotas.
- **Dual-Stack Transport (Multi-TCP & UDP Datagrams):**
  - **UDP Datagram Mode:** Ultra-low latency, stateless per-packet ChaCha20 encryption with automatic NAT mobility handling.
  - **8-Lane Multi-TCP Transport Engine:** Establishes **8 parallel, independent encrypted TCP streams** between client and server to bypass ISP single-stream bandwidth throttling.
  - **Intelligent 5-Tuple Flow Hashing:** Pins IP flows to lanes, guaranteeing **zero packet reordering**.
- **In-Tunnel Speed Test & Benchmark Tool:**
  - Integrated speed test suite on port 9090 measuring real in-tunnel RTT latency and throughput.
- **Remote Server Security & Centralized IP Blocklist:**
  - Server automatically cross-references GitHub `blocked_servers.json` to verify operational authorization.
- **MikroTik CHR (RouterOS v7 Container) Ready:**
  - Dedicated pre-packaged `.tar` image (`livekadeh_tunnel-mikrotik-chr.tar`) ready for MikroTik `/container/add`.
  - Supports configurable tunnel ports (`PORT=8585` or custom).
  - Automatically displays the active encryption key in the MikroTik Container Log.

---

## 🌐 Official Downloads & Releases

- **Official Releases Repository:** [https://github.com/livekadeh/livekadeh-tunnel-releases](https://github.com/livekadeh/livekadeh-tunnel-releases)

### 📥 Client Packages & Downloads

<!-- DOWNLOAD_TABLE_START -->
| Platform | Engine & Architecture | Package Details | Direct Download |
| :---: | :--- | :--- | :--- |
| ![Android](https://img.shields.io/badge/Android-3DDC84?style=for-the-badge&logo=android&logoColor=white) | `arm64-v8a`, `armeabi-v7a`, `x86_64`<br>Android 7.0+ (API 24+) | **v1.9.47** (Dual Engine)<br>VpnService + WireGuard + Hotspot | [⬇️ **Download APK**](https://github.com/livekadeh/livekadeh-tunnel-releases/releases/download/v1.9.47/LivekadehTunnel.apk) |
| ![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white) | `x86_64` (64-bit)<br>Windows 10 / 11 / Server | **v1.9.48** (Dual Engine & Hotspot)<br>Livekadeh Multipath + WireGuard + Per-App | [⬇️ **Download Portable ZIP**](https://github.com/livekadeh/livekadeh-tunnel-releases/releases/download/v1.9.48/livekadeh_tunnel-windows-x86_64.zip)<br>[⬇️ **Standalone EXE**](https://github.com/livekadeh/livekadeh-tunnel-releases/releases/download/v1.9.48/livekadeh_tunnel.exe) |
| ![macOS](https://img.shields.io/badge/macOS-000000?style=for-the-badge&logo=apple&logoColor=white) | Universal (`arm64` & `x86_64`)<br>macOS 11.0+ (Big Sur+) | **v1.9.21** (Apple `utun`)<br>One-line terminal or DMG package | [⬇️ **Download DMG**](https://github.com/livekadeh/livekadeh-tunnel-releases/releases/download/v1.9.21/LivekadehTunnel-macOS.dmg) |
| ![iOS](https://img.shields.io/badge/iOS-000000?style=for-the-badge&logo=apple&logoColor=white) | `arm64` (iPhone & iPad)<br>iOS 15.0+ | **v1.9.10** (WebKit Client)<br>Anardoni, Sideloadly, TrollStore | [⬇️ **Download IPA**](https://github.com/livekadeh/livekadeh-tunnel-releases/releases/download/v1.9.10/LivekadehTunnel.ipa) |
| ![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black) | `x86_64` & `aarch64`<br>Ubuntu, Debian, CentOS, Alpine | **v1.9.10** (Kernel TUN)<br>Server & CLI Client in single binary | [⬇️ **Download Tarball**](https://github.com/livekadeh/livekadeh-tunnel-releases/releases/download/v1.9.10/livekadeh_tunnel-linux-x86_64.tar.gz) |
| ![MikroTik](https://img.shields.io/badge/MikroTik_CHR-222222?style=for-the-badge&logo=mikrotik&logoColor=white) | RouterOS v7 Container<br>`x86_64` Architecture | **v1.9.47** (Container Image)<br>Ready for `/container/add` import | [⬇️ **Download TAR Image**](https://github.com/livekadeh/livekadeh-tunnel-releases/releases/download/v1.9.47/livekadeh_tunnel-mikrotik-chr.tar) |
<!-- DOWNLOAD_TABLE_END -->

---

## 🚀 Quick Start & Deployment Guide

### 1. Linux Server 1-Line Quick Install (Recommended)

Run this single command on your Ubuntu, Debian, CentOS, or Alpine server as root:

```bash
curl -sSL https://raw.githubusercontent.com/livekadeh/livekadeh-tunnel/main/scripts/install_server.sh | sudo bash
```

The script automatically performs these tasks:
- Detects system architecture (`x86_64` or `aarch64`).
- Enables `net.ipv4.ip_forward=1`.
- Installs `livekadeh_tunnel` to `/usr/local/bin`.
- Installs and enables the `livekadeh-tunnel` systemd service.
- Deploys the Web Management Panel at `http://<SERVER_IP>:8444`.
- Generates a fresh 256-bit encryption key and prints complete connection credentials.

---

### 2. MikroTik CHR Server Deployment (Container)

#### A. Enable Container Mode on MikroTik:
```routeros
/system/device-mode/update container=yes
/system/reboot
```

#### B. Setup Network Bridge & VETH:
```routeros
/interface/veth/add name=veth-livekadeh address=172.17.0.2/24 gateway=172.17.0.1
/interface/bridge/add name=bridge-docker
/ip/address/add address=172.17.0.1/24 interface=bridge-docker
/interface/bridge/port add bridge=bridge-docker interface=veth-livekadeh

/ip/firewall/nat/add chain=srcnat action=masquerade src-address=172.17.0.0/24
/ip/firewall/nat/add chain=dstnat action=dst-nat to-addresses=172.17.0.2 to-ports=8443 protocol=tcp dst-port=8443
/ip/firewall/nat/add chain=dstnat action=dst-nat to-addresses=172.17.0.2 to-ports=8443 protocol=udp dst-port=8443
```
*(If forwarding on a custom port such as 8585, add env `PORT=8585` and adjust dst-nat to-ports).*

#### C. Upload and Start Container:
1. Upload `livekadeh_tunnel-mikrotik-chr.tar` to your MikroTik storage via WinBox (Files) or SFTP.
2. In RouterOS Terminal:
```routeros
/container/add file=livekadeh_tunnel-mikrotik-chr.tar interface=veth-livekadeh logging=yes
/container/start 0
```
3. Check the WinBox **Log** window or run:
```routeros
/log/print where topics~"container"
```
The container will auto-start the server and display the **Encryption Key** in the log!

---

### 3. Windows Client Deployment (GUI, Hotspot & Per-App)

1. Download and extract [livekadeh_tunnel-windows-x86_64.zip](https://github.com/livekadeh/livekadeh-tunnel-releases/releases/download/v1.9.48/livekadeh_tunnel-windows-x86_64.zip).
2. Run `livekadeh_tunnel.exe` as Administrator.
3. Import a configuration:
   - Click **"Import"** and select **Import File...**, **Paste Config**, or **Import QR File...**.
   - Or manually enter the server address (`<SERVER_IP>:8443`) and encryption key.
4. (Optional) Enable **Per-App Routing** to route only selected applications through the tunnel.
5. (Optional) Enable **Hotspot / LAN Sharing** to share the tunnel with other devices via HTTP/SOCKS5 proxy.
6. Click **[ CONNECT TUNNEL ]**.

---

### 4. Android Client (Dual Engine: Livekadeh & WireGuard)

1. Download and install [LivekadehTunnel.apk (v1.9.47)](https://github.com/livekadeh/livekadeh-tunnel-releases/releases/download/v1.9.47/LivekadehTunnel.apk).
2. Select your protocol tab at the top: **Livekadeh Tunnel** or **WireGuard**.
3. Import your server configuration:
   - **For Livekadeh:** Tap **"Scan / Import QR Code"** to scan a server key or paste a URI.
   - **For WireGuard:** Tap **"📂 Import"** to load a `.conf` file, or scan a WireGuard QR code.
4. (Optional) Open **Advanced Settings** to configure DNS Shield, MTU size, and Per-App routing.
5. Tap **[ CONNECT ]** to start the secure VPN connection.
6. (Optional) Use the **Hotspot Sharing** card to share VPN access with other devices on your Wi-Fi hotspot.
7. Use the Quick Settings Tile for instant 1-tap toggling.

---

### 5. macOS Client Deployment

#### Download DMG Package:
Download and mount [LivekadehTunnel-macOS.dmg](https://github.com/livekadeh/livekadeh-tunnel-releases/releases/download/v1.9.21/LivekadehTunnel-macOS.dmg).

#### One-Line Terminal Installation:
```bash
curl -sL https://raw.githubusercontent.com/livekadeh/livekadeh-tunnel/main/scripts/install_macos.sh | sudo bash
```

#### Connect as Full VPN Client:
```bash
# Multi-TCP Lane Mode:
sudo livekadeh client -s YOUR_SERVER_IP:8443 -k YOUR_KEY -g

# Ultra Low-Latency UDP Datagram Mode:
sudo livekadeh client -s YOUR_SERVER_IP:8443 -k YOUR_KEY -u -g
```

---

### 6. In-App Updates & Maintenance

- **CLI / Linux / macOS:** Run `livekadeh_tunnel -u` to check GitHub and automatically install the newest release.
- **Windows GUI:** Click **"About Tunnel"** -> **"Check Updates"**.
- **Android:** Tap the three dots menu -> **"About"** -> **"Check for Updates"**.
- **Status Check:** Run `livekadeh_tunnel -status` to see connected users, live speed, and active interface status.
