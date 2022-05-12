

def moeda_escolhida(op):
    if op == 1:
        return 'USD'
    if op == 2:
        return 'EUR'
    if op == 3:
        return 'JPY'
    if op == 4:
        return 'BRL'
    if op == 5:
        outra_moeda()

def moeda_para_converter(op):
    if op == 1:
        return '"USD"'
    if op == 2:
        return '"EUR"'
    if op == 3:
        return '"JPY"'
    if op == 4:
        return '"BRL"'
    if op == 5:
        outra_moeda()

def outra_moeda():
    print()
    divisor('Selecione uma opção:')
    return 0

def verifica_continente(op):
    if op == 1:
        return africa
    if op == 2:
        return america_norte
    if op == 3:
        return america_do_sul
    if op == 4:
        return asia
    if op == 5:
        return europa
    if op == 6:
        return oceania

def verifica_moeda_continente(op):
    if op == 1:
        return africa_moeda
    if op == 2:
        return america_norte_moeda
    if op == 3:
        return america_do_sul_moeda
    if op == 4:
        return asia_moeda
    if op == 5:
        return europa_moeda
    if op == 6:
        return oceania_moeada


moedas = {1:"Dólar", 2:"Euro", 3:"Iene", 4:"Real", 5:"Outro"}


continentes = { 1:"Africa",
                2:"América do Norte",
                3:"América do Sul",
                4:"Ásia",
                5:"Europa",
                6:"Oceania"}


africa = {  1:"África do Sul",
            2:"Angola",
            3:"Camarões",
            4:"Costa do Marfim",
            5:"Egito",
            6:"Gabão",
            7:"Guiné",
            8:"Marrocos",
            9:"Moçambique",
            10:"Nigéria",
            11:"República do Congo",
            12:"Senegal",
            13:"Tanzânia",
            14:"Tunísia",
            15:"Zâmbia"}

africa_moeda = {1:'"ZAR"',
                2:'"AOA"',
                3:'"XAF"',
                4:'"XOF"',
                5:'"EGP"',
                6:'"XAF"',
                7:'"GNF"',
                8:'"MAD"',
                9:'"MZN"',
                10:'"NGN"',
                11:'"XAF"',
                12:'"XOF"',
                13:'"TZS"',
                14:'"TND"',
                15:'"ZMW"',
                }

america_norte = {   1:"Estados Unidos",
                    2:"Canada",
                    3:"Mexico"}

america_norte_moeda = { 1:'"USD"',
                        2:'"CAD"',
                        3:'"MXN"',}

america_do_sul = {  1:"Argentina",
                    2:"Bolívia",
                    3:"Brasil",
                    4:"Chile",
                    5:"Colômbia",
                    6:"Equador",
                    7:"Guiana",
                    8:"Paraguai",
                    9:"Peru",
                    10:"Suriname",
                    11:"Uruguai",
                    12:"Venezuela"}

america_do_sul_moeda = {1:'"ARS"',
                        2:'"BOB"',
                        3:'"BRL"',
                        4:'"CLP"',
                        5:'"COP"',
                        6:'"USD"',
                        7:'"GYD"',
                        8:'"PYG"',
                        9:'"PEN"',
                        10:'"SRD"',
                        11:'"UYU"',
                        12:'"VED"',}

asia = {    1:"Afeganistão",
            2:"Arábia Saudita",
            3:"Azerbaijão",
            4:"Bahrein",
            5:"Bangladesh",
            6:"Brunei",
            7:"Camboja",
            8:"Cazaquistão",
            9:"Catar",
            10:"China",
            11:"Chipre",
            12:"Singapura",
            13:"Coreia do Norte",
            14:"Coreia do Sul",
            15:"Egito",
            16:"Emirados Árabes Unidos",
            17:"Geórgia",
            18:"Índia",
            19:"Indonésia",
            20:"Iraque",
            21:"Israel",
            22:"Jordânia",
            23:"Kuwait",
            24:"Laos",
            25:"Líbano",
            26:"Malásia",
            27:"Myanmar",
            28:"Mongólia",
            29:"Nepal",
            30:"Omã",
            31:"Paquistão",
            32:"Quirguistão",
            33:"Rússia",
            34:"SriLanka",
            35:"Tajiquistão",
            36:"Tailândia",
            37:"Timor-Leste",
            38:"Turquemenistão",
            39:"Turquia",
            40:"Uzbequistão",
            41:"Vietnã",}

asia_moeda = {  1:'"AFN"',
                2:'"SAR"',
                3:'"AZN"',
                4:'"BHD"',
                5:'"BDT"',
                6:'"BND"',
                7:'"KHR"',
                8:'"KZT"',
                9:'"QAR"',
                10:'"CNY"',
                11:'"EUR"',
                12:'"SGD"',
                13:'"KPW"',
                14:'"KRW"',
                15:'"EGP"',
                16:'"AED"',
                17:'"GEL"',
                18:'"INR"',
                19:'"IDR"',
                20:'"IQD"',
                21:'"ILS"',
                22:'"JOD"',
                23:'"KWD"',
                24:'"LAK"',
                25:'"LBP"',
                26:'"MYR"',
                27:'"MMK"',
                28:'"MNT"',
                29:'"NPR"',
                30:'"OMR"',
                31:'"PKR"',
                32:'"KGS"',
                33:'"RUB"',
                34:'"LKR"',
                35:'"TJS"',
                36:'"THB"',
                37:'"USD"',
                38:'"TMT"',
                39:'"TRY"',
                40:'"UZS"',
                41:'"VND"',
                }

oceania = { 1:"Austrália",
            2:"Estados Federados da Micronésia",
            3:"Fiji",
            4:"Ilhas Marshall",
            5:"Ilhas Salomão",
            6:"Kiribati",
            7:"Nauru",
            8:"Nova Zelândia",
            9:"Palau",
            10:"Papua Nova Guiné",
            11:"Samoa",
            12:"Tonga",
            13:"Tuvalu",
            14:"Vanuatu"}

oceania_moeada = {  1:'"AUD"',
                    2:'"USD"',
                    3:'"FJD"',
                    4:'"USD"',
                    5:'"SBD"',
                    6:'"AUD"',
                    7:'"AUD"',
                    8:'"NZD"',
                    9:'"USD"',
                    10:'"PGK"',
                    11:'"WST"',
                    12:'"TOP"',
                    13:'"AUD"',
                    14:'"VUV"',
                    }

europa = {  1:"Albânia",
            2:"Alemanha",
            3:"Andorra",
            4:"Áustria",
            5:"Bélgica",
            6:"Bielorrússia",
            7:"Bósnia e Herzegovina",
            8:"Bulgária",
            9:"Cazaquistão",
            10:"Chipre",
            11:"Croácia",
            12:"Dinamarca",
            13:"Eslováquia",
            14:"Eslovénia",
            15:"Espanha",
            16:"Estónia",
            17:"Finlândia",
            18:"França",
            19:"Grécia",
            20:"Hungria",
            21:"República da Irlanda",
            22:"Islândia",
            23:"Itália",
            24:"Letónia",
            25:"Liechtenstein",
            26:"Lituânia",
            27:"Luxemburgo",
            28:"Malta",
            29:"Moldávia",
            30:"Mónaco",
            31:"Montenegro",
            32:"Noruega",
            33:"Polónia",
            34:"Portugal",
            35:"Chéquia",
            36:"Macedónia do Norte",
            37:"Reino Unido",
            38:"Reino Unido",
            39:"Romênia",
            40:"Rússia",
            41:"San Marino",
            42:"Sérvia",
            43:"Suécia",
            44:"Suíça",
            45:"Turquia",
            46:"Vaticano"}

europa_moeda = {1:'"ALL"',
                2:'"EUR"',
                3:'"EUR"',
                4:'"EUR"',
                5:'"EUR"',
                6:'"BYN"',
                7:'"BAM"',
                8:'"BGN"',
                9:'"KZT"',
                10:'"EUR"',
                11:'"HRK"',
                12:'"DKK"',
                13:'"EUR"',
                14:'"EUR"',
                15:'"EUR"',
                16:'"EUR"',
                17:'"EUR"',
                18:'"EUR"',
                19:'"EUR"',
                20:'"HUF"',
                21:'"EUR"',
                22:'"ISK"',
                23:'"EUR"',
                24:'"EUR"',
                25:'"CHF"',
                26:'"EUR"',
                27:'"EUR"',
                28:'"EUR"',
                29:'"MDL"',
                30:'"EUR"',
                31:'"EUR"',
                32:'"NOK"',
                33:'"PLN"',
                34:'"EUR"',
                35:'"CZK"',
                36:'"MKD"',
                37:'"GBP"',
                38:'"GBP"',
                39:'"RON"',
                40:'"RUB"',
                41:'"EUR"',
                42:'"RSD"',
                43:'"SEK"',
                44:'"CHF"',
                45:'"TRY"',
                46:'"EUR"'}