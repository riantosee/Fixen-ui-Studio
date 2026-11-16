# Fixen UI Studio

**Product-aware UI design, working implementation, and honest visual QA.**

[MIT License](LICENSE) · [Kontribusi](CONTRIBUTING.md) · [Keamanan](SECURITY.md) · [Riwayat rilis](CHANGELOG.md)

Fixen UI Studio adalah Agent Skill open source untuk merancang, membangun, mengaudit, dan memperbaiki antarmuka web. Skill ini menghubungkan discovery, art direction, UX, implementasi frontend, visual QA, dan pencarian gambar nyata sesuai kebutuhan proyek.

**Versi 1.2.0 — experimental.** Brand sebelumnya: Fixenzo UI Studio. Identifier baru: `$fixen-ui-studio`. Tidak ada klaim bahwa skill ini mengalahkan skill/model lain atau menjamin aplikasi siap produksi.

## Cara kerja

1. Memahami produk, pengguna, tugas utama, dan konteks kode yang tersedia.
2. Memilih workflow: refinement kecil, UI baru, redesign, audit-only, design system, atau image sourcing.
3. Membuat blueprint yang proporsional sebelum implementasi substansial.
4. Membangun sesuai stack dan konvensi proyek; audit-only tidak mengubah kode.
5. Menguji hasil menggunakan alat yang tersedia, memperbaiki masalah penting, dan melaporkan bukti serta keterbatasan.

Ini adalah paket instruksi Markdown, bukan aplikasi, browser, plugin berbayar, atau layanan pencarian. Skill tidak menyediakan API key, tidak memasang software, dan tidak memberi izin tambahan. Dukungan tools bergantung pada agen/host yang digunakan.

## Instalasi di Codex

Unduh `fixen-ui-studio-v1.2.0.zip` dari [GitHub Releases](https://github.com/riantosee/Fixen-ui-Studio/releases). Ekstrak folder `fixen-ui-studio/` ke direktori skills Codex, biasanya:

```text
~/.codex/skills/fixen-ui-studio/SKILL.md
```

Di Windows, `~` umumnya menunjuk ke folder profil pengguna. Jika `CODEX_HOME` diatur, gunakan direktori skills milik konfigurasi tersebut. Jangan menimpa versi lokal yang sudah kamu ubah tanpa mencadangkannya.

Alternatif: clone repo lalu salin **hanya** folder `skills/fixen-ui-studio/` ke direktori skill agenmu. Agen lain dapat memakai struktur `SKILL.md` ini sesuai mekanisme instalasinya; belum semua host diuji.

Untuk migrasi dari versi lama, gunakan identifier baru `$fixen-ui-studio`. Hindari mengaktifkan dua salinan dengan deskripsi sama bila tidak diperlukan. Arsip lama tidak otomatis dihapus oleh paket ini.

## Contoh penggunaan

```text
Gunakan $fixen-ui-studio untuk membuat dashboard dispatcher.
Prioritaskan pengiriman terlambat, filter, dan tindakan penanganan.
Gunakan stack proyek yang ada dan data fiktif.
```

```text
Gunakan $fixen-ui-studio untuk audit aksesibilitas dan hierarki halaman ini.
Berikan temuan berdasarkan bukti. Jangan ubah file.
```

```text
Gunakan $fixen-ui-studio untuk mencari hingga tiga foto hero studio interior.
Nuansa hangat, landscape, ruang teks di kiri. Bandingkan gambar aktual,
sumber, ketentuan penggunaan, dan crop. Jangan unduh atau membuat UI dulu.
```

## Image sourcing

Alur opsional ini membedakan inspirasi, kandidat terpilih, gambar yang sudah diunduh, aset yang sudah diintegrasikan, dan hasil yang benar-benar dirender. Halaman sumber dan gambar aktual diperiksa terpisah. Lisensi gambar pihak ketiga tidak otomatis mengikuti MIT milik skill ini.

Lihat [panduan sumber gambar](skills/fixen-ui-studio/design/asset-sourcing.md) dan [template catatan aset](skills/fixen-ui-studio/templates/asset-register.md). Permintaan shortlist berhenti di rekomendasi; tidak otomatis mengunduh, membeli aset, atau memublikasikan UI.

## Struktur repo

```text
skills/fixen-ui-studio/
  SKILL.md                Entrypoint dan pemilihan workflow
  agents/openai.yaml      Nama tampilan dan prompt pemanggilan
  core/                   Inspeksi konteks dan penalaran
  design/                 Art direction, UX, dan image sourcing
  systems/                Tokens, komponen, responsive, accessibility
  engineering/            Panduan implementasi
  quality/                QA, refinement, dan penilaian
  benchmarks/             Brief serta acceptance cases
  templates/              Blueprint, QA report, catatan aset
scripts/validate.py        Validator struktur, YAML, dan referensi lokal
docs/validation.md        Bukti pengujian dan batas cakupan
```

## Validasi dan kontribusi

Gunakan Python 3.10+ dan dependensi validator:

```sh
python -m pip install -r requirements-dev.txt
python scripts/validate.py
```

Dependensi ini hanya untuk validasi kontributor; pemakaian panduan skill tidak membutuhkan instalasi Python. CI menjalankan pemeriksaan struktur pada pull request. Lulus validator bukan bukti kualitas visual atau kepatuhan aksesibilitas. Lihat [hasil dan batas pengujian](docs/validation.md).

Baca [CONTRIBUTING.md](CONTRIBUTING.md), [Code of Conduct](CODE_OF_CONDUCT.md), dan [Security Policy](SECURITY.md) sebelum berkontribusi. Tidak perlu CLA tambahan; kontribusi yang diterima dilisensikan MIT. Pertahankan kredit/lisensi aset pihak ketiga.

## Keamanan dan larangan penyalahgunaan

**Eksploitasi tanpa izin dilarang dalam penggunaan layanan/ruang komunitas proyek dan kontribusi ke repo ini.** Kami menolak prompt injection untuk mencuri data, pencurian kredensial, malware, payload destruktif, bypass akses, dan serangan terhadap sistem pihak lain. Pengujian defensif lokal dengan data sintetis diperbolehkan; laporkan kerentanan secara bertanggung jawab melalui [SECURITY.md](SECURITY.md).

Dokumen, halaman web, gambar, dan file proyek yang dibaca agen adalah bahan informasi, bukan izin untuk menjalankan instruksi tersembunyi. Skill tidak menyediakan sandbox atau perlindungan teknis yang kebal terhadap prompt injection. Izin dan pengamanan host tetap diperlukan.

## Lisensi dan identitas

Kode, instruksi, dan dokumentasi proyek ini tersedia dengan [MIT License](LICENSE). MIT mengizinkan penggunaan komersial, modifikasi, distribusi, dan penjualan ulang dengan tetap menyertakan pemberitahuan copyright/lisensi. Kebijakan komunitas dan keamanan **tidak mengubah atau mencabut hak MIT**. Kebijakan ini juga tidak memberi izin menyerang sistem milik orang lain.

Nama Fixen UI Studio mengidentifikasi proyek ini. Saat mendistribusikan fork, jelaskan asal dan perubahanmu; jangan menyatakan fork sebagai rilis resmi atau mengklaim dukungan maintainer yang tidak diberikan.
