var darkModeSwitch = document.querySelector('#dark-mode-switch');

const prefersDarkScheme = window.matchMedia("(prefers-color-scheme: dark)");

// if (prefersDarkScheme.matches) {
//   document.getElementsByTagName("HTML")[0].setAttribute("dark", "true");
// } else {
//   // document.body.classList.remove("dark-theme");
// }

darkModeSwitch.addEventListener('change', function() {
	if (darkModeSwitch.checked) {
		document.getElementsByTagName("HTML")[0].setAttribute("dark", "true");
		setCookie("dark", "true", 365)
	} else {
		document.getElementsByTagName("HTML")[0].removeAttribute("dark");
		setCookie("dark", "false", 365)
	}
});

function setCookie(cname, cvalue, exdays) {
  var d = new Date();
  d.setTime(d.getTime() + (exdays*24*60*60*1000));
  var expires = "expires="+ d.toUTCString();
  document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}