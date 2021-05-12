import typer

menu_dict = {}
pesanan_dict = {}
total_dict = {}
bayar_dict = {}

def main(
    menu: str = typer.Option(..., prompt=True),
    pesanan: str = typer.Option(..., prompt=True),
    diskon: int = typer.Option(..., prompt=True),
    ongkir: int = typer.Option(..., prompt=True)
    ):

    menu_list = menu.replace(" ", "").split(",")
    for m in menu_list:
        harga = m.split(":")
        menu_dict[harga[0]] = int(harga[1])

    # for m in menu_dict:
        # typer.echo(f"{m} : {menu_dict[m]}")

    pesanan_list = pesanan.replace(" ", "").split(";")
    orang = len(pesanan_list)
    for p in pesanan_list:
        beli = p.split(":")
        pesanan_dict[beli[0]] = beli[1]

    # for p in pesanan_dict:
        # typer.echo(f"{p} : {pesanan_dict[p]}")

    total_semua = 0
    for p in pesanan_dict:
        beli_list = pesanan_dict[p].split(",")

        total = 0
        for b in beli_list:
            total += menu_dict[b]

        total_dict[p] = total
        total_semua += total

    # typer.echo(f"{total_semua}")
    # for t in total_dict:
        # typer.echo(f"{t} : {total_dict[t]}")

    total_bayar = total_semua - diskon
    for t in total_dict:
        presentase = total_dict[t] / total_semua
        bayar = round(presentase*total_bayar) + round(ongkir/orang)
        bayar_dict[t] = bayar

    typer.echo(f"===== TAGIHAN =====")
    for b in bayar_dict:
        typer.echo(f"{b}: {bayar_dict[b]}")
    
if __name__ == "__main__":
    typer.run(main)
