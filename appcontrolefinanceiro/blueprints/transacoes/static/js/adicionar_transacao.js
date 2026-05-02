// submit do botão confirmar id=btn-confirmar
document
  .getElementById("form-add-transaction")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData.entries());

    // Limpa a formatação de moeda para enviar apenas o número
    if (data.valor) {
      data.valor = parseFloat(data.valor.replace(/\./g, "").replace(",", "."));
    }

    sendTransaction(data).then((response) => {
      console.log(response);
    });
  });

async function sendTransaction(data) {
  try {
    const content = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    };
    const response = await fetch("/transacoes/add_transaction", content);

    if (!response.ok) {
      throw new Error("Erro ao adicionar transação");
    }

    const responseData = await response.json();
    return responseData;
  } catch (error) {
    console.log(error);
    return error;
  }
}

// Máscara de Moeda para o campo Valor
const inputValor = document.getElementById("valor");
inputValor.addEventListener("input", function (e) {
  let value = e.target.value.replace(/\D/g, "");
  value = (value / 100).toFixed(2) + "";
  value = value.replace(".", ",");
  value = value.replace(/(\d)(?=(\d{3})+(?!\d))/g, "$1.");
  e.target.value = value;
});
