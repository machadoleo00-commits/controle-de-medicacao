document.getElementById("ativar-alertas").addEventListener("click", function() {
    Notification.requestPermission().then(function(resposta) {
        if (resposta === "granted") {
            new Notification("Alertas ativados", { body: "Você será avisado na hora das doses." });
        }
    });
});

if (Notification.permission === "granted") {
    document.querySelectorAll("tr[data-estado]").forEach(function(row) {
        const estado = row.getAttribute("data-estado");
        const nome = row.getAttribute("data-nome");
        if (estado === "Atrasado") {
            new Notification("Dose atrasada", { body: `A dose de ${nome} está atrasada.` });
        }
        else if (estado === "Hora_de_tomar") {
            new Notification("Hora de tomar", { body: `É hora de tomar a dose de ${nome}.` });
        }
    });
}