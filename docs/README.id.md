# Fixen UI Studio

[English — dokumentasi utama](../README.md) · Bahasa Indonesia · [Español](README.es.md) · [Português (Brasil)](README.pt-BR.md) · [简体中文](README.zh-CN.md)

**Desain berdasarkan konteks produk, implementasi yang berfungsi, dan QA dengan bukti.**

Fixen UI Studio adalah Agent Skill open source untuk merancang, membangun, mengaudit, dan memperbaiki antarmuka web. Alurnya mencakup discovery, art direction, UX, implementasi frontend, QA visual, serta pencarian gambar nyata bila diperlukan.

**v1.3.0 · Eksperimental.** Sebelumnya bernama Fixenzo UI Studio. Panggil dengan `$fixen-ui-studio`. Paket ini berisi instruksi Markdown/YAML; model, alat, dan izin disediakan oleh agen/host.

## Instalasi

Unduh `fixen-ui-studio-v1.3.0.zip` dari [GitHub Releases](https://github.com/riantosee/Fixen-ui-Studio/releases). Ekstrak folder `fixen-ui-studio/` ke direktori skills Codex sehingga entrypoint berada di:

```text
~/.codex/skills/fixen-ui-studio/SKILL.md
```

Di Windows, `~` biasanya adalah folder profil pengguna. Jika `CODEX_HOME` dikonfigurasi, gunakan direktori skills miliknya. Cadangkan instalasi yang sudah kamu modifikasi sebelum menggantinya. Alternatifnya, clone repo dan salin hanya `skills/fixen-ui-studio/`. Dukungan host lain belum semuanya diuji.

## Contoh penggunaan

```text
Gunakan $fixen-ui-studio untuk membuat dashboard dispatcher.
Prioritaskan pengiriman terlambat, filter, dan tindakan penanganan.
Gunakan stack proyek yang ada dan data sintetis.
```

```text
Gunakan $fixen-ui-studio untuk audit hierarki dan aksesibilitas halaman ini.
Berikan temuan berdasarkan bukti. Jangan ubah file.
```

```text
Gunakan $fixen-ui-studio untuk UI pemesanan dengan English sebagai bahasa
utama serta locale Indonesia dan Arab. Pakai sistem i18n yang ada;
periksa format harga/tanggal, tampilan mobile, dan navigasi RTL.
```

## Bahasa dan gambar

English adalah bahasa utama dokumentasi. Agen mengikuti bahasa komunikasi yang diminta pengguna; bahasa UI mengikuti arahan produk dan konvensi repo. Untuk produk baru tanpa arahan bahasa, gunakan English dan nyatakan asumsi tersebut. Lihat [panduan lokalisasi](../skills/fixen-ui-studio/systems/localization.md) untuk format locale, teks panjang, font, dan RTL. Skill tidak memasang mesin penerjemah atau menjamin kualitas semua bahasa.

[Pencarian gambar](../skills/fixen-ui-studio/design/asset-sourcing.md) bersifat opsional dan memakai alat host yang tersedia. Kandidat, unduhan, integrasi, dan verifikasi hasil render adalah tahapan terpisah. Permintaan shortlist berhenti pada rekomendasi. Catat sumber, pembuat, ketentuan, dan status pemeriksaan di [catatan aset](../skills/fixen-ui-studio/templates/asset-register.md). Lisensi gambar pihak ketiga tidak otomatis menjadi MIT.

## Kontribusi dan batas pengujian

Panduan kontribusi tersedia dalam English di [CONTRIBUTING.md](../CONTRIBUTING.md). Terjemahan dipersilakan; pertahankan identifier, perintah, path, makna lisensi, dan batas bukti. Jika isi berbeda, rujuk [README English](../README.md) dan [changelog](../CHANGELOG.md), lalu laporkan perbedaannya.

```sh
python -m pip install -r requirements-dev.txt
python scripts/validate.py
python -m unittest discover -s scripts -p "test_*.py" -v
```

Perintah tersebut memerlukan Python 3.10+ untuk validasi kontributor, bukan untuk sekadar memakai instruksi skill. Lulus validator tidak membuktikan kualitas visual, kualitas terjemahan, compliance aksesibilitas, atau keunggulan benchmark. Lihat [cakupan validasi](validation.md). Terjemahan README juga bukan bukti uji browser untuk setiap locale.

## Keamanan dan lisensi

Eksploitasi tanpa izin, pencurian kredensial, prompt injection berbahaya, malware, dan payload destruktif dilarang di kontribusi dan ruang komunitas proyek. Pengujian defensif berizin dengan fixture terisolasi serta data sintetis diperbolehkan. Laporkan kerentanan secara privat sesuai [Security Policy](../SECURITY.md); ikuti [Code of Conduct](../CODE_OF_CONDUCT.md). Skill ini bukan sandbox dan tidak menjamin perlindungan dari prompt injection.

[MIT License](../LICENSE) mengizinkan penggunaan komersial, modifikasi, distribusi, dan penjualan dengan menyertakan pemberitahuan copyright/lisensi. Kebijakan komunitas dan keamanan tidak mengubah hak MIT atau memberi izin menyerang sistem pihak lain. Fork harus menjelaskan asal dan perubahan, tanpa mengaku sebagai rilis resmi.
