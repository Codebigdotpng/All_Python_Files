let isLeft = true;

function addEvent() {
  const date = document.getElementById("eventDate").value.trim();
  const title = document.getElementById("eventTitle").value.trim();
  const desc = document.getElementById("eventDesc").value.trim();

  if (!date || !title || !desc) {
    alert("Please fill in all fields!");
    return;
  }

  const side = isLeft ? "entry-left" : "entry-right";
  isLeft = !isLeft;

  const newEntry = document.createElement("div");
  newEntry.className = `entry ${side}`;
  newEntry.innerHTML = `
    <p class="date">${date}</p>
    <p><strong>${title}</strong> — ${desc}</p>
  `;

  document.getElementById("timeline").appendChild(newEntry);

  // Clear inputs
  document.getElementById("eventDate").value = "";
  document.getElementById("eventTitle").value = "";
  document.getElementById("eventDesc").value = "";
}
