let weekEnd = ['saturday', 'sunday']
document.querySelector('#check').addEventListener('click', checkDay)

function checkDay() {
  const day = document.querySelector('#day').value.trim();
  let dayFormatted = day.toLowerCase()
  
  if (weekEnd.includes(dayFormatted)) {
    document.querySelector("#placeToSee").innerText = "Weekend";
  } else {
    document.querySelector("#placeToSee").innerText = "Weekday";
  }
}
