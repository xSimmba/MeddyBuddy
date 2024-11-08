
document.addEventListener('DOMContentLoaded', () => {
    
    const redPills = document.querySelectorAll('.red-pill');
    const greenPills = document.querySelectorAll('.green-pill');

    
    const toggleStatus = (event) => {
        const pill = event.currentTarget;
        const status = pill.getAttribute('data-status');
        const medicationBox = pill.closest('.medication-box');
        const medicationId = medicationBox.getAttribute('data-medication-id');

        
        if (status === 'not_taken') {
            medicationBox.style.backgroundColor = 'rgba(128, 0, 0, 0.4)';
            console.log('Medication with ID', medicationId, 'has been marked as taken');
        
        } else {
            medicationBox.style.backgroundColor = 'rgba(0, 128, 0, 0.4)';
        
        }
    };

    
    redPills.forEach(pill => {
        pill.addEventListener('click', toggleStatus);
    });

    
    greenPills.forEach(pill => {
        pill.addEventListener('click', toggleStatus);
    });

    let iconMeds = document.querySelectorAll(".icon-meds-svg");
    iconMeds.forEach(iconMed => {
        iconMed.addEventListener('mouseover', () => {
            iconMed.src = "/static/media/detail-meds/icon_meds_hover.svg";
            iconMed.style.width = "80px";
            iconMed.style.height = "80px";
        });
        iconMed.addEventListener('mouseout', () => {
            iconMed.src = "/static/media/detail-meds/icon_meds.svg";
        });
    });
});