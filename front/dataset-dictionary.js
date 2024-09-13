export const mushroomDatasetDictionary = {
    "gill-size": {
      description: "Tamanho da lamela (abaixo do chapéu do cogumelo)",
      mapping: {
        "b": 0, // broad (larga)
        "n": 1  // narrow (estreita)
      },
      reverseMapping: {
        0: "b",
        1: "n"
      },
      labelMapping: {
        0: "larga",
        1: "estreita"
      }
    },
    "gill-color": {
      description: "Cor da lamela",
      mapping: {
        "k": 0, // black (preto)
        "n": 1, // brown (marrom)
        "b": 2, // buff (castanho-claro)
        "h": 3, // chocolate
        "g": 4, // gray (cinza)
        "r": 5, // green (verde)
        "o": 6, // orange (laranja)
        "p": 7, // pink (rosa)
        "u": 8, // purple (roxo)
        "e": 9, // red (vermelho)
        "w": 10, // white (branco)
        "y": 11 // yellow (amarelo)
      },
      reverseMapping: {
        0: "k",
        1: "n",
        2: "b",
        3: "h",
        4: "g",
        5: "r",
        6: "o",
        7: "p",
        8: "u",
        9: "e",
        10: "w",
        11: "y"
      },
      labelMapping: {
        0: "preto",
        1: "marrom",
        2: "castanho claro",
        3: "chocolate",
        4: "cinza",
        5: "verde",
        6: "laranja",
        7: "rosa",
        8: "roxo",
        9: "vermelho",
        10: "branco",
        11: "amarelo"
      }
    },
    "stalk-root": {
      description: "Tipo de raiz do caule",
      mapping: {
        "b": 0, // bulbous (bulbosa)
        "c": 1, // club (em forma de clube)
        "u": 2, // cup (taça)
        "e": 3, // equal (igual)
        "z": 4, // rhizomorphs (rizomorfos)
        "r": 5, // rooted (enraizada)
        "?": 6  // missing (ausente)
      },
      reverseMapping: {
        0: "b",
        1: "c",
        2: "u",
        3: "e",
        4: "z",
        5: "r",
        6: "?"
      },
      labelMapping: {
        0: "bulbosa",
        1: "clava",
        2: "taça",
        3: "uniforme",
        4: "rizomorfa",
        5: "enraizada",
        6: "N/A"
      }
    },
    "ring-type": {
      description: "Tipo de anel no caule",
      mapping: {
        "c": 0, // cobwebby (teia de aranha)
        "e": 1, // evanescent (efêmero)
        "f": 2, // flaring (expandido)
        "l": 3, // large (grande)
        "n": 4, // none (nenhum)
        "p": 5, // pendant (pendente)
        "s": 6, // sheathing (encapado)
        "z": 7  // zone (zona)
      },
      reverseMapping: {
        0: "c",
        1: "e",
        2: "f",
        3: "l",
        4: "n",
        5: "p",
        6: "s",
        7: "z"
      },
      labelMapping: {
        0: "teia de aranha",
        1: "efêmero",
        2: "expandido",
        3: "grande",
        4: "nenhum",
        5: "pendente",
        6: "encapado",
        7: "zona"
      }
    },
    "spore-print-color": {
      description: "Cor do esporo",
      mapping: {
        "k": 0, // black (preto)
        "n": 1, // brown (marrom)
        "b": 2, // buff (castanho-claro)
        "h": 3, // chocolate
        "r": 4, // green (verde)
        "o": 5, // orange (laranja)
        "u": 6, // purple (roxo)
        "w": 7, // white (branco)
        "y": 8 // yellow (amarelo)
      },
      reverseMapping: {
        0: "k",
        1: "n",
        2: "b",
        3: "h",
        4: "r",
        5: "o",
        6: "u",
        7: "w",
        8: "y"
      },
      labelMapping: {
        0: "preto",
        1: "marrom",
        2: "castanho-claro",
        3: "chocolate",
        4: "verde",
        5: "laranja",
        6: "roxo",
        7: "branco",
        8: "amarelo"
      }
    },
    "odor": {
      description: "Odor do cogumelo",
      mapping: {
        "a": 0, // almond (amêndoa)
        "l": 1, // anise (anis)
        "c": 2, // creosote
        "y": 3, // fishy (cheiro de peixe)
        "f": 4, // foul (fétido)
        "m": 5, // musty (mofo)
        "n": 6, // none (nenhum)
        "p": 7, // pungent (pungente)
        "s": 8  // spicy (picante)
      },
      reverseMapping: {
        0: "a",
        1: "l",
        2: "c",
        3: "y",
        4: "f",
        5: "m",
        6: "n",
        7: "p",
        8: "s"
      }
    },
    "population": {
      description: "População de cogumelos",
      mapping: {
        "a": 0, // abundant (abundante)
        "c": 1, // clustered (agrupado)
        "n": 2, // numerous (numeroso)
        "s": 3, // scattered (disperso)
        "v": 4, // several (vários)
        "y": 5  // solitary (solitário)
      },
      reverseMapping: {
        0: "a",
        1: "c",
        2: "n",
        3: "s",
        4: "v",
        5: "y"
      }
    },
    "bruises": {
      description: "Se o cogumelo apresenta machucados",
      mapping: {
        "t": 0, // bruises (sim)
        "f": 1  // no bruises (não)
      },
      reverseMapping: {
        0: "t",
        1: "f"
      }
    },
    "stalk-surface-above-ring": {
      description: "Superfície do caule acima do anel",
      mapping: {
        "f": 0, // fibrous (fibroso)
        "y": 1, // scaly (escamoso)
        "k": 2, // silky (sedoso)
        "s": 3  // smooth (liso)
      },
      reverseMapping: {
        0: "f",
        1: "y",
        2: "k",
        3: "s"
      }
    }
  };
  
  console.log(mushroomDatasetDictionary);
  