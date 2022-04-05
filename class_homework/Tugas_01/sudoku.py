def find_empty(puzzle):
    """
    subroutine untuk mencari indeks baris dan indeks kolom
    yang tidak terisi.

    argumen
    ---------
    puzzle:
        list dengan 9 elemen yang setiap elemennya
        adalah list berisi 9 elemen

    return
    ---------
    row, col:
        index dari baris dan kolom yang kosong, jika puzzle sudah
        penuh maka return None, None
    """
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == 0: return row, col
    return None, None


def is_valid(puzzle, guess, row, col):
    """
    subroutine untuk melihat apakah tebakan untuk mengisi
    sel yang kosong valid. Subroutine ini melakukan horizontal
    scan, kemudian vertical scan dan terakhir local grid scan.

    argumen
    --------
    puzzle:
        puzzle sudoku (list of lists)
    guess:
        tebakan angka untuk mengisi sudoku
    row:
        indeks baris yang ingin diisi
    col:
        indeks kolom yang ingin diisi

    return
    ---------
    boolean:
        jika tidak ditemukan angka yang sama dari hasil
        horizontal scan dan vertical scan dan local grid scan,
        maka return True, jika tidak maka False.
    """

    # horizontal scan
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    # vertical scan
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    
    # local grid scan (mini 3x3 grid)
    # cari indeks awal grid 3x3 dimana row, col berada
    row_start = (row//3) * 3
    col_start = (col//3) * 3

    for r in range(row_start, row_start+3):
        for c in range(col_start, col_start+3):
            if puzzle[r][c] == guess:
                return False

    return True


def solve_sudoku(puzzle):
    # Fungsi utama

    # 1. cari sel kosong
    row, col = find_empty(puzzle)

    # jika row atau col == None, maka puzzle sudah selesai
    if row is None:
        return True
        
    
    # 2. jika ada sel kosong, buat tebakan dengan nilai 1 sampai 9
    for guess in range(1, 10):
        
        # 3. cek apakah tebakannya valid
        # atau tidak ada elemen yg sama dalam satu baris, kolom, dan grid lokal
        if is_valid(puzzle, guess, row, col):

            # Jika valid, maka ganti nilai di puzzle[row][col]
            # dengan tebakannya
            puzzle[row][col] = guess

            # 4. panggil fungsi secara rekursif
            if solve_sudoku(puzzle):
                return True


        # 5. Jika tidak valid maka ubah kembali nilai sel menjadi 0
        puzzle[row][col] = 0

    # 6. jika tidak ada solusi, maka puzzle tidak bisa diselesaikan
    return False


if __name__ == "__main__":

    from pprint import pprint
    
    puzzle =[[5, 3, 0, 0, 7, 0, 0, 0, 0],
             [6, 0, 0, 1, 9, 5, 0, 0, 0],
             [0, 9, 8, 0, 0, 0, 0, 6, 0],
             [8, 0, 0, 0, 6, 0, 0, 0, 3],
             [4, 0, 0, 8, 0, 3, 0, 0, 1],
             [7, 0, 0, 0, 2, 0, 0, 0, 6],
             [0, 6, 0, 0, 0, 0, 2, 8, 0],
             [0, 0, 0, 4, 1, 9, 0, 0, 5],
             [0, 0, 0, 0, 8, 0, 0, 7, 9]]

    solve_sudoku(puzzle)
    pprint(puzzle)

























    
    
