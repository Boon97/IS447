let nav = 0;
let clicked = null;
let events = seperated_into_each_day // From calendar.html, an object of individual dates

const calendar = document.getElementById('calendar');
const newEventModal = document.getElementById('newEventModal');
const deleteEventModal = document.getElementById('deleteEventModal');
const backDrop = document.getElementById('modalBackDrop');
const eventTitleInput = document.getElementById('eventTitleInput');
const weekdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];

function openModal(date) {
  clicked = date;
  // console.log("you have clicked: ", clicked)

  const eventForDay = events.find(e => e.date === clicked);

  // if (eventForDay) {
  //   console.log("WE ARE DELETING EVENT NOW")
  //   document.getElementById('eventText').innerText = eventForDay.title;
  //   deleteEventModal.style.display = 'block';
  // } else {
  //   console.log("WE ARE ADDING EVENT NOW")
  //   newEventModal.style.display = 'block';
  // }
  // console.log("WE ARE ADDING EVENT NOW")
  newEventModal.style.display = 'block';
  // console.log (eventForDay)

  backDrop.style.display = 'block';
}

function load() {
  const dt = new Date();

  if (nav !== 0) {
    dt.setMonth(new Date().getMonth() + nav);
  }

  const day = dt.getDate();
  const month = dt.getMonth();
  const year = dt.getFullYear();

  const firstDayOfMonth = new Date(year, month, 1);
  const daysInMonth = new Date(year, month + 1, 0).getDate();
  
  const dateString = firstDayOfMonth.toLocaleDateString('en-GB', {
    weekday: 'long',
    year: 'numeric',
    month: 'numeric',
    day: 'numeric',
  });
  const paddingDays = weekdays.indexOf(dateString.split(', ')[0]);

  document.getElementById('monthDisplay').innerText = 
    `${dt.toLocaleDateString('en-GB', { month: 'long' })} ${year}`;

  calendar.innerHTML = '';

  for(let i = 1; i <= paddingDays + daysInMonth; i++) {
    const daySquare = document.createElement('div');
    daySquare.classList.add('day');
    var events_for_day_array = []
    const dayString = `${i - paddingDays}/${month + 1}/${year}`;
    // console.log("daystring: ", dayString)

    if (i > paddingDays) {
      // console.log('paddingDays: ', paddingDays)
      daySquare.innerText = i - paddingDays;
      const eventForDay = events.find(e => e.date === dayString);
      // console.log("eventForDay: ", eventForDay)
      for (each_event of events){
        // console.log(each_event)
        if (each_event.date == dayString){
          events_for_day_array.push(each_event)
        }
      }
      // console.log(events_for_day_array)

      if (i - paddingDays === day && nav === 0) {
        daySquare.id = 'currentDay';
        // console.log('daysquare: ', daySquare)
      }

      // if (eventForDay) {
      //   const eventDiv = document.createElement('div');
      //   console.log('eventDiv: ', eventDiv)
      //   eventDiv.classList.add('event');
      //   eventDiv.innerText = eventForDay.title;
      //   console.log('eventForDay.title: ', eventForDay.title)

      //   daySquare.appendChild(eventDiv);
      // }
      var event_index = 0
      if (events_for_day_array.length > 0 ) {
        for (each_event of events_for_day_array){
          // console.log(each_event)
          const eventDiv = document.createElement('div');
          // console.log('eventDiv: ', eventDiv)
          eventDiv.classList.add('event');
          eventDiv.innerText = each_event.title;
          // console.log('eventForDay.title: ', each_event.title)

          daySquare.appendChild(eventDiv);
          event_index += 1
          // console.log("event_index: ", event_index)
        
        }
        }

      
      daySquare.addEventListener('click', () => openModal(dayString));
    } else {
      daySquare.classList.add('padding');
    }

    calendar.appendChild(daySquare);    
  }
}

function closeModal() {
  eventTitleInput.classList.remove('error');
  newEventModal.style.display = 'none';
  deleteEventModal.style.display = 'none';
  backDrop.style.display = 'none';
  eventTitleInput.value = '';
  clicked = null;
  load();
}

function saveEvent() {
  if (eventTitleInput.value) {
    console.log('eventTitleInput: ',eventTitleInput.value)
    eventTitleInput.classList.remove('error');

    events.push({
      date: clicked,
      title: eventTitleInput.value,
    });

    localStorage.setItem('events', JSON.stringify(events));
    closeModal();
  } else {
    eventTitleInput.classList.add('error');
  }
}

function deleteEvent() {
  events = events.filter(e => e.date !== clicked);
  localStorage.setItem('events', JSON.stringify(events));
  closeModal();
}

function initButtons() {
  document.getElementById('nextButton').addEventListener('click', () => {
    nav++;
    load();
  });

  document.getElementById('backButton').addEventListener('click', () => {
    nav--;
    load();
  });

  document.getElementById('saveButton').addEventListener('click', saveEvent);
  document.getElementById('cancelButton').addEventListener('click', closeModal);
  document.getElementById('deleteButton').addEventListener('click', deleteEvent);
  document.getElementById('closeButton').addEventListener('click', closeModal);
}

// zj function delete all items
function deleteItems(){
  localStorage.clear()
}

initButtons();
load();
deleteItems();
// console.log(events)
