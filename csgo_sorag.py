import random

# CS:GO Ekspert Wiktorinasy - 40 sany kyn sorag
questions = [
    {"q": "CS:GO-da 128-tick serwerde böküp 'smoke' zyňmak üçin näme ulanylmaly?", "o": ["Jump-throw bind", "Run-throw", "Crouch-jump", "Diňe garaşmak"], "a": "Jump-throw bind"},
    {"q": "M4A1-S-iň sesi öçürijisi (silencer) aýrylsa näme bolýar?", "o": ["Has uly ses we pes takyklyk", "Has köp zeper", "Oklar has çalt uçýar", "Heç zat üýtgemeýär"], "a": "Has uly ses we pes takyklyk"},
    {"q": "CS:GO-da 'Wallbang' arkaly öldürende haýsy nyşan peýda bolýar?", "o": ["Diwaryň deşigi", "Sary ýyldyz", "Nyşanyň içinden ok", "Gyzyl nokat"], "a": "Nyşanyň içinden ok"},
    {"q": "Haýsy oýunçy iň köp 'Major' çempionlygyny gazandy (4 gezek)?", "o": ["S1mple", "Device", "NiKo", "ZywOo"], "a": "Device"},
    {"q": "Bomba (C4) goýlanda näçe sekuntda ýarylýar (resmi düzgün)?", "o": ["35 sekunt", "40 sekunt", "45 sekunt", "30 sekunt"], "a": "40 sekunt"},
    {"q": "Glock-18 'Burst Fire' rejiminde bir gezekde näçe ok atýar?", "o": ["2", "3", "4", "5"], "a": "3"},
    {"q": "Olofmeister 'Boost' wakasy haýsy kartada boldy?", "o": ["Overpass", "Dust II", "Train", "Mirage"], "a": "Overpass"},
    {"q": "CS:GO-da 'Kevlar + Helmet' bolan oýunçyny 1 okda kellesinden öldürip bilmeýän pistolet?", "o": ["Desert Eagle", "P250", "Glock-18", "R8 Revolver"], "a": "Glock-18"},
    {"q": "AWP-niň 'Kill Award' (öldürmek baýragy) näçe dollar?", "o": ["$300", "$100", "$50", "$600"], "a": "$100"},
    {"q": "Zeus x27 bilen öldürmek näçe dollar berýär?", "o": ["$0", "$300", "$100", "$1500"], "a": "$0"},
    {"q": "Haýsy karta 'Active Duty' sanawyndan iň soňky bolup aýryldy?", "o": ["Dust II", "Cache", "Train", "Overpass"], "a": "Overpass"},
    {"q": "Kewlar (bronýa) oýunçynyň hereketini näçe göterim haýalladýar?", "o": ["0%", "5%", "10%", "2%"], "a": "0%"},
    {"q": "Souvenir skinler haýsy sandyklardan çykýar?", "o": ["Major paketleri", "Operation cases", "Prime drop", "Heç haýsy"], "a": "Major paketleri"},
    {"q": "CS:GO-da 'Big Apple' lakamy haýsy oýunça degişli?", "o": ["EliGE", "S1mple", "Rain", "Lekr0"], "a": "EliGE"},
    {"q": "AK-47-niň 'Recoil' (yza urmasy) haýsy harpa meňzeýär?", "o": ["T", "S", "L", "7"], "a": "7"},
    {"q": "Haýsy ýaragda iň köp ok bar (zapasy bilen)?", "o": ["Negev", "M249", "PP-Bizon", "P90"], "a": "PP-Bizon"},
    {"q": "Inferno kartasyndaky 'Graveyard' (Gonamçylyk) nirede?", "o": ["A saýt", "B saýt", "Mid", "T spawn"], "a": "A saýt"},
    {"q": "Bombany çözmek üçin 'Kit' bolmasa näçe sekunt gerek?", "o": ["5", "10", "15", "8"], "a": "10"},
    {"q": "Scout (SSG 08) ýaragynda bökülen wagty takyklyk barmy?", "o": ["Hawa", "Ýok", "Diňe aşak gaýdanda", "Diňe iň ýokary nokatda"], "a": "Diňe iň ýokary nokatda"},
    {"q": "Oýunda iň çalt ýöreýän ýarag haýsysy?", "o": ["Pyçak", "Scout", "Negev", "Pyçak we Scout meňzeş"], "a": "Pyçak we Scout meňzeş"},
    {"q": "Stickerleriň 'Wear' (köneleme) derejesi barmy?", "o": ["Hawa", "Ýok", "Diňe käbirlerinde", "Diňe Majorlarda"], "a": "Hawa"},
    {"q": "Oýunda 'God mode' açmak üçin haýsy komanda ýazylýar?", "o": ["sv_cheats 1; god", "give god", "cl_god 1", "set_health 999"], "a": "sv_cheats 1; god"},
    {"q": "Ulag (maşyn) sürülýän resmi karta haýsy?", "o": ["Heç haýsy", "Dust II", "Danger Zone kartalary", "Overpass"], "a": "Danger Zone kartalary"},
    {"q": "He Grenade (oskolok) iň köp näçe zeper ýetirip bilýär?", "o": ["98", "100", "50", "120"], "a": "98"},
    {"q": "CZ75-Auto öldürse näçe dollar berýär?", "o": ["$300", "$100", "$600", "$50"], "a": "$100"},
    {"q": "Mirage kartasynda 'Palace' nirede?", "o": ["B girelge", "A girelge", "Underpass", "Connector"], "a": "A girelge"},
    {"q": "Haýsy Major turnyry iň uly baýrak fonduna ($2 mln) eýe boldy?", "o": ["PGL Stockholm 2021", "Berlin 2019", "Katowice 2014", "Paris 2023"], "a": "PGL Stockholm 2021"},
    {"q": "CS:GO-da haýsy ýaragda 'Double Zoom' (iki gat ulaltma) bar?", "o": ["AWP", "SSG 08", "AUG", "AWP we SSG 08"], "a": "AWP we SSG 08"},
    {"q": "Bomba goýlandan soň näçe sekunt geçse çözüp ýetişip bolmaýar (kitli)?", "o": ["35.1", "34.9", "30.0", "39.0"], "a": "35.1"},
    {"q": "Haýsy skin 'StatTrak' bolup bilmeýär?", "o": ["Gloves (Ellikler)", "Knives (Pyçaklar)", "Dragon Lore", "M4A1-S"], "a": "Gloves (Ellikler)"},
    {"q": "Train kartasynda 'Green' diýlip haýsy wagon aýdylýar?", "o": ["B saýtdaky", "A saýtdaky", "Popdog", "T spawn"], "a": "A saýtdaky"},
    {"q": "Nova drobwiginiň 'Kill Award' puly näçe?", "o": ["$300", "$600", "$900", "$100"], "a": "$900"},
    {"q": "Oýunçynyň iň ýokary saglyk (HP) mukdary näçe (adaty)?", "o": ["100", "110", "150", "200"], "a": "100"},
    {"q": "Glock-18 'Water Elemental' skini haýsy reňkde?", "o": ["Gök", "Gyzyl", "Sary", "Ýaşyl"], "a": "Gyzyl"},
    {"q": "Dust II-de 'Xbox' nirede?", "o": ["A-long", "Mid (orta)", "B-dark", "T-spawn"], "a": "Mid (orta)"},
    {"q": "Nuke kartasynda näçe sany 'vent' (wentilýasiýa) bar?", "o": ["1", "2", "3", "4"], "a": "2"},
    {"q": "Mac-10 ýaragy diňe haýsy tarapda bar?", "o": ["CT", "T", "Iki tarapda-da", "Diňe Majorlarda"], "a": "T"},
    {"q": "Oýunda 'Flash' iň köp näçe sekunt kör edip bilýär?", "o": ["4.87", "6.20", "3.50", "5.50"], "a": "4.87"},
    {"q": "Haýsy 'Case' (sandyk) iň köne?", "o": ["Chroma", "Weapon Case 1", "Operation Bravo", "Phoenix"], "a": "Weapon Case 1"},
    {"q": "Oýunda 'Defuse Kit' satyn almagyň bahasy näçe?", "o": ["$200", "$400", "$600", "$100"], "a": "$400"}
]

def run_hard_quiz():
    random.shuffle(questions)
    score = 0
    total = len(questions)
    
    print("=== CS:GO EKSPERT WIKTORINASY (40 SORAG) ===")
    
    for i, item in enumerate(questions):
        print(f"\n{i+1}/{total}: {item['q']}")
        for idx, opt in enumerate(item['o']):
            print(f"  {idx+1}) {opt}")
        
        try:
            ans = int(input("Jogabyňyz (1-4): "))
            if item['o'][ans-1] == item['a']:
                print("Dogry! 🎯")
                score += 1
            else:
                print(f"Ýalňyş! ⚠️ Dogry: {item['a']}")
        except:
            print("Ýalňyş giriş, indiki soraga geçildi.")

    print(f"\nNetije: {score}/{total}")
    if score == total: print("Siz hakyky CS:GO Legendasy!")
    elif score > 30: print("Gaty gowy bilim!")
    else: print("Has köp türgenleşmeli.")

if __name__ == "__main__":
    run_hard_quiz()
