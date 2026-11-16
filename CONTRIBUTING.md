# Berkontribusi ke Fixen UI Studio

Kontribusi dokumentasi, workflow, accessibility, image sourcing, dan benchmark dipersilakan. Baca [Code of Conduct](CODE_OF_CONDUCT.md) dan [Security Policy](SECURITY.md) terlebih dahulu.

## Memilih perubahan

- Typo dan perbaikan kecil boleh langsung melalui PR.
- Untuk workflow baru, perubahan luas, atau perubahan perilaku, buat issue yang menjelaskan kebutuhan dan acceptance criteria.
- Kerentanan keamanan dilaporkan privat, bukan issue publik. Pengujian defensif yang aman tetap boleh disertakan sebagai fixture sintetis.

Prioritaskan petunjuk yang mengubah keputusan agen secara konkret. Hindari memperpanjang prompt dengan nasihat umum, persona tambahan, aturan absolut tanpa alasan, atau instruksi yang mengabaikan permintaan pengguna. Pertahankan mode audit-only, batas tool, dan workflow ringan untuk perubahan kecil.

## Alur kerja

1. Fork repo dan buat branch untuk satu perubahan yang terfokus.
2. Edit paket di `skills/fixen-ui-studio/`; jangan mengubah instalasi global pengguna.
3. Kaitkan referensi baru dari entrypoint atau referensi yang relevan dan jelaskan kapan dibaca. Jangan memaksa semua referensi dimuat setiap tugas.
4. Jalankan `python -m pip install -r requirements-dev.txt` lalu `python scripts/validate.py`.
5. Untuk perubahan perilaku, jalankan setidaknya satu brief realistis yang relevan. Sertakan prompt, kondisi alat, hasil, dan hal yang tidak diuji. Perubahan dokumentasi kecil tidak wajib menjalankan seluruh benchmark.
6. Buka PR dengan masalah, hasil perubahan, dan bukti validasi. Tautkan issue bila ada.

## Standar bukti

- Gunakan data sintetis dan fixture yang hak penggunaannya jelas.
- Catat browser, viewport, renderer, dan versi/konfigurasi yang berpengaruh.
- Bedakan pengecekan statis, simulasi, implementasi, dan uji browser nyata.
- Berikan screenshot jika menilai layout; build sukses bukan bukti desain sukses.
- Jangan mengklaim compliance, skor benchmark, penggunaan alat, atau hak aset tanpa bukti.
- Benchmark perbandingan harus menjaga brief, tools, kondisi, dan rubrik setara.

## Keamanan kontribusi

Jangan sertakan rahasia, token, kredensial, data pribadi, salinan proyek privat, atau eksploit yang membahayakan sistem nyata. Jangan menyisipkan perintah yang diam-diam mengunggah data, mengubah izin, menjalankan payload, atau mengabaikan otorisasi pengguna. Reproduksi keamanan harus minimal, tidak aktif menyerang, dan memakai sandbox/fixture lokal; kirim rincian sensitif melalui proses privat.

Kontribusi dengan penyalahgunaan keamanan, klaim menyesatkan, plagiarisme, atau pelanggaran lisensi akan ditolak. Maintainer dapat menutup issue/PR dan membatasi partisipasi sesuai Code of Conduct. Kebijakan moderasi ini tidak menambahkan pembatasan baru pada MIT.

## Lisensi

Dengan mengirim kontribusi, kamu menyatakan berhak menyumbangkannya dan setuju kontribusi yang diterima tersedia di bawah [MIT License](LICENSE). Aset pihak ketiga harus dicatat dengan lisensinya sendiri; jangan menandainya MIT jika tidak demikian. Tidak ada CLA tambahan untuk kontribusi biasa.
