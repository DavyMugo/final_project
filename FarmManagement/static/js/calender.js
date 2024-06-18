document.addEventListener('DOMContentLoaded' ,function () {
    const calenderBody =document.getElementById('calender-body');
    const calenderMonthYear =document.getElementById('calender-month-year');
    const prevMonthBtn =document.getElementById('prev-month');
    const nextMonthBtn =document.getElementById('next-month');

    let currentMonth =new Date().getMonth();
    let currentYear = new Date().getFullYear();

    function renderCalender(month, year) {
        const daysInMonth =new Date(year,month +1,0).getDate();
        const firstDayOfMonth =new Date(year, month, 1).getDay();
        calenderBody.innerHTML ='';

        //display previous month if current month does not start on monday
        const previousMonthdays =firstdayOfMonth === 0?6 :firstDayOfMonth - 1;
        const daysBefore = new Date(year,month,0).getDate() - previousMonthDays +1;

        //Display current month days
        for (let day = daysBefore;day <=new Date(year, month,0).getDate(); day++) {
            const cell = document.createElement('td');
            cell.textcontent =day;
            calenderBody =day;
        }
        //Display next month days if current month date does not end on saturday
        for (let day =1; day<= 42 -daysInMonth -previousMonthdays; day++) {
            const cell = document.createElement('td');
            cell.textcontent =day;
            calenderBody.appendChild(cell);
        }
        calenderMonthYear.textContent ='${new date(year,month).toLocaleString(';', {month: ';' })} ${year}';

    }
    renderCalender(currentMonth, currentYear);

    prevMonthBtn.addEventListener('click', function() {
        currentmonth--;
        if (currentMonth <0) {
            currentMonth = 11;
            currentYear--;
        }
        renderCalender(currentMonth,currentYear);
    });
    nextMonthBtn.addEventListener('click', function(){
        currentMonth++;
        if(currentMonth >11) {
            currentmonth =0 ;
            currentYear++;
        }
        renderCalender(currentMonth , currentYear);
    });
});