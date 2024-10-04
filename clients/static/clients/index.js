
function addDate(date, days, months, years) {
    let newDate = new Date(date)

    newDate.setFullYear(newDate.getFullYear() + years)
    newDate.setMonth(newDate.getMonth() + months)
    newDate.setDate(newDate.getDate() + days)

    return newDate
}

function addRenewalDate() {
    const dateValue = document.querySelector('#start-date')
    // const endDate = document.querySelector('#end-date')
    const startDate = dateValue.value

    let endDate = addDate(startDate, -1, 0, 1)
    let renewalDate = addDate(startDate, 0, 0, 1)
    const formattedDate = formatDate(renewalDate)
    const endDateFormatted = formatDate(endDate)

    console.log(formattedDate, endDateFormatted)
    document.querySelector('#renewal-date').value = formattedDate
    document.querySelector('#end-date').value = endDateFormatted
}

function formatDate(date) {
    const d = new Date(date);
    const year = d.getFullYear();
    const month = String(d.getMonth() + 1).padStart(2, '0'); // Months are zero-based
    const day = String(d.getDate()).padStart(2, '0');
    return `${year}-${month}-${day}`;
}

document.addEventListener('input', function(e) {
    if (e.target.matches('#start-date')) {
        addRenewalDate()
    }
})


function highlightRenewalDates() {
    const elements = document.querySelectorAll('.clients-renewal-date');
    const currentDate = new Date();

    elements.forEach(element => {
        const renewalDate = new Date(element.textContent.trim());
        const timeDifference = renewalDate - currentDate;
        const daysDifference = timeDifference / (1000 * 3600 * 24);

        if (daysDifference < 30) {
            element.classList.add("highlight-late");
        }
    });
}


highlightRenewalDates()


// disply all clients details
document.querySelectorAll('.more').forEach((moreButton, index) => {
    moreButton.addEventListener('click', function() {
        const details = document.querySelectorAll('.all-details')[index];
        if (details.style.display === 'flex') {
            details.style.display = 'none';
        } else {
            details.style.display = 'flex';
        }
    });
});

