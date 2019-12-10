""" Prevezme data filmu a presklada je do podoby tabulky v HTML """

def uloz_data_do_html_stranky(data):
    hlavicka_stranky = """<html><head></head><body>"""
    paticka_stranky = """</body></html>"""
    nazev_souboru = 'index.html'
    fw = open(nazev_souboru, 'w')
    fw.write(hlavicka_stranky + data + paticka_stranky)
    fw.close()

def radek_dat_do_html(radek):
    html_radek = """<tr>
                        <td>{}</td>
                        <td>{}</td>
                        <td>{}</td>
                        <td>{}</td>
                    <tr>""".format(radek[0], radek[1], radek[2], radek[3],)
    return html_radek


def tabulka_html(data_filmu):
    html_radky_tabulky = ""
    for radek in data_filmu:
        html_radky_tabulky += radek_dat_do_html(radek)
    return "<table>" + html_radky_tabulky + "</table>"


