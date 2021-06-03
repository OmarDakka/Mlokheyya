$(document).ready(function () {
	console.log("HELLO")
	$('#sidebarCollapse').on('click', function () {
		$('#sidebar').toggleClass('active');
	});
});