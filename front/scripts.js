
const getDataForList = () => {

  let url = 'http://127.0.0.1:5000/listar_cogumelos';
  fetch(url, {
    method: 'get',
  })
    .then((response) => response.json())
    .then((data) => {
      data["cogumelos"].forEach(item => {
        addDataToList(item);
      })
    })
    .catch((error) => {
      console.error('Error:', error);
    });

}

getDataForList();

const addDataToList = (data) => {


  let columns = ["name", 'gill_size', 'gill_color', 'stalk_root', 'ring_type', 'spore_print_color', 'odor', 'population',
    'bruises', 'stalk_surface_above_ring', 'outcome'];


  let table = document.getElementById('table');


  let row = table.insertRow();
  let name = data.name.replace(' ',"_");
  row.id = `${name}_Row`;

  for (let i = 0; i < columns.length; i++) {

    let cell = row.insertCell(i);
    let cellValue = data[columns[i]];
    let colName = columns[i];

    if (colName != 'name') {
      cellValue = mushroomDatasetDictionary[colName].labelMapping[cellValue];
    }


    cell.textContent = cellValue;
  }

  insertRemoveButton(row.insertCell(-1), data.name);

}

//exibe o formulario de novo registro e esconde a tabela e o botao de adicionar novo registro
const showForm = () => {

  let newDataContainer = document.getElementById('newDataContainer');
  newDataContainer.removeAttribute('hidden');

  let tableContainer = document.getElementById('tableContainer');
  tableContainer.setAttribute('hidden', null);

  let btnContainer = document.getElementById('btnContainer');
  btnContainer.setAttribute('hidden', null);

}

//Limpa os dados do form, esconde o form e exibe a lista e o botão de inserção de novo registro
const resetForm = () => {

  let nameElement = document.getElementById('name');
  nameElement.value = '';

  document.querySelectorAll('select')
    .forEach(element => {
      element.value = 0;
    });

  let tableContainer = document.getElementById('tableContainer');
  tableContainer.removeAttribute('hidden');

  let btnContainer = document.getElementById('btnContainer');
  btnContainer.removeAttribute('hidden');

  let newDataContainer = document.getElementById('newDataContainer');
  newDataContainer.setAttribute('hidden', null);

}

//Método para executar o commit das operações realizadas no formulário
const commitOperation = () => {
  let formData = processData();
  if (formData === undefined) {
    return;
  }
  
  postData(formData);
  resetForm();
  

}


//Metodo para processar os dados inseridos no formulario
const processData = () => {


  let data = {};
  data["name"] = document.getElementById("name").value || 'Cogumelo';


  document.querySelectorAll('select')
    .forEach(element => {


      let attr = element.id.replace("_select", "");
      data[attr] = element.value;



    });

  return data;

}



//Seção com métodos para criar botões programaticamente
const insertRemoveButton = (parent, name) => {
  let removeBtn = document.createElement("button");
  removeBtn.setAttribute('name', name);
  removeBtn.classList.add('icon-button', 'matter-button-contained');
  removeBtn.innerHTML = '<i class="fa fa-trash">';
  parent.appendChild(removeBtn);

  removeBtn.onclick = () => removeDataFromList(name);

}




const removeDataFromList = (name) => {

  let rowName = name.replace(" ","_");

  let row = document.getElementById(`${rowName}_Row`);

  if (confirm("Deseja remover o registro?")) {
    row.remove();
    removeData(name);
  }

}

const postData = (data) => {


  let url = 'http://127.0.0.1:5000/inserir_predicao';


  
  fetch(url, {
      method: 'post',
      body:  JSON.stringify(data),
      headers: { "Content-type": "application/json; charset=UTF-8" }
  })
      .then((response) =>  response.json())
      .then((data) => {
        console.log(data)
        window.location.reload();
      })
      .catch((error) => {
          console.error('Error:', error);
      });

}

const removeData = (name) => {
  let url = `http://127.0.0.1:5000/deletar_cogumelo?name=${name}`;
  fetch(url, {
      method: 'delete'
  })
      .then((response) => response.json())
      .catch((error) => {
          console.error('Error:', error);
      });
}




const mushroomDatasetDictionary = {
  "gill_size": {
    description: "Tamanho da lamela (abaixo do chapéu do cogumelo)",
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