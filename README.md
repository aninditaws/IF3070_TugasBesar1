# A Diagonal Magic Cube Local Search Solver

## Deskripsi Singkat
<p align="justify"> Proyek ini mengimplementasikan berbagai algoritma local search untuk menyelesaikan masalah Diagonal Magic Cube, di mana tujuannya adalah mengatur angka-angka dalam kubus 5x5x5 sehingga setiap baris, kolom, pilar, dan diagonal memiliki jumlah yang sama dengan magic number. Solusi yang dihasilkan bertujuan meminimalkan selisih dari magic number pada seluruh komponen kubus, sehingga tercapai susunan optimal.

## Algoritma
Berikut merupakan algoritma _local search_ yang implementasikan.
1. _**Steepest Ascent Hill-Climbing**_  
   Bergerak menuju tetangga dengan perbaikan tertinggi hingga mencapai titik maksimum lokal.
2. _**Hill-Climbing dengan Sideways Move**_  
   Mirip dengan steepest ascent, tetapi memungkinkan perpindahan lateral ketika tidak ada perbaikan langsung, untuk menghindari lokal maksimum.
3. _**Random Restart Hill-Climbing**_  
   Melakukan restart dengan kondisi awal acak untuk meningkatkan peluang menemukan solusi optimal global.
4. _**Stochastic Hill-Climbing**_  
   Memilih tetangga secara acak, memungkinkan eksplorasi solusi yang lebih luas.
5. _**Simulated Annealing**_  
   Menggunakan pendekatan berbasis probabilitas untuk menerima solusi yang lebih buruk sesekali, sehingga mengurangi risiko terjebak di lokal maksimum.
6. _**Genetic Algorithm**_  
   Menggunakan seleksi, crossover, dan mutasi untuk mengembangkan populasi solusi menuju susunan optimal.

## Fungsi Objektif
<p align="justify"> Fungsi objektif mengevaluasi setiap keadaan kubus dengan menghitung selisih antara komponen kubus dan magic number. Nilai yang lebih rendah menunjukkan solusi yang lebih dekat dengan susunan optimal.

## Cara Kompilasi Program
1. Clone repository github dan cd ke folder src
```sh
git clone https://github.com/aninditaws/IF3070_TugasBesar1/tree/main
cd src
```
2. Pastikan Anda sudah memiliki library `matplotlib`, apabila belum unduh dengan perintah berikut
```sh
pip install matplotlib
```
3. Compile program
```sh
python main.py
```

## Struktur Program
```
│ README.md
│
├─── doc
│     └─── Tubes1_18222113_18222116_18222123_18222128.pdf
│
├─── src
│     ├─── algorithms
│     │          │ genetic_algorithm.py
│     │          │ random_restart.py
│     │          │ sideways_move.py
│     │          │ simulated_annealing.py
│     │          │ steepest_hill_climbing.py
│     │          │ stochastic.py
│     │
│     ├─── cube
│     │          │ magic_cube.py
│     │
│     └─── main.py
│
└───
```

## Pembagian Tugas
| NIM      | Nama Lengkap           | Tugas                                                                                     |
|----------|------------------------|-------------------------------------------------------------------------------------------|
| 18222113 | Angelica Aliwinata     | Random Restart Hill Climbing                                                              |
| 18222116 | Jason Jahja            | Steepest Ascent Hill Climbing, Hill Climbing with Sideways Move, Stochastic Hill Climbing |
| 18222123 | Melissa Trenggono      | Simulated Annealing                                                                       |
| 18222128 | Anindita Widya Santoso | Genetic Algorithm                                                                         |