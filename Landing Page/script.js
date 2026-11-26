// 1. Mobile menu toggle
var menuBtn = document.getElementById("menuBtn");
var menu = document.getElementById("menu");
menuBtn.addEventListener("click", function () {
  var isOpen = menu.classList.toggle("open");
  menuBtn.setAttribute("aria-expanded", isOpen);
});
// close menu after clicking a link
menu.addEventListener("click", function (e) {
  if (e.target.tagName === "A") {
    menu.classList.remove("open");
    menuBtn.setAttribute("aria-expanded", "false");
  }
});

// 2. Highlight active nav link while scrolling
var links = document.querySelectorAll("nav ul a");
window.addEventListener("scroll", function () {
  var current = "";
  document.querySelectorAll("main section[id]").forEach(function (sec) {
    if (window.scrollY >= sec.offsetTop - 120) current = sec.id;
  });
  links.forEach(function (a) {
    a.classList.toggle("active", a.getAttribute("href") === "#" + current);
  });
});

// 3. Simple form validation
document.getElementById("pilotForm").addEventListener("submit", function (e) {
  e.preventDefault();
  var msg = document.getElementById("msg");
  var name = document.getElementById("name").value.trim();
  var email = document.getElementById("email").value.trim();
  var course = document.getElementById("course").value.trim();
  if (!name || !email || !course) {
    msg.textContent = "Please fill in all fields.";
    msg.className = "err-t";
  } else if (!/^\S+@\S+\.edu$/i.test(email)) {
    msg.textContent = "Please use your institutional .edu email.";
    msg.className = "err-t";
  } else {
    msg.textContent = "Thank you, " + name + "! We will contact you soon.";
    msg.className = "ok-t";
    this.reset();
  }
});
