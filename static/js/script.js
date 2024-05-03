function toggleAside() {
    var aside = document.getElementById('aside');
    var asideRight = getComputedStyle(aside).right;
    aside.style.right = (asideRight === '0px' || asideRight === 'auto') ? '-250px' : '0px';
}


var calendarContainer = document.getElementById('calendarContainer');
    var dateInfoContainer = document.getElementById('dateInfo');

    function generateCalendar(year, month) {
        var daysInMonth = new Date(year, month + 1, 0).getDate();
        var currentDate = new Date();
        var currentYear = currentDate.getFullYear();
        var currentMonth = currentDate.getMonth() + 1;
        var currentDay = currentDate.getDate();

        var table = '<table>';
        table += '<thead><tr><th colspan="7">' + currentDay + '/' + currentMonth + '/' + currentYear + '<br><a style="font-size:16px">dd/mm/yy</a></th></tr>';
        table += '<tr><th>Sun</th><th>Mon</th><th>Tue</th><th>Wed</th><th>Thu</th><th>Fri</th><th>Sat</th></tr></thead>';
        table += '<tbody>';

        var date = new Date(year, month, 1);
        var dayOfWeek = date.getDay();

        table += '<tr>';
        for (var i = 0; i < dayOfWeek; i++) {
            table += '<td></td>';
        }

        for (var day = 1; day <= daysInMonth; day++) {
            var cellClass = '';
            if (year === currentYear && month === currentDate.getMonth() && day === currentDay) {
                cellClass = 'current-date';
            }
            table += '<td class="' + cellClass + '" data-date="' + year + '-' + (month + 1) + '-' + day + '">' + day + '</td>';
            if (new Date(year, month, day).getDay() === 6) {
                table += '</tr><tr>';
            }
        }

        for (var i = new Date(year, month, daysInMonth).getDay() + 1; i <= 6; i++) {
            table += '<td></td>';
        }

        table += '</tbody></table>';

        calendarContainer.innerHTML = table;
    }

    function updateCalendar() {
        var currentDate = new Date();
        var year = currentDate.getFullYear();
        var month = currentDate.getMonth();
        generateCalendar(year, month);
    }

    function handleDateClick(event) {
        var clickedDate = event.target.getAttribute('data-date');
        if (clickedDate) {
            dateInfoContainer.style.display = 'none';
            
            var xhr = new XMLHttpRequest();
            xhr.onreadystatechange = function() {
                if (xhr.readyState === XMLHttpRequest.DONE) {
                    if (xhr.status === 200) {
                        var response = JSON.parse(xhr.responseText);
                        
                        dateInfoContainer.innerHTML = '';
                        if (response.tasks && response.tasks.length > 0) {
                            var tasksHtml = '';
                            response.tasks.forEach(function(taskData) {
                                var tmpUrl = getTaskURLTemplate.replace('0', taskData.id);
                                tasksHtml += '<div class="task-container">';

                                tasksHtml += '<div class="task-container-left">'
                                tasksHtml += '<a href="' + tmpUrl + '"><img src="https://cdn.iconscout.com/icon/free/png-256/free-profile-1481935-1254808.png"/></a>'
                                tasksHtml += '</div>'

                                tasksHtml += '<div class="task-container-center">'
                                tasksHtml += '<a href="' + tmpUrl + '"><strong>Subject:</strong>' + taskData.subject + '</a><br>';
                                tasksHtml += '<a href="' + tmpUrl + '"><strong>Task Name:</strong> ' + taskData.task + '</a><br>';
                                tasksHtml += '</div>';

                                tasksHtml += '<div class="task-container-right">'
                                tasksHtml += '<a href="' + tmpUrl + '"><img src="https://static.thenounproject.com/png/4176414-200.png"/></a>'
                                tasksHtml += '</div>'

                                tasksHtml += '</div>';
                                console.log(response);
                            });
                            dateInfoContainer.innerHTML = tasksHtml;
                        } else {
                            dateInfoContainer.innerHTML = '<h3>No tasks for this date.</h3>';
                        }
                        
                        dateInfoContainer.style.display = 'block';
                    } else {
                        dateInfoContainer.innerHTML = '<h3>Error occurred while processing your request.</h3>';
                    }
                }
            };
            var url = getTaskByDateURL.replace('placeholder_date', encodeURIComponent(clickedDate));
            xhr.open('GET', url, true);
            xhr.send();
        }
    }
    calendarContainer.addEventListener('click', handleDateClick);
    updateCalendar();