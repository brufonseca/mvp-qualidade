
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

  let columns = ["name", 'gill_size', 'gill_color', 'stalk_root', 'ring_type', 'spore_print_color', 'odor', 'population',
    'bruises', 'stalk_surface_above_ring', 'outcome'];


  let table = document.getElementById('table');


  let row = table.insertRow();
  row.id = `${entry.id}_Row`;





  for (let i = 0; i < columns.length; i++) {

    let cell = row.insertCell(i);
    let cellValue =  entry[columns[i]];
    let colName = columns[i];

    if(colName!='name'){
      cellValue = mushroomDatasetDictionary[colName].labelMapping[cellValue];
    }
    
    
    cell.textContent = cellValue;
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
  removeBtn.classList.add('icon-button', 'matter-button-contained');
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
  "gill_size": {
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
      0: "Larga",
      1: "Estreita"
    }
  },
  "gill_color": {
    description: "Cor da lamela",
    mapping: {
      "k": 4, // black (preto)
      "n": 5, // brown (marrom)
      "b": 0, // buff (castanho-claro)
      "h": 3, // chocolate
      "g": 2, // gray (cinza)
      "r": 8, // green (verde)
      "o": 6, // orange (laranja)
      "p": 7, // pink (rosa)
      "u": 9, // purple (roxo)
      "e": 1, // red (vermelho)
      "w": 10, // white (branco)
      "y": 11 // yellow (amarelo)
    },
    reverseMapping: {
      4: "k",
      5: "n",
      0: "b",
      3: "h",
      2: "g",
      8: "r",
      6: "o",
      7: "p",
      9: "u",
      1: "e",
      10: "w",
      11: "y"
    },
    labelMapping: {
      4: "Preto",
      5: "Marrom",
      0: "Castanho claro",
      3: "Chocolate",
      2: "Cinza",
      8: "Verde",
      6: "Laranja",
      7: "Rosa",
      9: "Roxo",
      1: "Vermelho",
      10: "Branco",
      11: "Amarelo"
    }
  },
  "stalk_root": {
    description: "Tipo de raiz do caule",
    mapping: {
      "b": 1, // bulbous (bulbosa)
      "c": 2, // club (em forma de clube)
      "e": 3, // equal (igual)
      "?": 0  // missing (ausente)
    },
    reverseMapping: {
      1: "b",
      2: "c",
      3: "e",
      0: "?"
    },
    labelMapping: {
      1: "Bulbosa",
      2: "Clava",
      3: "Uniforme",
      0: "N/A"
    }
  },
  "ring_type": {
    description: "Tipo de anel no caule",
    mapping: {
      "e": 0, // evanescent (efêmero)
      "f": 1, // flaring (expandido)
      "l": 2, // large (grande)
      "n": 3, // none (nenhum)
      "p": 4, // pendant (pendente)
    },
    reverseMapping: {
      0: "e",
      1: "f",
      2: "l",
      3: "n",
      4: "p",
    },
    labelMapping: {
      0: "Efêmero",
      1: "Expandido",
      2: "Grande",
      3: "Nenhum",
      4: "Pendente",
    }
  },
  "spore_print_color": {
    description: "Cor do esporo",
    mapping: {
      "k": 2, // black (preto)
      "n": 3, // brown (marrom)
      "b": 0, // buff (castanho-claro)
      "h": 1, // chocolate
      "r": 5, // green (verde)
      "o": 4, // orange (laranja)
      "u": 6, // purple (roxo)
      "w": 7, // white (branco)
      "y": 8 // yellow (amarelo)
    },
    reverseMapping: {
      2: "k",
      3: "n",
      0: "b",
      1: "h",
      5: "r",
      4: "o",
      6: "u",
      7: "w",
      8: "y"
    },
    labelMapping: {
      2: "Preto",
      3: "Marrom",
      0: "Castanho claro",
      1: "Chocolate",
      5: "Verde",
      4: "Laranja",
      6: "Roxo",
      7: "Branco",
      8: "Amarelo"
    }
  },
  "odor": {
    description: "Odor do cogumelo",
    mapping: {
      "a": 0, // almond (amêndoa)
      "l": 3, // anise (anis)
      "c": 1, // creosote
      "y": 8, // fishy (cheiro de peixe)
      "f": 2, // foul (fétido)
      "m": 4, // musty (mofo)
      "n": 5, // none (nenhum)
      "p": 6, // pungent (pungente)
      "s": 7  // spicy (picante)
    },
    reverseMapping: {
      0: "a",
      3: "l",
      1: "c",
      8: "y",
      2: "f",
      4: "m",
      5: "n",
      6: "p",
      7: "s"
    },
    labelMapping: {
      0: "Amêndoa",
      3: "Anis",
      1: "Creosote",
      8: "Peixe",
      2: "Fétido",
      4: "Mofo",
      5: "Nenhum",
      6: "Pungente",
      7: "Picante"
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
    },
    labelMapping: {
      0: "Abundante",
      1: "Agrupado",
      2: "Numeroso",
      3: "Disperso",
      4: "Vários",
      5: "Solitário"
    }
  },
  "bruises": {
    description: "Se o cogumelo apresenta manchas",
    mapping: {
      "t": 0, // bruises (sim)
      "f": 1  // no bruises (não)
    },
    reverseMapping: {
      0: "t",
      1: "f"
    },
    labelMapping: {
      0: "Sim",
      1: "Não"
    }
  },
  "stalk_surface_above_ring": {
    description: "Superfície do caule acima do anel",
    mapping: {
      "f": 0, // fibrous (fibroso)
      "y": 3, // scaly (escamoso)
      "k": 1, // silky (sedoso)
      "s": 2  // smooth (liso)
    },
    reverseMapping: {
      0: "f",
      3: "y",
      1: "k",
      2: "s"
    },
    labelMapping: {
      0: "Fibroso",
      3: "Escamoso",
      1: "Sedoso",
      2: "Liso"
    }
  },
  "outcome": {
    description: "Classificação do cogumelo",
    mapping: {
      "e": 0, // edible (comestivel)
      "p": 1, // poisonous (venenoso)
    },
    reverseMapping: {
      0: "e",
      1: "p",
    },
    labelMapping: {
      0: "Comestível",
      1: "Venenoso",
    }
  }
};