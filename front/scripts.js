
const getEntriesForList = () => {

    let url = 'http://127.0.0.1:5000/listar_cogumelos';
    fetch(url, {
        method: 'get',
    })
        .then((response) => response.json())
        .then((data) => {
            data["cogumelos"].forEach(entry => {


                console.log(entry);

                    addEntryToList(entry);
            


            })
        })
        .catch((error) => {
            console.error('Error:', error);
        });

}

getEntriesForList();

const addEntryToList = (entry) => {

    let columns = ["name", 'gill_size', 'gill_color', 'stalk_root', 'ring_type', 'spore_print_color','odor','population',
           'bruises','stalk_surface_above_ring', 'outcome'];


    let table = document.getElementById('table');


    let row = table.insertRow();
    row.id = `${entry.id}_Row`;
    
    



    for (let i = 0; i < columns.length; i++) {

        let cell = row.insertCell(i);
        cell.textContent = entry[columns[i]];
    }

    insertRemoveButton(row.insertCell(-1), entry.id)

}

//exibe o formulario de novo registro e esconde a tabela e o botao de adicionar novo registro
const showEntryForm = () => {

    let newEntryContainer = document.getElementById('newEntryContainer');
    newEntryContainer.removeAttribute('hidden');

    let tableContainer = document.getElementById('tableContainer');
    tableContainer.setAttribute('hidden', null);

    let btnContainer = document.getElementById('btnContainer');
    btnContainer.setAttribute('hidden', null);

}

//Seção com métodos para criar botões programaticamente
const insertRemoveButton = (parent, entryId) => {
    let removeBtn = document.createElement("button");
    removeBtn.setAttribute('entryId', entryId);
    removeBtn.classList.add('icon-button','matter-button-contained');
    removeBtn.innerHTML = '<i class="fa fa-trash">';
    parent.appendChild(removeBtn);

    removeBtn.onclick = () => removeEntryFromList(entryId);

}

const removeEntryFromList = (entryId) => {

    let row = document.getElementById(`${entryId}_Row`);

    if (confirm("Deseja remover o registro?")) {
        row.remove();
        //removeEntry(entryId);
    }

}





const mushroomDatasetDictionary = {
    "gill-size": {
      description: "Tamanho da lamela (abaixo do chapéu do cogumelo)",
      mapping: {
        "b": 0, // broad (larga)
        "n": 1  // narrow (estreita)
      },
      reverseMapping: {
        0: "b",
        1: "n"
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
  