from varasto import Varasto

def printer(eka, tok = None, kol = None, nel = None, vii = None):

    print(eka)
    if tok is not None:
        print(tok)
    if kol is not None:
        print(kol)
    if nel is not None:
        print(nel)
    if vii is not None:
        print(vii)

def osa_yks(mehua, olutta):
    printer("Luonnin jälkeen:", f"Mehuvarasto: {mehua}",
    f"Olutvarasto: {olutta}", "Olut getterit:",
    f"saldo = {olutta.saldo}", )
    printer(f"tilavuus = {olutta.tilavuus}",
    f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}", 
    "Mehu setterit:", "Lisätään 50.7")

def lisaa_ja_ota(nestet):
    nestet.lisaa_varastoon(50.7)
    printer(f"Mehuvarasto: {nestet}", "Otetaan 3.14")
    nestet.ota_varastosta(3.14)
    printer(f"Mehuvarasto: {nestet}", "Virhetilanteita:",
    "Varasto(-100.0);")
    return nestet

def main(mehua, olutta):
    osa_yks(mehua, olutta)

    mehua = lisaa_ja_ota(mehua)

    huono = Varasto(-100.0)
    printer(huono, "Varasto(100.0, -50.7)")

    huono = Varasto(100.0, -50.7)
    printer(huono, f"Olutvarasto: {olutta}",
    "olutta.lisaa_varastoon(1000.0)")

    olutta.lisaa_varastoon(1000.0)
    printer(f"Olutvarasto: {olutta}", f"Mehuvarasto: {mehua}",
    "mehua.lisaa_varastoon(-666.0)")

    mehua.lisaa_varastoon(-666.0)
    printer(f"Mehuvarasto: {mehua}", f"Olutvarasto: {olutta}",
    "olutta.ota_varastosta(1000.0)")

    saatiin = olutta.ota_varastosta(1000.0)
    printer(f"saatiin {saatiin}", f"Olutvarasto: {olutta}",
    f"Mehuvarasto: {mehua}", "mehua.otaVarastosta(-32.9)")

    saatiin = mehua.ota_varastosta(-32.9)
    printer(f"saatiin {saatiin}", f"Mehuvarasto: {mehua}")

if __name__ == "__main__":
    main(Varasto(100.0), Varasto(100.0, 20.2))
