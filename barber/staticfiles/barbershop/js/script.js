document.getElementById('sidebarToggle').addEventListener('click', function() {
    document.getElementById('sidebar').classList.toggle('active');
    document.getElementById('content').classList.toggle('active');
    document.querySelector('.navbar').classList.toggle('active');
});


// Función para inicializar la gráfica de contabilidad
function initializeContabilidadChart(labels, ingresos, gastos, beneficios) {
    var ctx = document.getElementById('contabilidadChart').getContext('2d');
    var chart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: 'Ingresos',
                data: ingresos,
                borderColor: 'rgb(75, 192, 192)',
                tension: 0.1
            }, {
                label: 'Gastos',
                data: gastos,
                borderColor: 'rgb(255, 99, 132)',
                tension: 0.1
            }, {
                label: 'Beneficios',
                data: beneficios,
                borderColor: 'rgb(54, 162, 235)',
                tension: 0.1
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

// Función para alternar el sidebar
document.addEventListener('DOMContentLoaded', function() {
    const sidebarToggle = document.getElementById('sidebarToggle');
    const sidebar = document.getElementById('sidebar');
    const content = document.getElementById('content');
    const navbar = document.querySelector('.navbar');

    if (sidebarToggle) {
        sidebarToggle.addEventListener('click', function() {
            sidebar.classList.toggle('active');
            content.classList.toggle('active');
            navbar.classList.toggle('active');
        });
    }
});

